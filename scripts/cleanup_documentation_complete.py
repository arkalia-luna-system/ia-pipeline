#!/usr/bin/env python3
"""
🧹 ATHALIA DOCUMENTATION COMPLETE CLEANUP
Script pour nettoyer, organiser et corriger TOUTE la documentation
"""

import os
import shutil
from datetime import datetime
from pathlib import Path

# Configuration du nettoyage
PROJECT_ROOT = Path(".")
ARCHIVE_DIR = PROJECT_ROOT / "archive" / "cleaned_docs"
TEMP_DIR = PROJECT_ROOT / "temp_cleanup"

# Fichiers à SUPPRIMER (obsolètes, dupliqués, inutiles)
FILES_TO_DELETE = {
    # Fichiers Apple Double (macOS)
    "._*",
    # Rapports obsolètes et dupliqués
    "RAPPORT_AMELIORATION_ATHALIA.md",
    "RAPPORT_AMELIORATIONS_RESTANTES_ATHALIA_20250803.md",
    "RAPPORT_CORRECTION_MASSIVE_TOUS_MD_20250803.md",
    "RAPPORT_COUVERTURE_EXACTE.md",
    "RAPPORT_COUVERTURE_TESTS.md",
    "RAPPORT_FINAL_CORRECTION_COMPLETE_TOUS_MD_20250803.md",
    "RAPPORT_FINAL_MISSION_TESTS_COMPLETE.md",
    "RAPPORT_FINAL_TESTS_SUPPLEMENTAIRES.md",
    "RAPPORT_MISE_A_JOUR_FINALE_MD_20250803.md",
    "RAPPORT_NETTOYAGE_FINAL_TOUS_MD_ATHALIA.md",
    "RAPPORT_NETTOYAGE_MD_ATHALIA_20250803.md",
    "RAPPORT_SESSION_3_TESTS_ADDITIONNELS.md",
    "RAPPORT_TEST_UTILISATEUR_COMPLET_ATHALIA_20250803.md",
    "RAPPORT_VERIFICATION_OUTILS_QUALITE.md",
    # Documents obsolètes
    "ANALYSE_COMPLETE_TOUS_MD_ATHALIA.md",
    "AUDIT_COMPLET_DOCUMENTATION_ATHALIA.md",
    "DECISION_FINALE_DOCUMENTATION_ATHALIA.md",
    "DOCUMENTATION_PARFAITE_FINALE_ATHALIA.md",
    "DOCUMENTATION_PROFESSIONNELLE_FINALE_ATHALIA.md",
    "EVALUATION_ATHALIA_COMPLETE_25_EXPERTS.md",
    "GUIDE_CORRECTION_PROBLEMES_ATHALIA_20250803.md",
    "MISE_A_JOUR_DOCUMENTATION_HONNETE_ATHALIA.md",
    "MON_ANALYSE_REELLE_ATHALIA_CLAUDE.md",
    "PLAN_ACTION_TESTS_DETAILLE.md",
    "PLAN_AMELIORATION_CV_ATHALIA_PAR_PHASES.md",
    "PLAN_NETTOYAGE_MD_ATHALIA_20250803.md",
    "PROMPT_ANALYSE_MULTI_PERSPECTIVES_ATHALIA.md",
    "PROMPT_ULTIME_TABLE_RONDE_EXPERTE_ATHALIA.md",
    "README_NAVIGATION_ATHALIA.md",
    "SYNTHESE_FINALE_MISSION_TESTS.md",
    "SYNTHESE_FINALE_TODO_ATHALIA.md",
    "SYNTHESE_TESTS_CREES.md",
    "VERIFICATION_COMPLETE_REELLE_ATHALIA.md",
    "VERIFICATION_FINALE_DOCUMENTATION_PERFECTIONNEE.md",
    # README dupliqués et inutiles
    "test/README.md",
    "tests/fixtures/README.md",
    "tests/performance/README.md",
    "tests/regression/README.md",
    "tests/security/README.md",
    "tests/unit/agents/README.md",
    "tests/unit/README.md",
    "docs/SPECIALIZED/DISTILLATION/README.md",
    "docs/SPECIALIZED/INTERNATIONALISATION/README.md",
    "docs/SPECIALIZED/MODULES_AVANCÉS/README.md",
    "docs/SPECIALIZED/OPTIMISATION/README.md",
    "docs/SPECIALIZED/prompts/README.md",
    "docs/SPECIALIZED/TEMPLATES/README.md",
}

# Fichiers à ARCHIVER (garder mais déplacer)
FILES_TO_ARCHIVE = {
    # Rapports de correction (garder pour historique)
    "RAPPORT_CORRECTION_TECHNIQUE_IA_ATHALIA.md",
    # Documents d'analyse (garder pour référence)
    "doc_quality_report.md",
    # Plans et guides (garder pour maintenance)
    "GUIDE_UTILISATION_ATHALIA.md",
}

# Fichiers à CONSERVER (essentiels)
ESSENTIAL_FILES = {
    "README.md",  # README principal
    "CHANGELOG.md",  # Historique des versions
    "docs/README.md",  # Index de la documentation
    "docs/NAVIGATION_GLOBALE.md",  # Navigation globale
    "docs/ARCHITECTURE/INDEX.md",  # Architecture
    "docs/API/INDEX.md",  # API Reference
    "docs/USER_GUIDES/INDEX.md",  # Guides utilisateur
    "docs/DEVELOPER/INDEX.md",  # Guides développeur
    "docs/SPECIALIZED/README.md",  # Documentation spécialisée
    "athalia_core/README.md",  # README du core
    "bin/README.md",  # README des commandes
    "data/README.md",  # README des données
    "scripts/README.md",  # README des scripts
    "tests/README.md",  # README des tests
    "dashboard/dashboard.md",  # Documentation des dashboards
}


def find_all_md_files() -> list[Path]:
    """Trouve tous les fichiers .md dans le projet"""
    md_files = []
    for root, _dirs, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith(".md"):
                md_files.append(Path(root) / file)
    return md_files


def identify_problems(md_files: list[Path]) -> dict[str, list[Path]]:
    """Identifie les problèmes dans les fichiers MD"""
    problems: dict[str, list[Path]] = {
        "duplicates": [],
        "obsolete": [],
        "archivable": [],
        "essential": [],
    }

    for md_file in md_files:
        file_name = md_file.name
        relative_path = str(md_file.relative_to(PROJECT_ROOT))

        # Vérifier si c'est un fichier essentiel
        if relative_path in ESSENTIAL_FILES:
            problems["essential"].append(md_file)
            continue

        # Vérifier si c'est un fichier à supprimer
        for pattern in FILES_TO_DELETE:
            if pattern.startswith("*"):
                if file_name.endswith(pattern[1:]):
                    problems["obsolete"].append(md_file)
                    break
            elif pattern.startswith("._"):
                if file_name.startswith("._"):
                    problems["obsolete"].append(md_file)
                    break
            elif file_name == pattern:
                problems["obsolete"].append(md_file)
                break
        else:
            # Vérifier si c'est un fichier à archiver
            if relative_path in FILES_TO_ARCHIVE:
                problems["archivable"].append(md_file)
            else:
                # Fichier non classé - potentiellement dupliqué
                problems["duplicates"].append(md_file)

    return problems


def create_cleanup_plan(problems: dict[str, list[Path]]) -> dict[str, list[str]]:
    """Crée un plan de nettoyage basé sur les problèmes identifiés"""
    plan: dict[str, list[str]] = {
        "delete": [],
        "archive": [],
        "keep": [],
    }

    # Fichiers à supprimer
    for file_list in [
        problems["obsolete"],
        problems["duplicates"],
    ]:
        for file_path in file_list:
            plan["delete"].append(str(file_path))

    # Fichiers à archiver
    for file_path in problems["archivable"]:
        plan["archive"].append(str(file_path))

    # Fichiers à conserver
    for file_path in problems["essential"]:
        plan["keep"].append(str(file_path))

    return plan


def execute_cleanup(plan: dict[str, list[str]]) -> dict[str, int]:
    """Exécute le plan de nettoyage"""
    results = {"deleted": 0, "archived": 0, "errors": 0}

    # Créer les dossiers nécessaires
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    # Supprimer les fichiers
    for file_path in plan["delete"]:
        try:
            Path(file_path).unlink()
            results["deleted"] += 1
            print(f"🗑️ Supprimé: {file_path}")
        except Exception as e:
            print(f"❌ Erreur suppression {file_path}: {e}")
            results["errors"] += 1

    # Archiver les fichiers
    for file_path in plan["archive"]:
        try:
            source = Path(file_path)
            if source.exists():
                archive_path = ARCHIVE_DIR / source.name
                shutil.copy2(source, archive_path)
                source.unlink()
                results["archived"] += 1
                print(f"📦 Archivé: {file_path}")
        except Exception as e:
            print(f"❌ Erreur archivage {file_path}: {e}")
            results["errors"] += 1

    return results


def generate_cleanup_report(
    problems: dict[str, list[Path]], plan: dict[str, list[str]], results: dict[str, int]
) -> str:
    """Génère un rapport de nettoyage"""
    report = "# 🧹 RAPPORT DE NETTOYAGE DOCUMENTATION ATHALIA\n\n"
    report += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    # Résumé des problèmes
    report += "## 📊 RÉSUMÉ DES PROBLÈMES IDENTIFIÉS\n\n"
    report += f"- **Fichiers obsolètes:** {len(problems['obsolete'])}\n"
    report += f"- **Fichiers dupliqués:** {len(problems['duplicates'])}\n"
    report += f"- **Fichiers à archiver:** {len(problems['archivable'])}\n"
    report += f"- **Fichiers essentiels:** {len(problems['essential'])}\n\n"

    # Plan de nettoyage
    report += "## 📋 PLAN DE NETTOYAGE\n\n"
    report += f"- **À supprimer:** {len(plan['delete'])}\n"
    report += f"- **À archiver:** {len(plan['archive'])}\n"
    report += f"- **À conserver:** {len(plan['keep'])}\n\n"

    # Résultats
    report += "## ✅ RÉSULTATS DU NETTOYAGE\n\n"
    report += f"- **Supprimés:** {results['deleted']}\n"
    report += f"- **Archivés:** {results['archived']}\n"
    report += f"- **Erreurs:** {results['errors']}\n\n"

    # Détails des actions
    if plan["delete"]:
        report += "### 🗑️ Fichiers supprimés\n\n"
        for file_path in plan["delete"]:
            report += f"- `{file_path}`\n"
        report += "\n"

    if plan["archive"]:
        report += "### 📦 Fichiers archivés\n\n"
        for file_path in plan["archive"]:
            report += f"- `{file_path}` → `{ARCHIVE_DIR}`\n"
        report += "\n"

    if plan["keep"]:
        report += "### 💾 Fichiers conservés\n\n"
        for file_path in plan["keep"]:
            report += f"- `{file_path}`\n"
        report += "\n"

    return report


def main() -> None:
    """Fonction principale"""
    print("🧹 Démarrage du nettoyage de la documentation Athalia...")

    # Trouver tous les fichiers MD
    print("🔍 Recherche des fichiers .md...")
    md_files = find_all_md_files()
    print(f"📁 {len(md_files)} fichiers .md trouvés")

    # Identifier les problèmes
    print("🔍 Analyse des problèmes...")
    problems = identify_problems(md_files)

    # Créer le plan de nettoyage
    print("📋 Création du plan de nettoyage...")
    plan = create_cleanup_plan(problems)

    # Afficher le plan
    print("\n📋 PLAN DE NETTOYAGE:")
    print(f"🗑️ À supprimer: {len(plan['delete'])}")
    print(f"📦 À archiver: {len(plan['archive'])}")
    print(f"💾 À conserver: {len(plan['keep'])}")

    # Demander confirmation
    response = input("\n❓ Continuer le nettoyage? (y/N): ")
    if response.lower() != "y":
        print("❌ Nettoyage annulé")
        return

    # Exécuter le nettoyage
    print("🚀 Exécution du nettoyage...")
    results = execute_cleanup(plan)

    # Générer le rapport
    print("📊 Génération du rapport...")
    report = generate_cleanup_report(problems, plan, results)

    # Sauvegarder le rapport
    report_path = PROJECT_ROOT / "RAPPORT_NETTOYAGE_DOCUMENTATION.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✅ Rapport sauvegardé: {report_path}")
    print("🎉 Nettoyage terminé!")

    # Nettoyer le dossier temporaire
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)


if __name__ == "__main__":
    main()
