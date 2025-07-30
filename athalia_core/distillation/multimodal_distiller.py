# -*- coding: utf-8 -*-
"""
Distillation multimodale pour Athalia/Arkalia
- Fusionne réponses texte et image (LLaVA)
- Appel réel à LLaVA via RobustAI (Ollama)
"""
import subprocess
from typing import Any, Dict, List, Optional

from athalia_core.ai_robust import AIModel, RobustAI

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


class MultimodalDistiller:
    def distill(
        self,
        text_prompts: List[str],
        image_paths: List[str],
        context: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
          Fusionne les réponses texte et image en utilisant LLaVA (Ollama) et
          d'autres modèles si besoin.
        :param text_prompts: Liste de prompts texte
        :param image_paths: Liste de chemins d'images (un par prompt ou global)
        :param context: Contexte optionnel
        :return: Réponse multimodale fusionnée
        """
        ai = RobustAI()
        text_responses = []
        image_responses = []
        # Appel texte pur (Qwen/Mistral/Mock)
        for prompt in text_prompts:
            res = ai._call_model(AIModel.OLLAMA_QWEN, prompt)
            if res:
                text_responses.append(res)
        # Appel image+texte (LLaVA)
        for prompt, image_path in zip(text_prompts, image_paths):
            llava_response = self.call_llava(prompt, image_path)
            if llava_response:
                image_responses.append(llava_response)
        # Fusion intelligente (texte + image)
        best_text = text_responses[0] if text_responses else ""
        best_image = image_responses[0] if image_responses else ""
        return f"{best_text}\n[Image: {best_image}]"

    def call_llava(self, prompt: str, image_path: str) -> str:
        """
          Appelle LLaVA via Ollama pour une analyse multimodale (texte + image).
        :param prompt: Prompt texte
        :param image_path: Chemin de l'image à analyser
        :return: Réponse de LLaVA (str)
        """
        # Ollama LLaVA supporte --image <path> en CLI
        try:
            result = validate_and_run(
                ["ollama", "run", "llava:latest", "--image", image_path, prompt],
                capture_output=True,
                text=True,
                timeout=60,
            )
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"[LLaVA erreur: {result.stderr}]"
        except Exception as e:
            return f"[LLaVA exception: {e}]"
