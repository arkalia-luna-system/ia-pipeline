# Guide d'installation - athalia_core

## Vue d'ensemble

Ce guide explique comment installer et configurer athalia_core.

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
# config.yml
app:
  name: athalia_core
  debug: true
  port: 8000

database:
  url: sqlite:///app.db
  echo: false
```

## Lancement rapide

```bash
python main.py
```

---
*Généré automatiquement par Athalia* - 2025-07-19
