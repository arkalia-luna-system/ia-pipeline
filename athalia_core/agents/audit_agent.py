import logging
from typing import Any

import requests


class AuditAgent:
    """Agent d'audit intelligent"""

    def __init__(self) -> None:
        self.audit_results: list[Any] = []

    def act(self, prompt: str) -> str:
        """Exécute un audit basé sur le prompt"""
        return f"Audit exécuté: {prompt}"


def query_qwen(prompt: str) -> str:
    """Appel local à Qwen 7B via Ollama."""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "qwen:7b", "prompt": prompt, "stream": False},
            timeout=30,
        )
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            logging.error(f"Erreur Qwen: {response.status_code}")
            return ""
    except Exception as e:
        logging.error(f"Erreur Qwen: {e}")
        return ""


if __name__ == "__main__":
    agent = AuditAgent()
    print(agent.act("Audit ce code: def foo(): pass"))
