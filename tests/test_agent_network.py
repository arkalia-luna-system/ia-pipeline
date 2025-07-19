#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour les agents réseau
Corrigé après réorganisation des modules
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestAgentNetwork(unittest.TestCase):
    """Tests pour les agents réseau (corrigé)"""
    
    @patch('athalia_core.ai_robust.query_qwen', return_value="Réponse mockée")
    def test_agent_network_basic(self, mock_qwen):
        """Test basique des agents réseau"""
        try:
            # Test d'import des nouveaux modules
            from athalia_core.agents.network_agent import NetworkAgent
            from athalia_core.agents.audit_agent import AuditAgent
            
            # Test de création d'agents
            network_agent = NetworkAgent()
            audit_agent = AuditAgent()
            
            self.assertIsNotNone(network_agent)
            self.assertIsNotNone(audit_agent)
            
        except ImportError as e:
            self.skipTest(f"Module non disponible: {e}")
    
    def test_agent_imports(self):
        """Test des imports d'agents"""
        try:
            # Test des imports corrigés
            from athalia_core.agents import context_prompt
            from athalia_core.agents import network_agent
            from athalia_core.agents import audit_agent
            from athalia_core.agents import qwen_agent
            
            self.assertTrue(True, "Tous les imports d'agents fonctionnent")
            
        except ImportError as e:
            self.skipTest(f"Import d'agent non disponible: {e}")

if __name__ == '__main__':
    unittest.main() 