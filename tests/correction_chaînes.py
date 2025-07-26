#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction des chaînes non terminées dans athalia_core
"""

import os
import re
from pathlib import Path


def corriger_chaînes_fichier(file_path):
    """Corrige les chaînes non terminées dans un fichier"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Correction des chaînes malformées
        # Pattern: """...'...""" -> """......"""
        content = re.sub(r'"""([^"]*)\'([^"]*)"""', r'"""\1\2"""', content)

        # Pattern: """...dict_data...""" -> """......"""
        content = re.sub(
            r'"""([^"]*)dict_data([^"]*)"""', r'"""\1\2"""', content
        )

        # Pattern: "..."'..." -> "......"
        content = re.sub(r'"([^"]*)\'([^"]*)"', r'"\1\2"', content)

        # Correction des f-strings malformées
        content = re.sub(r'ff"([^"]*)"', r'f"\1"', content)

        # Correction des chaînes avec des espaces dans l'encodage
        content = content.replace("utf - 8", "utf-8")

        # Correction des chaînes avec des caractères spéciaux malformés
        content = re.sub(r'"""([^"]*)\'([^"]*)"""', r'"""\1\2"""', content)

        # Correction des docstrings malformées
        content = re.sub(r'"""([^"]*)\'([^"]*)"""', r'"""\1\2"""', content)

        # Correction des chaînes avec des guillemets mal fermés
        lines = content.split("\n")
        fixed_lines = []

        for line in lines:
            # Compter les guillemets
            single_quotes = line.count("'")
            double_quotes = line.count('"')

            # Si nombre impair de guillemets simples, ajouter un guillemet fermant
            if single_quotes % 2 == 1:
                line += "'"

            # Si nombre impair de guillemets doubles, ajouter un guillemet fermant
            if double_quotes % 2 == 1:
                line += '"'

            fixed_lines.append(line)

        content = "\n".join(fixed_lines)

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Corrigé: {file_path}")
            return True
        return False

    except Exception as e:
        print(f"❌ Erreur lors de la correction de {file_path}: {e}")
        return False


def main():
    """Fonction principale"""
    print("🔧 Correction des chaînes non terminées dans athalia_core...")

    # Fichiers avec des erreurs de chaînes non terminées
    fichiers_problematiques = [
        "athalia_core/audit.py",
        "athalia_core/generation.py",
        "athalia_core/main.py",
        "athalia_core/analytics.py",
        "athalia_core/onboarding.py",
        "athalia_core/security.py",
        "athalia_core/plugins_manager.py",
        "athalia_core/plugins_validator.py",
        "athalia_core/ai_robust.py",
        "athalia_core/cli.py",
        "athalia_core/project_importer.py",
        "athalia_core/auto_fixer.py",
        "athalia_core/intelligent_auditor.py",
        "athalia_core/auto_cleaner.py",
        "athalia_core/auto_documenter.py",
        "athalia_core/auto_tester.py",
        "athalia_core/auto_cicd.py",
        "athalia_core/athalia_orchestrator.py",
        "athalia_core/code_linter.py",
        "athalia_core/security_auditor.py",
        "athalia_core/advanced_analytics.py",
        "athalia_core/auto_documenter_fixed.py",
        "athalia_core/module_discovery.py",
    ]

    fichiers_corriges = 0

    for fichier in fichiers_problematiques:
        if os.path.exists(fichier):
            if corriger_chaînes_fichier(fichier):
                fichiers_corriges += 1
        else:
            print(f"⚠️ Fichier non trouvé: {fichier}")

    print(f"\n📊 Résumé: {fichiers_corriges} fichiers corrigés")

    # Test de compilation après correction
    print("\n🧪 Test de compilation après correction...")
    for fichier in fichiers_problematiques:
        if os.path.exists(fichier):
            try:
                with open(fichier, "r", encoding="utf-8") as f:
                    content = f.read()
                compile(content, fichier, "exec")
                print(f"✅ {fichier} compile correctement")
            except Exception as e:
                print(f"❌ {fichier} ne compile toujours pas: {e}")


if __name__ == "__main__":
    main()
