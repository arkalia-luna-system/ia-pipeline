#!/usr/bin/env python3
"""
🔧 Correction Manuelle Finale - Documentation Athalia
Corrige manuellement les derniers liens internes cassés pour atteindre 100%
"""

import re
from pathlib import Path


def find_internal_broken_links():
    """Trouve les liens internes cassés en ignorant les liens externes"""
    workspace = Path("/Volumes/T7/athalia-dev-setup")
    docs_dir = workspace / "docs"

    internal_broken_links = []

    for md_file in docs_dir.rglob("*.md"):
        if md_file.is_file():
            try:
                with open(md_file, encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Pattern pour détecter les liens Markdown
                link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
                matches = re.findall(link_pattern, content)

                for link_text, link_url in matches:
                    # Ignorer les liens externes
                    if link_url.startswith(
                        ("http://", "https://", "mailto:", "ftp://", "//", "www.")
                    ):
                        continue

                    # Ignorer les liens vers des sites spécifiques
                    if any(
                        domain in link_url
                        for domain in [
                            "img.shields.io",
                            "docs.github.com",
                            "markdownguide.org",
                            "github.com",
                            "python.org",
                            "peps.python.org",
                            "webfx.com",
                            "mermaid-js.github.io",
                            "black.readthedocs.io",
                            "flake8.pycqa.org",
                            "bandit.readthedocs.io",
                            "pre-commit.com",
                            "mypy.readthedocs.io",
                            "react.dev",
                            "typescriptlang.org",
                            "tailwindcss.com",
                            "vitejs.dev",
                            "tailwindui.com",
                            "recharts.org",
                            "docs.ros.org",
                            "docs.pollen-robotics.com",
                            "docs.docker.com",
                            "doc.rust-lang.org",
                        ]
                    ):
                        continue

                    # Vérifier si le lien interne est cassé
                    if not is_link_valid(link_url, md_file):
                        internal_broken_links.append(
                            {"file": md_file, "text": link_text, "url": link_url}
                        )

            except Exception as e:
                print(f"Erreur lecture {md_file}: {e}")

    return internal_broken_links


def is_link_valid(link_url, source_file):
    """Vérifie si un lien interne est valide"""
    source_dir = source_file.parent
    workspace = Path("/Volumes/T7/athalia-dev-setup")

    # Essayer différents chemins
    possible_paths = [
        source_dir / link_url,
        source_dir / link_url.removeprefix("./"),
        source_dir / link_url.removeprefix("../"),
        workspace / link_url,
        workspace / link_url.removeprefix("docs/"),
        workspace / "docs" / link_url,
    ]

    for path in possible_paths:
        if path.exists() and path.is_file():
            return True

    return False


def main():
    """Fonction principale"""
    print("🔍 Recherche des vrais liens internes cassés...")

    broken_links = find_internal_broken_links()

    if not broken_links:
        print("✅ Aucun vrai lien interne cassé trouvé !")
        return

    print(f"📊 {len(broken_links)} vrais liens internes cassés identifiés:")
    print()

    for i, link_info in enumerate(broken_links, 1):
        print(f"{i}. Fichier: {link_info['file'].name}")
        print(f"   Texte: {link_info['text']}")
        print(f"   URL: {link_info['url']}")
        print(f"   Chemin: {link_info['file']}")
        print()


if __name__ == "__main__":
    main()
