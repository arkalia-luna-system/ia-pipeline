import unittest
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import conditionnel
try:
    from athalia_core.agents.agent_network import AuditAgent, CorrectionAgent, SynthesisAgent
except ImportError:
    AuditAgent = None
    CorrectionAgent = None
    SynthesisAgent = None

class TestIntegrationAutoGen(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        if AuditAgent is None:
            self.skipTest("Module agent_network non disponible")
    
    def test_autogen_orchestration(self):
        """Test d'orchestration avec AutoGen
        
        Scénario : Test de l'orchestration des agents
        Données : Agents d'audit, correction et synthèse
        Résultat attendu : Synthèse contenant les résultats des agents
        """
        audit = AuditAgent()
        correction = CorrectionAgent()
        synth = SynthesisAgent()
        prompt = "Test prompt"
        
        r1 = audit.act(prompt)
        r2 = correction.act(prompt)
        result = synth.act(prompt, [r1, r2])
        
        self.assertIsInstance(result, str, "Le résultat doit être une chaîne")
        self.assertIn(r1, result, "Le résultat de l'audit doit être dans la synthèse")
        self.assertIn(r2, result, "Le résultat de la correction doit être dans la synthèse")

if __name__ == '__main__':
    unittest.main() 