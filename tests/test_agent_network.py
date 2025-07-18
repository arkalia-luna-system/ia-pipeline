import unittest
from unittest.mock import patch
from agents.agent_network import AuditAgent, CorrectionAgent, SynthesisAgent

class TestAgentNetwork(unittest.TestCase):
    @patch('athalia_core.ai_robust.query_qwen', return_value="Réponse mockée")
    def test_agent_network(self, mock_qwen):
        audit = AuditAgent()
        correction = CorrectionAgent()
        synth = SynthesisAgent()
        prompt = "Test prompt"
        r1 = audit.act(prompt)
        r2 = correction.act(prompt)
        result = synth.act(prompt, [r1, r2])
        self.assertIsInstance(result, str)
        self.assertIn(r1, result)
        self.assertIn(r2, result)

if __name__ == '__main__':
    unittest.main() 