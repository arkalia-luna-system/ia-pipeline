#!/usr/bin/env python3
"""
jeu_ultra_test - Jeu Ultra-Avancé
Jeu de plateforme ultra-avancé avec physique réaliste, IA ennemie et effets visuels
"""

import pygame
import random
import math
import logging
import asyncio
from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum

# Configuration avancée du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("game.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)


# États du jeu
class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


# Classes de jeu avancées
@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag > 0:
            return Vector2D(self.x / mag, self.y / mag)
        return Vector2D(0, 0)


class PhysicsObject:
    def __init__(self, pos: Vector2D, velocity: Vector2D = Vector2D(0, 0)):
        self.position = pos
        self.velocity = velocity
        self.acceleration = Vector2D(0, 0)
        self.mass = 1.0
        self.gravity = Vector2D(0, 0.5)
        self.friction = 0.98

    def update(self):
        # Appliquer la gravité
        self.acceleration += self.gravity

        # Mettre à jour la vélocité
        self.velocity += self.acceleration
        self.velocity.x *= self.friction

        # Mettre à jour la position
        self.position += self.velocity

        # Réinitialiser l'accélération
        self.acceleration = Vector2D(0, 0)


class Player(PhysicsObject):
    def __init__(self, pos: Vector2D):
        super().__init__(pos)
        self.size = 40
        self.color = BLUE
        self.jump_power = -15
        self.speed = 8
        self.on_ground = False
        self.health = 100
        self.max_health = 100
        self.score = 0
        self.invulnerable = False
        self.invulnerable_timer = 0

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False
            logger.info("🦘 Saut du joueur")

    def move(self, direction: int):
        self.velocity.x = direction * self.speed

    def take_damage(self, damage: int):
        if not self.invulnerable:
            self.health -= damage
            self.invulnerable = True
            self.invulnerable_timer = 60  # 1 seconde à 60 FPS
            logger.info(f"💥 Joueur touché! Santé: {self.health}")

    def update(self):
        super().update()

        # Gestion de l'invulnérabilité
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False

        # Limiter la vélocité de chute
        if self.velocity.y > 20:
            self.velocity.y = 20

        # Vérifier les limites de l'écran
        if self.position.x < 0:
            self.position.x = 0
            self.velocity.x = 0
        elif self.position.x > SCREEN_WIDTH - self.size:
            self.position.x = SCREEN_WIDTH - self.size
            self.velocity.x = 0

        if self.position.y > SCREEN_HEIGHT - self.size:
            self.position.y = SCREEN_HEIGHT - self.size
            self.velocity.y = 0
            self.on_ground = True

    def draw(self, screen):
        color = (
            self.color
            if not self.invulnerable
            else (self.color[0] // 2, self.color[1] // 2, self.color[2] // 2)
        )
        pygame.draw.rect(
            screen, color, (self.position.x, self.position.y, self.size, self.size)
        )

        # Barre de santé
        health_width = (self.health / self.max_health) * self.size
        pygame.draw.rect(
            screen, RED, (self.position.x, self.position.y - 10, self.size, 5)
        )
        pygame.draw.rect(
            screen, GREEN, (self.position.x, self.position.y - 10, health_width, 5)
        )


class Enemy(PhysicsObject):
    def __init__(self, pos: Vector2D):
        super().__init__(pos)
        self.size = 30
        self.color = RED
        self.speed = 2
        self.direction = 1
        self.patrol_distance = 100
        self.start_x = pos.x
        self.health = 50

    def update(self, player_pos: Vector2D):
        super().update()

        # IA simple: patrouille et suit le joueur si proche
        distance_to_player = (self.position - player_pos).magnitude()

        if distance_to_player < 150:
            # Suivre le joueur
            direction = (player_pos - self.position).normalize()
            self.velocity.x = direction.x * self.speed * 1.5
        else:
            # Patrouille
            if abs(self.position.x - self.start_x) > self.patrol_distance:
                self.direction *= -1
            self.velocity.x = self.direction * self.speed

        # Limiter la vélocité de chute
        if self.velocity.y > 15:
            self.velocity.y = 15

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, (self.position.x, self.position.y, self.size, self.size)
        )


class Platform:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Tuple[int, int, int] = GREEN,
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.moving = False
        self.move_speed = 1
        self.start_x = x
        self.move_distance = 50

    def update(self):
        if self.moving:
            self.rect.x += self.move_speed
            if abs(self.rect.x - self.start_x) > self.move_distance:
                self.move_speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Particle:
    def __init__(
        self,
        pos: Vector2D,
        velocity: Vector2D,
        color: Tuple[int, int, int],
        lifetime: int = 30,
    ):
        self.position = pos
        self.velocity = velocity
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.size = random.randint(2, 6)

    def update(self):
        self.position += self.velocity
        self.velocity.x *= 0.95
        self.velocity.y *= 0.95
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            pygame.draw.circle(
                screen,
                self.color,
                (int(self.position.x), int(self.position.y)),
                self.size,
            )


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("jeu_ultra_test - Jeu Ultra-Avancé")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU

        # Objets du jeu
        self.player = Player(Vector2D(100, 100))
        self.enemies: List[Enemy] = []
        self.platforms: List[Platform] = []
        self.particles: List[Particle] = []

        # UI
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Statistiques
        self.score = 0
        self.level = 1
        self.enemies_killed = 0

        # Initialiser le niveau
        self.init_level()

        logger.info("🎮 Jeu initialisé avec succès")

    def init_level(self):
        # Créer les plateformes
        self.platforms = [
            Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),  # Sol
            Platform(200, 600, 200, 20),
            Platform(500, 500, 200, 20),
            Platform(800, 400, 200, 20),
            Platform(300, 300, 200, 20),
            Platform(600, 200, 200, 20),
        ]

        # Créer les ennemis
        self.enemies = [
            Enemy(Vector2D(300, 550)),
            Enemy(Vector2D(600, 450)),
            Enemy(Vector2D(900, 350)),
        ]

        # Réinitialiser le joueur
        self.player.position = Vector2D(100, 100)
        self.player.health = self.player.max_health

        logger.info(f"🎯 Niveau {self.level} initialisé")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.PLAYING
                elif event.key == pygame.K_SPACE:
                    if self.state == GameState.MENU:
                        self.state = GameState.PLAYING
                    elif self.state == GameState.GAME_OVER:
                        self.restart_game()
                    elif self.state == GameState.PLAYING:
                        self.player.jump()
                elif event.key == pygame.K_r:
                    if self.state == GameState.GAME_OVER:
                        self.restart_game()

    def update(self):
        if self.state != GameState.PLAYING:
            return

        # Mettre à jour le joueur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-1)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(1)
        else:
            self.player.velocity.x *= 0.8

        self.player.update()

        # Mettre à jour les ennemis
        for enemy in self.enemies:
            enemy.update(self.player.position)

        # Mettre à jour les plateformes
        for platform in self.platforms:
            platform.update()

        # Mettre à jour les particules
        self.particles = [p for p in self.particles if p.lifetime > 0]
        for particle in self.particles:
            particle.update()

        # Collision joueur-plateformes
        self.check_platform_collisions()

        # Collision joueur-ennemis
        self.check_enemy_collisions()

        # Vérifier la victoire
        if len(self.enemies) == 0:
            self.next_level()

        # Vérifier la défaite
        if self.player.health <= 0:
            self.state = GameState.GAME_OVER

    def check_platform_collisions(self):
        player_rect = pygame.Rect(
            self.player.position.x,
            self.player.position.y,
            self.player.size,
            self.player.size,
        )

        for platform in self.platforms:
            if player_rect.colliderect(platform.rect):
                # Collision par le haut de la plateforme
                if (
                    self.player.velocity.y > 0
                    and player_rect.bottom > platform.rect.top
                    and player_rect.top < platform.rect.top
                ):
                    self.player.position.y = platform.rect.top - self.player.size
                    self.player.velocity.y = 0
                    self.player.on_ground = True

    def check_enemy_collisions(self):
        player_rect = pygame.Rect(
            self.player.position.x,
            self.player.position.y,
            self.player.size,
            self.player.size,
        )

        for enemy in self.enemies[:]:
            enemy_rect = pygame.Rect(
                enemy.position.x, enemy.position.y, enemy.size, enemy.size
            )

            if player_rect.colliderect(enemy_rect):
                # Le joueur saute sur l'ennemi
                if (
                    self.player.velocity.y > 0
                    and player_rect.bottom < enemy_rect.centery
                ):
                    self.enemies.remove(enemy)
                    self.player.velocity.y = -10  # Rebond
                    self.score += 100
                    self.enemies_killed += 1

                    # Effet de particules
                    for _ in range(10):
                        particle = Particle(
                            Vector2D(
                                enemy.position.x + enemy.size / 2,
                                enemy.position.y + enemy.size / 2,
                            ),
                            Vector2D(random.uniform(-3, 3), random.uniform(-3, 3)),
                            YELLOW,
                        )
                        self.particles.append(particle)

                    logger.info(f"💀 Ennemi éliminé! Score: {self.score}")
                else:
                    # Le joueur est touché
                    self.player.take_damage(20)

    def next_level(self):
        self.level += 1
        self.score += 500
        self.init_level()
        logger.info(f"🎉 Niveau {self.level} atteint!")

    def restart_game(self):
        self.score = 0
        self.level = 1
        self.enemies_killed = 0
        self.state = GameState.PLAYING
        self.init_level()
        logger.info("🔄 Partie redémarrée")

    def draw(self):
        self.screen.fill(BLACK)

        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_pause_overlay()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()

        pygame.display.flip()

    def draw_menu(self):
        title = self.font.render("jeu_ultra_test - Jeu Ultra-Avancé", True, WHITE)
        subtitle = self.small_font.render(
            "Appuyez sur ESPACE pour commencer", True, WHITE
        )
        controls = self.small_font.render(
            "Contrôles: A/D ou ←/→ pour bouger, ESPACE pour sauter", True, WHITE
        )

        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        self.screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 300))
        self.screen.blit(controls, (SCREEN_WIDTH // 2 - controls.get_width() // 2, 400))

    def draw_game(self):
        # Dessiner les plateformes
        for platform in self.platforms:
            platform.draw(self.screen)

        # Dessiner les ennemis
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Dessiner les particules
        for particle in self.particles:
            particle.draw(self.screen)

        # Dessiner le joueur
        self.player.draw(self.screen)

        # UI
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.small_font.render(f"Niveau: {self.level}", True, WHITE)
        health_text = self.small_font.render(
            f"Santé: {self.player.health}", True, WHITE
        )
        enemies_text = self.small_font.render(
            f"Ennemis: {len(self.enemies)}", True, WHITE
        )

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 30))
        self.screen.blit(health_text, (10, 50))
        self.screen.blit(enemies_text, (10, 70))

    def draw_pause_overlay(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        pause_text = self.font.render("PAUSE", True, WHITE)
        self.screen.blit(
            pause_text,
            (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2),
        )

    def draw_game_over(self):
        game_over_text = self.font.render("GAME OVER", True, RED)
        score_text = self.small_font.render(f"Score final: {self.score}", True, WHITE)
        restart_text = self.small_font.render(
            "Appuyez sur R pour recommencer", True, WHITE
        )

        self.screen.blit(
            game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 300)
        )
        self.screen.blit(
            score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 350)
        )
        self.screen.blit(
            restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 400)
        )

    def run(self):
        logger.info("🎮 Démarrage du jeu")
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        logger.info("🎮 Jeu terminé")


async def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    asyncio.run(main())
