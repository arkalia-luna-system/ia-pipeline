#!/usr/bin/env python3
"""
Tests pour le module audit_agent.py
Tests unitaires et d'intégration pour AuditAgent
"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Ajout du chemin du projet pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from athalia_core.agents.audit_agent import AuditAgent

    AUDIT_AGENT_AVAILABLE = True
except ImportError:
    AUDIT_AGENT_AVAILABLE = False


class TestAuditAgent(unittest.TestCase):
    """Tests pour la classe AuditAgent"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        if not AUDIT_AGENT_AVAILABLE:
            self.skipTest("AuditAgent non disponible")
        self.agent = AuditAgent()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Nettoyage après chaque test"""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_audit_agent_initialization(self):
        """Test de l'initialisation de l'agent"""
        self.assertIsNotNone(self.agent)
        self.assertTrue(hasattr(self.agent, "act"))

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_act_method_with_simple_prompt(self, mock_query_qwen):
        """Test de la méthode act avec un prompt simple"""
        # Configuration du mock
        mock_query_qwen.return_value = "Audit terminé avec succès"

        # Test
        result = self.agent.act("Audit ce code: def foo(): pass")

        # Vérifications
        self.assertEqual(result, "Audit terminé avec succès")
        mock_query_qwen.assert_called_once_with("Audit ce code: def foo(): pass")

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_act_method_with_complex_prompt(self, mock_query_qwen):
        """Test de la méthode act avec un prompt complexe"""
        # Configuration du mock
        mock_query_qwen.return_value = "Analyse approfondie effectuée"

        # Test avec un prompt plus complexe
        complex_prompt = """
        Audit complet du projet:
        - Vérification de la qualité du code
        - Analyse des performances
        - Contrôle de sécurité
        - Documentation
        """

        result = self.agent.act(complex_prompt)

        # Vérifications
        self.assertEqual(result, "Analyse approfondie effectuée")
        mock_query_qwen.assert_called_once_with(complex_prompt)

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_act_method_with_empty_prompt(self, mock_query_qwen):
        """Test de la méthode act avec un prompt vide"""
        # Configuration du mock
        mock_query_qwen.return_value = ""

        # Test
        result = self.agent.act("")

        # Vérifications
        self.assertEqual(result, "")
        mock_query_qwen.assert_called_once_with("")

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_act_method_with_special_characters(self, mock_query_qwen):
        """Test de la méthode act avec des caractères spéciaux"""
        # Configuration du mock
        mock_query_qwen.return_value = "Audit avec caractères spéciaux"

        # Test avec des caractères spéciaux
        special_prompt = "Audit: éàçù€$£¥@#%&*()[]{}|\\:;\"'<>?,./"

        result = self.agent.act(special_prompt)

        # Vérifications
        self.assertEqual(result, "Audit avec caractères spéciaux")
        mock_query_qwen.assert_called_once_with(special_prompt)

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_act_method_with_multiline_prompt(self, mock_query_qwen):
        """Test de la méthode act avec un prompt multi-lignes"""
        # Configuration du mock
        mock_query_qwen.return_value = "Audit multi-lignes terminé"

        # Test avec un prompt multi-lignes
        multiline_prompt = """Audit du code Python:

        def fonction_test():
            print("Hello World")
            return True

        class MaClasse:
            def __init__(self):
                self.valeur = 42
        """

        result = self.agent.act(multiline_prompt)

        # Vérifications
        self.assertEqual(result, "Audit multi-lignes terminé")
        mock_query_qwen.assert_called_once_with(multiline_prompt)

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_act_method_error_handling(self, mock_query_qwen):
        """Test de la gestion d'erreur dans la méthode act"""
        # Configuration du mock pour lever une exception
        mock_query_qwen.side_effect = Exception("Erreur de connexion")

        # Test
        with self.assertRaises(RuntimeError):
            self.agent.act("Test d'erreur")

    def test_agent_inheritance(self):
        """Test de l'héritage de l'agent"""
        # Vérification que l'agent a les attributs nécessaires
        self.assertTrue(hasattr(self.agent, "act"))
        self.assertTrue(callable(self.agent.act))

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_agent_consistency(self, mock_query_qwen):
        """Test de la cohérence de l'agent sur plusieurs appels"""
        # Configuration du mock
        mock_query_qwen.return_value = "Résultat cohérent"

        # Tests multiples
        for i in range(5):
            result = self.agent.act(f"Test {i}")
            self.assertEqual(result, "Résultat cohérent")

        # Vérification du nombre d'appels
        self.assertEqual(mock_query_qwen.call_count, 5)

    def test_agent_attributes(self):
        """Test des attributs de l'agent"""
        # Vérification des attributs essentiels
        self.assertTrue(hasattr(self.agent, "act"))
        self.assertTrue(callable(self.agent.act))

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_agent_performance(self, mock_query_qwen):
        """Test de performance de l'agent"""
        import time

        # Configuration du mock
        mock_query_qwen.return_value = "Test de performance"

        # Test de performance
        start_time = time.time()
        for _ in range(10):
            self.agent.act("Test rapide")
        end_time = time.time()

        # Vérification que le temps d'exécution est raisonnable (< 1 seconde)
        execution_time = end_time - start_time
        self.assertLess(execution_time, 1.0)


class TestAuditAgentIntegration(unittest.TestCase):
    """Tests d'intégration pour AuditAgent"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        if not AUDIT_AGENT_AVAILABLE:
            self.skipTest("AuditAgent non disponible")
        self.agent = AuditAgent()

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_integration_with_real_audit_scenario(self, mock_query_qwen):
        """Test d'intégration avec un scénario d'audit réel"""
        # Configuration du mock pour simuler une réponse d'audit
        mock_query_qwen.return_value = """
        AUDIT RÉSULTAT:
        - Qualité du code: 8/10
        - Performance: 7/10
        - Sécurité: 9/10
        - Documentation: 6/10

        RECOMMANDATIONS:
        1. Améliorer la documentation
        2. Optimiser les boucles
        3. Ajouter des tests unitaires
        """

        # Test d'audit complet
        audit_prompt = """
        Effectue un audit complet du code suivant:

        def calculer_moyenne(nombres):
            total = 0
            for n in nombres:
                total += n
            return total / len(nombres)
        """

        result = self.agent.act(audit_prompt)

        # Vérifications
        self.assertIn("AUDIT RÉSULTAT", result)
        self.assertIn("RECOMMANDATIONS", result)
        mock_query_qwen.assert_called_once_with(audit_prompt)

    @patch("athalia_core.agents.audit_agent.query_qwen")
    def test_integration_with_code_analysis(self, mock_query_qwen):
        """Test d'intégration avec analyse de code"""
        # Configuration du mock
        mock_query_qwen.return_value = "Code analysé avec succès"

        # Test d'analyse de code
        code_to_analyze = """
        class MonProjet:
            def __init__(self):
                self.data = []

            def ajouter(self, item):
                self.data.append(item)

            def obtenir(self, index):
                return self.data[index]
        """

        result = self.agent.act(f"Analyse ce code: {code_to_analyze}")

        # Vérifications
        self.assertEqual(result, "Code analysé avec succès")
        mock_query_qwen.assert_called_once()


if __name__ == "__main__":
    # Configuration des tests
    unittest.main(verbosity=2)
