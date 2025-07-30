from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from athalia_core.autocomplete_engine import AutocompleteEngine

app = FastAPI(title="Athalia Autocomplete Server")


class AutocompleteRequest(BaseModel):
    prompt: str
    max_suggestions: int = 5


class AutocompleteResponse(BaseModel):
    suggestions: List[str]


def get_engine():
    return AutocompleteEngine()


@app.post("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(request: AutocompleteRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Le prompt ne peut pas être vide.")
    engine = get_engine()
    # Utiliser get_suggestions_for_context avec un contexte par défaut
    suggestions = engine.get_suggestions_for_context("python", request.prompt)
    # Limiter le nombre de suggestions
    suggestions = suggestions[:request.max_suggestions]
    return AutocompleteResponse(suggestions=suggestions)


# Pour lancer : uvicorn athalia_core.autocomplete_server:app --reload
