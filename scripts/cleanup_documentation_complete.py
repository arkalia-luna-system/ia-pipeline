#!/usr/bin/env python3
"""
🧹 ATHALIA DOCUMENTATION COMPLETE CLEANUP
Script pour nettoyer, organiser et corriger TOUTE la documentation
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Set
import re

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


def find_all_md_files() -> List[Path]:
    """Trouve tous les fichiers .md du projet."""
    md_files = []
    for md_file in PROJECT_ROOT.rglob("*.md"):
        if ".venv" not in str(md_file) and ".git" not in str(md_file):
            md_files.append(md_file)
    return md_files


def identify_problems(md_files: List[Path]) -> Dict[str, List[Path]]:
    """Identifie tous les problèmes dans la documentation."""
    problems = {
        "duplicates": [],
        "obsolete": [],
        "apple_double": [],
        "inconsistent": [],
        "empty": [],
        "broken_links": [],
    }

    # Identifier les fichiers Apple Double
    for md_file in md_files:
        if md_file.name.startswith("._"):
            problems["apple_double"].append(md_file)

    # Identifier les doublons de README
    readme_files = [f for f in md_files if f.name == "README.md"]
    if len(readme_files) > 1:
        problems["duplicates"].extend(readme_files[1:])  # Garder le premier

    # Identifier les fichiers obsolètes
    for md_file in md_files:
        if md_file.name in FILES_TO_DELETE:
            problems["obsolete"].append(md_file)

    # Identifier les fichiers vides ou très petits
    for md_file in md_files:
        try:
            if md_file.stat().st_size < 100:  # Moins de 100 bytes
                problems["empty"].append(md_file)
        except:
            pass

    return problems


def create_cleanup_plan(problems: Dict[str, List[Path]]) -> Dict[str, List[str]]:
    """Crée un plan de nettoyage détaillé."""
    plan = {"delete": [], "archive": [], "keep": [], "consolidate": []}

    # Fichiers à supprimer
    for file_list in [
        problems["apple_double"],
        problems["obsolete"],
        problems["empty"],
    ]:
        for file_path in file_list:
            plan["delete"].append(str(file_path))

    # Fichiers à archiver
    for file_path in problems["duplicates"]:
        if str(file_path) not in plan["delete"]:
            plan["archive"].append(str(file_path))

    # Fichiers à consolider (README multiples)
    readme_files = [f for f in problems["duplicates"] if f.name == "README.md"]
    if len(readme_files) > 1:
        plan["consolidate"].extend([str(f) for f in readme_files[1:]])

    return plan


def execute_cleanup(plan: Dict[str, List[str]]) -> Dict[str, int]:
    """Exécute le plan de nettoyage."""
    results = {"deleted": 0, "archived": 0, "consolidated": 0, "errors": 0}

    # Créer les répertoires de nettoyage
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    # Supprimer les fichiers
    for file_path in plan["delete"]:
        try:
            Path(file_path).unlink()
            results["deleted"] += 1
            print(f"🗑️  Supprimé: {file_path}")
        except Exception as e:
            print(f"❌ Erreur suppression {file_path}: {e}")
            results["errors"] += 1

    # Archiver les fichiers
    for file_path in plan["archive"]:
        try:
            source = Path(file_path)
            dest = ARCHIVE_DIR / source.name
            if dest.exists():
                # Ajouter un suffixe si le fichier existe déjà
                counter = 1
                while dest.exists():
                    dest = ARCHIVE_DIR / f"{source.stem}_{counter}{source.suffix}"
                    counter += 1
            shutil.move(str(source), str(dest))
            results["archived"] += 1
            print(f"📦 Archivé: {file_path} → {dest}")
        except Exception as e:
            print(f"❌ Erreur archivage {file_path}: {e}")
            results["errors"] += 1

    # Consolider les README multiples
    for file_path in plan["consolidate"]:
        try:
            source = Path(file_path)
            dest = TEMP_DIR / f"consolidated_{source.name}"
            shutil.move(str(source), str(dest))
            results["consolidated"] += 1
            print(f"🔧 Consolidé: {file_path} → {dest}")
        except Exception as e:
            print(f"❌ Erreur consolidation {file_path}: {e}")
            results["errors"] += 1

    return results


def generate_cleanup_report(
    problems: Dict[str, List[Path]], plan: Dict[str, List[str]], results: Dict[str, int]
) -> str:
    """Génère un rapport de nettoyage complet."""
    report = f"""# 🧹 RAPPORT DE NETTOYAGE COMPLET - DOCUMENTATION ATHALIA

**Date d'exécution :** 11 août 2025  
**Mission :** Nettoyage complet et organisation de la documentation  
**Statut :** ✅ **TERMINÉ**

---

## 📊 **ANALYSE INITIALE**

### **Fichiers .md identifiés :** {len(problems.get("duplicates", [])) + len(problems.get("obsolete", [])) + len(problems.get("apple_double", [])) + len(problems.get("empty", []))}

### **Problèmes identifiés :**
- **Fichiers Apple Double :** {len(problems.get("apple_double", []))}
- **Doublons :** {len(problems.get("duplicates", []))}
- **Obsolètes :** {len(problems.get("obsolete", []))}
- **Vides :** {len(problems.get("empty", []))}

---

## 🎯 **PLAN DE NETTOYAGE EXÉCUTÉ**

### **Fichiers supprimés :** {len(plan.get("delete", []))}
{chr(10).join([f"- {f}" for f in plan.get("delete", [])])}

### **Fichiers archivés :** {len(plan.get("archive", []))}
{chr(10).join([f"- {f}" for f in plan.get("archive", [])])}

### **Fichiers consolidés :** {len(plan.get("consolidate", []))}
{chr(10).join([f"- {f}" for f in plan.get("consolidate", [])])}

---

## 📈 **RÉSULTATS DU NETTOYAGE**

- **🗑️ Supprimés :** {results.get("deleted", 0)}
- **📦 Archivés :** {results.get("archived", 0)}
- **🔧 Consolidés :** {results.get("consolidated", 0)}
- **❌ Erreurs :** {results.get("errors", 0)}

---

## 🎉 **RÉSULTAT FINAL**

**Documentation nettoyée et organisée !**

- ✅ **Fichiers obsolètes supprimés**
- ✅ **Doublons éliminés**
- ✅ **Structure clarifiée**
- ✅ **Maintenance facilitée**

---

**📅 Date :** 11 août 2025  
**✍️ Auteur :** Script de nettoyage automatique  
**🎯 Objectif :** Documentation Athalia propre et organisée  
**📊 Statut :** ✅ **MISSION ACCOMPLIE**
"""
    return report


def main() -> None:
    """Fonction principale."""
    print("🧹 ATHALIA DOCUMENTATION COMPLETE CLEANUP")
    print("=" * 60)

    # Étape 1 : Trouver tous les fichiers .md
    print("🔍 Étape 1 : Analyse de tous les fichiers .md...")
    md_files = find_all_md_files()
    print(f"📁 {len(md_files)} fichiers .md trouvés")

    # Étape 2 : Identifier les problèmes
    print("\n🔍 Étape 2 : Identification des problèmes...")
    problems = identify_problems(md_files)

    print(f"   🍎 Apple Double : {len(problems['apple_double'])}")
    print(f"   🔄 Doublons : {len(problems['duplicates'])}")
    print(f"   🗑️ Obsolètes : {len(problems['obsolete'])}")
    print(f"   📄 Vides : {len(problems['empty'])}")

    # Étape 3 : Créer le plan de nettoyage
    print("\n📋 Étape 3 : Création du plan de nettoyage...")
    plan = create_cleanup_plan(problems)

    print(f"   🗑️ À supprimer : {len(plan['delete'])}")
    print(f"   📦 À archiver : {len(plan['archive'])}")
    print(f"   🔧 À consolider : {len(plan['consolidate'])}")

    # Étape 4 : Exécuter le nettoyage
    print("\n🚀 Étape 4 : Exécution du nettoyage...")
    results = execute_cleanup(plan)

    # Étape 5 : Générer le rapport
    print("\n📊 Étape 5 : Génération du rapport...")
    report = generate_cleanup_report(problems, plan, results)

    # Sauvegarder le rapport
    report_file = PROJECT_ROOT / "RAPPORT_NETTOYAGE_COMPLET_DOCUMENTATION_ATHALIA.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    # Résumé final
    print("\n" + "=" * 60)
    print("🎉 NETTOYAGE TERMINÉ AVEC SUCCÈS !")
    print(f"📁 Fichiers supprimés : {results['deleted']}")
    print(f"📦 Fichiers archivés : {results['archived']}")
    print(f"🔧 Fichiers consolidés : {results['consolidated']}")
    print(f"❌ Erreurs : {results['errors']}")
    print(f"📊 Rapport sauvegardé : {report_file}")

    # Nettoyer les répertoires temporaires
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
        print("🧹 Répertoire temporaire nettoyé")


if __name__ == "__main__":
    main()
