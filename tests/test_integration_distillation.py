import unittest
from athalia_core.athalia_orchestrator import AthaliaOrchestrator

class TestIntegrationDistillation(unittest.TestCase):
    def setUp(self):
        self.orch = AthaliaOrchestrator()

    def test_distillation_voting(self):
        result = self.orch.distill_ia_responses("Prompt test", strategy="voting")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result.strip()) > 0)

    def test_distillation_stacking(self):
        result = self.orch.distill_ia_responses("Prompt test", strategy="stacking")
        self.assertIsInstance(result, str)
        self.assertIn("|", result)

    def test_distillation_bagging(self):
        result = self.orch.distill_ia_responses("Prompt test", strategy="bagging")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result.strip()) > 0)

    def test_distillation_consensus(self):
        result = self.orch.distill_ia_responses("Prompt test", strategy="consensus")
        self.assertIsInstance(result, str)
        self.assertTrue("Consensus:" in result or len(result.strip()) > 0)

    def test_distillation_creative(self):
        result = self.orch.distill_ia_responses("Prompt test", strategy="creative")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("[Fusion IA]"))

if __name__ == '__main__':
    unittest.main() 