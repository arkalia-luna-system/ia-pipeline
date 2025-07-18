import unittest
from agents.agent_network import AuditAgent, CorrectionAgent, SynthesisAgent

class TestIntegrationAutoGen(unittest.TestCase):
    def test_autogen_orchestration(self):
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