#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent unifié pour Athalia - Combine les fonctionnalités de
network_agent et qwen_agent
"""

from athalia_core.ai_robust import query_qwen


class UnifiedAgent:
    """Agent unifié pour toutes les tâches IA"""

    def __init__(self, agent_type="general"):
        self.agent_type = agent_type
        self.name = f"{agent_type}_agent"
        self.description = f"Agent {agent_type} unifié"

    def act(self, prompt, responses=None):
        """Action principale de l'agent"""
        if self.agent_type == "synthesis" and responses:
            return self._synthesize_responses(prompt, responses)
        else:
            return self._process_prompt(prompt)

    def _process_prompt(self, prompt):
        """Traite un prompt avec l'IA"""
        if self.agent_type == "correction":
            return query_qwen(prompt + " (corrige)")
        else:
            return query_qwen(prompt)

    def _synthesize_responses(self, prompt, responses):
        """Synthétise plusieurs réponses"""
        return " | ".join(responses)


# Classes spécialisées pour compatibilité


class AuditAgent(UnifiedAgent):
    """Agent d'audit spécialisé"""

    def __init__(self):
        super().__init__("audit")


class CorrectionAgent(UnifiedAgent):
    """Agent de correction spécialisé"""

    def __init__(self):
        super().__init__("correction")


class SynthesisAgent(UnifiedAgent):
    """Agent de synthèse spécialisé"""

    def __init__(self):
        super().__init__("synthesis")


class QwenAgent(UnifiedAgent):
    """Agent Qwen spécialisé (compatibilité)"""

    def __init__(self):
        super().__init__("qwen")


# Test et démonstration
if __name__ == "__main__":
    # Test des agents unifiés
    audit = AuditAgent()
    correction = CorrectionAgent()
    synth = SynthesisAgent()
    qwen = QwenAgent()

    prompt = "Corrige ce code: def foo(): pass"

    print("=== Test des agents unifiés ===")
    print(f"Audit: {audit.act(prompt)}")
    print(f"Correction: {correction.act(prompt)}")
    print(f"Qwen: {qwen.act(prompt)}")
    print(f"Synthèse: {synth.act(prompt, ['Réponse 1', 'Réponse 2'])}")
