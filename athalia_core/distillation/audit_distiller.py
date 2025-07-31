# -*- coding: utf-8 -*-
"""
Module de distillation d'audits pour Athalia/Arkalia
Fusionne et pondère plusieurs audits (sécurité, qualité, performance...)
"""

from typing import Any, Dict, List, Optional


class AuditDistiller:
    def __init__(self, weights: Optional[Dict[str, float]] = None):
        # Pondération par type d'audit (ex: {'securite': 0.3, 'qualite': 0.4,
        # ...})
        self.weights = weights or {}

    def distill(self, audits: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Fusionne plusieurs audits en un score global et des recommandations
        synthétiques.
        :param audits: Liste de résultats d'audit (dict)
        :return: Audit distillé (dict)
        """
        if not audits:
            return {}
        # Exemple simple: moyenne pondérée des scores
        total_score = 0.0
        total_weight = 0.0
        for audit in audits:
            t = audit.get("type", "autre")
            score = audit.get("score", 0)
            w = self.weights.get(t, 1.0)
            total_score += score * w
            total_weight += w
        global_score = total_score / total_weight if total_weight else 0.0
        return {"global_score": global_score, "details": audits}
