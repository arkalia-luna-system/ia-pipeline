#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from datetime import datetime
import logging


# Configuration du log
log_dir = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f'test_continue_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Test de présence des modèles dans la config Continue
def test_models_presence():
    config_path = os.path.expanduser('~/.continue/config.yaml')
    assert os.path.exists(config_path), f"Fichier de config introuvable : {config_path}"
    with open(config_path, 'r') as file_handle:
        content = file_handle.read()
    assert 'claude-3-sonnet-20240229' in content, "Claude 3.5 Sonnet absent de la config."
    assert 'mistral' in content, "Mistral absent de la config."
    logging.info("Présence des modèles vérifiée dans config.yaml.")

if __name__ == "__main__":
    try:
        test_models_presence()
        logging.info("Tests passés avec succès.")
    except AssertionError as e:
        logging.error(f"Erreur : {e}")
        exit(1)