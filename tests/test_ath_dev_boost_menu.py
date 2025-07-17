#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from datetime import datetime
import logging
import subprocess


# Configuration du log
dir_path = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(dir_path, '../logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f'test_ath_dev_boost_menu_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

SCRIPT_PATH = os.path.abspath(os.path.join(dir_path, '../setup/ath-dev-boost.sh'))

MENU_INPUTS = [
    ('1\n', 'débogage'),
    ('2\n', 'fun'),
    ('3\n', 'design'),
    ('4\n', 'tests'),
    ('5\n', 'refactorisation'),
]

def run_menu_test(user_input, expected):
    result = subprocess.run(['bash', SCRIPT_PATH], input=user_input, capture_output=True, text=True)
    logging.info(f"Menu test input {user_input.strip()}:\n{result.stdout}")
    assert expected in result.stdout.lower(), f"Prompt attendu non trouvé pour menu choix {user_input.strip()}"

if __name__ == "__main__":
    try:
        for user_input, expected in MENU_INPUTS:
            run_menu_test(user_input, expected)
        logging.info("Tous les tests du menu interactif ath-dev-boost sont passés.")
    except AssertionError as e:
        logging.error(f"Erreur : {e}")
        exit(1)