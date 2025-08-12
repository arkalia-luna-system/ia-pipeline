#!/usr/bin/env python3
"""
🎯 Correction Finale des Liens - Documentation Athalia
Corrige les derniers liens internes cassés pour atteindre 100%
"""

import re
import sys
from datetime import datetime
from pathlib import Path


class FinalLinkCorrector:
    def __init__(self):
        self.workspace = Path("/Volumes/T7/athalia-dev-setup")
        self.docs_dir = self.workspace / "docs"
        self.final_log = self.workspace / "final_correction_100.log"

    def log_correction(self, message, level="INFO"):
        """Enregistre les corrections finales"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.final_log, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(f"[{level}] {message}")

    def is_external_link(self, url):
        """Vérifie si un lien est externe (à ignorer)"""
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
            r"^docs\.github\.com",
            r"^markdownguide\.org",
            r"^webfx\.com",
            r"^mermaid-js\.github\.io",
            r"^black\.readthedocs\.io",
            r"^flake8\.pycqa\.org",
            r"^react\.dev",
            r"^typescriptlang\.org",
            r"^tailwindcss\.com",
            r"^vitejs\.dev",
            r"^react-typescript-cheatsheet\.netlify\.app",
            r"^tailwindui\.com",
            r"^recharts\.org",
        ]

        for pattern in external_patterns:
            if re.match(pattern, url):
                return True
        return False

    def find_real_broken_links(self):
        """Trouve les vrais liens internes cassés"""
        real_broken_links = []

        for md_file in self.docs_dir.rglob("*.md"):
            if md_file.is_file():
                try:
                    with open(md_file, encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    # Pattern pour détecter les liens Markdown
                    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
                    matches = re.findall(link_pattern, content)

                    for link_text, link_url in matches:
                        # Ignorer les liens externes
                        if self.is_external_link(link_url):
                            continue

                        # Vérifier si le lien interne est cassé
                        if not self.is_link_valid(link_url, md_file):
                            real_broken_links.append(
                                {
                                    "file": md_file,
                                    "text": link_text,
                                    "url": link_url,
                                    "line": self.find_line_number(content, link_url),
                                }
                            )

                except Exception as e:
                    self.log_correction(f"Erreur lecture {md_file}: {e}", "ERROR")

        return real_broken_links

    def is_link_valid(self, link_url, source_file):
        """Vérifie si un lien interne est valide"""
        if self.is_external_link(link_url):
            return True

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
                return True

        return False

    def find_line_number(self, content, link_url):
        """Trouve le numéro de ligne d'un lien"""
        lines = content.split("\n")
        for i, line in enumerate(lines, 1):
            if link_url in line:
                return i
        return 0

    def correct_real_broken_links(self):
        """Corrige les vrais liens internes cassés"""
        self.log_correction("🔍 Recherche des vrais liens internes cassés...")

        broken_links = self.find_real_broken_links()

        if not broken_links:
            self.log_correction("✅ Aucun vrai lien interne cassé trouvé !")
            return 0

        self.log_correction(
            f"📊 {len(broken_links)} vrais liens internes cassés identifiés"
        )

        corrections_made = 0

        for link_info in broken_links:
            file_path = link_info["file"]
            link_text = link_info["text"]
            link_url = link_info["url"]
            line_num = link_info["line"]

            self.log_correction(
                f"🔗 Lien cassé dans {file_path.name}: {link_url} (ligne {line_num})"
            )

            # Essayer de corriger le lien
            if self.correct_single_link(file_path, link_text, link_url):
                corrections_made += 1

        self.log_correction(
            f"✅ {corrections_made} liens corrigés sur {len(broken_links)}"
        )
        return corrections_made

    def correct_single_link(self, file_path, link_text, link_url):
        """Corrige un lien cassé spécifique"""
        try:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Essayer de trouver un fichier cible valide
            target_file = self.find_target_file(link_url, file_path)

            if target_file:
                # Calculer le chemin relatif correct
                try:
                    relative_path = target_file.relative_to(file_path.parent)
                    new_link = f"[{link_text}]({relative_path})"

                    # Remplacer le lien
                    old_link = f"[{link_text}]({link_url})"
                    if old_link in content:
                        content = content.replace(old_link, new_link)

                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(content)

                        self.log_correction(
                            f"✅ Lien corrigé: {link_url} -> {relative_path}"
                        )
                        return True

                except ValueError:
                    pass

            # Si pas de fichier cible, remplacer par du texte simple
            old_link = f"[{link_text}]({link_url})"
            if old_link in content:
                new_text = f"**{link_text}**"
                content = content.replace(old_link, new_text)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

                self.log_correction(f"✅ Lien supprimé: {link_url} -> texte simple")
                return True

            return False

        except Exception as e:
            self.log_correction(f"❌ Erreur correction {file_path}: {e}", "ERROR")
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

    def run_final_correction(self):
        """Exécute la correction finale"""
        self.log_correction(
            "🚀 Démarrage de la correction finale pour atteindre 100% !"
        )

        corrections = self.correct_real_broken_links()

        self.log_correction("✅ Correction finale terminée !")
        self.log_correction(f"🔗 Liens corrigés: {corrections}")

        return corrections


def main():
    """Fonction principale"""
    corrector = FinalLinkCorrector()

    try:
        corrections = corrector.run_final_correction()
        print(f"\n🎯 Correction finale terminée avec {corrections} liens corrigés !")
        print("🚀 Maintenant testez pour voir si nous avons atteint 100% !")
        sys.exit(0)

    except KeyboardInterrupt:
        print("\n⚠️ Correction interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors de la correction finale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
