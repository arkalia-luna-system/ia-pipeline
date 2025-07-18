# -*- coding: utf-8 -*-
"""
Agent AutoGen pour Qwen 7B (prototype)
"""
try:
    import autogen
except ImportError:
    autogen = None
from athalia_core.ai_robust import query_qwen

class QwenAgent:
    def act(self, prompt):
        return query_qwen(prompt)

# Test simple
if __name__ == "__main__":
    agent = QwenAgent()
    print(agent.act("Explique la distillation IA.")) 