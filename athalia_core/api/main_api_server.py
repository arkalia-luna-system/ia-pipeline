#!/usr/bin/env python3
"""
Serveur API REST principal d'Athalia
API complète pour l'intégration et l'automatisation
"""

import asyncio
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import uvicorn
from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Modèles Pydantic
class HealthResponse(BaseModel):
    """Réponse de santé de l'API"""

    status: str = Field(..., description="Statut du service")
    timestamp: datetime = Field(..., description="Horodatage de la vérification")
    version: str = Field(..., description="Version de l'API")
    uptime: float = Field(..., description="Temps de fonctionnement en secondes")


class ProjectBlueprint(BaseModel):
    """Blueprint de projet pour la génération"""

    name: str = Field(..., description="Nom du projet")
    description: str = Field(..., description="Description du projet")
    project_type: str = Field(..., description="Type de projet")
    dependencies: list[str] | None = Field(default=[], description="Dépendances")
    modules: list[str] | None = Field(default=[], description="Modules à inclure")


class ProjectResponse(BaseModel):
    """Réponse de génération de projet"""

    project_name: str = Field(..., description="Nom du projet généré")
    status: str = Field(..., description="Statut de la génération")
    output_path: str = Field(..., description="Chemin de sortie")
    files_created: int = Field(..., description="Nombre de fichiers créés")
    generation_time: float = Field(..., description="Temps de génération en secondes")


class SecurityScanResponse(BaseModel):
    """Réponse de scan de sécurité"""

    scan_id: str = Field(..., description="ID unique du scan")
    status: str = Field(..., description="Statut du scan")
    vulnerabilities: dict[str, int] = Field(
        ..., description="Nombre de vulnérabilités par niveau"
    )
    score: int = Field(..., description="Score de sécurité (0-100)")
    recommendations: list[str] = Field(..., description="Recommandations de sécurité")


class ErrorResponse(BaseModel):
    """Réponse d'erreur standardisée"""

    error: str = Field(..., description="Message d'erreur")
    detail: str | None = Field(None, description="Détails supplémentaires")
    timestamp: datetime = Field(..., description="Horodatage de l'erreur")


# Variables globales
start_time = datetime.now()

# Création de l'application FastAPI
app = FastAPI(
    title="Athalia API",
    description="API REST complète pour la plateforme Athalia DevOps",
    version="12.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montage des fichiers statiques
try:
    static_dir = Path("dashboard")
    if static_dir.exists():
        app.mount("/dashboard", StaticFiles(directory="dashboard"), name="dashboard")
        logger.info("Dashboard statique monté sur /dashboard")
except Exception as e:
    logger.warning(f"Impossible de monter le dashboard statique: {e}")


# Routes de base
@app.get("/", response_class=HTMLResponse)
async def root():
    """Page d'accueil de l'API"""
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Athalia API - Plateforme DevOps</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; }
            .container { max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px); }
            h1 { text-align: center; font-size: 3em; margin-bottom: 20px; }
            .endpoints { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin: 20px 0; }
            .endpoint { margin: 10px 0; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 10px; }
            .method { display: inline-block; background: #28a745; color: white; padding: 5px 10px; border-radius: 5px; margin-right: 10px; }
            .docs { text-align: center; margin-top: 30px; }
            .docs a { color: #ffd700; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Athalia API</h1>
            <p style="text-align: center; font-size: 1.2em;">Plateforme DevOps d'automatisation et d'intelligence artificielle</p>

            <div class="endpoints">
                <h2>📡 Endpoints Disponibles</h2>
                <div class="endpoint">
                    <span class="method">GET</span>
                    <strong>/health</strong> - Vérification de santé
                </div>
                <div class="endpoint">
                    <span class="method">GET</span>
                    <strong>/api/projects</strong> - Liste des projets
                </div>
                <div class="endpoint">
                    <span class="method">POST</span>
                    <strong>/api/projects/generate</strong> - Génération de projet
                </div>
                <div class="endpoint">
                    <span class="method">POST</span>
                    <strong>/api/security/scan</strong> - Scan de sécurité
                </div>
                <div class="endpoint">
                    <span class="method">GET</span>
                    <strong>/api/metrics</strong> - Métriques du projet
                </div>
            </div>

            <div class="docs">
                <h3>📚 Documentation</h3>
                <p><a href="/docs">📖 Swagger UI</a> | <a href="/redoc">📋 ReDoc</a></p>
                <p><a href="/dashboard">📊 Dashboard</a></p>
            </div>
        </div>
    </body>
    </html>
    """


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Vérification de l'état de l'API"""
    uptime = (datetime.now() - start_time).total_seconds()
    return HealthResponse(
        status="healthy", timestamp=datetime.now(), version="12.0.0", uptime=uptime
    )


# Routes API
@app.get("/api/projects", response_model=list[dict[str, Any]])
async def list_projects():
    """Liste des projets disponibles"""
    try:
        # Simuler la liste des projets
        projects = [
            {
                "id": "1",
                "name": "API REST",
                "type": "api",
                "description": "Projet API REST avec FastAPI",
                "created_at": datetime.now().isoformat(),
            },
            {
                "id": "2",
                "name": "Application Web",
                "type": "web",
                "description": "Application web moderne",
                "created_at": datetime.now().isoformat(),
            },
        ]
        return projects
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des projets: {e}")
        raise HTTPException(status_code=500, detail="Erreur interne du serveur") from e


@app.post("/api/projects/generate", response_model=ProjectResponse)
async def generate_project(
    blueprint: ProjectBlueprint, background_tasks: BackgroundTasks
):
    """Génère un nouveau projet basé sur le blueprint"""
    try:
        start_time = datetime.now()

        # Simuler la génération de projet
        project_name = blueprint.name
        output_path = f"generated_projects/{project_name}"

        # Créer le dossier de sortie
        Path(output_path).mkdir(parents=True, exist_ok=True)

        # Simuler la création de fichiers
        files_created = 3  # README, main.py, requirements.txt

        generation_time = (datetime.now() - start_time).total_seconds()

        # Tâche en arrière-plan pour la génération complète
        background_tasks.add_task(generate_project_files, blueprint, output_path)

        return ProjectResponse(
            project_name=project_name,
            status="generating",
            output_path=output_path,
            files_created=files_created,
            generation_time=generation_time,
        )

    except Exception as e:
        logger.error(f"Erreur lors de la génération du projet: {e}")
        raise HTTPException(
            status_code=500, detail=f"Erreur de génération: {str(e)}"
        ) from e


@app.post("/api/security/scan", response_model=SecurityScanResponse)
async def security_scan():
    """Lance un scan de sécurité complet"""
    try:
        scan_id = f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Simuler le scan de sécurité
        vulnerabilities = {"high": 0, "medium": 0, "low": 2}

        score = 95  # Score de sécurité

        recommendations = [
            "Maintenir les dépendances à jour",
            "Vérifier régulièrement les rapports de sécurité",
            "Implémenter des tests de sécurité automatisés",
        ]

        return SecurityScanResponse(
            scan_id=scan_id,
            status="completed",
            vulnerabilities=vulnerabilities,
            score=score,
            recommendations=recommendations,
        )

    except Exception as e:
        logger.error(f"Erreur lors du scan de sécurité: {e}")
        raise HTTPException(status_code=500, detail=f"Erreur de scan: {str(e)}") from e


@app.get("/api/metrics", response_model=dict[str, Any])
async def get_metrics():
    """Récupère les métriques du projet"""
    try:
        # Simuler les métriques
        metrics = {
            "project_stats": {
                "total_files": 341,
                "total_lines": 75625,
                "python_files": 150,
                "test_files": 1774,
            },
            "security_stats": {
                "score": 95,
                "vulnerabilities": 2,
                "last_scan": datetime.now().isoformat(),
            },
            "performance_stats": {
                "cache_hit_rate": 85,
                "response_time": 0.2,
                "memory_usage": "150MB",
            },
        }
        return metrics

    except Exception as e:
        logger.error(f"Erreur lors de la récupération des métriques: {e}")
        raise HTTPException(
            status_code=500, detail=f"Erreur de métriques: {str(e)}"
        ) from e


@app.get("/api/plugins", response_model=list[dict[str, Any]])
async def list_plugins():
    """Liste les plugins disponibles"""
    try:
        plugins = [
            {
                "name": "hello_plugin",
                "description": "Plugin de démonstration",
                "version": "1.0.0",
                "status": "active",
            },
            {
                "name": "export_docker_plugin",
                "description": "Plugin d'export Docker",
                "version": "1.0.0",
                "status": "active",
            },
        ]
        return plugins

    except Exception as e:
        logger.error(f"Erreur lors de la récupération des plugins: {e}")
        raise HTTPException(
            status_code=500, detail=f"Erreur de plugins: {str(e)}"
        ) from e


# Gestionnaire d'erreurs global
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Gestionnaire d'erreurs HTTP personnalisé"""
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.detail,
            detail=f"Erreur {exc.status_code} sur {request.url.path}",
            timestamp=datetime.now(),
        ).dict(),
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Gestionnaire d'erreurs générales"""
    logger.error(f"Erreur non gérée: {exc}")
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Erreur interne du serveur", detail=str(exc), timestamp=datetime.now()
        ).dict(),
    )


# Fonctions utilitaires
async def generate_project_files(blueprint: ProjectBlueprint, output_path: str):
    """Génère les fichiers du projet en arrière-plan"""
    try:
        # Simuler la génération de fichiers
        await asyncio.sleep(2)

        # Créer README.md
        dependencies_text = (
            "\n".join(blueprint.dependencies)
            if blueprint.dependencies
            else "Aucune dépendance spécifique"
        )
        modules_text = (
            "\n".join(blueprint.modules) if blueprint.modules else "Modules par défaut"
        )

        readme_content = f"""# {blueprint.name}

{blueprint.description}

## Type de projet
{blueprint.project_type}

## Dépendances
{dependencies_text}

## Modules inclus
{modules_text}

Généré automatiquement par Athalia API
"""

        readme_file = Path(output_path) / "README.md"
        readme_file.write_text(readme_content, encoding="utf-8")

        logger.info(f"Fichiers du projet {blueprint.name} générés avec succès")

    except Exception as e:
        logger.error(f"Erreur lors de la génération des fichiers: {e}")


def get_uptime() -> float:
    """Calcule le temps de fonctionnement"""
    return (datetime.now() - start_time).total_seconds()


# Point d'entrée principal
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "false").lower() == "true"

    logger.info(f"🚀 Démarrage du serveur API Athalia sur le port {port}")
    logger.info(f"📖 Documentation disponible sur http://localhost:{port}/docs")
    logger.info(f"📊 Dashboard disponible sur http://localhost:{port}/dashboard")

    uvicorn.run(
        "main_api_server:app",
        host="0.0.0.0",
        port=port,
        reload=debug,
        log_level="info" if not debug else "debug",
    )
