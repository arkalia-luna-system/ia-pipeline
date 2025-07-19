from athalia_core.ai_robust import query_qwen

class AuditAgent:
    name = "audit_agent"
    description = "Agent d'audit AutoGen"
    def act(self, prompt):
        return query_qwen(prompt)

class CorrectionAgent:
    name = "correction_agent"
    description = "Agent de correction AutoGen"
    def act(self, prompt):
        return query_qwen(prompt + " (corrige)")

class SynthesisAgent:
    name = "synthesis_agent"
    description = "Agent de synthèse AutoGen"
    def act(self, prompt, responses):
        return " | ".join(responses)

if __name__ == "__main__":
    audit = AuditAgent()
    correction = CorrectionAgent()
    synth = SynthesisAgent()
    prompt = "Corrige ce code : def foo(): pass"
    r1 = audit.act(prompt)
    r2 = correction.act(prompt)
    print(synth.act(prompt, [r1, r2])) 