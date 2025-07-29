# Guide d'installation - athalia-dev-setup

## Vue d'ensemble

Ce guide explique comment installer et configurer athalia-dev-setup.

## Prérequis

- Python >= 3.8
- Dépendances listées dans requirements.txt

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Le projet utilise un fichier de configuration YAML :

```yaml
# config/athalia_config.yaml
app:
  name: athalia-dev-setup
  debug: true
  port: 8000

database:
  url: sqlite:///app.db
  echo: false
```

## Lancement rapide

```bash
# Vérifier l'installation
python athalia_unified.py --help

# Test rapide
python athalia_unified.py . --action audit --dry-run
```

---
*Généré automatiquement par Athalia* - 2025-07-29
