import os
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from athalia_core.autocomplete_engine import (
    OllamaAutocompleteEngine,
    SimpleAutocompleteEngine,
)

app = FastAPI(title="Athalia Autocomplete Server")


class AutocompleteRequest(BaseModel):
    prompt: str
    max_suggestions: int = 5


class AutocompleteResponse(BaseModel):
    suggestions: List[str]


def get_engine():
    engine_type = os.environ.get("ATH_AUTOCOMPLETE_ENGINE", "simple").lower()
    if engine_type == "ollama":
        return OllamaAutocompleteEngine()
    return SimpleAutocompleteEngine()


@app.post("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(request: AutocompleteRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Le prompt ne peut pas être vide.")
    engine = get_engine()
    suggestions = engine.suggest(request.prompt, request.max_suggestions)
    return AutocompleteResponse(suggestions=suggestions)


# Pour lancer : uvicorn athalia_core.autocomplete_server:app --reload
