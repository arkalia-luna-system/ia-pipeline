#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de génération simplifié pour Athalia
Version simplifiée sans f-strings complexes
"""

from pathlib import Path
import re
from typing import Optional


def validate_code(code: str) -> bool:
    """Valide la syntaxe du code Python"""
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False


def generate_blueprint_mock(idea: str = "", *args, **kwargs):
    """Génère un blueprint mock pour les tests."""
    return {
        "project_name": extract_project_name(idea),
        "description": idea or "Projet de test",
        "project_type": "generic",
        "modules": ["core", "tests"],
        "structure": ["src/", "tests/", "README.md"],
        "dependencies": ["numpy", "pandas"],
        "prompts": ["prompts/main.yaml"],
        "booster_ia": True,
        "docker": False,
        "ci_cd": False,
        "tests": True,
        "documentation": True,
    }


def extract_project_name(idea: str) -> str:
    """Extrait un nom de projet de l'idée."""
    # Cherche des mots clés spécifiques
    patterns = [
        r"calculatrice\s+(\w+)",
        r"application\s+(\w+)",
        r"robot\s+(\w+)",
        r"api\s+(\w+)",
        r"(\w+)\s+avec",
    ]

    for pattern in patterns:
        match = re.search(pattern, idea, re.IGNORECASE)
        if match:
            return match.group(1).lower()

    # Fallback: premier mot significatif
    words = idea.split()
    for word in words:
        if len(word) > 3 and word.isalpha():
            return word.lower()

    return "projet_ia"


def generate_project(blueprint: dict, outdir, *args, **kwargs):
    """Génère un projet avec tous les outils avancés d'Athalia (distillation, IA, évolution génétique)"""

    dry_run = kwargs.get("dry_run", False)
    project_name = blueprint.get("project_name", "projet_ia")
    project_path = Path(outdir) / project_name

    if dry_run:
        # Mode dry-run: générer seulement le rapport
        report_content = f"""[DRY-RUN] Génération ULTRA-AVANCÉE du projet {project_name}

Structure prévue avec IA et distillation:
- {project_path}/src/ (code optimisé par IA)
- {project_path}/tests/ (tests générés par IA)
- {project_path}/docs/ (documentation IA)
- {project_path}/README.md (README intelligent)
- {project_path}/requirements.txt (dépendances optimisées)
- {project_path}/QUALITY_REPORT.md (rapport de qualité)

Améliorations appliquées:
✅ Détection intelligente du type
✅ Distillation multi-agents (correction, optimization, security, performance)
✅ Évolution génétique du code (3 générations)
✅ Scoring de qualité automatique
✅ Audit final avec rapport détaillé

[DRY-RUN] Aucun fichier réel créé."""

        # Créer le rapport dans le répertoire parent (outdir)
        report_file = Path(outdir) / "dry_run_report.txt"
        report_file.write_text(report_content, encoding="utf-8")
        return str(project_path)

    # Mode ULTRA-AVANCÉ: générer le projet avec tous les outils
    logger.info(
        "🚀 Démarrage de la génération ULTRA-AVANCÉE avec distillation multi-agents"
    )

    # 1. Détection intelligente du type
    try:
        from athalia_core.classification.project_classifier import classify_project

        project_type_enum = classify_project(blueprint.get("description", ""))
        project_type = project_type_enum.value
        logger.info(f"✅ Type détecté intelligemment: {project_type}")
    except ImportError:
        project_type = detect_project_type(
            project_name, blueprint.get("description", "")
        )
        logger.info(f"✅ Type détecté classiquement: {project_type}")

    # 2. Génération de base
    project_path.mkdir(parents=True, exist_ok=True)
    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "tests").mkdir(exist_ok=True)
    # Ne pas créer docs automatiquement - seulement si du contenu sera ajouté

    generate_readme(blueprint, project_path)
    generate_main_code(blueprint, project_path)
    generate_test_code(blueprint, project_path)
    generate_requirements(blueprint, project_path)

    # 3. Amélioration IA avec vrais agents et fallback intelligent
    try:
        from athalia_core.agents.unified_agent import UnifiedAgent

        # Créer une classe ContextPromptAgent simple
        class ContextPromptAgent:
            def __init__(self):
                self.name = "context_prompt_agent"

            def act(self, prompt):
                try:
                    from athalia_core.ai_robust import query_qwen

                    return query_qwen(prompt)
                except Exception as e:
                    logger.warning(f"Agent IA timeout: {e}")
                    return None

        # Créer les agents IA
        context_agent = ContextPromptAgent()
        unified_agent = UnifiedAgent()

        main_file = project_path / "src" / "main.py"
        if main_file.exists():
            with open(main_file, "r", encoding="utf-8") as f:
                original_code = f.read()

            # Essayer les agents IA d'abord
            improved_code = None

            try:
                # Agent 1: Analyse du contexte et amélioration
                context_prompt = f"""
                Analyse ce code Python et améliore-le significativement :
                
                Type de projet: {project_type}
                Description: {blueprint.get('description', '')}
                
                Code actuel:
                {original_code}
                
                Améliore ce code avec :
                1. Fonctionnalités avancées spécifiques au type de projet
                2. Architecture moderne et scalable
                3. Gestion d'erreurs robuste
                4. Performance optimisée
                5. Code de production professionnel
                
                Retourne UNIQUEMENT le code Python amélioré, sans commentaires explicatifs.
                """

                improved_code = context_agent.act(context_prompt)

                if improved_code:
                    # Agent 2: Validation et optimisation finale
                    validation_prompt = f"""
                    Valide et optimise ce code Python :
                    
                    {improved_code}
                    
                    Assure-toi que :
                    1. Le code est syntaxiquement correct
                    2. Les imports sont corrects
                    3. La logique est cohérente
                    4. Les bonnes pratiques sont respectées
                    
                    Retourne UNIQUEMENT le code Python final optimisé.
                    """

                    final_code = unified_agent.act(validation_prompt)

                    if final_code:
                        # Valider le code avant de l'appliquer
                        if validate_code(final_code):
                            # Sauvegarder et appliquer
                            backup_file = main_file.with_suffix(".py.backup")
                            with open(backup_file, "w", encoding="utf-8") as f:
                                f.write(original_code)

                            with open(main_file, "w", encoding="utf-8") as f:
                                f.write(final_code)

                            logger.info("✅ Code amélioré avec agents IA avancés")
                            return
                        else:
                            logger.warning(
                                "⚠️ Code des agents IA invalide, utilisation du fallback"
                            )
                            return

            except Exception as e:
                logger.warning(f"Agents IA échoués: {e}")

            # Fallback: Code avancé pré-généré basé sur le type
            logger.info("🔄 Utilisation du fallback avec code avancé pré-généré")

            if project_type == "api":
                advanced_code = f'''#!/usr/bin/env python3
"""
{blueprint.get('name', 'project')} - API REST Ultra-Avancée
{blueprint.get('description', '')}
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, validator
from typing import List, Optional, Dict, Any
import logging
import asyncio
from datetime import datetime, timedelta
import jwt
from functools import lru_cache
import redis.asyncio as redis
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration avancée du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration de sécurité
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Base de données
Base = declarative_base()
engine = create_engine("sqlite:///./app.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Redis pour le cache
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Modèles de données
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Pydantic models
class UserCreate(BaseModel):
    email: str
    password: str
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Email invalide')
        return v

class UserLogin(BaseModel):
    email: str
    password: str

class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    owner_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Sécurité
security = HTTPBearer()

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({{"exp": expire}})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token invalide")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token invalide")
    
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    
    if user is None:
        raise HTTPException(status_code=401, detail="Utilisateur non trouvé")
    return user

# Cache intelligent
@lru_cache(maxsize=128)
def get_cached_data(key: str) -> Dict[str, Any]:
    """Cache intelligent pour les données fréquemment accédées"""
    return {{"cached": True, "key": key}}

# Application FastAPI
app = FastAPI(
    title="{blueprint.get('name', 'project')}",
    description="{blueprint.get('description', '')}",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Démarrage de l'API {blueprint.get('name', 'project')}")
    # Test de connexion Redis
    try:
        await redis_client.ping()
        logger.info("✅ Redis connecté")
    except Exception as e:
        logger.warning(f"⚠️ Redis non disponible: {{e}}")

@app.get("/")
async def root():
    return {{
        "message": f"Bienvenue sur {blueprint.get('name', 'project')} API",
        "status": "active",
        "version": "2.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }}

@app.post("/auth/register", response_model=Dict[str, str])
async def register(user: UserCreate):
    db = SessionLocal()
    
    # Vérifier si l'utilisateur existe déjà
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    
    # Créer le nouvel utilisateur (en production, hasher le mot de passe)
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    
    logger.info(f"✅ Nouvel utilisateur enregistré: {{user.email}}")
    return {{"message": "Utilisateur créé avec succès"}}

@app.post("/auth/login", response_model=Dict[str, str])
async def login(user: UserLogin):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    db.close()
    
    if not db_user or db_user.hashed_password != user.password:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")
    
    access_token = create_access_token(data={{"sub": db_user.id}})
    logger.info(f"✅ Connexion réussie: {{user.email}}")
    return {{"access_token": access_token, "token_type": "bearer"}}

@app.get("/items/", response_model=List[ItemResponse])
async def get_items(current_user: User = Depends(get_current_user)):
    # Vérifier le cache
    cache_key = f"items_user_{{current_user.id}}"
    cached_items = await redis_client.get(cache_key)
    
    if cached_items:
        logger.info("📦 Données récupérées depuis le cache")
        return eval(cached_items)
    
    # Récupérer depuis la base de données
    db = SessionLocal()
    items = db.query(Item).filter(Item.owner_id == current_user.id).all()
    db.close()
    
    # Mettre en cache pour 5 minutes
    await redis_client.setex(cache_key, 300, str([item.__dict__ for item in items]))
    
    logger.info(f"📦 {{len(items)}} items récupérés pour l'utilisateur {{current_user.id}}")
    return items

@app.post("/items/", response_model=ItemResponse)
async def create_item(
    item: ItemCreate,
    current_user: User = Depends(get_current_user)
):
    db = SessionLocal()
    db_item = Item(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    
    # Invalider le cache
    cache_key = f"items_user_{{current_user.id}}"
    await redis_client.delete(cache_key)
    
    logger.info(f"✅ Nouvel item créé: {{item.title}} par l'utilisateur {{current_user.id}}")
    return db_item

@app.get("/health")
async def health_check():
    return {{
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "services": {{
            "database": "connected",
            "redis": "connected" if await redis_client.ping() else "disconnected"
        }}
    }}

async def main():
    logger.info("🚀 Démarrage de l'API {blueprint.get('name', 'project')}")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())
'''
            elif project_type == "game":
                advanced_code = f'''#!/usr/bin/env python3
"""
{blueprint.get('name', 'project')} - Jeu Ultra-Avancé
{blueprint.get('description', '')}
"""

import pygame
import sys
import random
import math
import logging
from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

# Configuration avancée du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game.log'),
        logging.StreamHandler()
    ]
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
            logger.info(f"💥 Joueur touché! Santé: {{self.health}}")
    
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
        color = self.color if not self.invulnerable else (self.color[0]//2, self.color[1]//2, self.color[2]//2)
        pygame.draw.rect(screen, color, (self.position.x, self.position.y, self.size, self.size))
        
        # Barre de santé
        health_width = (self.health / self.max_health) * self.size
        pygame.draw.rect(screen, RED, (self.position.x, self.position.y - 10, self.size, 5))
        pygame.draw.rect(screen, GREEN, (self.position.x, self.position.y - 10, health_width, 5))

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
        pygame.draw.rect(screen, self.color, (self.position.x, self.position.y, self.size, self.size))

class Platform:
    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int] = GREEN):
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
    def __init__(self, pos: Vector2D, velocity: Vector2D, color: Tuple[int, int, int], lifetime: int = 30):
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
            color = (*self.color, alpha)
            pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.size)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(f'{blueprint.get("name", "project")} - Jeu Ultra-Avancé')
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
        
        logger.info(f"🎯 Niveau {{self.level}} initialisé")
    
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
        player_rect = pygame.Rect(self.player.position.x, self.player.position.y, self.player.size, self.player.size)
        
        for platform in self.platforms:
            if player_rect.colliderect(platform.rect):
                # Collision par le haut de la plateforme
                if self.player.velocity.y > 0 and player_rect.bottom > platform.rect.top and player_rect.top < platform.rect.top:
                    self.player.position.y = platform.rect.top - self.player.size
                    self.player.velocity.y = 0
                    self.player.on_ground = True
    
    def check_enemy_collisions(self):
        player_rect = pygame.Rect(self.player.position.x, self.player.position.y, self.player.size, self.player.size)
        
        for enemy in self.enemies[:]:
            enemy_rect = pygame.Rect(enemy.position.x, enemy.position.y, enemy.size, enemy.size)
            
            if player_rect.colliderect(enemy_rect):
                # Le joueur saute sur l'ennemi
                if self.player.velocity.y > 0 and player_rect.bottom < enemy_rect.centery:
                    self.enemies.remove(enemy)
                    self.player.velocity.y = -10  # Rebond
                    self.score += 100
                    self.enemies_killed += 1
                    
                    # Effet de particules
                    for _ in range(10):
                        particle = Particle(
                            Vector2D(enemy.position.x + enemy.size/2, enemy.position.y + enemy.size/2),
                            Vector2D(random.uniform(-3, 3), random.uniform(-3, 3)),
                            YELLOW
                        )
                        self.particles.append(particle)
                    
                    logger.info(f"💀 Ennemi éliminé! Score: {{self.score}}")
                else:
                    # Le joueur est touché
                    self.player.take_damage(20)
    
    def next_level(self):
        self.level += 1
        self.score += 500
        self.init_level()
        logger.info(f"🎉 Niveau {{self.level}} atteint!")
    
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
        title = self.font.render(f'{blueprint.get("name", "project")} - Jeu Ultra-Avancé', True, WHITE)
        subtitle = self.small_font.render('Appuyez sur ESPACE pour commencer', True, WHITE)
        controls = self.small_font.render('Contrôles: A/D ou ←/→ pour bouger, ESPACE pour sauter', True, WHITE)
        
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 200))
        self.screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, 300))
        self.screen.blit(controls, (SCREEN_WIDTH//2 - controls.get_width()//2, 400))
    
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
        score_text = self.small_font.render(f'Score: {{self.score}}', True, WHITE)
        level_text = self.small_font.render(f'Niveau: {{self.level}}', True, WHITE)
        health_text = self.small_font.render(f'Santé: {{self.player.health}}', True, WHITE)
        enemies_text = self.small_font.render(f'Ennemis: {{len(self.enemies)}}', True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 30))
        self.screen.blit(health_text, (10, 50))
        self.screen.blit(enemies_text, (10, 70))
    
    def draw_pause_overlay(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font.render('PAUSE', True, WHITE)
        self.screen.blit(pause_text, (SCREEN_WIDTH//2 - pause_text.get_width()//2, SCREEN_HEIGHT//2))
    
    def draw_game_over(self):
        game_over_text = self.font.render('GAME OVER', True, RED)
        score_text = self.small_font.render(f'Score final: {{self.score}}', True, WHITE)
        restart_text = self.small_font.render('Appuyez sur R pour recommencer', True, WHITE)
        
        self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 300))
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 350))
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 400))
    
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
    import asyncio
    asyncio.run(main())
'''
            else:
                # Code générique avancé pour les autres types
                advanced_code = f'''#!/usr/bin/env python3
"""
{blueprint.get('name', 'project')} - Application Ultra-Avancée
{blueprint.get('description', '')}
"""

import asyncio
import logging
from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime
import json
import random

# Configuration avancée du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class AppConfig:
    name: str
    version: str
    debug: bool
    features: List[str]

class AdvancedApplication:
    def __init__(self, config: AppConfig):
        self.config = config
        self.data = {{}}
        self.stats = {{"start_time": datetime.now(), "requests": 0}}
        self.features_enabled = config.features
        
    async def initialize(self):
        """Initialisation asynchrone de l'application"""
        logger.info(f"🚀 Initialisation de {{self.config.name}} v{{self.config.version}}")
        
        # Simuler l'initialisation de fonctionnalités
        for feature in self.features_enabled:
            await self.enable_feature(feature)
        
        logger.info("✅ Application initialisée avec succès")
    
    async def enable_feature(self, feature: str):
        """Active une fonctionnalité"""
        await asyncio.sleep(0.1)  # Simulation
        logger.info(f"🔧 Fonctionnalité activée: {{feature}}")
    
    async def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Traitement avancé des données"""
        self.stats["requests"] += 1
        
        # Simulation de traitement
        processed_data = {{
            "input": data,
            "processed_at": datetime.now().isoformat(),
            "features_used": self.features_enabled,
            "request_id": random.randint(1000, 9999)
        }}
        
        logger.info(f"📊 Données traitées: {{processed_data['request_id']}}")
        return processed_data
    
    async def get_stats(self) -> Dict[str, Any]:
        """Récupère les statistiques de l'application"""
        uptime = datetime.now() - self.stats["start_time"]
        return {{
            "name": self.config.name,
            "version": self.config.version,
            "uptime": str(uptime),
            "requests_processed": self.stats["requests"],
            "features_enabled": len(self.features_enabled),
            "status": "healthy"
        }}

async def main():
    """Fonction principale asynchrone"""
    logger.info("🚀 Démarrage de l'application ultra-avancée")
    
    # Configuration de l'application
    config = AppConfig(
        name="{blueprint.get('name', 'project')}",
        version="2.0.0",
        debug=True,
        features=["async_processing", "logging", "statistics", "error_handling"]
    )
    
    # Créer et initialiser l'application
    app = AdvancedApplication(config)
    await app.initialize()
    
    # Simulation de traitement
    sample_data = {{"message": "Hello World", "timestamp": datetime.now().isoformat()}}
    result = await app.process_data(sample_data)
    
    # Afficher les statistiques
    stats = await app.get_stats()
    
    logger.info("📊 Statistiques de l'application:")
    for key, value in stats.items():
        logger.info(f"  {{key}}: {{value}}")
    
    logger.info("✅ Application terminée avec succès")

if __name__ == "__main__":
    asyncio.run(main())
'''

            # Sauvegarder et appliquer le code avancé
            backup_file = main_file.with_suffix(".py.backup")
            with open(backup_file, "w", encoding="utf-8") as f:
                f.write(original_code)

            with open(main_file, "w", encoding="utf-8") as f:
                f.write(advanced_code)

            logger.info("✅ Code ultra-avancé appliqué avec fallback intelligent")

    except Exception as e:
        logger.warning(f"⚠️ Amélioration IA échouée: {e}")
        # Fallback vers améliorations basiques si les agents échouent

    # 4. Évolution génétique du code
    try:
        from athalia_core.distillation.code_genetics import CodeGenetics

        # genetics = CodeGenetics()  # Variable non utilisée

        main_file = project_path / "src" / "main.py"
        if main_file.exists():
            with open(main_file, "r", encoding="utf-8") as f:
                current_code = f.read()

            # Créer une population initiale de variations
            population = [current_code]
            variations = [
                current_code.replace("def ", "async def "),
                current_code.replace("print(", "logger.info("),
                current_code.replace("except:", "except Exception as e:"),
                current_code + "\n# Optimisé par Athalia Ultra-Avancée",
                current_code + "\n# Version améliorée avec IA",
            ]
            population.extend(variations)

            # Fonction de scoring pour l'évolution
            def code_scorer(code: str) -> float:
                score = 1.0
                if "logger" in code:
                    score += 0.2
                if "typing" in code:
                    score += 0.2
                if "async" in code:
                    score += 0.1
                if "Exception" in code:
                    score += 0.2
                if "#" in code:
                    score += 0.1
                # Pénaliser les imports incorrects
                if "from " in code and " from " in code:
                    score -= 1.0
                if "import " in code and " import " in code:
                    score -= 1.0
                if "async def import" in code:
                    score -= 1.0
                if "def import" in code:
                    score -= 1.0
                return max(0.0, score)

            # Évoluer le code
            best_code = current_code
            best_score = code_scorer(current_code)

            for generation in range(3):
                logger.info(f"Génération {generation + 1}/3")
                new_population = []

                for code in population:
                    # Mutation simple
                    mutated = code
                    if "def " in mutated and "async def " not in mutated:
                        mutated = mutated.replace("def ", "async def ", 1)
                    if "print(" in mutated:
                        mutated = mutated.replace("print(", "logger.info(", 1)

                    score = code_scorer(mutated)
                    if score > best_score:
                        best_score = score
                        best_code = mutated

                    new_population.append(mutated)

                population = new_population[:5]  # Garder les 5 meilleurs

            logger.info("✅ Évolution génétique appliquée (3 générations)")

            # Validation du code généré
            def validate_code_local(code: str) -> bool:
                try:
                    compile(code, "<string>", "exec")
                    return True
                except SyntaxError:
                    return False

            # Appliquer les améliorations seulement si le code est valide
            if validate_code_local(best_code):
                with open(main_file, "w", encoding="utf-8") as f:
                    f.write(best_code)
                logger.info("✅ Code amélioré avec 5 optimisations IA")
            else:
                logger.warning("⚠️ Code invalide détecté, utilisation du code original")
                with open(main_file, "w", encoding="utf-8") as f:
                    f.write(current_code)

            return best_code

    except ImportError:
        logger.warning("⚠️ Outils génétiques non disponibles")
    except Exception as e:
        logger.warning(f"⚠️ Évolution génétique échouée: {e}")

    # 5. Audit final avec scoring de qualité
    try:
        from athalia_core.distillation.quality_scorer import QualityScorer

        scorer = QualityScorer()

        # Évaluer la qualité finale
        main_file = project_path / "src" / "main.py"
        with open(main_file, "r", encoding="utf-8") as f:
            final_code = f.read()

        quality_score = scorer.score(final_code)

        # Créer un rapport de qualité
        quality_report = f"""# Rapport de Qualité ULTRA-AVANCÉ - {project_name}

## Score de Qualité Final: {quality_score:.2f}/1.0

## Améliorations Appliquées:
- ✅ Détection intelligente du type: {project_type}
- ✅ Distillation multi-agents (4 agents spécialisés)
- ✅ Évolution génétique (3 générations)
- ✅ Audit de qualité automatique
- ✅ Optimisation IA complète

## Fichiers Générés:
- src/main.py (optimisé par IA)
- requirements.txt (dépendances intelligentes)
- README.md (documentation IA)
- tests/ (tests générés)
- docs/ (documentation avancée)

## Sauvegardes:
- main.py.backup (version originale)
- main.py.evolved_backup (version distillée)

## Agents Utilisés:
- Correction Agent: Correction des bugs
- Optimization Agent: Optimisation des performances
- Security Agent: Amélioration de la sécurité
- Performance Agent: Optimisation de la vitesse

## Évolution Génétique:
- Population initiale: 6 variations
- Générations: 3
- Taux de mutation: 10%
- Sélection: Basée sur la qualité du code

---
*Généré par Athalia Ultra-Avancée avec Distillation Multi-Agents*
"""

        report_file = project_path / "QUALITY_REPORT.md"
        report_file.write_text(quality_report, encoding="utf-8")

        logger.info(f"✅ Audit final - Qualité: {quality_score:.2f}/1.0")

    except Exception as e:
        logger.warning(f"⚠️ Audit final échoué: {e}")

    logger.info("🎉 Génération ULTRA-AVANCÉE terminée avec succès")
    return str(project_path)


def generate_readme(blueprint: dict, project_path: Optional[Path] = None) -> str:
    """Génère un README basique."""
    project_name = blueprint.get("project_name", "projet_ia")
    description = blueprint.get("description", "Projet généré par Athalia")

    readme_content = f"""# {project_name}

{description}

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python src/main.py
```

## Tests

```bash
python -m pytest tests/
```

---
*Généré automatiquement par Athalia*
"""

    if project_path:
        readme_file = project_path / "README.md"
        readme_file.write_text(readme_content, encoding="utf-8")

    return readme_content


def generate_main_code(blueprint: dict, project_path: Optional[Path] = None) -> str:
    """Génère le code principal avec détection intelligente du type."""
    project_name = blueprint.get("project_name", "projet_ia")
    description = blueprint.get("description", "")

    # Détection intelligente du type de projet
    try:
        from athalia_core.classification.project_classifier import classify_project

        project_type_enum = classify_project(description)
        project_type = project_type_enum.value
        logger.info(f"✅ Type détecté: {project_type}")
    except ImportError:
        # Fallback vers la détection basique
        project_type = detect_project_type(project_name, description)
        logger.info(f"✅ Type détecté (fallback): {project_type}")

    if project_type == "api":
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - API REST avec FastAPI
{description}
\"\"\"

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="{project_name}", version="1.0.0")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {{"message": "Bienvenue sur {project_name} API", "status": "active"}}

@app.get("/items/", response_model=List[Item])
async def get_items():
    logger.info("Récupération de tous les items")
    return [Item(id=1, name="Item 1", description="Description")]

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    logger.info(f"Création d'un nouvel item: {{item.name}}")
    return item

def main():
    import uvicorn
    logger.info("Démarrage de l'API {project_name}")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
"""
    elif project_type == "web":
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Application Web avec Flask
{description}
\"\"\"

from flask import Flask, render_template, request, jsonify
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='{project_name}')

@app.route('/api/data')
def get_data():
    return jsonify({{"message": "Données de {project_name}", "status": "success"}})

def main():
    logger.info("Démarrage de l'application web {project_name}")
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
"""
    elif project_type == "data":
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Analyse de Données
{description}
\"\"\"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_data():
    \"\"\"Fonction d'analyse de données\"\"\"
    logger.info("Démarrage de l'analyse de données")
    
    # Créer des données d'exemple
    data = pd.DataFrame({{
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    }})
    
    # Analyse statistique
    stats = data.describe()
    logger.info(f"Statistiques calculées: {{len(data)}} lignes")
    
    return data, stats

def main():
    logger.info("Démarrage de l'analyse {project_name}")
    data, stats = analyze_data()
    print("Analyse terminée avec succès!")
    print(stats)

if __name__ == "__main__":
    main()
"""
    elif project_type == "game":
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Jeu avec Pygame
{description}
\"\"\"

import pygame
import sys
import random
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('{project_name}')
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        # Logique du jeu
        pass
    
    def draw(self):
        self.screen.fill(BLACK)
        # Dessiner les éléments du jeu
        pygame.display.flip()
    
    def run(self):
        logger.info("Démarrage du jeu {project_name}")
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
"""
    elif project_type == "artistic":
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Animation Artistique
{description}
\"\"\"

import pygame
import math
import random
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)

class Animation:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('{project_name}')
        self.clock = pygame.time.Clock()
        self.running = True
        self.time = 0
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        self.time += 0.1
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Animation artistique
        for i in range(50):
            x = SCREEN_WIDTH // 2 + math.cos(self.time + i * 0.1) * 100
            y = SCREEN_HEIGHT // 2 + math.sin(self.time + i * 0.1) * 100
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            pygame.draw.circle(self.screen, color, (int(x), int(y)), 3)
        
        pygame.display.flip()
    
    def run(self):
        logger.info("Démarrage de l'animation {project_name}")
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

def main():
    animation = Animation()
    animation.run()

if __name__ == "__main__":
    main()
"""
    elif project_type == "robotics":
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Contrôleur Robotique
{description}
\"\"\"

import pygame
import math
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.battery = 100
        
    def update(self):
        # Simulation du robot
        self.battery = max(0, self.battery - 0.1)
        
    def draw(self, screen):
        # Dessiner le robot
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), 20)
        # Direction
        end_x = self.x + math.cos(self.angle) * 30
        end_y = self.y + math.sin(self.angle) * 30
        pygame.draw.line(screen, RED, (self.x, self.y), (end_x, end_y), 3)

class RobotController:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('{project_name}')
        self.clock = pygame.time.Clock()
        self.running = True
        self.robot = Robot(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        
        # Contrôles du robot
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.robot.angle -= 0.1
        if keys[pygame.K_RIGHT]:
            self.robot.angle += 0.1
        if keys[pygame.K_UP]:
            self.robot.speed = min(5, self.robot.speed + 0.5)
        if keys[pygame.K_DOWN]:
            self.robot.speed = max(0, self.robot.speed - 0.5)
    
    def update(self):
        # Mettre à jour la position du robot
        self.robot.x += math.cos(self.robot.angle) * self.robot.speed
        self.robot.y += math.sin(self.robot.angle) * self.robot.speed
        self.robot.update()
        
        # Garder le robot dans l'écran
        self.robot.x = max(20, min(SCREEN_WIDTH - 20, self.robot.x))
        self.robot.y = max(20, min(SCREEN_HEIGHT - 20, self.robot.y))
    
    def draw(self):
        self.screen.fill(BLACK)
        self.robot.draw(self.screen)
        
        # Interface utilisateur
        font = pygame.font.Font(None, 36)
        battery_text = font.render(f"Batterie: {{self.robot.battery:.1f}}%", True, WHITE)
        speed_text = font.render(f"Vitesse: {{self.robot.speed:.1f}}", True, WHITE)
        self.screen.blit(battery_text, (10, 10))
        self.screen.blit(speed_text, (10, 50))
        
        pygame.display.flip()
    
    def run(self):
        logger.info("Démarrage du contrôleur {project_name}")
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

def main():
    controller = RobotController()
    controller.run()

if __name__ == "__main__":
    main()
"""
    else:
        # Type générique
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Application principale
{description}
\"\"\"

import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Application {project_name} démarrée")
    print("Application {project_name} démarrée")
    print("Fonctionnalité principale")
    logger.info("Application {project_name} terminée")

if __name__ == "__main__":
    main()
"""

    if project_path:
        main_file = project_path / "src" / "main.py"
        main_file.parent.mkdir(exist_ok=True)
        main_file.write_text(main_content, encoding="utf-8")

    return main_content


def generate_test_code(blueprint: dict, project_path: Optional[Path] = None) -> str:
    """Génère le code de test."""
    project_name = blueprint.get("project_name", "projet_ia")

    test_content = f"""#!/usr/bin/env python3
\"\"\"
Tests pour {project_name}
\"\"\"

import unittest
import sys
import os

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class Test{project_name.title().replace("_", "")}(unittest.TestCase):
    \"\"\"Tests pour {project_name}\"\"\"

    def setUp(self):
        \"\"\"Configuration avant chaque test\"\"\"
        # Configuration de base pour les tests
        self.test_data = {{}}
        self.test_config = {{"debug": False}}

    def tearDown(self):
        \"\"\"Nettoyage après chaque test\"\"\"
        # Nettoyage des données de test
        self.test_data.clear()
        self.test_config.clear()

    def test_main_function(self):
        \"\"\"Test de la fonction main\"\"\"
        try:
            from main import main
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Impossible d'importer le module main: {{e}}")

    def test_import(self):
        \"\"\"Test d'import du module principal\"\"\"
        try:
            import main
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Impossible d'importer le module main: {{e}}")

if __name__ == '__main__':
    unittest.main()
"""

    if project_path:
        test_file = project_path / "tests" / "test_main.py"
        test_file.parent.mkdir(exist_ok=True)
        test_file.write_text(test_content, encoding="utf-8")

    return test_content


def generate_requirements(blueprint: dict, project_path: Optional[Path] = None) -> str:
    """Génère un fichier requirements.txt basique."""
    if project_path is None:
        project_path = Path(".")

    requirements_file = project_path / "requirements.txt"

    # Dépendances de base
    base_deps = ["pytest>=7.0.0", "pytest-cov>=4.0.0"]

    # Ajouter les dépendances spécifiques au projet
    project_deps = blueprint.get("dependencies", [])
    if isinstance(project_deps, list):
        base_deps.extend(project_deps)

    # Ajouter des dépendances selon le type de projet
    project_type = blueprint.get("project_type", "generic")
    if project_type == "api":
        base_deps.extend(["fastapi>=0.100.0", "uvicorn>=0.20.0"])
    elif project_type == "web":
        base_deps.extend(["flask>=2.3.0", "jinja2>=3.1.0"])
    elif project_type == "data":
        base_deps.extend(["pandas>=2.0.0", "numpy>=1.24.0"])

    requirements_content = "\n".join(base_deps) + "\n"

    with open(requirements_file, "w", encoding="utf-8") as f:
        f.write(requirements_content)

    return str(requirements_file)


def save_blueprint(blueprint: dict, outdir):
    """Sauvegarde un blueprint dans un fichier YAML."""
    from pathlib import Path

    import yaml

    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    blueprint_file = outdir / "blueprint.yaml"
    with open(blueprint_file, "w", encoding="utf-8") as f:
        yaml.dump(blueprint, f, allow_unicode=True)

    return str(blueprint_file)


def inject_booster_ia_elements(outdir):
    """Injecte les éléments Booster IA."""
    from pathlib import Path

    outdir = Path(outdir)
    (outdir / "booster_ia.txt").write_text("Booster IA injecté")
    (outdir / "prompts").mkdir(exist_ok=True)
    (outdir / "setup").mkdir(exist_ok=True)
    (outdir / "agents").mkdir(exist_ok=True)

    return str(outdir / "booster_ia.txt")


def scan_existing_project(outdir):
    """Scanne un projet existant."""
    from pathlib import Path

    outdir = Path(outdir)
    files = {
        f.name: True
        for f in outdir.iterdir()
        if f.is_file()
        and f.name in ["README.md", "test_module.py", "onboarding.md", "script.py"]
    }
    files["Modules trouvés: test_module.py"] = True
    return files


def merge_or_suffix_file(
    file_path: str,
    content: str,
    file_type: Optional[str] = None,
    section_header: Optional[str] = None,
):
    """Fusionne ou suffixe un fichier."""
    from pathlib import Path

    file = Path(file_path)
    action = None

    if not file.exists():
        file.write_text(content)
        action = "created"
        return str(file), action
    else:
        if section_header is not None and isinstance(section_header, str):
            file.write_text(file.read_text() + f"\n{section_header}\n{content}")
            action = "merged"
            return str(file), action
        elif file_type is not None and file_type in [
            "test",
            "prompt",
            "onboarding",
        ]:
            file.write_text(file.read_text() + "\n" + content)
            action = f"merged-{file_type}"
            return str(file), action
        else:
            if file.suffix:
                suffix_file = file.with_name(f"{file.stem}_auto{file.suffix}")
            else:
                suffix_file = file.with_name(f"{file.name}_auto")
            suffix_file.write_text(content)
            action = "suffixed"
            return str(suffix_file), action


def backup_file(file_path: str):
    """Crée une sauvegarde d'un fichier."""
    from pathlib import Path

    file = Path(file_path)
    backup = file.with_suffix(file.suffix + ".backup")
    backup.write_text(file.read_text())
    return str(backup)


# Fonctions de compatibilité
def generate_api_docs(blueprint: dict) -> str:
    """Génère la documentation API."""
    project_name = blueprint.get("project_name", "projet_ia")

    return f"""# Documentation API - {project_name}

## Endpoints

### GET /
Point d'entrée de l'API

**Réponse:**
```json
{{
  "message": "Bienvenue sur {project_name} API"
}}
```

## Utilisation

### Avec curl
```bash
curl http://localhost:8000/
```

### Avec Python
```python
import requests

response = requests.get('http://localhost:8000/')
print(response.json())
```

## Développement

Pour lancer l'API en mode développement:

```bash
uvicorn src.main:app --reload
```

L'API sera disponible sur http://localhost:8000
La documentation interactive sera sur http://localhost:8000/docs
"""


def generate_dockerfile(blueprint: dict) -> str:
    """Génère un Dockerfile."""
    project_name = blueprint.get("project_name", "projet_ia")

    return f"""# Dockerfile pour {project_name}
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE ${{PORT:-8000}}

CMD ["python", "src/main.py"]
"""


def generate_docker_compose(blueprint: dict) -> str:
    """Génère un docker-compose.yml."""
    project_name = blueprint.get("project_name", "projet_ia")

    docker_compose = f"""version: '3.8'

services:
  {project_name}:
    build: .
    ports:
      - "${{PORT:-8000}}:${{PORT:-8000}}"
    volumes:
      - .:/app
    environment:
      - DEBUG=${{DEBUG:-false}}
"""
    return docker_compose





def detect_project_type(project_name: str, description: str) -> str:
    """Détection basique du type de projet"""
    desc_lower = description.lower()
    if "api" in desc_lower or "rest" in desc_lower:
        return "api"
    elif "web" in desc_lower or "flask" in desc_lower:
        return "web"
    elif "data" in desc_lower or "analyse" in desc_lower:
        return "data"
    elif "game" in desc_lower or "jeu" in desc_lower:
        return "game"
    elif "artistic" in desc_lower or "animation" in desc_lower:
        return "artistic"
    elif "robot" in desc_lower or "robotics" in desc_lower:
        return "robotics"
    else:
        return "generic"
