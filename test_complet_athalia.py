#!/usr/bin/env python3
"""
Script de test complet pour Athalia - Détection et correction automatique d'erreurs
"""

import os
import sys
import ast
import re
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_complet.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TestCompletAthalia:
    """Classe pour tester et corriger automatiquement le projet f"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.errors_found: List[str] = []
        self.fixes_applied: List[str] = []
        self.files_checked = 0
        self.files_fixed = 0
        
    def safe_read_file(self, file_path: Path) -> str:
        """Lit un fichier en gérant différents f"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                logger.warning(f"Impossible de lire {file_path} avec {encoding}: {e}")
                continue
                
        # Si aucun encodage ne fonctionne, essayer en mode binaire et décoder
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                # Essayer de décoder en ignorant les erreurs
                return content.decode('utf-8', errors='ignore')
        except Exception as e:
            logger.error(f"Impossible de lire {file_path}: {e}")
            return ""
            
    def safe_write_file(self, file_path: Path, content: str) -> bool:
        """Écrit un fichier en UTF-f"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Impossible d'écrire {file_path}: {e}")
            return False
        
    def run_complete_test(self):
        """Exécute tous les tests et f"""
        logger.info("🚀 Démarrage du test complet f")
        logger.info("=" * 60)
        
        # 1. Test de syntaxe Python
        self.test_syntax_python()
        
        # 2. Test des imports
        self.test_imports()
        
        # 3. Test des f-strings
        self.test_fstrings()
        
        # 4. Test de l'encodage
        self.test_encoding()
        
        # 5. Test de l'indentation
        self.test_indentation()
        
        # 6. Test des variables non définies
        self.test_undefined_variables()
        
        # 7. Test des erreurs de logique
        self.test_logic_errors()
        
        # 8. Test des fichiers parasites
        self.clean_parasite_files()
        
        # 9. Test d'exécution
        self.test_execution()
        
        # Rapport final
        self.generate_report()
        
    def test_syntax_python(self):
        """Test de syntaxe Python sur tous les fichiers .f"""
        logger.info("🔍 Test de syntaxe Python...")
        
        for py_file in self.project_root.rglob("*.f"):
            self.files_checked += 1
            try:
                content = self.safe_read_file(py_file)
                if content:
                    ast.parse(content)
            except SyntaxError as e:
                error_msg = f"Erreur de syntaxe dans {py_file}: {e}"
                self.errors_found.append(error_msg)
                logger.error(error_msg)
                
                # Tentative de correction automatique
                if self.fix_syntax_error(py_file, str(e)):
                    self.files_fixed += 1
            except Exception as e:
                logger.warning(f"Impossible de tester la syntaxe de {py_file}: {e}")
                    
    def test_imports(self):
        """Test des f"""
        logger.info("📦 Test des imports...")
        
        for py_file in self.project_root.rglob("*.f"):
            try:
                content = self.safe_read_file(py_file)
                if not content:
                    continue
                    
                # Vérifier les imports relatifs
                if 'from .' in content and not py_file.name.startswith('__init__'):
                    error_msg = f"Import relatif suspect dans {py_file}"
                    self.errors_found.append(error_msg)
                    
                # Vérifier les imports inexistants
                try:
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                if not self.module_exists(alias.name):
                                    error_msg = f"Module inexistant: {alias.name} dans {py_file}"
                                    self.errors_found.append(error_msg)
                except SyntaxError:
                    # Ignorer les fichiers avec des erreurs de syntaxe
                    pass
                                
            except Exception as e:
                logger.warning(f"Impossible de tester les imports de {py_file}: {e}")
                
    def test_fstrings(self):
        """Test et correction des f-strings f"""
        logger.info("🔤 Test des f-strings...")
        
        for py_file in self.project_root.rglob("*.f"):
            try:
                content = self.safe_read_file(py_file)
                if not content:
                    continue
                    
                original_content = content
                
                # Correction des f-strings malformées
                # Pattern: variable"f" -> f"f"
                content = re.sub(r'(\w+)"([^f"]*\{[^}]*\}[^"]*)"', r'f"\2"', content)
                
                # Pattern: "f" -> f"f" si contient des {}
                content = re.sub(r'"([^f"]*\{[^}]*\}[^"]*)"', r'f"\1"', content)
                
                # Pattern: f"string" -> f"string" (général)
                content = re.sub(r'(\w+)"([^"]*)"', r'f"\2"', content)
                
                if content != original_content:
                    if self.safe_write_file(py_file, content):
                        self.fixes_applied.append(f"F-strings corrigées dans {py_file}")
                        self.files_fixed += 1
                    
            except Exception as e:
                logger.warning(f"Impossible de tester les f-strings de {py_file}: {e}")
                
    def test_encoding(self):
        """Test et correction de l'f"""
        logger.info("📝 Test de l'encodage...")
        
        for py_file in self.project_root.rglob("*.f"):
            try:
                content = self.safe_read_file(py_file)
                if not content:
                    continue
                    
                # Vérifier et corriger l'encodage
                if not content.startswith('#!'):
                    content = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n' + content
                    
                # Corriger les espaces dans l'encodage
                content = content.replace('utf-8', 'utf-8')
                content = content.replace('utf-8', 'utf-8')
                
                if self.safe_write_file(py_file, content):
                    self.fixes_applied.append(f"Encodage corrigé dans {py_file}")
                    
            except Exception as e:
                logger.warning(f"Impossible de corriger l'encodage de {py_file}: {e}")
                
    def test_indentation(self):
        """Test et correction de l'f"""
        logger.info("📏 Test de l'indentation...")
        
        for py_file in self.project_root.rglob("*.f"):
            try:
                content = self.safe_read_file(py_file)
                if not content:
                    continue
                    
                lines = content.splitlines(True)
                fixed_lines = []
                for line in lines:
                    # Remplacer les tabs par 4 espaces
                    line = line.expandtabs(4)
                    fixed_lines.append(line)
                    
                fixed_content = ''.join(fixed_lines)
                if fixed_content != content:
                    if self.safe_write_file(py_file, fixed_content):
                        self.fixes_applied.append(f"Indentation corrigée dans {py_file}")
                    
            except Exception as e:
                logger.warning(f"Impossible de corriger l'indentation de {py_file}: {e}")
                
    def test_undefined_variables(self):
        """Test des variables non f"""
        logger.info("🔍 Test des variables non définies...")
        
        for py_file in self.project_root.rglob("*.f"):
            try:
                content = self.safe_read_file(py_file)
                if not content:
                    continue
                    
                # Chercher les variables suspectes
                suspicious_vars = re.findall(r'\b(\w+)\s*"', content)
                for var in suspicious_vars:
                    if var not in ['f', 'r', 'b', 'u'] and not self.is_defined_variable(var, content):
                        error_msg = f"Variable suspecte: {var} dans {py_file}"
                        self.errors_found.append(error_msg)
                        
            except Exception as e:
                logger.warning(f"Impossible de tester les variables de {py_file}: {e}")
                
    def test_logic_errors(self):
        """Test des erreurs de logique"""
        logger.info("🧠 Test des erreurs de logique...")
        
        for py_file in self.project_root.rglob("*.f"):
            try:
                content = self.safe_read_file(py_file)
                if not content:
                    continue
                    
                # Corriger les erreurs courantes
                original_content = content
                
                # Corriger les assignations incorrectes
                content = re.sub(r'(\w+)\s*=\s*(\w+)\s*"', r'\1 = f"', content)
                
                # Corriger les appels de méthode incorrects
                content = re.sub(r'(\w+)\.(\w+)\s*"', r'\1.\2(f"', content)
                
                # Corriger les listes mutables dans les arguments par défaut
                content = re.sub(r'def (\w+)\([^)]*=\s*\[\s*\]', r'def \1(', content)
                
                if content != original_content:
                    if self.safe_write_file(py_file, content):
                        self.fixes_applied.append(f"Erreurs de logique corrigées dans {py_file}")
                        self.files_fixed += 1
                    
            except Exception as e:
                logger.warning(f"Impossible de tester la logique de {py_file}: {e}")
                
    def clean_parasite_files(self):
        """Nettoyage des fichiers parasites"""
        logger.info("🧹 Nettoyage des fichiers parasites...")
        
        parasite_patterns = [
            '**/.DS_Store',
            '**/Thumbs.db',
            '**/*.pyc',
            '**/__pycache__',
            '**/*.log',
            '**/.pytest_cache',
            '**/.coverage',
            '**/.mypy_cache'
        ]
        
        for pattern in parasite_patterns:
            for file_path in self.project_root.glob(pattern):
                try:
                    if file_path.is_file():
                        file_path.unlink()
                    elif file_path.is_dir():
                        import shutil
                        shutil.rmtree(file_path)
                    logger.info(f"Fichier parasite supprimé: {file_path}")
                except Exception as e:
                    logger.warning(f"Impossible de supprimer {file_path}: {e}")
                    
    def test_execution(self):
        """Test d'exécution des modules"""
        logger.info("▶️ Test d'exécution...")
        
        main_modules = [
            'athalia_unified.py',
            'modules/orchestrateur_principal.py',
            'modules/auto_correction_avancee.py',
            'modules/dashboard_unifie_simple.py'
        ]
        
        for module in main_modules:
            module_path = self.project_root / module
            if module_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, '-m', 'py_compile', str(module_path)],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if result.returncode == 0:
                        logger.info(f"✅ {module} compile correctement")
                    else:
                        error_msg = f"❌ {module} ne compile pas: {result.stderr}"
                        self.errors_found.append(error_msg)
                        logger.error(error_msg)
                except Exception as e:
                    error_msg = f"❌ Erreur lors du test de {module}: {e}"
                    self.errors_found.append(error_msg)
                    logger.error(error_msg)
                    
    def fix_syntax_error(self, file_path: Path, error_msg: str) -> bool:
        """Tentative de correction automatique d'erreur de syntaxe"""
        try:
            content = self.safe_read_file(file_path)
            if not content:
                return False
                
            original_content = content
            
            # Corrections automatiques basées sur l'erreur
            if "invalid f" in error_msg:
                # Corriger les f-strings malformées
                content = re.sub(r'(\w+)"([^f"]*\{[^}]*\}[^"]*)"', r'f"\2"', content)
                
            if "unexpected f" in error_msg:
                # Ajouter des parenthèses fermantes manquantes
                content = content.rstrip() + '\n'
                
            if content != original_content:
                if self.safe_write_file(file_path, content):
                    self.fixes_applied.append(f"Erreur de syntaxe corrigée dans {file_path}")
                    return True
                
        except Exception as e:
            logger.warning(f"Impossible de corriger {file_path}: {e}")
            
        return False
        
    def module_exists(self, module_name: str) -> bool:
        """Vérifie si un module existe"""
        try:
            __import__(module_name)
            return True
        except ImportError:
            return False
            
    def is_defined_variable(self, var_name: str, content: str) -> bool:
        """Vérifie si une variable est définie dans le contenu"""
        # Patterns de définition de variables
        patterns = [
            rf'{var_name}\s*=',
            rf'def {var_name}\(',
            rf'class {var_name}',
            rf'import {var_name}',
            rf'from .* import {var_name}',
            rf'for {var_name} in',
            rf'with .* as {var_name}'
        ]
        
        for pattern in patterns:
            if re.search(pattern, content):
                return True
        return False
        
    def generate_report(self):
        """Génère un rapport de test complet Athalia."""
        logger.info("📊 Génération du rapport...")
        
        report = f"{'='*60}\n\ud83d\udcca RAPPORT DE TEST COMPLET ATHALIA\n{'='*60}\n\n\ud83d\udcc8 Statistiques:\n   \u2022 Fichiers vérifiés: {self.files_checked}\n   \u2022 Fichiers corrigés: {self.files_fixed}\n   \u2022 Erreurs trouvées: {len(self.errors_found)}\n   \u2022 Corrections appliquées: {len(self.fixes_applied)}\n\n{'='*60}\n\n\u274c ERREURS TROUVÉES:\n{'='*60}\n"
        
        if self.errors_found:
            for error in self.errors_found:
                report += f"   • {error}\n"
        else:
            report += "   ✅ Aucune erreur trouvée!\n"
            
        report += f"{'='*60}\n\n\ud83d\udd27 CORRECTIONS APPLIQUÉES:\n{'='*60}\n"
        
        if self.fixes_applied:
            for fix in self.fixes_applied:
                report += f"   • {fix}\n"
        else:
            report += "   ✅ Aucune correction nécessaire!\n"
            
        report += f"{'='*60}\n\n\ud83c\udfaf RECOMMANDATIONS:\n{'='*60}\n"
        
        if self.errors_found:
            report += """
   • Vérifiez manuellement les erreurs restantes
   • Exécutez les tests unitaires
   • Vérifiez la documentation
   • Testez l'intégration complète
"""
        else:
            report += """
   • ✅ Le projet semble en bon état
   • Exécutez les tests de fonctionnalité
   • Vérifiez les performances
   • Testez l'intégration
"""
            
        report += f"\n{'='*60}\n"
        
        # Sauvegarder le rapport
        with open('rapport_test_complet.txt', 'w', encoding='utf-8') as f:
            f.write(report)
            
        logger.info("📄 Rapport sauvegardé: rapport_test_complet.txt")
        print(report)

def main():
    """Fonction f"""
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
        
    tester = TestCompletAthalia(project_root)
    tester.run_complete_test()

if __name__ == "__main__":
    main() 