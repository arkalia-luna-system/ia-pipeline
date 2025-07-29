import unittest

from athalia_core import ai_robust


class TestAiRobust(unittest.TestCase):
    def test_robust_ai_instance(self):
        instance = ai_robust.robust_ai()
        self.assertIsInstance(instance, ai_robust.RobustAI)

    def test_fallback_ia(self):
        result = ai_robust.fallback_ia('Test prompt')
        self.assertIsInstance(result, str)

    def test_query_qwen(self):
        result = ai_robust.query_qwen('Test prompt')
        self.assertIsInstance(result, str)

    def test_query_mistral(self):
        result = ai_robust.query_mistral('Test prompt')
        self.assertIsInstance(result, str)

    def test_robustai_generate_blueprint(self):
        instance = ai_robust.robust_ai()
        result = instance.generate_blueprint('Créer un assistant')
        self.assertIsInstance(result, dict)

    def test_robustai_review_code(self):
        instance = ai_robust.robust_ai()
        result = instance.review_code('print("ok")', 'main.py', 'python', 80)
        self.assertIsInstance(result, dict)

    def test_robustai_generate_documentation(self):
        instance = ai_robust.robust_ai()
        result = instance.generate_documentation('TestProject', 'python', ['main.py'])
        self.assertIsInstance(result, str)

    def test_robustai_classify_project_complexity(self):
        instance = ai_robust.robust_ai()
        result = instance.classify_project_complexity('.')
        self.assertIsInstance(result, dict)

    def test_robustai_get_dynamic_prompt(self):
        instance = ai_robust.robust_ai()
        result = instance.get_dynamic_prompt('test')
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main() 