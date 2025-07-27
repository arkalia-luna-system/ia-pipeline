import autogen
from athalia_core.ai_robust import query_qwen


class AuditAgent(autogen.Agent):
    def act(self, prompt):
        return query_qwen(prompt)


if __name__ == "__main__":
    agent = AuditAgent()
    print(agent.act("Audit ce code : def foo(): pass"))
