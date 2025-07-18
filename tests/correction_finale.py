#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction finale pour Athalia
Corrige toutes les erreurs restantes dans les fichiers principaux
"""

import os
import re
from pathlib import Path

def corriger_fichier(file_path):
    """Corrige un fichier en remplaçant les patterns problématiques"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Correction des f-strings malformées
        content = re.sub(r'ff"([^"]*)"', r'f"\1"', content)
        
        # Correction des variables malformées
        content = re.sub(r'"f"', '"succes"', content)
        content = re.sub(r'"f"', '"erreur"', content)
        content = re.sub(r'"f"', '"etapes"', content)
        content = re.sub(r'"f"', '"nom"', content)
        content = re.sub(r'"f"', '"statut"', content)
        content = re.sub(r'"f"', '"details"', content)
        content = re.sub(r'"f"', '"score_final"', content)
        content = re.sub(r'"f"', '"projet"', content)
        content = re.sub(r'"f"', '"utilisateur"', content)
        content = re.sub(r'"f"', '"timestamp"', content)
        content = re.sub(r'"f"', '"industrialisation"', content)
        content = re.sub(r'"f"', '"nettoyage"', content)
        content = re.sub(r'"f"', '"correction"', content)
        content = re.sub(r'"f"', '"linting"', content)
        content = re.sub(r'"f"', '"securite"', content)
        content = re.sub(r'"f"', '"documentation"', content)
        content = re.sub(r'"f"', '"tests"', content)
        content = re.sub(r'"f"', '"cicd"', content)
        content = re.sub(r'"f"', '"fichiers_supprimes"', content)
        content = re.sub(r'"f"', '"corrections_appliquees"', content)
        content = re.sub(r'"f"', '"fichiers_generes"', content)
        content = re.sub(r'"f"', '"score"', content)
        content = re.sub(r'"f"', '"vulnerabilites"', content)
        content = re.sub(r'"f"', '"100"', content)
        content = re.sub(r'"f"', '"terminer"', content)
        content = re.sub(r'"f"', '"succes"', content)
        content = re.sub(r'"f"', '"echec"', content)
        
        # Correction des chaînes malformées
        content = re.sub(r'"""([^"]*)\'([^"]*)"""', r'"""\1\2"""', content)
        content = re.sub(r'"""([^"]*)dict_data([^"]*)"""', r'"""\1\2"""', content)
        
        # Correction des espaces dans l'encodage
        content = content.replace('utf - 8', 'utf-8')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Corrigé: {file_path}")
            return True
        return False
        
    except Exception as e:
        print(f"❌ Erreur lors de la correction de {file_path}: {e}")
        return False

def main():
    """Fonction principale"""
    print("🔧 Correction finale des fichiers Athalia...")
    
    fichiers_a_corriger = [
        'modules/orchestrateur_principal.py',
        'modules/auto_correction_avancee.py',
        'modules/dashboard_unifie_simple.py',
        'athalia_core/intelligent_auditor.py'
    ]
    
    fichiers_corriges = 0
    
    for fichier in fichiers_a_corriger:
        if os.path.exists(fichier):
            if corriger_fichier(fichier):
                fichiers_corriges += 1
        else:
            print(f"⚠️ Fichier non trouvé: {fichier}")
    
    print(f"\n📊 Résumé: {fichiers_corriges} fichiers corrigés")
    
    # Test de compilation
    print("\n🧪 Test de compilation...")
    for fichier in fichiers_a_corriger:
        if os.path.exists(fichier):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    content = f.read()
                compile(content, fichier, 'exec')
                print(f"✅ {fichier} compile correctement")
            except Exception as e:
                print(f"❌ {fichier} ne compile pas: {e}")

if __name__ == "__main__":
    main() 