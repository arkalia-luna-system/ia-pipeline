import unittest
from unittest.mock import patch

from athalia_core.distillation.multimodal_distiller import MultimodalDistiller
from athalia_core.ai_robust import RobustAI


class TestMultimodalDistiller(unittest.TestCase):
    @patch.object(MultimodalDistiller, "call_llava", return_value="Analyse image OK")
    @patch.object(RobustAI, "_call_model", return_value="Réponse texte OK")
    def test_distill(self, mock_model, mock_llava):
        distiller = MultimodalDistiller()
        text_prompts = ["Décris cette image"]
        image_paths = ["img1.png"]
        result = distiller.distill(text_prompts, image_paths)
        self.assertIn("[Image: Analyse image OK]", result)
        # Vérifie que la partie texte contient la réponse mockée
        text_part = result.split("\n[Image:")[0].strip()
        self.assertIn("Réponse texte OK", text_part)

    def test_empty(self):
        distiller = MultimodalDistiller()
        result = distiller.distill([], [])
        self.assertEqual(result, "\n[Image: ]")


if __name__ == "__main__":
    unittest.main()
