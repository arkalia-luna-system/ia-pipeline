"""
Tests de charge pour Athalia avec Locust
Simule des utilisateurs pour tester les performances
"""

import json
import random

from locust import HttpUser, between, task


class AthaliaAPIUser(HttpUser):
    """Utilisateur simulé pour l'API Athalia"""

    wait_time = between(1, 3)  # Attente entre 1 et 3 secondes

    def on_start(self):
        """Démarrage de l'utilisateur"""
        self.client.verify = False  # Désactiver la vérification SSL pour les tests

    @task(3)
    def health_check(self):
        """Test de santé de l'API (fréquent)"""
        with self.client.get("/health", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Health check failed: {response.status_code}")

    @task(2)
    def get_docs(self):
        """Récupération de la documentation"""
        with self.client.get("/docs", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Docs failed: {response.status_code}")

    @task(1)
    def get_openapi(self):
        """Récupération du schéma OpenAPI"""
        with self.client.get("/openapi.json", catch_response=True) as response:
            if response.status_code == 200:
                try:
                    json.loads(response.text)
                    response.success()
                except json.JSONDecodeError:
                    response.failure("Invalid JSON response")
            else:
                response.failure(f"OpenAPI failed: {response.status_code}")

    @task(1)
    def get_metrics(self):
        """Récupération des métriques (si disponibles)"""
        with self.client.get("/metrics", catch_response=True) as response:
            # 404 est acceptable si les métriques ne sont pas implémentées
            if response.status_code in [200, 404]:
                response.success()
            else:
                response.failure(f"Metrics failed: {response.status_code}")


class AthaliaCLIUser(HttpUser):
    """Utilisateur simulé pour les tests CLI"""

    wait_time = between(2, 5)

    def on_start(self):
        """Démarrage de l'utilisateur CLI"""
        self.client.verify = False

    @task(2)
    def cli_help(self):
        """Test de la commande d'aide CLI"""
        # Simuler une requête vers un endpoint CLI (si disponible)
        with self.client.get("/cli/help", catch_response=True) as response:
            if response.status_code in [200, 404]:  # 404 si pas implémenté
                response.success()
            else:
                response.failure(f"CLI help failed: {response.status_code}")

    @task(1)
    def cli_version(self):
        """Test de la commande version CLI"""
        with self.client.get("/cli/version", catch_response=True) as response:
            if response.status_code in [200, 404]:  # 404 si pas implémenté
                response.success()
            else:
                response.failure(f"CLI version failed: {response.status_code}")


class AthaliaDashboardUser(HttpUser):
    """Utilisateur simulé pour le dashboard"""

    wait_time = between(3, 7)

    def on_start(self):
        """Démarrage de l'utilisateur dashboard"""
        self.client.verify = False

    @task(3)
    def dashboard_main(self):
        """Accès au dashboard principal"""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Dashboard failed: {response.status_code}")

    @task(2)
    def dashboard_analytics(self):
        """Accès aux analytics"""
        with self.client.get("/analytics", catch_response=True) as response:
            if response.status_code in [200, 404]:  # 404 si pas implémenté
                response.success()
            else:
                response.failure(f"Analytics failed: {response.status_code}")

    @task(1)
    def dashboard_security(self):
        """Accès aux rapports de sécurité"""
        with self.client.get("/security", catch_response=True) as response:
            if response.status_code in [200, 404]:  # 404 si pas implémenté
                response.success()
            else:
                response.failure(f"Security reports failed: {response.status_code}")


# Configuration des scénarios de test
class WebsiteUser(HttpUser):
    """Utilisateur web général"""

    tasks = [AthaliaAPIUser, AthaliaDashboardUser]
    weight = 1


class DeveloperUser(HttpUser):
    """Utilisateur développeur"""

    tasks = [AthaliaAPIUser, AthaliaCLIUser]
    weight = 1


class AdminUser(HttpUser):
    """Utilisateur administrateur"""

    tasks = [AthaliaAPIUser, AthaliaDashboardUser, AthaliaCLIUser]
    weight = 1
