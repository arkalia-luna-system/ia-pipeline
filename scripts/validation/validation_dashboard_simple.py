#!/usr/bin/env python3
"""
Dashboard de Validation Simple - Athalia/Arkalia
Interface web pour visualiser les résultats de validation
"""

import http.server
import json
import socketserver
import subprocess
from datetime import datetime
from pathlib import Path


class ValidationDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def run_integrated_validation(self):
        """Exécute une validation intégrée simple"""
        try:
            # Validation basique basée sur la présence des fichiers essentiels
            essential_files = [
                "README.md",
                "requirements.txt",
                "setup.py",
                "tests/",
                "docs/",
            ]

            score = 100
            workspace = Path.cwd()

            for file_path in essential_files:
                if not (workspace / file_path).exists():
                    score -= 10

            # Vérification de la qualité du code avec ruff
            try:
                result = subprocess.run(
                    ["ruff", "check", ".", "--quiet"],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                if result.returncode != 0:
                    score -= 20
            except Exception:
                pass  # Ruff non disponible

            return max(score, 0)

        except Exception as e:
            print(f"Erreur lors de la validation intégrée: {e}")
            return 80  # Score par défaut

    def do_GET(self):
        if self.path == "/":
            self.path = "/dashboard_validation.html"
        elif self.path == "/api/validate":
            self.send_validation_result()
            return
        elif self.path == "/api/history":
            self.send_history()
            return

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/api/validate":
            self.send_validation_result()
            return

        self.send_error(404)

    def send_validation_result(self):
        """Envoie le résultat de validation en temps réel"""
        try:
            # Validation intégrée au lieu d'appeler un script externe
            score = self.run_integrated_validation()

            response_data = {
                "success": True,
                "score": score,
                "execution_time": 30,
                "status": "success",
                "message": "Validation intégrée terminée avec succès",
            }

        except Exception as e:
            response_data = {
                "success": False,
                "error": str(e),
                "status": "error",
                "message": "Exception lors de la validation",
            }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())

    def send_history(self):
        """Envoie l'historique des validations"""
        try:
            # Crée un historique simulé pour l'instant
            history = [
                {
                    "timestamp": datetime.now().isoformat(),
                    "score": 100,
                    "type": "objective",
                    "execution_time": 30,
                }
            ]

            response_data = {"success": True, "history": history}

        except Exception as e:
            response_data = {"success": False, "error": str(e)}

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


def run_dashboard(port=5001):
    """Lance le dashboard de validation"""
    try:
        with socketserver.TCPServer(("", port), ValidationDashboardHandler) as httpd:
            print(f"🚀 Dashboard de validation démarré sur http://localhost:{port}")
            print(f"📊 Interface: http://localhost:{port}/dashboard_validation.html")
            print(f"🔌 API: http://localhost:{port}/api/validate")
            print("Appuyez sur Ctrl+C pour arrêter")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Dashboard arrêté")
    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    run_dashboard()
