#!/usr/bin/env python3
"""
🔗 Correcteur de Liens Internes - Documentation Athalia
Corrige uniquement les liens internes cassés pour atteindre 100%
"""

import re
import sys
from datetime import datetime
from pathlib import Path

# Ajouter le répertoire parent au path pour importer athalia_core
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from athalia_core.core.logger import Logger


class InternalLinksCorrector:
    """Correcteur de liens internes dans la documentation."""

    def __init__(self):
        """Initialise le correcteur."""
        self.workspace = Path(__file__).parent.parent.parent
        self.logger = Logger(__name__)
        self.docs_dir = self.workspace / "docs"
        self.correction_log = self.workspace / "internal_links_correction.log"

    def log_correction(self, message, level="INFO"):
        """Enregistre les corrections effectuées"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.correction_log, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(f"[{level}] {message}")

    def is_external_link(self, url):
        """Vérifie si un lien est externe"""
        external_patterns = [
            r"^https?://",
            r"^mailto:",
            r"^ftp://",
            r"^//",
            r"^www\.",
            r"^img.shields.io",
            r"^docs\.ros\.org",
            r"^docs\.pollen-robotics\.com",
            r"^docs\.docker\.com",
            r"^doc\.rust-lang\.org",
            r"^github\.com",
            r"^mypy\.readthedocs\.io",
            r"^bandit\.readthedocs\.io",
            r"^pre-commit\.com",
            r"^python\.org",
            r"^peps\.python\.org",
        ]

        for pattern in external_patterns:
            if re.match(pattern, url):
                return True
        return False

    def is_internal_link(self, url):
        """Vérifie si un lien est interne et potentiellement cassé"""
        if self.is_external_link(url):
            return False

        # Liens internes typiques
        internal_patterns = [
            r"\.md$",  # Fichiers Markdown
            r"^[^/]",  # Fichiers relatifs
            r"^\.\./",  # Chemins relatifs
            r"^docs/",  # Chemins docs
            r"^\./",  # Chemins relatifs
        ]

        for pattern in internal_patterns:
            if re.search(pattern, url):
                return True
        return False

    def find_target_file(self, link_url, source_file):
        """Trouve le fichier cible d'un lien"""
        source_dir = source_file.parent

        # Essayer différents chemins
        possible_paths = [
            source_dir / link_url,
            source_dir / link_url.removeprefix("./"),
            source_dir / link_url.removeprefix("../"),
            self.workspace / link_url,
            self.workspace / link_url.removeprefix("docs/"),
            self.workspace / "docs" / link_url,
        ]

        for path in possible_paths:
            if path.exists() and path.is_file():
                return path

        return None

    def suggest_correction(self, link_url, source_file):
        """Suggère une correction pour un lien cassé"""
        # Si c'est un lien externe, le laisser tel quel
        if self.is_external_link(link_url):
            return None

        # Essayer de trouver le fichier cible
        target_file = self.find_target_file(link_url, source_file)

        if target_file:
            # Calculer le chemin relatif correct
            try:
                relative_path = target_file.relative_to(source_file.parent)
                return str(relative_path)
            except ValueError:
                return None

        # Si le fichier n'existe pas, suggérer une suppression ou un remplacement
        if link_url.endswith(".md"):
            return f"FICHIER_SUPPRIMÉ: {link_url}"

        return None

    def correct_file_links(self, file_path):
        """Corrige les liens dans un fichier"""
        try:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()

            corrections_made = 0

            # Pattern pour détecter les liens Markdown
            link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"

            def replace_link(match):
                nonlocal corrections_made
                link_text = match.group(1)
                link_url = match.group(2)

                # Vérifier si c'est un lien interne cassé
                if self.is_internal_link(link_url):
                    correction = self.suggest_correction(link_url, file_path)
                    if correction:
                        if correction.startswith("FICHIER_SUPPRIMÉ:"):
                            # Remplacer par du texte simple
                            corrections_made += 1
                            self.log_correction(
                                f"Lien supprimé: {link_url} -> texte simple dans {file_path.name}"
                            )
                            return f"**{link_text}**"
                        else:
                            # Corriger le chemin
                            corrections_made += 1
                            self.log_correction(
                                f"Lien corrigé: {link_url} -> {correction} dans {file_path.name}"
                            )
                            return f"[{link_text}]({correction})"

                # Lien externe ou valide, le laisser tel quel
                return match.group(0)

            # Appliquer les corrections
            corrected_content = re.sub(link_pattern, replace_link, content)

            # Sauvegarder si des corrections ont été faites
            if corrections_made > 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(corrected_content)

                self.log_correction(
                    f"✅ {corrections_made} corrections appliquées dans {file_path.name}"
                )
                return corrections_made

            return 0

        except Exception as e:
            self.log_correction(
                f"❌ Erreur lors de la correction de {file_path}: {e}", "ERROR"
            )
            return 0

    def run_correction(self):
        """Exécute la correction des liens internes"""
        self.log_correction("🚀 Démarrage de la correction des liens internes...")

        total_corrections = 0
        files_processed = 0

        # Traiter tous les fichiers Markdown
        for md_file in self.docs_dir.rglob("*.md"):
            if md_file.is_file():
                corrections = self.correct_file_links(md_file)
                total_corrections += corrections
                files_processed += 1

        self.log_correction("✅ Correction terminée !")
        self.log_correction(f"📁 Fichiers traités: {files_processed}")
        self.log_correction(f"🔗 Corrections appliquées: {total_corrections}")

        return total_corrections


def main():
    """Fonction principale"""
    corrector = InternalLinksCorrector()

    try:
        corrections = corrector.run_correction()
        print(f"\n🎯 Correction terminée avec {corrections} liens corrigés !")
        sys.exit(0)

    except KeyboardInterrupt:
        print("\n⚠️ Correction interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors de la correction: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
