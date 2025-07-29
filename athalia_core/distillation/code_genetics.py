# -*- coding: utf-8 -*-
"""
Code Genetics pour Athalia/Arkalia
- Croisement, mutation, sélection, évolution de solutions IA
"""
import random
from typing import Callable, List


class CodeGenetics:
    def crossover(self, solutions: List[str]) -> str:
        """
        Croisement de solutions : mélange aléatoire de fragments de chaque solution.
        :param solutions: Liste de solutions (str)
        :return: Nouvelle solution croisée
        """
        if not solutions:
            return ""
        fragments = [sol.split() for sol in solutions]
        length = min(len(f) for f in fragments)
        child = []
        for i in range(length):
            parent = random.choice(fragments)
            child.append(parent[i])
        return " ".join(child)

    def mutate(self, solution: str, mutation_rate: float = 0.1) -> str:
        """
        Mutation simple : modifie aléatoirement des mots de la solution.
        :param solution: Solution à muter
        :param mutation_rate: Taux de mutation (0-1)
        :return: Solution mutée
        """
        words = solution.split()
        for i in range(len(words)):
            if random.random() < mutation_rate:
                words[i] = f"MUT_{random.randint(0,999)}"
        return " ".join(words)

    def select(
        self, solutions: List[str], scorer: Callable[[str], float], top_k: int = 2
    ) -> List[str]:
        """
        Sélectionne les meilleures solutions selon un score.
        :param solutions: Liste de solutions
        :param scorer: Fonction de scoring (str -> float)
        :param top_k: Nombre de solutions à garder
        :return: Liste des meilleures solutions
        """
        scored = sorted(solutions, key=scorer, reverse=True)
        return scored[:top_k]

    def evolve(
        self,
        solutions: List[str],
        scorer: Callable[[str], float],
        generations: int = 3,
        mutation_rate: float = 0.1,
    ) -> str:
        """
        Fait évoluer les solutions sur plusieurs générations (croisement, mutation, sélection).
        :param solutions: Liste initiale
        :param scorer: Fonction de scoring
        :param generations: Nombre de générations
        :param mutation_rate: Taux de mutation
        :return: Meilleure solution finale
        """
        population = solutions[:]
        for _ in range(generations):
            # Croisement
            children = [
                self.crossover(random.sample(population, min(2, len(population))))
                for _ in range(len(population))
            ]
            # Mutation
            mutated = [self.mutate(child, mutation_rate) for child in children]
            # Sélection
            population = self.select(population + mutated, scorer, top_k=len(solutions))
        return population[0] if population else ""
