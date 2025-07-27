from athalia_core.ai_robust import query_qwen


class AuditAgent:
    """Agent d'audit simplifié pour les tests"""
    
    def __init__(self):
        self.name = "AuditAgent"
    
    def act(self, prompt):
        return query_qwen(prompt)


if __name__ == "__main__":
    agent = AuditAgent()
    print(agent.act("Audit ce code : def foo(): pass"))
