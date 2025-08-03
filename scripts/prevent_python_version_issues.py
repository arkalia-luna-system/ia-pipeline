#!/usr/bin/env python3
"""
Script de prévention des problèmes de versions Python
Vérifie et corrige automatiquement les versions non supportées
"""

import re
import sys
from pathlib import Path


class PythonVersionPreventer:
    """Préventeur des problèmes de versions Python"""

    def __init__(self):
        self.project_root = Path.cwd()
        self.supported_versions = ["3.8", "3.9", "3.10", "3.11", "3.12"]
        self.unsupported_versions = ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7"]
        self.recommended_version = "3.10"
        self.workflow_dir = self.project_root / ".github" / "workflows"

    def check_file_for_unsupported_versions(
        self, file_path: Path
    ) -> list[tuple[str, int, str]]:
        """Vérifie un fichier pour les versions non supportées"""
        issues = []

        # Ignorer les fichiers Apple Double
        if file_path.name.startswith("._"):
            return issues

        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
                lines = content.split("\n")

                for line_num, line in enumerate(lines, 1):
                    # Chercher spécifiquement les versions Python
                    # (pas les versions de dépendances)
                    # Pattern pour python-version: "3.1"
                    python_version_matches = re.findall(
                        r'python-version:\s*["\']?([3]\.[0-9]+)["\']?',
                        line,
                    )
                    for version in python_version_matches:
                        if version in self.unsupported_versions:
                            issues.append((version, line_num, line.strip()))

                    # Pattern pour les matrices de versions Python [3.1, 3.2]
                    if "python-version" in line and "[" in line:
                        matrix_version_matches = re.findall(r"([3]\.[0-9]+)", line)
                        for version in matrix_version_matches:
                            if version in self.unsupported_versions:
                                issues.append((version, line_num, line.strip()))

                    # Pattern pour FROM python:3.1
                    docker_matches = re.findall(r"FROM python:([3]\.[0-9]+)", line)
                    for version in docker_matches:
                        if version in self.unsupported_versions:
                            issues.append((version, line_num, line.strip()))
        except Exception as e:
            print(f"⚠️  Erreur lecture {file_path}: {e}")

        return issues

    def fix_unsupported_versions(self, file_path: Path) -> bool:
        """Corrige automatiquement les versions non supportées"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Remplacer les versions non supportées par la version recommandée
            for version in self.unsupported_versions:
                # Pattern pour python-version: "3.1"
                content = re.sub(
                    rf'python-version:\s*["\']?{re.escape(version)}["\']?',
                    f'python-version: "{self.recommended_version}"',
                    content,
                )

                # Pattern pour les matrices [3.1, 3.2]
                content = re.sub(
                    rf"\b{re.escape(version)}\b", self.recommended_version, content
                )

            # Si le contenu a changé, sauvegarder
            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return True

            return False
        except Exception as e:
            print(f"❌ Erreur correction {file_path}: {e}")
            return False

    def scan_and_fix_workflows(self) -> bool:
        """Scanne et corrige les workflows GitHub Actions"""
        print("🔍 Scan et correction des workflows GitHub Actions...")

        if not self.workflow_dir.exists():
            print("❌ Dossier .github/workflows/ non trouvé")
            return False

        workflow_files = list(self.workflow_dir.glob("*.yaml")) + list(
            self.workflow_dir.glob("*.yml")
        )
        fixed_files = []

        for workflow_file in workflow_files:
            print(f"\n📋 Vérification de {workflow_file.name}:")

            # Vérifier les problèmes
            issues = self.check_file_for_unsupported_versions(workflow_file)

            if issues:
                print("   ❌ Problèmes détectés:")
                for version, line_num, line in issues:
                    print(f"      - Version {version} (ligne {line_num}): {line}")

                # Corriger automatiquement
                if self.fix_unsupported_versions(workflow_file):
                    print(f"   ✅ {workflow_file.name}: Corrigé automatiquement")
                    fixed_files.append(workflow_file.name)
                else:
                    print(f"   ❌ {workflow_file.name}: Échec de la correction")
            else:
                print(f"   ✅ {workflow_file.name}: Aucun problème détecté")

        if fixed_files:
            print(f"\n✅ Fichiers corrigés: {', '.join(fixed_files)}")
            return True
        else:
            print("\n✅ Aucun fichier à corriger")
            return False

    def scan_and_fix_configs(self) -> bool:
        """Scanne et corrige les fichiers de configuration"""
        print("\n🔍 Scan et correction des fichiers de configuration...")

        config_files = [
            "config/pyproject.toml",
            "config/requirements.txt",
            "config/requirements-minimal.txt",
            "config/Dockerfile",
        ]

        fixed_files = []

        for config_file in config_files:
            file_path = self.project_root / config_file
            if not file_path.exists():
                print(f"   ⚠️  {config_file}: Fichier non trouvé")
                continue

            print(f"   📋 Vérification de {config_file}:")

            # Vérifier les problèmes
            issues = self.check_file_for_unsupported_versions(file_path)

            if issues:
                print("      ❌ Problèmes détectés:")
                for version, line_num, line in issues:
                    print(f"         - Version {version} (ligne {line_num}): {line}")

                # Corriger automatiquement
                if self.fix_unsupported_versions(file_path):
                    print(f"      ✅ {config_file}: Corrigé automatiquement")
                    fixed_files.append(config_file)
                else:
                    print(f"      ❌ {config_file}: Échec de la correction")
            else:
                print(f"      ✅ {config_file}: Aucun problème détecté")

        if fixed_files:
            print(f"\n✅ Fichiers de config corrigés: {', '.join(fixed_files)}")
            return True
        else:
            print("\n✅ Aucun fichier de config à corriger")
            return False

    def create_prevention_hook(self) -> bool:
        """Crée un hook de prévention pour Git"""
        print("\n🔧 Création du hook de prévention...")

        hook_content = """#!/bin/bash
# Hook de prévention des versions Python non supportées
# Exécuté avant chaque commit

echo "🔍 Vérification des versions Python..."

# Vérifier les versions Python dans les fichiers modifiés
python_files=$(git diff --cached --name-only --diff-filter=ACM | \
    grep -E '\\.(yaml|yml|toml|txt|Dockerfile)$')

if [ -n "$python_files" ]; then
        echo "📋 Fichiers à vérifier: $python_files"

    # Vérifier les versions non supportées (3.1 à 3.7, pas 3.10+)
    unsupported_versions=$(grep -r "3\\.[1-7][^0-9]" $python_files 2>/dev/null || true)

    if [ -n "$unsupported_versions" ]; then
        echo "❌ Versions Python non supportées détectées:"
        echo "$unsupported_versions"
        echo ""
        echo "🚨 Veuillez corriger ces versions avant de committer."
        echo "   Versions supportées: 3.8, 3.9, 3.10, 3.11, 3.12"
        echo "   Version recommandée: 3.10"
        exit 1
    else
        echo "✅ Toutes les versions Python sont supportées"
    fi
else
    echo "ℹ️  Aucun fichier de configuration modifié"
fi
"""

        hook_dir = self.project_root / ".git" / "hooks"
        hook_file = hook_dir / "pre-commit"

        try:
            hook_dir.mkdir(parents=True, exist_ok=True)
            with open(hook_file, "w") as f:
                f.write(hook_content)

            # Rendre le hook exécutable
            hook_file.chmod(0o755)

            print(f"✅ Hook de prévention créé: {hook_file}")
            return True
        except Exception as e:
            print(f"❌ Erreur création hook: {e}")
            return False

    def run_prevention(self) -> bool:
        """Exécute la prévention complète"""
        print("🚀 Démarrage de la prévention des problèmes de versions Python...")
        print("=" * 60)

        # Scan et correction des workflows
        workflows_fixed = self.scan_and_fix_workflows()

        # Scan et correction des configs
        configs_fixed = self.scan_and_fix_configs()

        # Création du hook de prévention
        hook_created = self.create_prevention_hook()

        print("\n" + "=" * 60)
        print("📋 RAPPORT DE PRÉVENTION")
        print("=" * 60)

        if workflows_fixed or configs_fixed:
            print("✅ Corrections appliquées avec succès")
            print("📝 Veuillez vérifier les modifications et committer si nécessaire")
        else:
            print("✅ Aucune correction nécessaire")

        if hook_created:
            print("🔧 Hook de prévention installé")
            print(
                "   Le hook vérifiera automatiquement les versions Python avant "
                "chaque commit"
            )

        print("\n🎯 Recommandations:")
        print("1. Utiliser Python 3.10+ pour la stabilité")
        print("2. Utiliser Python 3.11+ pour les performances")
        print("3. Utiliser Python 3.12+ pour les dernières fonctionnalités")
        print("4. Éviter les versions Python < 3.8")

        print("=" * 60)

        return True


def main():
    """Fonction principale"""
    preventer = PythonVersionPreventer()

    try:
        success = preventer.run_prevention()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Prévention interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors de la prévention: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
