import unittest
from athalia_core.distillation.response_distiller import ResponseDistiller
from athalia_core.distillation.audit_distiller import AuditDistiller
from athalia_core.distillation.correction_distiller import CorrectionDistiller
from athalia_core.distillation.quality_scorer import QualityScorer

class TestResponseDistiller(unittest.TestCase):
    def test_majority_voting(self):
        distiller = ResponseDistiller(strategy='voting')
        responses = ["A", "B", "A", "C", "A", "B"]
        result = distiller.distill(responses)
        self.assertEqual(result, "A")
    def test_empty(self):
        distiller = ResponseDistiller()
        self.assertEqual(distiller.distill([]), "")

    def test_stacking(self):
        distiller = ResponseDistiller(strategy='stacking')
        responses = ["print('hello world')", "print('hello')", "world = 1"]
        result = distiller.distill(responses)
        self.assertIn("print('hello'", result)
        self.assertIn("world", result)

    def test_consensus(self):
        distiller = ResponseDistiller(strategy='consensus')
        responses = ["def foo(): return 1", "def foo(): return 2", "def foo(): return 3"]
        result = distiller.distill(responses)
        self.assertIn("def foo(): return ", result)

    def test_consensus_divergents(self):
        distiller = ResponseDistiller(strategy='consensus')
        responses = ["def foo(): return 1", "def bar(): return 2", "def foo(): return 3"]
        result = distiller.distill(responses)
        assert "Consensus:" in result
        assert "Divergents:" in result

class TestAuditDistiller(unittest.TestCase):
    def test_weighted_average(self):
        audits = [
            {'type': 'securite', 'score': 8},
            {'type': 'qualite', 'score': 6},
            {'type': 'performance', 'score': 10}
        ]
        weights = {'securite': 0.5, 'qualite': 0.3, 'performance': 0.2}
        distiller = AuditDistiller(weights=weights)
        result = distiller.distill(audits)
        expected = (8*0.5 + 6*0.3 + 10*0.2) / (0.5+0.3+0.2)
        self.assertAlmostEqual(result['global_score'], expected)
    def test_empty(self):
        distiller = AuditDistiller()
        self.assertEqual(distiller.distill([]), {})

class TestCorrectionDistiller(unittest.TestCase):
    def test_best_score(self):
        corrections = ["fix1", "fix2", "fix3"]
        scores = [0.2, 0.9, 0.5]
        distiller = CorrectionDistiller(strategy='score')
        result = distiller.distill(corrections, scores=scores)
        self.assertEqual(result, "fix2")
    def test_empty(self):
        distiller = CorrectionDistiller()
        self.assertEqual(distiller.distill([]), "")

class TestQualityScorer(unittest.TestCase):
    def test_score_default(self):
        scorer = QualityScorer()
        self.assertEqual(scorer.score("solution"), 1.0)

if __name__ == '__main__':
    unittest.main() 