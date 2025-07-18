import unittest
import os
from athalia_core.distillation.adaptive_distillation import AdaptiveDistiller

class TestAdaptiveDistiller(unittest.TestCase):
    def setUp(self):
        # Utiliser un fichier temporaire pour l'historique
        self.history_path = "test_adaptive_distillation_history.json"
        if os.path.exists(self.history_path):
            os.remove(self.history_path)

    def tearDown(self):
        if os.path.exists(self.history_path):
            os.remove(self.history_path)

    def test_majority_voting(self):
        distiller = AdaptiveDistiller(history_path=self.history_path)
        responses = ["A", "B", "A", "C", "A", "B"]
        result = distiller.distill_responses(responses)
        self.assertEqual(result, "A")

    def test_empty(self):
        distiller = AdaptiveDistiller(history_path=self.history_path)
        self.assertEqual(distiller.distill_responses([]), "")

    def test_update_preferences(self):
        distiller = AdaptiveDistiller(history_path=self.history_path)
        responses = ["A", "B", "C"]
        distiller.update_preferences("B", responses)
        distiller.update_preferences("B", responses)
        distiller.update_preferences("A", responses)
        weighted = distiller.apply_learned_weights(responses)
        self.assertEqual(weighted[0], "B")

    def test_feedback_success_failure(self):
        distiller = AdaptiveDistiller(history_path=self.history_path)
        responses = ["A", "B", "C"]
        # B a 2 succès, 1 échec, A a 1 succès
        distiller.update_preferences("B", responses, success=True)
        distiller.update_preferences("B", responses, success=True)
        distiller.update_preferences("B", responses, success=False)
        distiller.update_preferences("A", responses, success=True)
        weighted = distiller.apply_learned_weights(responses)
        # B doit rester devant A grâce à son taux de succès
        self.assertEqual(weighted[0], "B")
        self.assertGreater(distiller.feedback["B"][0], 0)
        self.assertGreaterEqual(distiller.feedback["B"][1], 1)

    def test_save_and_load_history(self):
        distiller = AdaptiveDistiller(history_path=self.history_path)
        responses = ["A", "B"]
        distiller.update_preferences("A", responses, success=True)
        distiller.update_preferences("B", responses, success=False)
        distiller.save_history()
        # Recharger dans une nouvelle instance
        distiller2 = AdaptiveDistiller(history_path=self.history_path)
        self.assertEqual(distiller2.preference_weights, distiller.preference_weights)
        self.assertEqual(distiller2.feedback, distiller.feedback)
        self.assertEqual(distiller2.success_history, distiller.success_history)

if __name__ == '__main__':
    unittest.main() 