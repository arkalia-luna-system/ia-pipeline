#!/usr/bin/env python3
"""
🔗 Test Parfait de la Qualité de Navigation - Documentation Athalia
Version améliorée qui ne considère pas les liens externes comme cassés
"""

import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


class PerfectNavigationTester:
    def __init__(self):
        self.workspace = Path("/Volumes/T7/athalia-dev-setup")
        self.docs_dir = self.workspace / "docs"
        self.results_file = self.workspace / "navigation_test_perfect_results.json"

        # Patterns pour les liens externes valides
        self.valid_external_patterns = [
            r"https?://[^\s]+",  # URLs HTTP/HTTPS
            r"mailto:[^\s]+",  # Emails
            r"#[^\s]+",  # Ancres internes
        ]

        # Sites externes considérés comme valides
        self.valid_external_sites = [
            "github.com",
            "docs.github.com",
            "www.github.com",
            "python.org",
            "www.python.org",
            "readthedocs.io",
            "docs.readthedocs.io",
            "pycqa.org",
            "flake8.pycqa.org",
            "black.readthedocs.io",
            "black.vercel.app",
            "mypy.readthedocs.io",
            "mypy-lang.org",
            "bandit.readthedocs.io",
            "bandit.readthedocs.io",
            "pre-commit.com",
            "www.pre-commit.com",
            "mermaid-js.github.io",
            "mermaid.live",
            "tailwindcss.com",
            "www.tailwindcss.com",
            "vitejs.dev",
            "www.vitejs.dev",
            "react.dev",
            "reactjs.org",
            "typescriptlang.org",
            "www.typescriptlang.org",
            "recharts.org",
            "www.recharts.org",
            "tailwindui.com",
            "www.tailwindui.com",
            "webfx.com",
            "www.webfx.com",
            "example.com",
            "www.example.com",  # Pour les exemples
        ]

    def is_valid_external_link(self, url):
        """Vérifie si un lien externe est valide"""
        if not url.startswith(("http://", "https://", "mailto:", "#")):
            return False

        # Vérifier si c'est un site externe valide
        if url.startswith(("http://", "https://")):
            try:
                parsed = urlparse(url)
                domain = parsed.netloc.lower()
                return any(
                    valid_site in domain for valid_site in self.valid_external_sites
                )
            except Exception:
                return False

        return True

    def is_broken_link(self, link, file_path):
        """Vérifie si un lien est cassé (version améliorée)"""
        if self.is_valid_external_link(link):
            return False  # Liens externes valides ne sont pas cassés

        if link.startswith(("http://", "https://", "mailto:", "#")):
            return False

        # Gestion des chemins relatifs
        if link.startswith("/"):
            target_path = self.workspace / link.lstrip("/")
        else:
            target_path = file_path.parent / link

        return not target_path.exists()

    def test_file_navigation(self, file_path):
        """Teste la navigation d'un fichier Markdown"""
        try:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Détection des liens Markdown
            link_patterns = [
                r"\[([^\]]+)\]\(([^)]+)\)",  # [texte](lien)
                r"!\[([^\]]*)\]\(([^)]+)\)",  # ![alt](lien)
                r"`([^`]+)`",  # `lien`
                r"([a-zA-Z0-9_\-\.]+\.md)",  # fichier.md
            ]

            links = []
            for pattern in link_patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        if len(match) == 2:
                            text, url = match
                        else:
                            url = match[0]
                    else:
                        url = match

                    if url and not url.startswith("#"):
                        links.append(
                            {
                                "type": (
                                    "markdown" if "[" in pattern else "file_reference"
                                ),
                                "text": (
                                    text
                                    if isinstance(match, tuple) and len(match) > 0
                                    else url
                                ),
                                "url": url,
                                "line": content[: content.find(url)].count("\n") + 1,
                            }
                        )

            # Vérification des liens
            valid_links = []
            broken_links = []

            for link_info in links:
                url = link_info["url"]
                if self.is_broken_link(url, file_path):
                    broken_links.append(link_info)
                else:
                    valid_links.append(link_info)

            # Calcul du score
            total_links = len(links)
            if total_links == 0:
                navigation_score = 100.0
            else:
                navigation_score = (len(valid_links) / total_links) * 100

            return {
                "file_path": str(file_path.relative_to(self.workspace)),
                "total_links": total_links,
                "valid_links": len(valid_links),
                "broken_links": len(broken_links),
                "critical_links": total_links,
                "critical_broken_links": len(broken_links),
                "navigation_score": round(navigation_score, 1),
                "links": links,
            }

        except Exception as e:
            return {
                "file_path": str(file_path.relative_to(self.workspace)),
                "total_links": 0,
                "valid_links": 0,
                "broken_links": 0,
                "critical_links": 0,
                "critical_broken_links": 0,
                "navigation_score": 0.0,
                "links": [],
                "error": str(e),
            }

    def run_perfect_test(self):
        """Exécute le test parfait de navigation"""
        print("🚀 Test parfait de la qualité de navigation de la documentation Athalia")
        print("=" * 80)
        print("🔍 Test parfait de navigation en cours...")

        # Recherche des fichiers Markdown
        md_files = list(self.docs_dir.rglob("*.md"))
        print(f"📁 {len(md_files)} fichiers Markdown à tester")

        # Test de chaque fichier
        file_results = {}
        total_links = 0
        total_broken_links = 0
        total_critical_broken_links = 0
        scores = []

        for md_file in md_files:
            result = self.test_file_navigation(md_file)
            file_results[result["file_path"]] = result

            total_links += result["total_links"]
            total_broken_links += result["broken_links"]
            total_critical_broken_links += result["critical_broken_links"]
            scores.append(result["navigation_score"])

        # Calcul des statistiques globales
        if scores:
            average_navigation_score = sum(scores) / len(scores)
            link_success_rate = (
                ((total_links - total_broken_links) / total_links * 100)
                if total_links > 0
                else 100
            )
        else:
            average_navigation_score = 0
            link_success_rate = 0

        # Génération du rapport
        report = {
            "test_date": datetime.now().isoformat(),
            "global_stats": {
                "total_files": len(md_files),
                "total_links": total_links,
                "broken_links": total_broken_links,
                "critical_broken_links": total_critical_broken_links,
                "average_navigation_score": round(average_navigation_score, 1),
                "link_success_rate": round(link_success_rate, 1),
            },
            "file_results": file_results,
        }

        # Sauvegarde des résultats
        with open(self.results_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Affichage du rapport
        print("\n# 🔗 RAPPORT PARFAIT DE TEST NAVIGATION DOCUMENTATION ATHALIA")
        print(f"**Date :** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print()
        print("## 📊 RÉSUMÉ GLOBAL")
        print(f"- **Fichiers testés :** {len(md_files)}")
        print(f"- **Liens totaux :** {total_links}")
        print(f"- **Liens cassés :** {total_broken_links}")
        print(f"- **Liens critiques cassés :** {total_critical_broken_links}")
        print(
            f"- **Score de navigation moyen :** {round(average_navigation_score, 1)}/100"
        )
        print(f"- **Taux de succès des liens :** {round(link_success_rate, 1)}%")
        print()

        # Fichiers avec problèmes
        problematic_files = {
            k: v for k, v in file_results.items() if v["broken_links"] > 0
        }
        if problematic_files:
            print("## 🚨 FICHIERS AVEC PROBLÈMES")
            for file_path, result in sorted(
                problematic_files.items(),
                key=lambda x: x[1]["broken_links"],
                reverse=True,
            ):
                print(
                    f"- **`{file_path}`** - {result['broken_links']} liens cassés (score: {result['navigation_score']}/100)"
                )
        else:
            print("## ✅ TOUS LES FICHIERS ONT UNE NAVIGATION PARFAITE !")

        print()
        print("## ✅ FICHIERS AVEC NAVIGATION PARFAITE")
        perfect_files = {
            k: v for k, v in file_results.items() if v["broken_links"] == 0
        }
        for file_path, result in list(perfect_files.items())[:10]:
            print(f"- **`{file_path}`** - {result['valid_links']} liens valides")
        if len(perfect_files) > 10:
            print(f"- ... et {len(perfect_files) - 10} autres")

        print()
        print("=" * 80)
        print("🔍 Test parfait de navigation en cours...")
        print(f"📁 {len(md_files)} fichiers Markdown à tester")
        print(f"💾 Résultats parfaits sauvegardés dans {self.results_file}")
        print("🔍 Test parfait de navigation en cours...")
        print(f"📁 {len(md_files)} fichiers Markdown à tester")
        print()
        print("📊 RÉSUMÉ RAPIDE :")
        print(f"✅ Navigation moyenne : {round(average_navigation_score, 1)}/100")
        print(f"🔗 Taux de succès : {round(link_success_rate, 1)}%")
        print(f"🚨 Liens cassés totaux : {total_broken_links}")
        print(f"🚨 Liens critiques cassés : {total_critical_broken_links}")

        return report


def main():
    """Fonction principale"""
    tester = PerfectNavigationTester()
    try:
        report = tester.run_perfect_test()
        print("\n✅ Test parfait terminé avec succès !")
        print(
            f"📊 Score final : {report['global_stats']['average_navigation_score']}/100"
        )
        return 0
    except Exception as e:
        print(f"❌ Erreur lors du test parfait : {e}")
        return 1


if __name__ == "__main__":
    exit(main())
