# -*- coding: utf-8 -*-
"""
Module de distillation de corrections IA pour Athalia/Arkalia
Fusionne, score et sélectionne la meilleure correction parmi plusieurs suggestions IA.
"""
from typing import Any, Dict, List, Optional


class CorrectionDistiller:
    def __init__(self, strategy: str = "score"):
        self.strategy = strategy

    def distill(
        self,
        corrections: List[str],
        scores: Optional[List[float]] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
            Sélectionne ou fusionne la meilleure correction IA.
        :param corrections: Liste de corrections proposées (str)
        :param scores: Scores optionnels pour chaque correction
        :param context: Contexte optionnel
        :return: Correction distillée (str)
        """
        if not corrections:
            return ""
        if self.strategy == "score" and scores:
            # Prend la correction avec le meilleur score
            idx = scores.index(max(scores))
            return corrections[idx]
        # Placeholder pour d'autres stratégies (fusion, feedback, etc.)
        return corrections[0]  # fallback
