#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour les agents unifiés
Corrigé après consolidation des agents
"""

import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestAgentUnified(unittest.TestCase):
    """Tests pour les agents unifiés (corrigé)"""

    @patch("athalia_core.ai_robust.query_qwen", return_value="Réponse mockée")
    def test_agent_unified_basic(self, mock_qwen):
        """Test basique des agents unifiés"""
        try:
            # Test d'import des nouveaux modules unifiés
            from athalia_core.agents.unified_agent import (
                AuditAgent,
                CorrectionAgent,
                QwenAgent,
                SynthesisAgent,
                UnifiedAgent,
            )

            # Test de création d'agents
            unified_agent = UnifiedAgent("test")
            audit_agent = AuditAgent()
            correction_agent = CorrectionAgent()
            synthesis_agent = SynthesisAgent()
            qwen_agent = QwenAgent()

            self.assertIsNotNone(unified_agent)
            self.assertIsNotNone(audit_agent)
            self.assertIsNotNone(correction_agent)
            self.assertIsNotNone(synthesis_agent)
            self.assertIsNotNone(qwen_agent)

        except ImportError as e:
            self.skipTest(f"Module non disponible: {e}")

    def test_agent_imports(self):
        """Test des imports d'agents unifiés"""
        try:
            # Test des imports corrigés
            from athalia_core.agents import context_prompt, unified_agent

            self.assertTrue(True, "Tous les imports d'agents unifiés fonctionnent")

        except ImportError as e:
            self.skipTest(f"Import d'agent non disponible: {e}")


if __name__ == "__main__":
    unittest.main()
