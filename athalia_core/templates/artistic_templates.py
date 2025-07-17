"""
Templates de code pour projets artistiques.
Spécialement conçu pour "fleure qui danse" et projets similaires.
"""

from typing import Dict, Any

def get_artistic_templates() -> Dict[str, str]:
    """Retourne les templates de code pour projets artistiques."""
    
    return {
        "animation/main.py": '''"""
Module d'animation pour projet artistique.
Gère les animations et les mouvements.
"""

import pygame
import math
import time
from typing import Tuple, List

class FlowerAnimation:
    """Animation d'une fleure qui danse."""
    
    def __init__(self, screen_size: Tuple[int, int] = (800, 600)):
        self.screen_size = screen_size
        self.center = (screen_size[0] // 2, screen_size[1] // 2)
        self.petal_count = 8
        self.petal_length = 100
        self.animation_speed = 0.02
        self.time = 0
        
    def draw_flower(self, screen: pygame.Surface):
        """Dessine la fleure avec animation de danse."""
        # Couleur de base
        flower_color = (255, 182, 193)  # Rose clair
        
        # Animation des pétales
        for i in range(self.petal_count):
            angle = (2 * math.pi * i) / self.petal_count
            wave_offset = math.sin(self.time + i * 0.5) * 20
            
            # Position du pétale avec mouvement de danse
            petal_x = self.center[0] + math.cos(angle) * (self.petal_length + wave_offset)
            petal_y = self.center[1] + math.sin(angle) * (self.petal_length + wave_offset)
            
            # Dessiner le pétale
            pygame.draw.circle(screen, flower_color, (int(petal_x), int(petal_y)), 15)
        
        # Centre de la fleure
        pygame.draw.circle(screen, (255, 215, 0), self.center, 25)
        
        # Tige
        stem_start = (self.center[0], self.center[1] + 30)
        stem_end = (self.center[0], self.screen_size[1] - 50)
        pygame.draw.line(screen, (34, 139, 34), stem_start, stem_end, 5)
        
    def update(self):
        """Met à jour l'animation."""
        self.time += self.animation_speed
        
    def set_music_beat(self, beat_intensity: float):
        """Synchronise l'animation avec la musique."""
        self.animation_speed = 0.02 + beat_intensity * 0.01

def main():
    """Fonction principale pour tester l'animation."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fleure qui danse")
    clock = pygame.time.Clock()
    
    flower = FlowerAnimation()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((135, 206, 235))  # Ciel bleu
        flower.update()
        flower.draw_flower(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
''',

        "audio/main.py": '''"""
Module audio pour projet artistique.
Gère la musique et la synchronisation.
"""

import pygame
import numpy as np
from typing import Optional, Callable

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
            print(f"Erreur chargement musique: {e}")
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
    print("Module audio artistique initialisé")
    print("Fonctionnalités: chargement musique, synchronisation rythme")

if __name__ == "__main__":
    main()
''',

        "visualization/main.py": '''"""
Module de visualisation pour projet artistique.
Gère les effets visuels et particules.
"""

import pygame
import random
import math
from typing import List, Tuple

class ParticleSystem:
    """Système de particules pour effets visuels."""
    
    def __init__(self):
        self.particles = []
        
    def add_particle(self, x: int, y: int, color: Tuple[int, int, int]):
        """Ajoute une particule à la position donnée."""
        particle = {
            'x': x,
            'y': y,
            'vx': random.uniform(-2, 2),
            'vy': random.uniform(-3, -1),
            'life': 60,
            'color': color,
            'size': random.randint(2, 5)
        }
        self.particles.append(particle)
    
    def update(self):
        """Met à jour toutes les particules."""
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen: pygame.Surface):
        """Dessine toutes les particules."""
        for particle in self.particles:
            alpha = particle['life'] / 60.0
            color = tuple(int(c * alpha) for c in particle['color'])
            pygame.draw.circle(screen, color, 
                             (int(particle['x']), int(particle['y'])), 
                             particle['size'])

class VisualEffects:
    """Gestionnaire d'effets visuels."""
    
    def __init__(self):
        self.particle_system = ParticleSystem()
        self.rainbow_mode = False
        
    def add_sparkle_effect(self, x: int, y: int):
        """Ajoute un effet de scintillement."""
        colors = [(255, 255, 0), (255, 0, 255), (0, 255, 255)]
        for _ in range(5):
            color = random.choice(colors)
            self.particle_system.add_particle(x, y, color)
    
    def update(self):
        """Met à jour tous les effets."""
        self.particle_system.update()
    
    def draw(self, screen: pygame.Surface):
        """Dessine tous les effets."""
        self.particle_system.draw(screen)

def main():
    """Test du module de visualisation."""
    effects = VisualEffects()
    print("Module de visualisation artistique initialisé")
    print("Fonctionnalités: particules, effets visuels, scintillement")

if __name__ == "__main__":
    main()
''',

        "interaction/main.py": '''"""
Module d'interaction pour projet artistique.
Gère les interactions utilisateur.
"""

import pygame
from typing import Dict, Any

class InteractionManager:
    """Gestionnaire d'interactions pour projet artistique."""
    
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.click_handlers = {}
        self.key_handlers = {}
        
    def handle_mouse_click(self, pos: tuple, button: int):
        """Gère les clics de souris."""
        self.mouse_pos = pos
        for handler in self.click_handlers.values():
            handler(pos, button)
    
    def handle_key_press(self, key: int):
        """Gère les touches pressées."""
        if key in self.key_handlers:
            self.key_handlers[key]()
    
    def add_click_handler(self, name: str, handler):
        """Ajoute un gestionnaire de clic."""
        self.click_handlers[name] = handler
    
    def add_key_handler(self, key: int, handler):
        """Ajoute un gestionnaire de touche."""
        self.key_handlers[key] = handler
    
    def get_mouse_pos(self) -> tuple:
        """Retourne la position de la souris."""
        return self.mouse_pos

def main():
    """Test du module d'interaction."""
    interaction = InteractionManager()
    print("Module d'interaction artistique initialisé")
    print("Fonctionnalités: gestion clics, touches, position souris")

if __name__ == "__main__":
    main()
'''

    } 