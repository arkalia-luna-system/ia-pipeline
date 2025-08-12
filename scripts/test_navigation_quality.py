#!/usr/bin/env python3
"""
Script de test de la qualité de navigation de la documentation Athalia
Teste les liens internes et la cohérence de la structure
"""

import json
import re
from datetime import datetime
from pathlib import Path


class NavigationQualityTester:
    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.navigation_results = {}
        self.broken_links = []
        self.orphaned_files = []

    def extract_links_from_file(self, file_path: Path) -> list[dict]:
        """Extrait tous les liens d'un fichier Markdown"""
        try:
            with open(file_path, encoding="utf-8") as f:
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

        except Exception:
            return []

    def validate_link(self, link: dict, source_file: Path) -> dict:
        """Valide un lien individuel"""
        url = link["url"]
        validation_result = {
            "link": link,
            "source_file": str(source_file),
            "is_valid": False,
            "error_type": None,
            "suggested_fix": None,
        }

        try:
            # Liens locaux vers fichiers Markdown
            if url.endswith(".md"):
                # Lien relatif
                if url.startswith("./") or url.startswith("../"):
                    target_path = source_file.parent / url
                else:
                    target_path = source_file.parent / url

                if target_path.exists():
                    validation_result["is_valid"] = True
                else:
                    validation_result["error_type"] = "file_not_found"
                    validation_result["suggested_fix"] = (
                        f"Vérifier le chemin: {target_path}"
                    )

            # Liens vers sections (commençant par #)
            elif url.startswith("#"):
                validation_result["is_valid"] = (
                    True  # On ne peut pas valider les ancres facilement
                )

            # Liens externes (http/https)
            elif url.startswith(("http://", "https://")):
                validation_result["is_valid"] = (
                    True  # On ne peut pas valider les liens externes facilement
                )

            # Liens vers dossiers
            elif not url.endswith(".md") and not url.startswith("#"):
                # Vérifier si c'est un dossier
                if url.startswith("./") or url.startswith("../"):
                    target_path = source_file.parent / url
                else:
                    target_path = source_file.parent / url

                if target_path.exists() and target_path.is_dir():
                    validation_result["is_valid"] = True
                else:
                    validation_result["error_type"] = "directory_not_found"
                    validation_result["suggested_fix"] = (
                        f"Vérifier le dossier: {target_path}"
                    )

            else:
                validation_result["error_type"] = "unknown_link_type"
                validation_result["suggested_fix"] = "Type de lien non reconnu"

        except Exception as e:
            validation_result["error_type"] = "validation_error"
            validation_result["suggested_fix"] = f"Erreur de validation: {str(e)}"

        return validation_result

    def test_file_navigation(self, file_path: Path) -> dict:
        """Teste la navigation d'un fichier individuel"""
        relative_path = file_path.relative_to(self.docs_path)

        # Extraire tous les liens
        links = self.extract_links_from_file(file_path)

        # Valider chaque lien
        validated_links = []
        broken_links = []

        for link in links:
            validation = self.validate_link(link, file_path)
            validated_links.append(validation)

            if not validation["is_valid"]:
                broken_links.append(validation)
                self.broken_links.append(validation)

        # Calculer le score de navigation
        total_links = len(validated_links)
        valid_links = len([link for link in validated_links if link["is_valid"]])

        navigation_score = (valid_links / total_links * 100) if total_links > 0 else 100

        return {
            "file_path": str(relative_path),
            "total_links": total_links,
            "valid_links": valid_links,
            "broken_links": len(broken_links),
            "navigation_score": navigation_score,
            "links": validated_links,
        }

    def test_all_files(self) -> dict:
        """Teste la navigation de tous les fichiers"""
        print("🔍 Test de la qualité de navigation en cours...")

        md_files = list(self.docs_path.rglob("*.md"))
        print(f"📁 {len(md_files)} fichiers Markdown à tester")

        total_score = 0
        total_links = 0
        total_broken = 0

        for file_path in md_files:
            result = self.test_file_navigation(file_path)
            self.navigation_results[str(file_path.relative_to(self.docs_path))] = result

            total_score += result["navigation_score"]
            total_links += result["total_links"]
            total_broken += result["broken_links"]

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
            "average_navigation_score": avg_score,
            "link_success_rate": link_success_rate,
        }

    def generate_report(self) -> str:
        """Génère un rapport de test de navigation"""
        report = []
        report.append("# 🔗 RAPPORT DE TEST NAVIGATION DOCUMENTATION ATHALIA")
        report.append(f"**Date :** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append("")

        # Résumé global
        global_stats = self.test_all_files()

        report.append("## 📊 RÉSUMÉ GLOBAL")
        report.append(f"- **Fichiers testés :** {global_stats['total_files']}")
        report.append(f"- **Liens totaux :** {global_stats['total_links']}")
        report.append(f"- **Liens cassés :** {global_stats['broken_links']}")
        report.append(
            f"- **Score de navigation moyen :** {global_stats['average_navigation_score']:.1f}/100"
        )
        report.append(
            f"- **Taux de succès des liens :** {global_stats['link_success_rate']:.1f}%"
        )
        report.append("")

        # Fichiers avec problèmes
        problematic_files = [
            f for f, r in self.navigation_results.items() if r["broken_links"] > 0
        ]

        if problematic_files:
            report.append("## 🚨 FICHIERS AVEC PROBLÈMES DE NAVIGATION")
            for file_path in problematic_files[:10]:  # Top 10
                result = self.navigation_results[file_path]
                report.append(
                    f"- **`{file_path}`** - {result['broken_links']} liens cassés (score: {result['navigation_score']:.1f}/100)"
                )
            if len(problematic_files) > 10:
                report.append(f"- ... et {len(problematic_files) - 10} autres")
            report.append("")

        # Fichiers excellents
        excellent_files = [
            f
            for f, r in self.navigation_results.items()
            if r["navigation_score"] == 100
        ]

        if excellent_files:
            report.append("## ✅ FICHIERS AVEC NAVIGATION PARFAITE")
            for file_path in excellent_files[:10]:  # Top 10
                result = self.navigation_results[file_path]
                report.append(
                    f"- **`{file_path}`** - {result['total_links']} liens valides"
                )
            if len(excellent_files) > 10:
                report.append(f"- ... et {len(excellent_files) - 10} autres")
            report.append("")

        # Détails des liens cassés
        if self.broken_links:
            report.append("## 🔧 DÉTAILS DES LIENS CASSÉS")
            for broken_link in self.broken_links[:20]:  # Top 20
                report.append(
                    f"- **`{broken_link['source_file']}`** (ligne {broken_link['link']['line']})"
                )
                report.append(
                    f"  - Lien : `{broken_link['link']['text']}` → `{broken_link['link']['url']}`"
                )
                report.append(f"  - Erreur : {broken_link['error_type']}")
                report.append(f"  - Solution : {broken_link['suggested_fix']}")
                report.append("")
            if len(self.broken_links) > 20:
                report.append(
                    f"- ... et {len(self.broken_links) - 20} autres liens cassés"
                )

        return "\n".join(report)

    def save_results(self, output_file: str = "navigation_test_results.json"):
        """Sauvegarde les résultats au format JSON"""
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "test_date": datetime.now().isoformat(),
                    "global_stats": self.test_all_files(),
                    "file_results": self.navigation_results,
                    "broken_links": self.broken_links,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

        print(f"💾 Résultats sauvegardés dans {output_file}")


# Ligne vide pour respecter PEP 8


def main():
    """Fonction principale"""
    tester = NavigationQualityTester()

    # Test de navigation
    print("🚀 Test de la qualité de navigation de la documentation Athalia")
    print("=" * 70)

    # Générer le rapport
    report = tester.generate_report()

    # Affichage du rapport
    print(report)
    print("=" * 70)

    # Sauvegarder les résultats
    tester.save_results()

    # Statistiques rapides
    global_stats = tester.test_all_files()
    print("\n📊 RÉSUMÉ RAPIDE :")
    print(f"✅ Navigation moyenne : {global_stats['average_navigation_score']:.1f}/100")
    print(f"🔗 Taux de succès des liens : {global_stats['link_success_rate']:.1f}%")
    print(f"🚨 Liens cassés : {global_stats['broken_links']}")


if __name__ == "__main__":
    main()
