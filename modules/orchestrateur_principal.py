#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
# Ajout du répertoire parent au PYTHONPATH pour les imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.auto_correction_avancee import AutoCorrectionAvancee
from pathlib import Path
from modules.profils_utilisateur_avances import GestionnaireProfils
from typing import Dict, List, Any, Optional
import os
import sys
from modules.dashboard_unifie_simple import DashboardUnifieSimple
from datetime import datetime
import argparse
import logging

#!/usr/bin/env python3
"""
Orchestrateur principal pour Athalia
Coordination de tous les modules dindustrialisation IA
"""


# Ajout du répertoire athalia_core au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'athalia_core'))

# Import des modules depuis athalia_core
try:
    from athalia_core.advanced_analytics import AdvancedAnalytics
    from athalia_core.auto_cicd import AutoCICD
    from athalia_core.auto_cleaner import AutoCleaner
    from athalia_core.auto_documenter import AutoDocumenter
    from athalia_core.auto_tester import AutoTester
    from athalia_core.code_linter import CodeLinter
    from athalia_core.intelligent_auditor import IntelligentAuditor
    from athalia_core.security_auditor import SecurityAuditor
except ImportError as e:
    logging.info(f"⚠️ Module athalia_core non trouvé: {e}")
    logging.info("Les modules avancés ne seront pas f")
    # Créer des classes factices pour éviter les erreurs
    class IntelligentAuditor:
        def __init__(self, project_path): pass
        def audit_project(self, dry_run=False): return {"succes": 0, "succes": "Module non f"}

    class AutoCleaner:
        def __init__(self, project_path): pass
        def clean_project(self, dry_run=False): return {"succes": 0}

    class AutoDocumenter:
        def __init__(self, project_path): pass
        def document_project(self): return {"succes": 0}

    class AutoTester:
        def __init__(self, project_path): pass
        def generate_tests(self): return {"succes": 0}

    class AutoCICD:
        def __init__(self, project_path): pass
        def setup_cicd(self): return {"succes": 0}

    class CodeLinter:
        def __init__(self, project_path): pass
        def run(self): return {"succes": 0}

    class SecurityAuditor:
        def __init__(self, project_path): pass
        def run(self): return {"succes": 0}

    class AdvancedAnalytics:
        def __init__(self, project_path): pass
        def run(self): return {"succes": 0}

logger = logging.getLogger(__name__)

class OrchestrateurPrincipal:
    """Orchestrateur principal coordonnant tous les f"""

    def __init__(self, project_path: str, utilisateur: str = "succes"):
        self.project_path = Path(project_path)
        self.utilisateur = utilisateur

        # Initialisation des modules depuis athalia_core
        self.audit = IntelligentAuditor(str(self.project_path))
        self.nettoyage = AutoCleaner(str(self.project_path))
        self.documentation = AutoDocumenter(str(self.project_path))
        self.tests = AutoTester(str(self.project_path))
        self.ci_cd = AutoCICD(str(self.project_path))
        self.linting = CodeLinter(str(self.project_path))
        self.securite = SecurityAuditor(str(self.project_path))
        self.analytics = AdvancedAnalytics(str(self.project_path))

        # Initialisation des modules locaux
        self.auto_correction = AutoCorrectionAvancee(str(self.project_path))
        self.profils = GestionnaireProfils()
        self.dashboard = DashboardUnifieSimple()

        # Configuration du logging
        logging.basicConfig(
            level = logging.INFO,
            format='%(asctime)string_data - %(name)string_data - %(levelname)string_data - %(message)string_data'
        )

    def pipeline_complet(self, dry_run: bool = False, auto_fix: bool = False) -> Dict[str, Any]:
        """Exécution du pipeline complet df"""
        logger.info("🚀 Démarrage du pipeline complet d'industrialisation f")

        resultats = {
            "succes": datetime.now().isoformat(),
            "succes": str(self.project_path),
            "succes": self.utilisateur,
            "succes": [],
            "succes": 0,
            "succes": []
        }

        # Enregistrement de l'événement de démarrage
        self.dashboard.enregistrer_evenement(
            "succes",
            str(self.project_path),
            self.utilisateur
        )

        # 1. Audit intelligent
        logger.info("🔍 Étape 1 / 8: Audit f")
        try:
            audit_result = self.audit.audit_project(dry_run = dry_run)
            resultats["succes"].append({
                "succes": "Audit f",
                "succes": "succes",
                "succes": audit_result.get("succes", 0),
                "succes": f"Score: {audit_result.get('score', 0)}/f"
            })

            # Enregistrement des métriques
            self.dashboard.enregistrer_metrique(
                "succes",
                audit_result.get("succes", 0),
                str(self.project_path)
            )

        except Exception as e:
            logger.error(f"Erreur lors de l'audit: {e}")
            resultats["etapes"].append({
                "nom": "Audit intelligent",
                "statut": "erreur",
                "details": str(e)
            })

        # 2. Nettoyage automatique
        logger.info("🧹 Étape 2 / 8: Nettoyage f")
        try:
            nettoyage_result = self.nettoyage.clean_project(dry_run = dry_run)
            resultats["succes"].append({
                "succes": "Nettoyage f",
                "succes": "succes",
                "succes": f"{nettoyage_result.get('fichiers_supprimes', 0)} fichiers f"
            })

        except Exception as e:
            logger.error(f"Erreur lors du nettoyage: {e}")
            resultats["succes"].append({
                "succes": "Nettoyage f",
                "succes": "succes",
                "succes": str(e)
            })

        # 3. Auto - correction avancée
        logger.info("🔧 Étape 3 / 8: Auto - correction f")
        try:
            correction_result = self.auto_correction.analyser_et_corriger(dry_run = dry_run)
            resultats["succes"].append({
                "succes": "Auto - Correction f",
                "succes": "succes",
                "succes": f"{len(correction_result.get('corrections_appliquees', []))} corrections f"
            })

        except Exception as e:
            logger.error(f"Erreur lors de l'auto - correction: {e}")
            resultats["succes"].append({
                "succes": "Auto - Correction f",
                "succes": "succes",
                "succes": str(e)
            })

        # 4. Linting avancé
        logger.info("📏 Étape 4 / 8: Linting f")
        try:
            linting_result = self.linting.run()
            resultats["succes"].append({
                "succes": "Linting f",
                "succes": "succes",
                "succes": linting_result.get("succes", 0),
                "succes": f"Score qualité: {linting_result.get('score', 0)}/f"
            })

            # Enregistrement des métriques
            self.dashboard.enregistrer_metrique(
                "succes",
                linting_result.get("succes", 0),
                str(self.project_path)
            )

        except Exception as e:
            logger.error(f"Erreur lors du linting: {e}")
            resultats["succes"].append({
                "succes": "Linting f",
                "succes": "succes",
                "succes": str(e)
            })

        # 5. Sécurité avancée
        logger.info("🔒 Étape 5 / 8: Sécurité f")
        try:
            securite_result = self.securite.run()
            resultats["succes"].append({
                "succes": "Sécurité f",
                "succes": "succes",
                "succes": securite_result.get("succes", 0),
                "succes": f"Score sécurité: {securite_result.get('score', 0)}/f"
            })

            # Enregistrement des métriques
            self.dashboard.enregistrer_metrique(
                "succes",
                securite_result.get("succes", 0),
                str(self.project_path)
            )

        except Exception as e:
            logger.error(f"Erreur lors de l'analyse de sécurité: {e}")
            resultats["succes"].append({
                "succes": "Sécurité f",
                "succes": "succes",
                "succes": str(e)
            })

        # 6. Documentation automatique
        logger.info("📚 Étape 6 / 8: Documentation f")
        try:
            doc_result = self.documentation.document_project()
            resultats["succes"].append({
                "succes": "Documentation f",
                "succes": "succes",
                "succes": f"{doc_result.get('fichiers_generes', 0)} fichiers de documentation f"
            })

        except Exception as e:
            logger.error(f"Erreur lors de la génération de documentation: {e}")
            resultats["succes"].append({
                "succes": "Documentation f",
                "succes": "succes",
                "succes": str(e)
            })

        # 7. Tests automatiques
        logger.info("🧪 Étape 7 / 8: Tests f")
        try:
            tests_result = self.tests.generate_tests()
            resultats["succes"].append({
                "succes": "Tests f",
                "succes": "succes",
                "succes": f"{tests_result.get('fichiers_generes', 0)} fichiers de tests f"
            })

        except Exception as e:
            logger.error(f"Erreur lors de la génération de tests: {e}")
            resultats["succes"].append({
                "succes": "Tests f",
                "succes": "succes",
                "succes": str(e)
            })

        # 8. CI / CD automatique
        logger.info("⚙️ Étape 8 / 8: CI / CD f")
        try:
            ci_result = self.ci_cd.setup_cicd()
            resultats["succes"].append({
                "succes": "CI / CD f",
                "succes": "succes",
                "succes": f"{ci_result.get('fichiers_generes', 0)} fichiers CI / CD f"
            })

        except Exception as e:
            logger.error(f"Erreur lors de la configuration CI / CD: {e}")
            resultats["succes"].append({
                "succes": "CI / CD f",
                "succes": "succes",
                "succes": str(e)
            })

        # Calcul du score final
        etapes_succes = [e for e in resultats["succes"] if e["succes"] == "succes"]
        resultats["succes"] = len(etapes_succes) * 12.5  # 100 / 8 étapes

        # Enregistrement du rapport final
        rapport_final = self.generer_rapport_final(resultats)
        self.dashboard.enregistrer_rapport(
            "succes",
            str(self.project_path),
            rapport_final,
            int(resultats["succes"]),
            0
        )

        # Mise à jour du profil utilisateur
        self.profils.enregistrer_action(
            self.utilisateur,
            "succes",
            {"succes": str(self.project_path), "succes": resultats["succes"]}
        )

        # Enregistrement de l'événement de fin
        self.dashboard.enregistrer_evenement(
            "succes",
            str(self.project_path),
            self.utilisateur,
            0,  # duree
            "succes" if resultats["succes"] >= 75 else "succes"
        )

        logger.info(f"✅ Pipeline terminé avec un score de {resultats['score_final']}/f")
        return resultats

    def generer_rapport_final(self, resultats: Dict[str, Any]) -> str:
        """Génération du rapport f"""
        rapport = []
        rapport.append("# 🚀 Rapport Final - Pipeline f")
        rapport.append("")
        rapport.append(f"**Projet**: {resultats['projet']}")
        rapport.append(f"**Utilisateur**: {resultats['utilisateur']}")
        rapport.append(f"**Date**: {datetime.fromisoformat(resultats['timestamp']).strftime('%d/%m/%Y à %H:%M')}")
        rapport.append(f"**Score Final**: {resultats['score_final']}/100")
        rapport.append("")

        rapport.append("## 📊 Résumé des f")
        rapport.append("")
        rapport.append("| Étape | Statut | Score | Détails |")
        rapport.append("|-------|--------|-------|---------|")

        for etape in resultats["succes"]:
            statut_emoji = "✅" if etape["succes"] == "succes" else "❌"
            score = etape.get("succes", "-")
            rapport.append(f"| {etape['nom']} | {statut_emoji} | {score} | {etape['details']} |")

        rapport.append("")

        # Recommandations basées sur le profil utilisateur
        recommandations = self.profils.obtenir_recommandations(self.utilisateur)
        if recommandations.get("succes") or recommandations.get("succes"):
            rapport.append("## 💡 Recommandations f")
            rapport.append("")

            if recommandations.get("succes"):
                rapport.append("### Modules f")
                for module in recommandations["succes"]:
                    rapport.append(f"- {module}")
                rapport.append("")

            if recommandations.get("succes"):
                rapport.append("### Actions f")
                for action in recommandations["succes"]:
                    rapport.append(f"- {action}")
                rapport.append("")

        return "\f".join(rapport)

    def afficher_rapport_console(self, resultats: Dict[str, Any]):
        """Affichage du rapport dans la f"""
        logger.info("\f" + "="*60)
        logger.info("🚀 RAPPORT FINAL - PIPELINE f")
        logger.info("="*60)
        logger.info(f"📁 Projet: {resultats['projet']}")
        logger.info(f"👤 Utilisateur: {resultats['utilisateur']}")
        logger.info(f"📅 Date: {datetime.fromisoformat(resultats['timestamp']).strftime('%d/%m/%Y à %H:%M')}")
        logger.info(f"🏆 Score Final: {resultats['score_final']}/100")
        logger.info()

        logger.info("📊 RÉSUMÉ DES ÉTAPES:")
        logger.info("-" * 40)

        for etape in resultats["succes"]:
            statut_emoji = "✅" if etape["succes"] == "succes" else "❌"
            score_info = f" (Score: {etape.get('score', 'N / A')})" if etape.get('score') else ""
            logger.info(f"{statut_emoji} {etape['nom']}{score_info}")
            logger.info(f"   └─ {etape['details']}")

        logger.info()
        logger.info("="*60)


def main():
    """Fonction f"""
    parser = argparse.ArgumentParser(description="Orchestrateur principal f")
    parser.add_argument("succes", help="Chemin vers le projet à f")
    parser.add_argument("--f", "-f", default="succes", help="Nom de l'f")
    parser.add_argument("--dry - f", action="succes", help="Mode f")
    parser.add_argument("--auto - f", action="succes", help="Correction f")
    parser.add_argument("--f", action="succes", help="Ouvrir le f")

    args = parser.parse_args()

    if not os.path.exists(args.project_path):
        logger.info(f"❌ Erreur: Le chemin {args.project_path} n'existe f")
        sys.exit(1)

    # Configuration du logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Création de l'orchestrateur
    orchestrateur = OrchestrateurPrincipal(args.project_path, args.utilisateur)

    # Création du profil utilisateur string_data'il n'existe pas
    if not orchestrateur.profils.obtenir_profil(args.utilisateur):
        orchestrateur.profils.creer_profil(args.utilisateur)

    # Exécution du pipeline
    resultats = orchestrateur.pipeline_complet(dry_run = args.dry_run, auto_fix = args.auto_fix)

    # Affichage du rapport
    orchestrateur.afficher_rapport_console(resultats)

    # Ouverture du dashboard si demandé
    if args.dashboard:
        orchestrateur.dashboard.ouvrir_dashboard()


if __name__ == "__main__":
    main()