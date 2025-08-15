# Makefile professionnel pour Athalia - DevOps Automation Platform
# Usage: make <target>
# Exemple: make dev, make test, make lint

.PHONY: help dev install test cov lint format types sec build bench release pages demo clean audit

# Couleurs pour une sortie professionnelle
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
BLUE := \033[0;34m
NC := \033[0m # No Color

# Configuration du projet
PYTHON := python3
PIP := pip
PROJECT_NAME := athalia-ai
VENV := .venv
ACTIVATE := source $(VENV)/bin/activate

help: ## Affiche cette aide
	@echo "$(BLUE)🔧 ATHALIA - Makefile Professionnel$(NC)"
	@echo "$(YELLOW)=====================================$(NC)"
	@echo ""
	@echo "$(GREEN)Targets disponibles:$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Exemples:$(NC)"
	@echo "  make dev      # Setup environnement de développement"
	@echo "  make test     # Lance tous les tests"
	@echo "  make lint     # Vérifie la qualité du code"
	@echo "  make format   # Formate automatiquement le code"

dev: ## Setup environnement de développement complet
	@echo "$(BLUE)🚀 Setup environnement de développement Athalia...$(NC)"
	@if [ ! -d "$(VENV)" ]; then \
		echo "$(YELLOW)📦 Création de l'environnement virtuel...$(NC)"; \
		$(PYTHON) -m venv $(VENV); \
	fi
	@echo "$(GREEN)✅ Environnement virtuel prêt$(NC)"
	@echo "$(YELLOW)📥 Installation des dépendances...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install --upgrade pip
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt
	. $(VENV)/bin/activate && $(PIP) install -e .
	@echo "$(GREEN)✅ Installation terminée !$(NC)"
	@echo "$(BLUE)💡 Pour activer: source $(VENV)/bin/activate$(NC)"

install: ## Installation rapide des dépendances
	@echo "$(YELLOW)📥 Installation des dépendances...$(NC)"
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt
	. $(VENV)/bin/activate && $(PIP) install -e .
	@echo "$(GREEN)✅ Installation terminée$(NC)"

test: ## Lance tous les tests avec couverture
	@echo "$(BLUE)🧪 Lancement des tests Athalia...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) -m pytest --cov=athalia_core --cov-report=term --cov-report=html --cov-report=xml -v
	@echo "$(GREEN)✅ Tests terminés$(NC)"

test-fast: ## Tests rapides sans couverture
	@echo "$(YELLOW)⚡ Tests rapides...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) -m pytest -q --maxfail=1 --disable-warnings
	@echo "$(GREEN)✅ Tests rapides terminés$(NC)"

cov: ## Génère le rapport de couverture
	@echo "$(BLUE)📊 Génération du rapport de couverture...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) -m pytest --cov=athalia_core --cov-report=html --cov-report=xml
	@echo "$(GREEN)✅ Rapport de couverture généré dans htmlcov/$(NC)"
	@echo "$(BLUE)🌐 Ouvre htmlcov/index.html dans ton navigateur$(NC)"

lint: ## Vérifie la qualité du code (ruff + black)
	@echo "$(BLUE)🔍 Vérification de la qualité du code...$(NC)"
	. $(VENV)/bin/activate && ruff check .
	. $(VENV)/bin/activate && black --check .
	@echo "$(GREEN)✅ Qualité du code validée$(NC)"

format: ## Formate automatiquement le code
	@echo "$(BLUE)🎨 Formatage automatique du code...$(NC)"
	. $(VENV)/bin/activate && black .
	. $(VENV)/bin/activate && ruff check . --fix
	@echo "$(GREEN)✅ Code formaté$(NC)"

types: ## Vérification des types avec mypy
	@echo "$(BLUE)🔍 Vérification des types...$(NC)"
	. $(VENV)/bin/activate && mypy athalia_core/ --ignore-missing-imports
	@echo "$(GREEN)✅ Types validés$(NC)"

sec: ## Audit de sécurité
	@echo "$(BLUE)🛡️ Audit de sécurité...$(NC)"
	. $(VENV)/bin/activate && pip-audit -r requirements.txt || true
	. $(VENV)/bin/activate && bandit -r athalia_core/ || true
	@echo "$(GREEN)✅ Audit de sécurité terminé$(NC)"

build: ## Construction du package
	@echo "$(BLUE)📦 Construction du package...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) -m build
	@echo "$(GREEN)✅ Package construit$(NC)"

bench: ## Lancement des benchmarks
	@echo "$(BLUE)⚡ Lancement des benchmarks...$(NC)"
	. $(VENV)/bin/activate && $(PYTHON) scripts/performance/run_performance_tests.py
	@echo "$(GREEN)✅ Benchmarks terminés$(NC)"

release: ## Préparation de la release
	@echo "$(BLUE)🚀 Préparation de la release...$(NC)"
	@echo "$(YELLOW)📋 Vérifications pré-release:$(NC)"
	@make lint
	@make test
	@make build
	@echo "$(GREEN)✅ Prêt pour la release !$(NC)"
	@echo "$(BLUE)💡 Crée un tag: git tag v0.1.0 && git push origin v0.1.0$(NC)"

pages: ## Génération de la documentation pour GitHub Pages
	@echo "$(BLUE)📚 Génération de la documentation...$(NC)"
	@if [ -f "mkdocs.yml" ]; then \
		. $(VENV)/bin/activate && mkdocs build; \
		echo "$(GREEN)✅ Documentation générée dans site/$(NC)"; \
	else \
		echo "$(YELLOW)⚠️  mkdocs.yml non trouvé - création d'une config basique...$(NC)"; \
		@make mkdocs-setup; \
	fi

mkdocs-setup: ## Setup MkDocs basique
	@echo "$(BLUE)📚 Setup MkDocs...$(NC)"
	. $(VENV)/bin/activate && pip install mkdocs mkdocs-material
	@echo "$(GREEN)✅ MkDocs installé$(NC)"

demo: ## Démo rapide du projet
	@echo "$(BLUE)🎯 Démo rapide d'Athalia...$(NC)"
	. $(VENV)/bin/activate && athalia --help
	@echo "$(GREEN)✅ Démo terminée$(NC)"

clean: ## Nettoyage complet
	@echo "$(BLUE)🧹 Nettoyage complet...$(NC)"
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	@echo "$(GREEN)✅ Nettoyage terminé$(NC)"

audit: ## Audit complet du projet
	@echo "$(BLUE)🔍 Audit complet d'Athalia...$(NC)"
	@echo "$(YELLOW)📊 Métriques du projet:$(NC)"
	@echo "  Python files: $(shell find . -name "*.py" | wc -l | tr -d ' ')"
	@echo "  Lines of code: $(shell find . -name "*.py" -exec wc -l {} + | tail -1 | awk '{print $$1}')"
	@echo "  Test files: $(shell find tests/ -name "*.py" | wc -l | tr -d ' ')"
	@echo "  Documentation: $(shell find docs/ -name "*.md" | wc -l | tr -d ' ')"
	@echo "$(GREEN)✅ Audit terminé$(NC)"

status: ## État du projet
	@echo "$(BLUE)📊 État du projet Athalia$(NC)"
	@echo "$(YELLOW)=====================================$(NC)"
	@echo "  🐍 Python: $(shell python3 --version 2>/dev/null || echo 'Non installé')"
	@echo "  📦 Package: $(shell pip show athalia-ai 2>/dev/null | grep Version | cut -d' ' -f2 || echo 'Non installé')"
	@echo "  🧪 Tests: $(shell find tests/ -name "*.py" | wc -l | tr -d ' ') fichiers de test"
	@echo "  📚 Docs: $(shell find docs/ -name "*.md" | wc -l | tr -d ' ') fichiers de documentation"
	@echo "  🔧 CLI: $(shell which athalia 2>/dev/null && echo '✅ Installé' || echo '❌ Non installé')"

# Target par défaut
.DEFAULT_GOAL := help
