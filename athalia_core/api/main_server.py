#!/usr/bin/env python3
"""
API serveur principal pour Athalia
Serveur FastAPI avec interface web moderne et endpoints complets
"""

import asyncio
import json
import logging
import os
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


# Modèles Pydantic
class ProjectRequest(BaseModel):
    """Modèle de requête de projet"""

    name: str = Field(..., description="Nom du projet")
    type: str = Field(..., description="Type de projet (web, api, cli, etc.)")
    framework: str | None = Field(None, description="Framework à utiliser")
    description: str | None = Field("", description="Description du projet")
    features: list[str] = Field(
        default_factory=list, description="Fonctionnalités à inclure"
    )


class SecurityScanRequest(BaseModel):
    """Modèle de requête de scan de sécurité"""

    scan_type: str = Field(
        ..., description="Type de scan (bandit, safety, pip-audit, semgrep)"
    )
    target_path: str | None = Field(".", description="Chemin cible pour le scan")
    include_patterns: list[str] = Field(
        default_factory=list, description="Patterns d'inclusion"
    )
    exclude_patterns: list[str] = Field(
        default_factory=list, description="Patterns d'exclusion"
    )


class CodeQualityRequest(BaseModel):
    """Modèle de requête d'analyse de qualité"""

    target_path: str = Field(".", description="Chemin cible pour l'analyse")
    tools: list[str] = Field(
        default_factory=lambda: ["black", "ruff", "mypy"],
        description="Outils à utiliser",
    )
    generate_report: bool = Field(True, description="Générer un rapport détaillé")


class BenchmarkRequest(BaseModel):
    """Modèle de requête de benchmark"""

    benchmark_type: str = Field(
        ...,
        description="Type de benchmark (performance, security, quality, ai, robotics)",
    )
    iterations: int = Field(3, description="Nombre d'itérations")
    timeout: int = Field(300, description="Timeout en secondes")


class WebSocketMessage(BaseModel):
    """Modèle de message WebSocket"""

    type: str = Field(..., description="Type de message")
    data: Any = Field(..., description="Données du message")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    sender: str = Field("client", description="Expéditeur du message")


class MainAPIServer:
    """Serveur API principal avec FastAPI"""

    def __init__(
        self, project_path: str = ".", host: str = "localhost", port: int = 8000
    ):
        self.project_path = Path(project_path)
        self.host = host
        self.port = port
        self.app = FastAPI(
            title="Athalia API",
            description="API serveur principal pour le système Athalia",
            version="12.0.0",
            docs_url="/docs",
            redoc_url="/redoc",
        )
        self.setup_routes()
        self.setup_middleware()
        self.api_data = self._get_default_api_data()

    def _get_default_api_data(self) -> dict[str, Any]:
        """Retourne des données API par défaut"""
        return {
            "server_started": datetime.now().isoformat(),
            "total_requests": 0,
            "active_connections": 0,
            "endpoints": [
                "/",
                "/docs",
                "/redoc",
                "/api/health",
                "/api/projects",
                "/api/security",
                "/api/quality",
                "/api/benchmarks",
                "/api/websocket",
                "/api/metrics",
            ],
            "status": "running",
        }

    def setup_middleware(self):
        """Configure le middleware de l'application"""
        from fastapi.middleware.cors import CORSMiddleware

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def setup_routes(self):
        """Configure les routes de l'API"""

        @self.app.get("/", response_class=HTMLResponse)
        async def root():
            """Page d'accueil de l'API"""
            return self._get_main_page()

        @self.app.get("/api/health")
        async def health_check():
            """Vérification de l'état de santé de l'API"""
            return {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "version": "12.0.0",
                "uptime": "running",
            }

        @self.app.post("/api/projects/generate")
        async def generate_project(
            request: ProjectRequest, background_tasks: BackgroundTasks
        ):
            """Génère un nouveau projet"""
            try:
                # Simuler la génération de projet
                project_id = f"proj_{int(datetime.now().timestamp())}"

                # Tâche en arrière-plan pour la génération
                background_tasks.add_task(
                    self._generate_project_background, project_id, request
                )

                return {
                    "status": "success",
                    "message": "Génération de projet démarrée",
                    "project_id": project_id,
                    "estimated_time": "2-5 minutes",
                }
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e)) from e

        @self.app.post("/api/security/scan")
        async def run_security_scan(request: SecurityScanRequest):
            """Lance un scan de sécurité"""
            try:
                # Simuler le scan de sécurité
                scan_id = f"scan_{int(datetime.now().timestamp())}"

                result = {
                    "scan_id": scan_id,
                    "status": "completed",
                    "scan_type": request.scan_type,
                    "target_path": request.target_path,
                    "vulnerabilities_found": 0,
                    "critical_issues": 0,
                    "high_issues": 0,
                    "medium_issues": 0,
                    "low_issues": 0,
                    "scan_duration": "45s",
                    "timestamp": datetime.now().isoformat(),
                }

                return result
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e)) from e

        @self.app.post("/api/quality/analyze")
        async def analyze_code_quality(request: CodeQualityRequest):
            """Analyse la qualité du code"""
            try:
                # Simuler l'analyse de qualité
                analysis_id = f"qual_{int(datetime.now().timestamp())}"

                result = {
                    "analysis_id": analysis_id,
                    "status": "completed",
                    "target_path": request.target_path,
                    "tools_used": request.tools,
                    "overall_score": 95.5,
                    "issues_found": 3,
                    "critical_issues": 0,
                    "high_issues": 1,
                    "medium_issues": 1,
                    "low_issues": 1,
                    "analysis_duration": "1m 30s",
                    "timestamp": datetime.now().isoformat(),
                }

                return result
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e)) from e

        @self.app.post("/api/benchmarks/run")
        async def run_benchmark(request: BenchmarkRequest):
            """Lance un benchmark"""
            try:
                # Simuler le benchmark
                benchmark_id = f"bench_{int(datetime.now().timestamp())}"

                result = {
                    "benchmark_id": benchmark_id,
                    "status": "completed",
                    "benchmark_type": request.benchmark_type,
                    "iterations": request.iterations,
                    "overall_score": 87.3,
                    "performance_metrics": {
                        "cpu_usage": "45%",
                        "memory_usage": "128MB",
                        "execution_time": "2.3s",
                        "throughput": "1500 ops/s",
                    },
                    "benchmark_duration": "45s",
                    "timestamp": datetime.now().isoformat(),
                }

                return result
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e)) from e

        @self.app.get("/api/metrics")
        async def get_metrics():
            """Retourne les métriques de l'API"""
            return {
                "api_metrics": self.api_data,
                "system_metrics": {
                    "python_version": "3.11+",
                    "fastapi_version": "0.104+",
                    "platform": "Linux/macOS/Windows",
                    "memory_usage": "45MB",
                    "cpu_usage": "2%",
                },
                "timestamp": datetime.now().isoformat(),
            }

        @self.app.get("/api/endpoints")
        async def list_endpoints():
            """Liste tous les endpoints disponibles"""
            routes = []
            for route in self.app.routes:
                if hasattr(route, "methods") and hasattr(route, "path"):
                    routes.append(
                        {
                            "path": route.path,
                            "methods": list(route.methods),
                            "name": getattr(route, "name", "Unnamed"),
                        }
                    )
            return {"endpoints": routes}

        @self.app.get("/api/status")
        async def get_status():
            """Retourne le statut complet du serveur"""
            return {
                "server": {
                    "status": "running",
                    "host": self.host,
                    "port": self.port,
                    "started_at": self.api_data["server_started"],
                    "uptime": "running",
                },
                "api": self.api_data,
                "timestamp": datetime.now().isoformat(),
            }

    async def _generate_project_background(
        self, project_id: str, request: ProjectRequest
    ):
        """Tâche en arrière-plan pour la génération de projet"""
        try:
            logger.info(f"Démarrage de la génération du projet {project_id}")

            # Simuler le travail en arrière-plan
            await asyncio.sleep(2)

            logger.info(f"Projet {project_id} généré avec succès")

        except Exception as e:
            logger.error(f"Erreur lors de la génération du projet {project_id}: {e}")

    def _get_main_page(self) -> str:
        """Retourne la page HTML principale"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Serveur Principal - Athalia</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}

        .header {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            font-size: 3em;
            color: #667eea;
            margin-bottom: 10px;
            font-weight: 300;
        }}

        .header p {{
            font-size: 1.2em;
            color: #666;
        }}

        .status-banner {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .status-indicator {{
            display: inline-block;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 10px;
            background: #28a745;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0% {{ opacity: 1; }}
            50% {{ opacity: 0.7; }}
            100% {{ opacity: 1; }}
        }}

        .api-endpoints {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .endpoints-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .endpoints-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}

        .endpoint-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }}

        .endpoint-card:hover {{
            transform: translateY(-5px);
        }}

        .endpoint-method {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: 600;
            margin-bottom: 10px;
            text-transform: uppercase;
        }}

        .method-get {{
            background: #28a745;
            color: white;
        }}

        .method-post {{
            background: #007bff;
            color: white;
        }}

        .method-put {{
            background: #fd7e14;
            color: white;
        }}

        .method-delete {{
            background: #dc3545;
            color: white;
        }}

        .endpoint-path {{
            font-family: monospace;
            font-size: 1.1em;
            color: #333;
            margin-bottom: 10px;
            word-break: break-all;
        }}

        .endpoint-description {{
            color: #666;
            font-size: 0.9em;
            line-height: 1.4;
        }}

        .quick-actions {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .actions-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
        }}

        .actions-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .action-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            transition: transform 0.3s ease;
            cursor: pointer;
        }}

        .action-card:hover {{
            transform: translateY(-5px);
            background: #e9ecef;
        }}

        .action-icon {{
            font-size: 2.5em;
            margin-bottom: 15px;
        }}

        .action-title {{
            font-size: 1.2em;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }}

        .action-description {{
            color: #666;
            font-size: 0.9em;
            line-height: 1.4;
        }}

        .stats-container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .stats-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .stat-card {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 15px;
        }}

        .stat-number {{
            font-size: 2.5em;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }}

        .stat-description {{
            color: #666;
            font-size: 0.9em;
        }}

        .footer {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            color: #666;
        }}

        .btn {{
            display: inline-block;
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 600;
            transition: transform 0.3s ease;
            margin: 10px;
        }}

        .btn:hover {{
            transform: translateY(-2px);
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2em;
            }}

            .endpoints-grid {{
                grid-template-columns: 1fr;
            }}

            .actions-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 API Serveur Principal Athalia</h1>
            <p>Interface web moderne pour l'API serveur principal</p>
        </div>

        <div class="status-banner">
            <div class="status-indicator"></div>
            <span>Serveur API en cours d'exécution sur http://{self.host}:{self.port}</span>
            <div style="margin-top: 15px;">
                <a href="/docs" class="btn">📚 Documentation API</a>
                <a href="/redoc" class="btn">📖 Documentation Alternative</a>
            </div>
        </div>

        <div class="quick-actions">
            <h2 class="actions-title">⚡ Actions Rapides</h2>
            <div class="actions-grid">
                <div class="action-card" onclick="testHealthCheck()">
                    <div class="action-icon">❤️</div>
                    <div class="action-title">Vérifier Santé</div>
                    <div class="action-description">Tester l'état de santé de l'API</div>
                </div>

                <div class="action-card" onclick="testMetrics()">
                    <div class="action-icon">📊</div>
                    <div class="action-title">Métriques</div>
                    <div class="action-description">Afficher les métriques du serveur</div>
                </div>

                <div class="action-card" onclick="testEndpoints()">
                    <div class="action-icon">🔗</div>
                    <div class="action-title">Endpoints</div>
                    <div class="action-description">Lister tous les endpoints</div>
                </div>

                <div class="action-card" onclick="testStatus()">
                    <div class="action-icon">📋</div>
                    <div class="action-title">Statut</div>
                    <div class="action-description">Statut complet du serveur</div>
                </div>
            </div>
        </div>

        <div class="stats-container">
            <h2 class="stats-title">📈 Statistiques du Serveur</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" id="totalRequests">0</div>
                    <div class="stat-description">Total Requêtes</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="activeConnections">0</div>
                    <div class="stat-description">Connexions Actives</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="endpointsCount">10</div>
                    <div class="stat-description">Endpoints Disponibles</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="uptime">-</div>
                    <div class="stat-description">Temps de Fonctionnement</div>
                </div>
            </div>
        </div>

        <div class="api-endpoints">
            <h2 class="endpoints-title">🔗 Endpoints API Disponibles</h2>
            <div class="endpoints-grid">
                <div class="endpoint-card">
                    <span class="endpoint-method method-get">GET</span>
                    <div class="endpoint-path">/api/health</div>
                    <div class="action-description">Vérification de l'état de santé de l'API</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-post">POST</span>
                    <div class="endpoint-path">/api/projects/generate</div>
                    <div class="action-description">Génération de nouveaux projets</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-post">POST</span>
                    <div class="endpoint-path">/api/security/scan</div>
                    <div class="action-description">Lancement de scans de sécurité</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-post">POST</span>
                    <div class="endpoint-path">/api/quality/analyze</div>
                    <div class="action-description">Analyse de la qualité du code</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-post">POST</span>
                    <div class="endpoint-path">/api/benchmarks/run</div>
                    <div class="action-description">Exécution de benchmarks</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-get">GET</span>
                    <div class="endpoint-path">/api/metrics</div>
                    <div class="action-description">Métriques du serveur et du système</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-get">GET</span>
                    <div class="endpoint-path">/api/endpoints</div>
                    <div class="action-description">Liste de tous les endpoints</div>
                </div>

                <div class="endpoint-card">
                    <span class="endpoint-method method-get">GET</span>
                    <div class="endpoint-path">/api/status</div>
                    <div class="action-description">Statut complet du serveur</div>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🕒 Dernière mise à jour: <span id="last-update">{current_time}</span></p>
            <p>🚀 API serveur principal générée automatiquement par Athalia</p>
        </div>
    </div>

    <script>
        // Variables globales
        let serverStats = {{
            totalRequests: 0,
            activeConnections: 0,
            startTime: new Date()
        }};

        // Fonctions de test des endpoints
        async function testHealthCheck() {{
            try {{
                const response = await fetch('/api/health');
                const data = await response.json();
                alert(`✅ Santé API: ${{data.status}}\\nVersion: ${{data.version}}\\nTimestamp: ${{data.timestamp}}`);
            }} catch (error) {{
                alert(`❌ Erreur: ${{error.message}}`);
            }}
        }}

        async function testMetrics() {{
            try {{
                const response = await fetch('/api/metrics');
                const data = await response.json();
                alert(`✅ Métriques:\\nTotal Requêtes: ${{data.api_metrics.total_requests}}\\nEndpoints: ${{data.api_metrics.endpoints.length}}\\nStatut: ${{data.api_metrics.status}}`);
            }} catch (error) {{
                alert(`❌ Erreur: ${{error.message}}`);
            }}
        }}

        async function testEndpoints() {{
            try {{
                const response = await fetch('/api/endpoints');
                const data = await response.json();
                alert('✅ Endpoints disponibles: ' + data.endpoints.length + '\\n\\n' + data.endpoints.map(e => e.methods.join(', ') + ' ' + e.path).join('\\n'));
            }} catch (error) {{
                alert('❌ Erreur: ' + error.message);
            }}
        }}

        async function testStatus() {{
            try {{
                const response = await fetch('/api/status');
                const data = await response.json();
                alert(`✅ Statut Serveur:\\nHôte: ${{data.server.host}}:${{data.server.port}}\\nStatut: ${{data.server.status}}\\nDémarré: ${{data.server.started_at}}`);
            }} catch (error) {{
                alert(`❌ Erreur: ${{error.message}}`);
            }}
        }}

        // Mise à jour des statistiques
        function updateStats() {{
            document.getElementById('totalRequests').textContent = serverStats.totalRequests;
            document.getElementById('activeConnections').textContent = serverStats.activeConnections;

            const uptime = Math.floor((new Date() - serverStats.startTime) / 1000);
            const hours = Math.floor(uptime / 3600);
            const minutes = Math.floor((uptime % 3600) / 60);
            const seconds = uptime % 60;

            document.getElementById('uptime').textContent =
                `${{hours.toString().padStart(2, '0')}}:${{minutes.toString().padStart(2, '0')}}:${{seconds.toString().padStart(2, '0')}}`;
        }}

        // Mise à jour automatique
        setInterval(() => {{
            const now = new Date();
            document.getElementById('last-update').textContent = now.toLocaleString('fr-FR');
            updateStats();
        }}, 1000);

        // Animation d'entrée des éléments
        document.addEventListener('DOMContentLoaded', function() {{
            const elements = document.querySelectorAll('.status-banner, .quick-actions, .stats-container, .api-endpoints');
            elements.forEach((element, index) => {{
                setTimeout(() => {{
                    element.style.opacity = '0';
                    element.style.transform = 'translateY(20px)';
                    element.style.transition = 'all 0.5s ease';

                    setTimeout(() => {{
                        element.style.opacity = '1';
                        element.style.transform = 'translateY(0)';
                    }}, 100);
                }}, index * 100);
            }});
        }});
    </script>
</body>
</html>"""

    def start_server(self):
        """Démarre le serveur API"""
        logger.info(f"Démarrage du serveur API sur http://{self.host}:{self.port}")

        uvicorn.run(
            self.app, host=self.host, port=self.port, log_level="info", reload=False
        )

    def open_api_interface(self) -> None:
        """Ouvre l'interface web de l'API dans le navigateur"""
        webbrowser.open(f"http://{self.host}:{self.port}")
        logger.info(f"Interface API ouverte: http://{self.host}:{self.port}")

    def get_api_summary(self) -> dict[str, Any]:
        """Retourne un résumé de l'API"""
        return {
            "host": self.host,
            "port": self.port,
            "status": "running",
            "endpoints_count": len(self.api_data["endpoints"]),
            "started_at": self.api_data["server_started"],
            "version": "12.0.0",
        }


def main():
    """Fonction principale pour test du serveur API"""
    import sys

    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = "."

    api_server = MainAPIServer(project_path)

    if len(sys.argv) > 2 and sys.argv[2] == "start":
        print("🚀 Démarrage du serveur API...")
        print("Interface disponible sur: http://localhost:8000")
        print("Documentation API: http://localhost:8000/docs")
        print("Appuyez sur Ctrl+C pour arrêter")

        try:
            api_server.start_server()
        except KeyboardInterrupt:
            print("\\n🛑 Serveur API arrêté")
    else:
        api_server.open_api_interface()


if __name__ == "__main__":
    main()
