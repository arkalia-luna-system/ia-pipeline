#!/usr/bin/env python3
"""
Module de distillation multimodale pour Athalia
Fusion de réponses texte et image via LLaVA et autres modèles
"""

import logging
from typing import Any

# Import des modules nécessaires
try:
    from ..ai.ai_robust import AIModel, RobustAI
except ImportError:
    # Fallback pour les tests
    class AIModel:
        OLLAMA_QWEN = "ollama_qwen"

    class RobustAI:
        def _call_model(self, model, prompt):
            return f"[Modèle {model} non disponible]"


# Import sécurisé pour subprocess
try:
    from ..utilities.secure_subprocess import secure_subprocess_run as validateand_run
    from ..validation.security_validator import SecurityError
except ImportError:
    # Fallback sécurisé
    def validateand_run(command, **kwargs):
        import subprocess

        safe_kwargs = {"shell": False, "check": False}
        safe_kwargs.update(kwargs)
        return subprocess.run(command, **safe_kwargs)

    class SecurityError(Exception):
        """Classe de fallback pour SecurityError"""

        pass


class MultimodalDistiller:
    def distill(
        self,
        text_prompts: list[str],
        image_paths: list[str],
        context: dict[str, Any] | None = None,
    ) -> str:
        """Fusionne les réponses texte et image en utilisant LLaVA (Ollama) et
        d'autres modèles si besoin.

        Args:
            text_prompts: Liste de prompts texte
            image_paths: Liste de chemins d'images (un par prompt ou global)
            context: Contexte optionnel

        Returns:
            Réponse multimodale fusionnée
        """
        ai = RobustAI()
        text_responses = []
        image_responses = []
        # Appel texte pur (Qwen/Mistral/Mock)
        for prompt in text_prompts:
            try:
                # Utiliser la méthode privée avec fallback
                if hasattr(ai, "_call_model"):
                    res = ai._call_model(AIModel.OLLAMA_QWEN, prompt)
                else:
                    # Fallback si la méthode n'existe pas
                    res = f"[Modèle {AIModel.OLLAMA_QWEN.value} non disponible]"

                if res:
                    text_responses.append(res)
            except Exception as e:
                # Fallback en cas d'erreur
                text_responses.append(f"[Erreur modèle: {e}]")
        # Appel image+texte (LLaVA)
        if len(image_paths) != len(text_prompts):
            # Si pas assez d'images, utiliser la première pour tous les prompts
            if image_paths:
                default_image = image_paths[0]
                for prompt in text_prompts:
                    llava_response = self.call_llava(prompt, default_image)
                    if llava_response:
                        image_responses.append(llava_response)
            else:
                # Pas d'images disponibles
                image_responses = ["[Aucune image disponible]"] * len(text_prompts)
        else:
            # Correspondance 1:1 entre prompts et images
            for prompt, image_path in zip(text_prompts, image_paths, strict=True):
                llava_response = self.call_llava(prompt, image_path)
                if llava_response:
                    image_responses.append(llava_response)
        # Fusion intelligente (texte + image)
        best_text = text_responses[0] if text_responses else "[Aucune réponse texte]"
        best_image = image_responses[0] if image_responses else "[Aucune réponse image]"

        # Construire la réponse fusionnée
        if best_text and best_image and best_text != "[Aucune réponse texte]":
            return f"{best_text}\n[Image: {best_image}]"
        elif best_text and best_text != "[Aucune réponse texte]":
            return best_text
        elif best_image and best_image != "[Aucune réponse image]":
            return f"[Image: {best_image}]"
        else:
            return "[Aucune réponse disponible]"

    def call_llava(self, prompt: str, image_path: str) -> str:
        """Appelle LLaVA via Ollama pour une analyse multimodale (texte + image).

        Args:
            prompt: Prompt texte
            image_path: Chemin de l'image à analyser

        Returns:
            Réponse de LLaVA (str)
        """
        # Ollama LLaVA supporte --image <path> en CLI
        try:
            result = validateand_run(
                [
                    "ollama",
                    "run",
                    "llava:latest",
                    "--image",
                    image_path,
                    prompt,
                ],
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
