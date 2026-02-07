# Installation

**Guide canonique :** [Installation (USER_GUIDES)](../USER_GUIDES/INSTALLATION.md)

Ce dossier centralise le démarrage. Pour l’installation pas à pas, les prérequis et la validation, consultez le guide complet :

- **[Guide d’installation (5 min)](../USER_GUIDES/INSTALLATION.md)** — prérequis, clone, venv, validation

Racourci :

```bash
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python bin/core/athalia_unified.py --help
```
