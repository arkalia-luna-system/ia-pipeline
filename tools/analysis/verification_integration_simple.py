#!/usr/bin/env python3
"""
🔍 VÉRIFICATION SIMPLE D'INTÉGRATION ORCHESTRATEUR
==================================================
Script simple pour vérifier l'intégration actuelle de l'orchestrateur unifié.
"""

import re
from pathlib import Path


def main():
    """Fonction principale"""
    print("🔍 VÉRIFICATION SIMPLE D'INTÉGRATION")
    print("=" * 40)

    # Chemin vers l'orchestrateur
    orchestrator_path = Path("athalia_core/unified_orchestrator.py")

    if not orchestrator_path.exists():
        print("❌ Orchestrateur unifié non trouvé")
        return

    # Lire le contenu
    with open(orchestrator_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Chercher les imports relatifs
    imports = re.findall(r"from \.(\w+) import (\w+)", content)

    print(f"📦 Imports trouvés: {len(imports)}")

    # Afficher les imports
    print("\n✅ MODULES INTÉGRÉS:")
    for module, class_name in imports:
        print(f"  - {module} -> {class_name}")

    # Chercher les modules athalia_core
    core_modules = []
    core_path = Path("athalia_core")
    for py_file in core_path.glob("*.py"):
        if py_file.name != "__init__.py" and not py_file.name.startswith("._"):
            module_name = py_file.stem
            core_modules.append(module_name)

    print(f"\n📦 Modules athalia_core totaux: {len(core_modules)}")

    # Identifier les modules non intégrés
    integrated_modules = [module for module, _ in imports]
    non_integrated = [m for m in core_modules if m not in integrated_modules]

    print(f"\n❌ MODULES NON INTÉGRÉS ({len(non_integrated)}):")
    for module in non_integrated:
        print(f"  - {module}")

    # Calculer le score
    integration_score = len(integrated_modules) / len(core_modules) * 10
    print(f"\n📈 SCORE D'INTÉGRATION: {integration_score:.2f}/10")

    # Recommandations
    print("\n🎯 RECOMMANDATIONS:")
    if integration_score < 5.0:
        print("  ⚠️ Score faible - Nécessite une amélioration urgente")

    if non_integrated:
        print(f"  📦 {len(non_integrated)} modules à intégrer")
        print("  🎯 Priorité (top 5):")
        for module in non_integrated[:5]:
            print(f"    - {module}")

    # Vérifier les tests
    print("\n🧪 VÉRIFICATION DES TESTS:")
    test_files = list(Path("tests").glob("*orchestrator*"))
    test_files.extend(Path("tests").glob("*unified*"))

    if test_files:
        print(f"  ✅ Tests trouvés: {len(test_files)}")
        for test_file in test_files:
            print(f"    - {test_file.name}")
    else:
        print("  ❌ Aucun test trouvé pour l'orchestrateur")


if __name__ == "__main__":
    main()
