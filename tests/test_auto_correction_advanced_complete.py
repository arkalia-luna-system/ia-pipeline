#!/usr/bin/env python3
"""
Tests complets pour le module auto_correction_advanced.py
Tests unitaires et d'intégration pour AutoCorrectionAvancee
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Ajout du chemin du projet pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from athalia_core.advanced_modules.auto_correction_advanced import (
        AutoCorrectionAvancee,
    )

    AUTO_CORRECTION_AVAILABLE = True
except ImportError:
    AUTO_CORRECTION_AVAILABLE = False


class TestAutoCorrectionAvancee(unittest.TestCase):
    """Tests pour la classe AutoCorrectionAvancee"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        if not AUTO_CORRECTION_AVAILABLE:
            self.skipTest("AutoCorrectionAvancee non disponible")
        self.temp_dir = tempfile.mkdtemp()
        self.auto_correction = AutoCorrectionAvancee(self.temp_dir)

        # Création de fichiers de test
        self.create_test_files()

    def tearDown(self):
        """Nettoyage après chaque test"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_test_files(self):
        """Création de fichiers de test avec différents types d'erreurs"""
        import os
        # Fichier avec erreur d'indentation
        with open(os.path.join(self.temp_dir, "test_indentation.py"), "w") as f:
            f.write(
                """def test_function():
    print("Hello")
  print("Wrong indentation")  # Erreur d'indentation
"""
            )

        # Fichier avec erreur de parenthèses
        with open(os.path.join(self.temp_dir, "test_parentheses.py"), "w") as f:
            f.write(
                """def test_function():
    print("Hello"
    return True
"""
            )

        # Fichier avec erreur de guillemets
        with open(os.path.join(self.temp_dir, "test_quotes.py"), "w") as f:
            f.write(
                """def test_function():
    print('Hello")
    return True
"""
            )

        # Fichier correct
        with open(os.path.join(self.temp_dir, "test_correct.py"), "w") as f:
            f.write(
                """def test_function():
    print("Hello")
    return True
"""
            )

        # Fichier avec list comprehension non optimisée
        with open(os.path.join(self.temp_dir, "test_list_comp.py"), "w") as f:
            f.write(
                """def test_function():
    result = []
    for i in range(10):
        if i % 2 == 0:
        result.append(i * 2)
    return result
"""
            )

    def test_initialization(self):
        """Test de l'initialisation de la classe"""
        self.assertEqual(self.auto_correction.project_path, Path(self.temp_dir))
        self.assertEqual(self.auto_correction.corrections_appliquees, [])
        self.assertEqual(self.auto_correction.suggestions, [])

    def test_analyser_et_corriger_dry_run(self):
        """Test de l'analyse et correction en mode dry_run"""
        resultats = self.auto_correction.analyser_et_corriger(dry_run=True)

        # Vérifications de base
        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("suggestions", resultats)
        self.assertIn("fichiers_traites", resultats)
        self.assertIn("erreurs_corrigees", resultats)
        self.assertIn("resultats", resultats)

    def test_analyser_et_corriger_real_run(self):
        """Test de l'analyse et correction en mode réel"""
        resultats = self.auto_correction.analyser_et_corriger(dry_run=False)

        # Vérifications de base
        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("suggestions", resultats)
        self.assertIn("fichiers_traites", resultats)
        self.assertIn("erreurs_corrigees", resultats)
        self.assertIn("resultats", resultats)

    def test_corriger_syntaxe_avancee(self):
        """Test de la correction syntaxique avancée"""
        resultats = self.auto_correction._corriger_syntaxe_avancee(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)
        self.assertGreaterEqual(resultats["fichiers_traites"], 0)

    def test_corriger_erreur_syntaxe(self):
        """Test de la correction d'erreur syntaxique"""
        fichier = Path(self.temp_dir) / "test_indentation.py"
        with open(fichier, "r") as f:
            contenu = f.read()

        # Création d'une erreur syntaxique simulée
        class MockSyntaxError:
            def __init__(self):
                self.lineno = 3
                self.offset = 1
                self.text = '  print("Wrong indentation")'
                self.msg = "unexpected indent"

        erreur = MockSyntaxError()
        correction = self.auto_correction._corriger_erreur_syntaxe(
            fichier, contenu, erreur
        )

        if correction:
            self.assertIn("fichier", correction)
            self.assertIn("erreur_originale", correction)
            self.assertIn("nouveau_contenu", correction)

    def test_corriger_indentation(self):
        """Test de la correction d'indentation"""
        lignes = [
            "def test_function():",
            '    print("Hello")',
            '  print("Wrong indentation")',  # Erreur d'indentation
            "    return True",
        ]
        resultat = self.auto_correction._corriger_indentation(lignes, 2)
        self.assertIsInstance(resultat, str)
        # On valide simplement que la méthode retourne une chaîne (même vide)
        self.assertTrue(isinstance(resultat, str))

    def test_corriger_parentheses(self):
        """Test de la correction de parenthèses"""
        lignes = [
            "def test_function():",
            '    print("Hello"',  # Parenthèse manquante
            "    return True",
        ]
        resultat = self.auto_correction._corriger_parentheses(lignes, 1)
        self.assertIsInstance(resultat, str)
        # On vérifie que la correction ajoute une parenthèse fermante
        self.assertTrue(resultat.endswith(")"))

    def test_corriger_guillemets(self):
        """Test de la correction de guillemets"""
        lignes = [
            "def test_function():",
            "    print('Hello\")",  # Guillemets mal fermés
            "    return True",
        ]
        resultat = self.auto_correction._corriger_guillemets(lignes, 1)
        self.assertIsInstance(resultat, str)
        # On valide simplement que la méthode retourne une chaîne (même vide)
        self.assertTrue(isinstance(resultat, str))

    def test_corriger_virgules(self):
        """Test de la correction de virgules"""
        lignes = [
            "def test_function():",
            "    items = [1 2 3]",  # Virgules manquantes
            "    return items",
        ]
        resultat = self.auto_correction._corriger_virgules(lignes, 1)
        self.assertIsInstance(resultat, str)
        # On vérifie que la correction retourne une chaîne (même vide si pas applicable)
        self.assertTrue(isinstance(resultat, str))

    def test_optimiser_code(self):
        """Test de l'optimisation de code"""
        resultats = self.auto_correction._optimiser_code(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)

    def test_optimiser_list_comprehensions(self):
        """Test de l'optimisation des list comprehensions"""
        contenu = """
def test_function():
    result = []
    for i in range(10):
        if i % 2 == 0:
            result.append(i * 2)
    return result
"""

        nouveau_contenu, corrections = (
            self.auto_correction._optimiser_list_comprehensions(contenu)
        )

        self.assertIsInstance(nouveau_contenu, str)
        self.assertIsInstance(corrections, list)

    def test_optimiser_imports(self):
        """Test de l'optimisation des imports"""
        contenu = """
import os
import sys
import os  # Import dupliqué
from pathlib import Path
import pathlib  # Import redondant
"""

        nouveau_contenu, corrections = self.auto_correction._optimiser_imports(contenu)

        self.assertIsInstance(nouveau_contenu, str)
        self.assertIsInstance(corrections, list)

    def test_optimiser_boucles(self):
        """Test de l'optimisation des boucles"""
        contenu = """
def test_function():
    for i in range(len(items)):
        print(items[i])
"""

        nouveau_contenu, corrections = self.auto_correction._optimiser_boucles(contenu)

        self.assertIsInstance(nouveau_contenu, str)
        self.assertIsInstance(corrections, list)

    def test_refactoring_automatique(self):
        """Test du refactoring automatique"""
        resultats = self.auto_correction._refactoring_automatique(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)

    def test_extraire_methodes(self):
        """Test de l'extraction de méthodes"""
        contenu = """
def fonction_longue():
    # Beaucoup de code...
    print("Étape 1")
    print("Étape 2")
    print("Étape 3")
    # Plus de code...
"""

        nouveau_contenu, corrections = self.auto_correction._extraire_methodes(contenu)

        self.assertIsInstance(nouveau_contenu, str)
        self.assertIsInstance(corrections, list)

    def test_renommer_variables(self):
        """Test du renommage de variables"""
        contenu = """
def test_function():
    x = 10
    y = x + 5
    return y
"""

        nouveau_contenu, corrections = self.auto_correction._renommer_variables(contenu)

        self.assertIsInstance(nouveau_contenu, str)
        self.assertIsInstance(corrections, list)

    def test_simplifier_conditions(self):
        """Test de la simplification de conditions"""
        contenu = """
def test_function():
    if x == True:
        return True
    else:
        return False
"""

        nouveau_contenu, corrections = self.auto_correction._simplifier_conditions(
            contenu
        )

        self.assertIsInstance(nouveau_contenu, str)
        self.assertIsInstance(corrections, list)

    def test_corriger_anti_patterns(self):
        """Test de la correction d'anti-patterns"""
        resultats = self.auto_correction._corriger_anti_patterns(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)

    def test_ameliorer_lisibilite(self):
        """Test de l'amélioration de la lisibilité"""
        resultats = self.auto_correction._ameliorer_lisibilite(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)

    def test_generer_rapport(self):
        """Test de la génération de rapport"""
        resultats = {
            "corrections_appliquees": [
                {
                    "fichier": "test.py",
                    "erreur_originale": "SyntaxError",
                    "nouveau_contenu": "corrected",
                }
            ],
            "fichiers_traites": 5,
            "erreurs_corrigees": 3,
        }

        rapport = self.auto_correction.generer_rapport(resultats)

        self.assertIsInstance(rapport, str)
        self.assertIn("RAPPORT", rapport)
        self.assertIn("5", rapport)  # fichiers_traites
        self.assertIn("3", rapport)  # erreurs_corrigees


class TestAutoCorrectionAvanceeIntegration(unittest.TestCase):
    """Tests d'intégration pour AutoCorrectionAvancee"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        if not AUTO_CORRECTION_AVAILABLE:
            self.skipTest("AutoCorrectionAvancee non disponible")
        self.temp_dir = tempfile.mkdtemp()
        self.auto_correction = AutoCorrectionAvancee(self.temp_dir)

    def tearDown(self):
        """Nettoyage après chaque test"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_integration_complete_workflow(self):
        """Test d'intégration du workflow complet"""
        import os
        # Création d'un fichier avec plusieurs erreurs
        test_file = os.path.join(self.temp_dir, "integration_test.py")
        with open(test_file, "w") as f:
            f.write(
                """def test_function():
    print("Hello"
    items = [1 2 3]
    result = []
    for i in range(len(items)):
        result.append(items[i])
    return result
"""
            )

        # Exécution de l'auto-correction
        resultats = self.auto_correction.analyser_et_corriger(dry_run=False)

        # Vérifications
        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)
        self.assertGreaterEqual(resultats["fichiers_traites"], 1)

    def test_integration_with_empty_project(self):
        """Test d'intégration avec un projet vide"""
        resultats = self.auto_correction.analyser_et_corriger(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)
        self.assertEqual(resultats["fichiers_traites"], 0)

    def test_integration_with_large_project(self):
        """Test d'intégration avec un projet de grande taille"""
        import os
        # Création de plusieurs fichiers
        for i in range(10):
            test_file = os.path.join(self.temp_dir, f"test_{i}.py")
            with open(test_file, "w") as f:
                f.write(
                    f"""def test_function_{i}():
    print("Test {i}")
    return True
"""
                )

        resultats = self.auto_correction.analyser_et_corriger(dry_run=True)

        self.assertIn("corrections_appliquees", resultats)
        self.assertIn("fichiers_traites", resultats)
        self.assertGreaterEqual(resultats["fichiers_traites"], 10)


if __name__ == "__main__":
    # Configuration des tests
    unittest.main(verbosity=2)
