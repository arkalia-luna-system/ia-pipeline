# -*- coding: utf-8 -*-
"""
Module de distillation de réponses IA pour Athalia/Arkalia
Permet de fusionner plusieurs réponses IA en une solution optimale
(voting, stacking, bagging, consensus scoring...)
"""
import random
from collections import Counter
from typing import Any, Dict, List, Optional


class ResponseDistiller:
    def __init__(self, strategy: str = "voting"):
        self.strategy = strategy

    def distill(
        self, responses: List[str], context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Fusionne plusieurs réponses IA selon la stratégie choisie.
        :param responses: Liste de réponses IA (str)
        :param context: Contexte optionnel (pour scoring avancé)
        :return: Réponse distillée (str)
        """
        if self.strategy == "voting":
            return self.majority_voting(responses)
        elif self.strategy == "stacking":
            return self.stacking(responses, context)
        elif self.strategy == "bagging":
            return self.bagging(responses)
        elif self.strategy == "consensus":
            return self.consensus_scoring(responses)
        elif self.strategy == "creative":
            return self.creative_fusion(responses)
        return responses[0] if responses else ""  # fallback

    def majority_voting(self, responses: List[str]) -> str:
        """Retourne la réponse la plus fréquente (majorité)."""
        if not responses:
            return ""
        counter = Counter(responses)
        return counter.most_common(1)[0][0]

    def stacking(
        self, responses: List[str], context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Concatène les parties communes, puis les parties uniques."""
        if not responses:
            return ""
        words = [set(r.split()) for r in responses]
        common = set.intersection(*words) if words else set()
        unique = set.union(*words) - common
        return " ".join(sorted(common)) + " | " + " ".join(sorted(unique))

    def bagging(self, responses: List[str]) -> str:
        """Retourne une réponse aléatoire parmi les plus fréquentes (bagging)."""
        if not responses:
            return ""
        counter = Counter(responses)
        top_count = counter.most_common(1)[0][1]
        top_responses = [resp for resp, count in counter.items() if count == top_count]
        return random.choice(top_responses)

    def consensus_scoring(self, responses: List[str]) -> str:
        """Retourne la plus longue sous-chaîne commune ET les parties divergentes."""
        if not responses:
            return ""
        from difflib import SequenceMatcher

        def lcs(a, b):
            match = SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))
            return a[match.a : match.a + match.size]

        consensus = responses[0]
        for r in responses[1:]:
            consensus = lcs(consensus, r)
        divergents = []
        for r in responses:
            if consensus not in r:
                divergents.append(r)
        if consensus and len(consensus) > 2:
            return (
                f"Consensus: {consensus} | Divergents: "
                f"{' || '.join(divergents) if divergents else 'Aucun'}"
            )
        return self.majority_voting(responses)

    def creative_fusion(self, responses: List[str]) -> str:
        """
        Fusion créative : mélange de fragments, ajout d'un tag IA, et concat unique.
        """
        if not responses:
            return ""
        fragments = set()
        for r in responses:
            fragments.update(r.split())
        fusion = " ".join(random.sample(list(fragments), min(len(fragments), 10)))
        return f"[Fusion IA] {fusion}"


def distill_responses(
    responses: list, strategy: str = "voting", context: Optional[dict] = None
) -> str:
    """Fonction utilitaire pour distiller une liste de réponses IA."""
    distiller = ResponseDistiller(strategy=strategy)
    return distiller.distill(responses, context)
