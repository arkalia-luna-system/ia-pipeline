import pygame
import random
from typing import Tuple

"""
Module de visualisation pour projet artistique.
Gère les effets visuels et particules.
"""


class ParticleSystem:
    """Système de particules pour effets visuels."""

    def __init__(self):
        self.particles = []

    def add_particle(self, x: int, y: int, color: Tuple[int, int, int]):
        """Ajoute une particule à la position donnée."""
        particle = {
            "x": x,
            "y": y,
            "vx": random.uniform(-2, 2),
            "vy": random.uniform(-3, -1),
            "life": 60,
            "color": color,
            "size": random.randint(2, 5),
        }
        self.particles.append(particle)

    def update(self):
        """Met à jour toutes les particules."""
        for particle in self.particles[:]:
            particle["x"] += particle["vx"]
            particle["y"] += particle["vy"]
            particle["life"] -= 1

            if particle["life"] <= 0:
                self.particles.remove(particle)

    def draw(self, screen: pygame.Surface):
        """Dessine toutes les particules."""
        for particle in self.particles:
            alpha = particle["life"] / 60.0
            color = tuple(int(c * alpha) for c in particle["color"])
            pygame.draw.circle(
                screen,
                color,
                (int(particle["x"]), int(particle["y"])),
                particle["size"],
            )


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
        """Met à jour les effets visuels."""
        self.particle_system.update()

    def draw(self, screen: pygame.Surface):
        """Dessine les effets visuels."""
        self.particle_system.draw(screen)


def main():
    """Test du module de visualisation."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    effects = VisualEffects()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                effects.add_sparkle_effect(event.pos[0], event.pos[1])

        screen.fill((0, 0, 0))
        effects.update()
        effects.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
