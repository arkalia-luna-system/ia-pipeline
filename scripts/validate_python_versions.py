#!/usr/bin/env python3
"""
Script de validation des versions Python dans les workflows GitHub Actions
Vérifie que toutes les versions Python utilisées sont supportées
"""

import re
import sys
from pathlib import Path


class PythonVersionValidator:
    """Validateur des versions Python"""

    def __init__(self):
        self.project_root = Path.cwd()
        self.supported_versions = ["3.8", "3.9", "3.10", "3.11", "3.12"]
        self.unsupported_versions = ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7"]
        self.workflow_dir = self.project_root / ".github" / "workflows"

    def find_python_versions_in_file(self, file_path: Path) -> list[tuple[str, int]]:
        """Trouve toutes les versions Python dans un fichier"""
        versions = []

        # Ignorer les fichiers Apple Double
        if file_path.name.startswith("._"):
            return versions

        try:
            with open(file_path, encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    # Chercher les patterns python-version spécifiques
                    matches = re.findall(
                        r'python-version:\s*["\']?([3]\.[0-9]+)["\']?', line
                    )
                    for match in matches:
                        versions.append((match, line_num))

                    # Chercher les patterns dans les matrices de versions Python
                    if "python-version" in line and "[" in line:
                        # Extraire les versions de la matrice
                        version_matches = re.findall(r"([3]\.[0-9]+)", line)
                        for version in version_matches:
                            versions.append((version, line_num))
        except Exception as e:
            print(f"⚠️  Erreur lecture {file_path}: {e}")

        return versions

    def validate_workflows(self) -> bool:
        """Valide tous les workflows GitHub Actions"""
        print("🔍 Validation des versions Python dans les workflows...")

        if not self.workflow_dir.exists():
            print("❌ Dossier .github/workflows/ non trouvé")
            return False

        all_valid = True
        workflow_files = list(self.workflow_dir.glob("*.yaml")) + list(
            self.workflow_dir.glob("*.yml")
        )

        for workflow_file in workflow_files:
            print(f"\n📋 Vérification de {workflow_file.name}:")
            versions = self.find_python_versions_in_file(workflow_file)

            if not versions:
                print("   ℹ️  Aucune version Python trouvée")
                continue

            file_valid = True
            for version, line_num in versions:
                if version in self.unsupported_versions:
                    print(f"   ❌ Version non supportée: {version} (ligne {line_num})")
                    file_valid = False
                    all_valid = False
                elif version in self.supported_versions:
                    print(f"   ✅ Version supportée: {version} (ligne {line_num})")
                else:
                    print(f"   ⚠️  Version inconnue: {version} (ligne {line_num})")
                    file_valid = False
                    all_valid = False

            if file_valid:
                print(
                    f"   ✅ {workflow_file.name}: Toutes les versions sont supportées"
                )
            else:
                print(f"   ❌ {workflow_file.name}: Problèmes détectés")

        return all_valid

    def validate_config_files(self) -> bool:
        """Valide les fichiers de configuration"""
        print("\n🔍 Validation des fichiers de configuration...")

        config_files = [
            "config/pyproject.toml",
            "config/requirements.txt",
            "config/requirements-minimal.txt",
            "config/Dockerfile",
        ]

        all_valid = True
        for config_file in config_files:
            file_path = self.project_root / config_file
            if not file_path.exists():
                print(f"   ⚠️  {config_file}: Fichier non trouvé")
                continue

            print(f"   📋 Vérification de {config_file}:")
            versions = self.find_python_versions_in_file(file_path)

            file_valid = True
            for version, line_num in versions:
                if version in self.unsupported_versions:
                    print(
                        f"      ❌ Version non supportée: {version} (ligne {line_num})"
                    )
                    file_valid = False
                    all_valid = False
                elif version in self.supported_versions:
                    print(f"      ✅ Version supportée: {version} (ligne {line_num})")
                else:
                    print(f"      ⚠️  Version inconnue: {version} (ligne {line_num})")

            if file_valid:
                print(f"      ✅ {config_file}: OK")
            else:
                print(f"      ❌ {config_file}: Problèmes détectés")

        return all_valid

    def generate_report(self) -> str:
        """Génère un rapport de validation"""
        print("\n📊 Génération du rapport de validation...")

        report = []
        report.append("# Rapport de Validation des Versions Python")
        report.append("")
        report.append("## Versions Supportées")
        report.append("- Python 3.8+")
        report.append("- Python 3.9+")
        report.append("- Python 3.10+ (recommandé)")
        report.append("- Python 3.11+")
        report.append("- Python 3.12+")
        report.append("")
        report.append("## Versions Non Supportées")
        report.append("- Python 3.1 (déprécié)")
        report.append("- Python 3.2 (déprécié)")
        report.append("- Python 3.3 (déprécié)")
        report.append("- Python 3.4 (déprécié)")
        report.append("- Python 3.5 (déprécié)")
        report.append("- Python 3.6 (déprécié)")
        report.append("- Python 3.7 (déprécié)")
        report.append("")

        # Validation des workflows
        workflows_valid = self.validate_workflows()
        status = "✅ VALIDE" if workflows_valid else "❌ PROBLÈMES DÉTECTÉS"
        report.append(f"## Workflows GitHub Actions: {status}")
        report.append("")

        # Validation des configs
        configs_valid = self.validate_config_files()
        status = "✅ VALIDE" if configs_valid else "❌ PROBLÈMES DÉTECTÉS"
        report.append(f"## Fichiers de Configuration: {status}")
        report.append("")

        # Recommandations
        report.append("## Recommandations")
        report.append("1. Utiliser Python 3.10+ pour la stabilité")
        report.append("2. Utiliser Python 3.11+ pour les performances")
        report.append("3. Utiliser Python 3.12+ pour les dernières fonctionnalités")
        report.append("4. Éviter les versions Python < 3.8")
        report.append("")

        overall_valid = workflows_valid and configs_valid
        status = "✅ VALIDATION RÉUSSIE" if overall_valid else "❌ PROBLÈMES À CORRIGER"
        report.append(f"## Résumé Global: {status}")

        return "\n".join(report)

    def run_validation(self) -> bool:
        """Exécute la validation complète"""
        print("🚀 Démarrage de la validation des versions Python...")
        print("=" * 60)

        # Validation des workflows
        workflows_valid = self.validate_workflows()

        # Validation des configs
        configs_valid = self.validate_config_files()

        # Génération du rapport
        report = self.generate_report()

        # Sauvegarde du rapport
        report_file = self.project_root / "python_versions_validation_report.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report)

        print("\n" + "=" * 60)
        print("📋 RAPPORT DE VALIDATION")
        print("=" * 60)
        print(report)
        print("=" * 60)

        overall_valid = workflows_valid and configs_valid
        if overall_valid:
            print("✅ Validation réussie ! Toutes les versions Python sont supportées.")
            print(f"📄 Rapport sauvegardé: {report_file}")
        else:
            print(
                "❌ Problèmes détectés ! Veuillez corriger les versions non supportées."
            )
            print(f"📄 Rapport détaillé: {report_file}")

        return overall_valid


def main():
    """Fonction principale"""
    validator = PythonVersionValidator()

    try:
        success = validator.run_validation()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Validation interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors de la validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
