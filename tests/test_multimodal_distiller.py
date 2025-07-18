import unittest
from unittest.mock import patch
from athalia_core.distillation.multimodal_distiller import MultimodalDistiller

class TestMultimodalDistiller(unittest.TestCase):
    @patch.object(MultimodalDistiller, 'call_llava', return_value="Analyse image OK")
    def test_distill(self, mock_llava):
        distiller = MultimodalDistiller()
        text_prompts = ["Décris cette image"]
        image_paths = ["img1.png"]
        result = distiller.distill(text_prompts, image_paths)
        self.assertIn("[Image: Analyse image OK]", result)
        # Vérifie simplement que la partie texte n'est pas vide
        self.assertTrue(result.split("\n[Image:")[0].strip())

    def test_empty(self):
        distiller = MultimodalDistiller()
        result = distiller.distill([], [])
        self.assertEqual(result, "\n[Image: ]")

if __name__ == '__main__':
    unittest.main() 