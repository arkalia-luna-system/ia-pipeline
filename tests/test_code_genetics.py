import unittest

from athalia_core.distillation.code_genetics import CodeGenetics


class TestCodeGenetics(unittest.TestCase):
    def setUp(self):
        self.genetics = CodeGenetics()
        self.solutions = ["print('hello world')", "print('hello')", "world = 1"]

    def test_crossover(self):
        # Le résultat doit être une combinaison de fragments des solutions
        result = self.genetics.crossover(self.solutions)
        self.assertTrue(
            any(
                word in result
                for word in ["print('hello", "world')", "world", "=", "1"]
            )
        )

    def test_mutate(self):
        solution = "print('hello world')"
        mutated = self.genetics.mutate(solution, mutation_rate=1.0)
        self.assertNotEqual(mutated, solution)
        self.assertTrue(mutated.startswith("MUT_") or "MUT_" in mutated)

    def test_select(self):
        # Score = longueur de la solution
        def scorer(s):
            return len(s)
        selected = self.genetics.select(self.solutions, scorer, top_k=2)
        self.assertEqual(len(selected), 2)
        self.assertTrue(all(isinstance(s, str) for s in selected))

    def test_evolve(self):
        def scorer(s):
            return len(s)  # Favorise les solutions longues
        best = self.genetics.evolve(
            self.solutions, scorer, generations=2, mutation_rate=0.5
        )
        self.assertIsInstance(best, str)
        self.assertTrue(len(best) > 0)

    def test_empty(self):
        def scorer(s):
            return 1
        self.assertEqual(self.genetics.crossover([]), "")
        self.assertEqual(self.genetics.evolve([], scorer), "")


if __name__ == "__main__":
    unittest.main()
