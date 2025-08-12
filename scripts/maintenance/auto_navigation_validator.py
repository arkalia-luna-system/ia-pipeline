#!/usr/bin/env python3
"""
🔗 Validateur Automatique de Navigation - Documentation Athalia
Automatise la validation et la maintenance de la qualité de navigation
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path


class NavigationValidator:
    def __init__(self):
        self.workspace = Path("/Volumes/T7/athalia-dev-setup")
        self.docs_dir = self.workspace / "docs"
        self.results_file = self.workspace / "navigation_validation_results.json"
        self.threshold_score = 80.0  # Score minimum acceptable

    def run_integrated_navigation_test(self):
        """Exécute un test de navigation intégré"""
        try:
            # Test basique de navigation
            total_files = 0
            broken_links = 0
            critical_broken_links = 0

            for md_file in self.docs_dir.rglob("*.md"):
                total_files += 1
                try:
                    with open(md_file, encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    # Détection simple des liens cassés
                    detected_links = self.detect_broken_links(content, md_file)
                    if detected_links:
                        broken_links += len(detected_links)
                        if len(detected_links) > 5:  # Plus de 5 liens cassés = critique
                            critical_broken_links += 1

                except Exception as e:
                    print(f"⚠️ Erreur lors de l'analyse de {md_file}: {e}")
                    broken_links += 1

            # Calcul du score
            if total_files == 0:
                score = 100
            else:
                score = max(0, 100 - (broken_links * 2) - (critical_broken_links * 10))

            return {
                "score": score,
                "critical_broken_links": critical_broken_links,
                "total_broken_links": broken_links,
                "files_tested": total_files,
                "link_success_rate": max(
                    0, 100 - (broken_links / max(total_files, 1) * 100)
                ),
            }

        except Exception as e:
            print(f"❌ Erreur lors du test intégré: {e}")
            return {
                "score": 0,
                "critical_broken_links": 0,
                "total_broken_links": 0,
                "files_tested": 0,
                "link_success_rate": 0,
            }

    def run_navigation_test(self):
        """Exécute le test de navigation intelligent intégré"""
        print("🔍 Exécution du test de navigation intelligent intégré...")
        try:
            # Test de navigation intégré au lieu d'appeler un script externe
            results = self.run_integrated_navigation_test()
            print("✅ Test de navigation intégré exécuté avec succès")
            return results
        except Exception as e:
            print(f"❌ Erreur lors de l'exécution du test intégré: {e}")
            return None

    def parse_navigation_results(self):
        """Parse les résultats du test de navigation"""
        try:
            with open(self.workspace / "navigation_test_smart_results.json") as f:
                data = json.load(f)

            return {
                "score": data.get("navigation_score", 0),
                "critical_links": data.get("critical_broken_links", 0),
                "total_links": data.get("total_broken_links", 0),
                "files_tested": data.get("files_tested", 0),
                "success_rate": data.get("link_success_rate", 0),
            }
        except Exception as e:
            print(f"❌ Erreur lors du parsing des résultats: {e}")
            return None

    def identify_problematic_files(self):
        """Identifie les fichiers avec des problèmes de navigation"""
        print("🔍 Identification des fichiers problématiques...")

        problematic_files = []

        # Recherche des fichiers avec des liens cassés
        for md_file in self.docs_dir.rglob("*.md"):
            try:
                # Vérifier si le nom de fichier n'est pas trop long
                if len(str(md_file)) > 200:
                    problematic_files.append(
                        {
                            "file": str(md_file.relative_to(self.workspace)),
                            "broken_links": ["nom_fichier_trop_long"],
                            "severity": 10,  # Priorité haute
                        }
                    )
                    continue

                with open(md_file, encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Détection des liens cassés potentiels
                broken_links = self.detect_broken_links(content, md_file)

                if broken_links:
                    problematic_files.append(
                        {
                            "file": str(md_file.relative_to(self.workspace)),
                            "broken_links": broken_links,
                            "severity": len(broken_links),
                        }
                    )

            except Exception as e:
                print(f"⚠️ Erreur lors de l'analyse de {md_file}: {e}")

        return sorted(problematic_files, key=lambda x: x["severity"], reverse=True)

    def detect_broken_links(self, content, file_path):
        """Détecte les liens cassés dans le contenu"""
        broken_links = []

        # Patterns pour détecter les liens Markdown
        link_patterns = [
            r"\[([^\]]+)\]\(([^)]+)\)",  # [texte](lien)
            r"`([^`]+)`",  # `lien`
            r"([a-zA-Z0-9_\-\.]+\.md)",  # fichier.md
        ]

        for pattern in link_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                if isinstance(match, tuple):
                    link = match[1]
                else:
                    link = match

                if self.is_broken_link(link, file_path):
                    broken_links.append(link)

        return list(set(broken_links))

    def is_broken_link(self, link, file_path):
        """Vérifie si un lien est cassé"""
        if link.startswith(("http://", "https://", "mailto:", "#")):
            return False

        if link.startswith("/"):
            target_path = self.workspace / link.lstrip("/")
        else:
            target_path = file_path.parent / link

        return not target_path.exists()

    def generate_cleanup_report(self, problematic_files):
        """Génère un rapport de nettoyage recommandé"""
        print("📊 Génération du rapport de nettoyage...")

        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_problematic_files": len(problematic_files),
                "high_priority": len(
                    [f for f in problematic_files if f["severity"] > 5]
                ),
                "medium_priority": len(
                    [f for f in problematic_files if 2 < f["severity"] <= 5]
                ),
                "low_priority": len(
                    [f for f in problematic_files if f["severity"] <= 2]
                ),
            },
            "recommendations": [],
        }

        # Recommandations par priorité
        high_priority = [f for f in problematic_files if f["severity"] > 5]
        if high_priority:
            report["recommendations"].append(
                {
                    "priority": "HAUTE",
                    "action": "Supprimer ou corriger immédiatement",
                    "files": [f["file"] for f in high_priority[:3]],  # Top 3
                }
            )

        medium_priority = [f for f in problematic_files if 2 < f["severity"] <= 5]
        if medium_priority:
            report["recommendations"].append(
                {
                    "priority": "MOYENNE",
                    "action": "Corriger les liens cassés",
                    "files": [f["file"] for f in medium_priority[:5]],  # Top 5
                }
            )

        return report

    def save_results(self, navigation_results, problematic_files, cleanup_report):
        """Sauvegarde les résultats de validation"""
        results = {
            "timestamp": datetime.now().isoformat(),
            "navigation_quality": navigation_results,
            "problematic_files": problematic_files,
            "cleanup_report": cleanup_report,
            "recommendations": self.generate_recommendations(
                navigation_results, problematic_files
            ),
        }

        with open(self.results_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"💾 Résultats sauvegardés dans {self.results_file}")

    def generate_recommendations(self, navigation_results, problematic_files):
        """Génère des recommandations d'action"""
        recommendations = []

        if navigation_results:
            score = navigation_results["score"]
            critical_links = navigation_results["critical_links"]

            if score < self.threshold_score:
                recommendations.append(
                    {
                        "type": "URGENT",
                        "message": (
                            f"Score de navigation ({score}/100) en dessous du seuil ({self.threshold_score}/100)"
                        ),
                        "action": "Corriger immédiatement les liens critiques",
                    }
                )

            if critical_links > 50:
                recommendations.append(
                    {
                        "type": "HIGH",
                        "message": f"Trop de liens critiques cassés ({critical_links})",
                        "action": (
                            "Nettoyer les fichiers obsolètes et corriger les liens"
                        ),
                    }
                )

        if problematic_files:
            high_severity = len([f for f in problematic_files if f["severity"] > 5])
            if high_severity > 0:
                recommendations.append(
                    {
                        "type": "HIGH",
                        "message": (
                            f"{high_severity} fichiers avec de nombreux liens cassés"
                        ),
                        "action": "Évaluer la suppression de ces fichiers",
                    }
                )

        return recommendations

    def run_validation(self):
        """Exécute la validation complète de la navigation"""
        print("🚀 Démarrage de la validation automatique de navigation...")
        print("=" * 60)

        # 1. Test de navigation
        navigation_results = self.run_navigation_test()

        # 2. Identification des fichiers problématiques
        problematic_files = self.identify_problematic_files()

        # 3. Rapport de nettoyage
        cleanup_report = self.generate_cleanup_report(problematic_files)

        # 4. Sauvegarde des résultats
        self.save_results(navigation_results, problematic_files, cleanup_report)

        # 5. Affichage du résumé
        self.display_summary(navigation_results, problematic_files, cleanup_report)

        return navigation_results is not None

    def display_summary(self, navigation_results, problematic_files, cleanup_report):
        """Affiche un résumé de la validation"""
        print("\n" + "=" * 60)
        print("📊 RÉSUMÉ DE LA VALIDATION AUTOMATIQUE")
        print("=" * 60)

        if navigation_results:
            print(f"🎯 Score de navigation : {navigation_results['score']}/100")
            print(f"🔗 Liens critiques cassés : {navigation_results['critical_links']}")
            print(f"📁 Fichiers testés : {navigation_results['files_tested']}")
            print(f"📈 Taux de succès : {navigation_results['success_rate']:.1f}%")

        print(f"\n🚨 Fichiers problématiques : {len(problematic_files)}")
        print(f"🔴 Priorité haute : {cleanup_report['summary']['high_priority']}")
        print(f"🟡 Priorité moyenne : {cleanup_report['summary']['medium_priority']}")
        print(f"🟢 Priorité basse : {cleanup_report['summary']['low_priority']}")

        print("\n💡 Recommandations :")
        for rec in cleanup_report["recommendations"]:
            print(f"  • {rec['priority']} : {rec['action']}")

        print("\n✅ Validation terminée !")


def main():
    """Fonction principale"""
    validator = NavigationValidator()

    try:
        success = validator.run_validation()
        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\n⚠️ Validation interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors de la validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
