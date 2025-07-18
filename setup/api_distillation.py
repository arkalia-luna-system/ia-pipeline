from fastapi import FastAPI
from pydantic import BaseModel
from athalia_core.athalia_orchestrator import AthaliaOrchestrator

app = FastAPI()
orch = AthaliaOrchestrator()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/distill")
def distill_ia(req: PromptRequest):
    return {"response": orch.distill_ia_responses(req.prompt)}

@app.post("/feedback")
def feedback(req: PromptRequest):
    orch = AthaliaOrchestrator()
    orch.distill_adaptive_responses([req.prompt])  # Simule l'apprentissage
    return {"status": "ok"} 