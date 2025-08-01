#!/usr/bin/env python3
"""
Script de correction des problèmes courants dans les fichiers Markdown
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple


def find_markdown_files(root_dir: str = ".") -> List[Path]:
    """Trouve tous les fichiers Markdown dans le projet"""
    markdown_files = []
    for root, dirs, files in os.walk(root_dir):
        # Ignorer les dossiers à exclure
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".")
            and d not in ["node_modules", "__pycache__", ".git"]
        ]

        for file in files:
            if file.endswith(".md"):
                markdown_files.append(Path(root) / file)

    return markdown_files


def analyze_markdown_file(file_path: Path) -> Dict[str, List[str]]:
    """Analyse un fichier Markdown pour identifier les problèmes"""
    issues = {
        "empty_headers": [],
        "broken_links": [],
        "inconsistent_formatting": [],
        "todo_items": [],
        "other_issues": [],
    }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split("\n")

        for i, line in enumerate(lines, 1):
            # Vérifier les en-têtes vides
            if re.match(r"^#{1,6}\s*$", line):
                issues["empty_headers"].append(f"Ligne {i}: En-tête vide")

            # Vérifier les TODO/FIXME
            if re.search(r"\b(TODO|FIXME|HACK)\b", line, re.IGNORECASE):
                issues["todo_items"].append(f"Ligne {i}: {line.strip()}")

            # Vérifier les liens cassés (basique)
            link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
            if link_match:
                link_text, link_url = link_match.groups()
                if link_url.startswith("./") or link_url.startswith("../"):
                    # Vérifier si le fichier existe
                    link_path = file_path.parent / link_url
                    if not link_path.exists() and not link_url.endswith("/"):
                        issues["broken_links"].append(
                            f"Ligne {i}: Lien cassé [{link_text}]({link_url})"
                        )

            # Vérifier le formatage incohérent
            if re.match(r"^[[:space:]]*#[[:space:]]*[^#]", line):
                if not re.match(r"^#{1,6}\s+", line):
                    issues["inconsistent_formatting"].append(
                        f"Ligne {i}: Formatage d'en-tête incohérent"
                    )

    except Exception as e:
        issues["other_issues"].append(f"Erreur lors de l'analyse: {e}")

    return issues


def fix_common_issues(file_path: Path) -> List[str]:
    """Corrige les problèmes courants dans un fichier Markdown"""
    fixes_applied = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Corriger les en-têtes vides
        content = re.sub(
            r"^(#{1,6})\s*$", r"\1 En-tête à compléter", content, flags=re.MULTILINE
        )

        # Corriger les espaces multiples
        content = re.sub(r"[ ]{3,}", "  ", content)

        # Corriger les lignes vides multiples
        content = re.sub(r"\n{4,}", "\n\n\n", content)

        # Corriger les listes mal formatées
        content = re.sub(
            r"^(\s*)[-*+]\s*$", r"\1- Item à compléter", content, flags=re.MULTILINE
        )

        # Corriger les liens relatifs cassés (basique)
        # Cette partie nécessiterait une analyse plus approfondie

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            fixes_applied.append("Corrections de formatage appliquées")

    except Exception as e:
        fixes_applied.append(f"Erreur lors de la correction: {e}")

    return fixes_applied


def main():
    """Fonction principale"""
    print("🔍 Analyse des fichiers Markdown...")

    markdown_files = find_markdown_files()
    print(f"📁 {len(markdown_files)} fichiers Markdown trouvés")

    total_issues = 0
    files_with_issues = 0

    for file_path in markdown_files:
        issues = analyze_markdown_file(file_path)

        # Compter les problèmes
        file_issues = sum(len(issue_list) for issue_list in issues.values())
        if file_issues > 0:
            files_with_issues += 1
            total_issues += file_issues

            print(f"\n📄 {file_path}")
            for issue_type, issue_list in issues.items():
                if issue_list:
                    print(f"  ⚠️  {issue_type}: {len(issue_list)} problèmes")
                    for issue in issue_list[:3]:  # Afficher les 3 premiers
                        print(f"    - {issue}")
                    if len(issue_list) > 3:
                        print(f"    ... et {len(issue_list) - 3} autres")

    print(f"\n📊 Résumé:")
    print(f"  - Fichiers analysés: {len(markdown_files)}")
    print(f"  - Fichiers avec problèmes: {files_with_issues}")
    print(f"  - Total des problèmes: {total_issues}")

    if total_issues > 0:
        print(f"\n🔧 Application des corrections automatiques...")
        for file_path in markdown_files:
            fixes = fix_common_issues(file_path)
            if fixes:
                print(f"  ✅ {file_path}: {', '.join(fixes)}")

    print(f"\n🎉 Analyse terminée!")


if __name__ == "__main__":
    main()
