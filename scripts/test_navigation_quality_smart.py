#!/usr/bin/env python3
"""
Script de test intelligent de la qualité de navigation de la documentation Athalia
Comprend la structure du projet et valide correctement les liens
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


class SmartNavigationQualityTester:
    def __init__(self, project_root: str = ".", docs_path: str = "docs"):
        self.project_root = Path(project_root)
        self.docs_path = Path(docs_path)
        self.navigation_results = {}
        self.broken_links = []
        self.validated_links = []

    def is_valid_file_reference(self, url: str, source_file: Path) -> bool:
        """Valide intelligemment une référence de fichier"""
        try:
            # Liens vers fichiers racine (non-critiques)
            if url in [
                "README.md",
                "CHANGELOG.md",
                "INVENTAIRE_COMPLET.md",
                "RAPPORT_FINAL.md",
                "FINAL_SUMMARY.md",
                "GENESIS.md",
                "CLEANUP_REPORT.md",
                "FAQ.md",
                "INSTALL.md",
            ]:
                # Vérifier si le fichier existe à la racine
                root_file = self.project_root / url
                return root_file.exists()

            # Liens vers fichiers dans docs/ (critiques)
            if url.endswith(".md"):
                # Lien relatif depuis le fichier source
                if url.startswith("./") or url.startswith("../"):
                    target_path = source_file.parent / url
                else:
                    target_path = source_file.parent / url

                # Vérifier l'existence
                if target_path.exists():
                    return True

                # Essayer depuis la racine de docs/
                docs_target = self.docs_path / url
                if docs_target.exists():
                    return True

                # Essayer depuis le dossier parent
                parent_target = source_file.parent.parent / url
                if parent_target.exists():
                    return True

                return False

            # Liens vers dossiers
            elif not url.endswith(".md") and not url.startswith("#"):
                # Vérifier si c'est un dossier
                if url.startswith("./") or url.startswith("../"):
                    target_path = source_file.parent / url
                else:
                    target_path = source_file.parent / url

                if target_path.exists() and target_path.is_dir():
                    return True

                # Essayer depuis la racine de docs/
                docs_target = self.docs_path / url
                if docs_target.exists() and docs_target.is_dir():
                    return True

                return False

            # Liens vers sections (commençant par #)
            elif url.startswith("#"):
                return True  # On ne peut pas valider les ancres facilement

            # Liens externes (http/https)
            elif url.startswith(("http://", "https://")):
                return True  # On ne peut pas valider les liens externes facilement

            return False

        except Exception as e:
            return False

    def extract_links_from_file(self, file_path: Path) -> List[Dict]:
        """Extrait tous les liens d'un fichier Markdown"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            links = []

            # Liens Markdown [texte](url)
            md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
            for text, url in md_links:
                links.append(
                    {
                        "type": "markdown",
                        "text": text,
                        "url": url,
                        "line": (
                            content[: content.find(f"[{text}]({url})")].count("\n") + 1
                        ),
                    }
                )

            # Liens vers fichiers locaux
            local_links = re.findall(r"\[([^\]]+)\]\(([^)]+\.md)\)", content)
            for text, url in local_links:
                links.append(
                    {
                        "type": "local_file",
                        "text": text,
                        "url": url,
                        "line": (
                            content[: content.find(f"[{text}]({url})")].count("\n") + 1
                        ),
                    }
                )

            # Références de fichiers
            file_refs = re.findall(r"`([^`]+\.md)`", content)
            for file_ref in file_refs:
                links.append(
                    {
                        "type": "file_reference",
                        "text": file_ref,
                        "url": file_ref,
                        "line": (
                            content[: content.find(f"`{file_ref}`")].count("\n") + 1
                        ),
                    }
                )

            return links

        except Exception as e:
            return []

    def validate_link_smart(self, link: Dict, source_file: Path) -> Dict:
        """Valide un lien de manière intelligente"""
        url = link["url"]
        validation_result = {
            "link": link,
            "source_file": str(source_file),
            "is_valid": False,
            "error_type": None,
            "suggested_fix": None,
            "is_critical": False,
        }

        # Déterminer si c'est un lien critique
        if url.endswith(".md") and not url.startswith("#"):
            validation_result["is_critical"] = True

        # Validation intelligente
        if self.is_valid_file_reference(url, source_file):
            validation_result["is_valid"] = True
        else:
            validation_result["error_type"] = "file_not_found"
            validation_result["suggested_fix"] = f"Vérifier le chemin: {url}"

        return validation_result

    def test_file_navigation_smart(self, file_path: Path) -> Dict:
        """Teste la navigation d'un fichier de manière intelligente"""
        relative_path = file_path.relative_to(self.docs_path)

        # Extraire tous les liens
        links = self.extract_links_from_file(file_path)

        # Valider chaque lien
        validated_links = []
        broken_links = []
        critical_broken_links = []

        for link in links:
            validation = self.validate_link_smart(link, file_path)
            validated_links.append(validation)

            if not validation["is_valid"]:
                broken_links.append(validation)
                self.broken_links.append(validation)

                if validation["is_critical"]:
                    critical_broken_links.append(validation)

        # Calculer le score de navigation (poids sur les liens critiques)
        total_links = len(validated_links)
        valid_links = len([link for link in validated_links if link["is_valid"]])
        critical_links = len([link for link in validated_links if link["is_critical"]])
        valid_critical_links = len(
            [
                link
                for link in validated_links
                if link["is_valid"] and link["is_critical"]
            ]
        )

        # Score pondéré : liens critiques comptent plus
        if total_links > 0:
            if critical_links > 0:
                critical_score = (
                    valid_critical_links / critical_links
                ) * 60  # 60% du score
                if (total_links - critical_links) > 0:
                    other_score = (
                        (valid_links - valid_critical_links)
                        / (total_links - critical_links)
                    ) * 40  # 40% du score
                else:
                    other_score = 0
                navigation_score = critical_score + other_score
            else:
                navigation_score = (valid_links / total_links) * 100
        else:
            navigation_score = 100

        return {
            "file_path": str(relative_path),
            "total_links": total_links,
            "valid_links": valid_links,
            "broken_links": len(broken_links),
            "critical_links": critical_links,
            "critical_broken_links": len(critical_broken_links),
            "navigation_score": navigation_score,
            "links": validated_links,
        }

    def test_all_files_smart(self) -> Dict:
        """Teste la navigation de tous les fichiers de manière intelligente"""
        print("🔍 Test intelligent de la qualité de navigation en cours...")

        md_files = list(self.docs_path.rglob("*.md"))
        print(f"📁 {len(md_files)} fichiers Markdown à tester")

        total_score = 0
        total_links = 0
        total_broken = 0
        total_critical_broken = 0

        for file_path in md_files:
            result = self.test_file_navigation_smart(file_path)
            self.navigation_results[str(file_path.relative_to(self.docs_path))] = result

            total_score += result["navigation_score"]
            total_links += result["total_links"]
            total_broken += result["broken_links"]
            total_critical_broken += result["critical_broken_links"]

        # Calculer les métriques globales
        avg_score = total_score / len(md_files) if md_files else 0
        link_success_rate = (
            ((total_links - total_broken) / total_links * 100)
            if total_links > 0
            else 100
        )

        return {
            "total_files": len(md_files),
            "total_links": total_links,
            "broken_links": total_broken,
            "critical_broken_links": total_critical_broken,
            "average_navigation_score": avg_score,
            "link_success_rate": link_success_rate,
        }

    def generate_smart_report(self) -> str:
        """Génère un rapport intelligent de test de navigation"""
        report = []
        report.append(
            "# 🔗 RAPPORT INTELLIGENT DE TEST NAVIGATION DOCUMENTATION ATHALIA"
        )
        report.append(f"**Date :** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append("")

        # Résumé global
        global_stats = self.test_all_files_smart()

        report.append("## 📊 RÉSUMÉ GLOBAL")
        report.append(f"- **Fichiers testés :** {global_stats['total_files']}")
        report.append(f"- **Liens totaux :** {global_stats['total_links']}")
        report.append(f"- **Liens cassés :** {global_stats['broken_links']}")
        report.append(
            f"- **Liens critiques cassés :** {global_stats['critical_broken_links']}"
        )
        report.append(
            f"- **Score de navigation moyen :** {global_stats['average_navigation_score']:.1f}/100"
        )
        report.append(
            f"- **Taux de succès des liens :** {global_stats['link_success_rate']:.1f}%"
        )
        report.append("")

        # Fichiers avec problèmes critiques
        critical_problematic_files = [
            f
            for f, r in self.navigation_results.items()
            if r["critical_broken_links"] > 0
        ]

        if critical_problematic_files:
            report.append("## 🚨 FICHIERS AVEC PROBLÈMES CRITIQUES")
            for file_path in critical_problematic_files[:10]:  # Top 10
                result = self.navigation_results[file_path]
                report.append(
                    f"- **`{file_path}`** - {result['critical_broken_links']} liens critiques cassés (score: {result['navigation_score']:.1f}/100)"
                )
            if len(critical_problematic_files) > 10:
                report.append(f"- ... et {len(critical_problematic_files) - 10} autres")
            report.append("")

        # Fichiers avec navigation parfaite
        perfect_files = [
            f
            for f, r in self.navigation_results.items()
            if r["navigation_score"] == 100
        ]

        if perfect_files:
            report.append("## ✅ FICHIERS AVEC NAVIGATION PARFAITE")
            for file_path in perfect_files[:10]:  # Top 10
                result = self.navigation_results[file_path]
                report.append(
                    f"- **`{file_path}`** - {result['total_links']} liens valides"
                )
            if len(perfect_files) > 10:
                report.append(f"- ... et {len(perfect_files) - 10} autres")
            report.append("")

        # Détails des liens critiques cassés
        critical_broken = [link for link in self.broken_links if link["is_critical"]]
        if critical_broken:
            report.append("## 🔧 DÉTAILS DES LIENS CRITIQUES CASSÉS")
            for broken_link in critical_broken[:20]:  # Top 20
                report.append(
                    f"- **`{broken_link['source_file']}`** (ligne {broken_link['link']['line']})"
                )
                report.append(
                    f"  - Lien : `{broken_link['link']['text']}` → `{broken_link['link']['url']}`"
                )
                report.append(f"  - Erreur : {broken_link['error_type']}")
                report.append(f"  - Solution : {broken_link['suggested_fix']}")
                report.append("")
            if len(critical_broken) > 20:
                report.append(
                    f"- ... et {len(critical_broken) - 20} autres liens critiques cassés"
                )

        return "\n".join(report)

    def save_smart_results(
        self, output_file: str = "navigation_test_smart_results.json"
    ):
        """Sauvegarde les résultats intelligents au format JSON"""
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "test_date": datetime.now().isoformat(),
                    "global_stats": self.test_all_files_smart(),
                    "file_results": self.navigation_results,
                    "broken_links": self.broken_links,
                    "critical_broken_links": [
                        link for link in self.broken_links if link["is_critical"]
                    ],
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

        print(f"💾 Résultats intelligents sauvegardés dans {output_file}")


# Ligne vide pour respecter PEP 8


def main():
    """Fonction principale"""
    tester = SmartNavigationQualityTester()

    # Test de navigation intelligent
    print("🚀 Test intelligent de la qualité de navigation de la documentation Athalia")
    print("=" * 80)

    # Générer le rapport
    report = tester.generate_smart_report()

    # Affichage du rapport
    print(report)
    print("=" * 80)

    # Sauvegarder les résultats
    tester.save_smart_results()

    # Statistiques rapides
    global_stats = tester.test_all_files_smart()
    print(f"\n📊 RÉSUMÉ RAPIDE :")
    print(f"✅ Navigation moyenne : {global_stats['average_navigation_score']:.1f}/100")
    print(f"🔗 Taux de succès des liens : {global_stats['link_success_rate']:.1f}%")
    print(f"🚨 Liens cassés totaux : {global_stats['broken_links']}")
    print(f"🚨 Liens critiques cassés : {global_stats['critical_broken_links']}")


if __name__ == "__main__":
    main()
