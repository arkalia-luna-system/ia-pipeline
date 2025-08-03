import pygame
import math

"""
Module d'animation pour projet artistique.
Gère les animations et les mouvements.
"""


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
        for index in range(self.petal_count):
            angle = (2 * math.pi * index) / self.petal_count
            wave_offset = math.sin(self.time + index * 0.5) * 20

            # Position du pétale avec mouvement de danse
            petal_x = self.center[0] + math.cos(angle) * (
                self.petal_length + wave_offset
            )
            petal_y = self.center[1] + math.sin(angle) * (
                self.petal_length + wave_offset
            )

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
