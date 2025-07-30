# -*- coding: utf-8 -*-
"""
Distillation adaptative pour Athalia/Arkalia
- Pondération dynamique selon préférences et feedback utilisateur
- Historique sauvegardé/chargé en JSON
"""
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class AdaptiveDistiller:
    def __init__(self, history_path: Optional[str] = None):
        """
          Initialise le distillateur adaptatif.
        :param history_path: Chemin du fichier JSON pour l'historique (optionnel)
        """
        self.preference_weights: Dict[str, float] = {}  # Pondération des réponses
        self.success_history: List[str] = []  # Historique des succès
        # {réponse: [succès, échecs]}
        self.feedback: Dict[str, List[int]] = {}
        self.history_path = history_path or "adaptive_distillation_history.json"
        self.load_history()

    def distill_responses(
        self, responses: List[str], context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
          Fusionne les réponses IA en tenant compte des préférences et du feedback utilisateur.
        :param responses: Liste de réponses IA
        :param context: Contexte optionnel
        :return: Réponse distillée
        """
        weighted_responses = self.apply_learned_weights(responses)
        return self.ensemble_fusion(weighted_responses, context)

    def update_preferences(
        self, chosen_response: str, responses: List[str], success: bool = True
    ):
        """
          Met à jour les préférences et le feedback selon la réponse choisie et le succès/échec.
        :param chosen_response: Réponse sélectionnée
        :param responses: Liste des réponses proposées
        :param success: Succès (True) ou échec (False) de la réponse
        """
        if chosen_response not in self.preference_weights:
            self.preference_weights[chosen_response] = 1.0
        else:
            self.preference_weights[chosen_response] += 1.0
        self.success_history.append(chosen_response)
        # Feedback succès/échec
        if chosen_response not in self.feedback:
            self.feedback[chosen_response] = [0, 0]  # [succès, échecs]
        if success:
            self.feedback[chosen_response][0] += 1
        else:
            self.feedback[chosen_response][1] += 1
        self.save_history()

    def apply_learned_weights(self, responses: List[str]) -> List[str]:
        """
          Trie les réponses selon leur poids appris et taux de succès.
        :param responses: Liste de réponses IA
        :return: Liste triée
        """

        def score(r):
            w = self.preference_weights.get(r, 0)
            s, f = self.feedback.get(r, [0, 0])
            total = s + f
            taux_succes = s / total if total > 0 else 0
            return w + taux_succes

        return sorted(responses, key=score, reverse=True)

    def ensemble_fusion(
        self, responses: List[str], context: Optional[Dict[str, Any]]
    ) -> str:
        """
          Fusionne les réponses (majority voting par défaut).
        :param responses: Liste de réponses pondérées
        :param context: Contexte optionnel
        :return: Réponse fusionnée
        """
        from collections import Counter

        if not responses:
            return ""
        counter = Counter(responses)
        return counter.most_common(1)[0][0]

    def save_history(self):
        """Sauvegarde l'historique et les poids en JSON."""
        data = {
            "preference_weights": self.preference_weights,
            "success_history": self.success_history,
            "feedback": self.feedback,
        }
        try:
            with open(self.history_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[AdaptiveDistiller] Erreur sauvegarde historique: {e}")

    def load_history(self):
        """Charge l'historique et les poids depuis un JSON si disponible."""
        path = Path(self.history_path)
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.preference_weights = data.get("preference_weights", {})
                self.success_history = data.get("success_history", [])
                self.feedback = data.get("feedback", {})
            except Exception as e:
                print(f"[AdaptiveDistiller] Erreur chargement historique: {e}")
