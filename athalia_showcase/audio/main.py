import numpy as np

import pygame
import logging
from typing import Callable

"""
Module audio pour projet artistique.
Gère la musique et la synchronisation.
"""


logger = logging.getLogger(__name__)


class AudioManager:
    """Gestionnaire audio pour la fleure qui danse."""

    def __init__(self):
        pygame.mixer.init()
        self.current_music = None
        self.beat_callback = None
        self.volume = 0.7

    def load_music(self, file_path: str):
        """Charge une musique de fond."""
        try:
            pygame.mixer.music.load(file_path)
            self.current_music = file_path
            return True
        except Exception as e:
            logger.info(f"Erreur chargement musique: {e}")
            return False

    def play_music(self, loop: bool = True):
        """Joue la musique avec détection de rythme."""
        if self.current_music:
            pygame.mixer.music.play(-1 if loop else 0)
            pygame.mixer.music.set_volume(self.volume)

    def set_beat_callback(self, callback: Callable[[float], None]):
        """Définit le callback pour la synchronisation rythmique."""
        self.beat_callback = callback

    def update_beat(self):
        """Met à jour la détection de rythme."""
        if self.beat_callback:
            # Simulation de détection de rythme
            beat_intensity = np.random.uniform(0.1, 0.9)
            self.beat_callback(beat_intensity)

    def stop_music(self):
        """Arrête la musique."""
        pygame.mixer.music.stop()

    def set_volume(self, volume: float):
        """Ajuste le volume (0.0 à 1.0)."""
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)


def main():
    """Test du module audio."""
    audio = AudioManager()
    logger.info("Module audio artistique initialisé")
    logger.info("Fonctionnalités: chargement musique, synchronisation rythmique")


if __name__ == "__main__":
    main()
