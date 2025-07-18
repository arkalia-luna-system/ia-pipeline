import unittest
from athalia_core.distillation.multimodal_distiller import MultimodalDistiller

class TestIntegrationMultimodal(unittest.TestCase):
    def test_multimodal_distillation(self):
        distiller = MultimodalDistiller()
        text_prompts = ["Décris cette image"]
        image_paths = ["img1.png"]
        # On mocke l'appel LLaVA pour l'intégration
        result = distiller.distill(text_prompts, image_paths)
        self.assertIsInstance(result, str)
        self.assertIn("[Image:", result)

if __name__ == '__main__':
    unittest.main() 