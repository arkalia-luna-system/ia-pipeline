from abc import ABC, abstractmethod
from typing import List
import requests


class BaseAutocompleteEngine(ABC):
    @abstractmethod
    def suggest(self, prompt: str, max_suggestions: int = 5) -> List[str]:
        """Retourne une liste de suggestions d'autocomplétion pour un prompt donné."""
        pass


class SimpleAutocompleteEngine(BaseAutocompleteEngine):
    def suggest(self, prompt: str, max_suggestions: int = 5) -> List[str]:
        # Logique simple : suggestions contextuelles basées sur le prompt
        base = prompt.strip() or "suggestion"
        return [f"{base}_auto_{i+1}" for i in range(max_suggestions)]


class OllamaAutocompleteEngine(BaseAutocompleteEngine):
    def __init__(self, model_name: str = "mistral:latest",
                 host: str = "http://localhost:11434"):
        self.model_name = model_name
        self.host = host.rstrip("/")

    def suggest(self, prompt: str, max_suggestions: int = 5) -> List[str]:
        url = f"{self.host}/api/generate"
        payload = {
            "model": self.model_name,
            "prompt": f"Complète ce code ou cette phrase : {prompt}",
            "stream": False,
            "options": {"num_predict": max_suggestions}
        }
        try:
            resp = requests.post(url, json=payload, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            # On découpe la réponse en suggestions (simple split pour la V1)
            text = data.get("response", "")
            suggestions = [s.strip() for s in text.split(
                "\n") if s.strip()][:max_suggestions]
            if not suggestions:
                suggestions = [
                    f"{prompt}_ollama_{i+1}" for i in range(max_suggestions)]
            return suggestions
        except Exception as e:
            # Fallback simple en cas d'erreur
            return [
                f"{prompt}_ollama_error_{i+1}" for i in range(max_suggestions)]
