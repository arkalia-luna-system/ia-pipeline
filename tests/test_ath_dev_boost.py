import subprocess
import os
import logging
from datetime import datetime

# Configuration du log
dir_path = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(dir_path, '../logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f'test_ath_dev_boost_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

SCRIPT_PATH = os.path.abspath(os.path.join(dir_path, '../setup/ath-dev-boost.sh'))

TESTS = [
    (['debug'], 'débogage'),
    (['ux'], 'fun'),
    (['design'], 'design'),
    (['test'], 'tests'),
    (['refactor'], 'refactorisation'),
]

def run_test(args, expected):
    result = subprocess.run(['bash', SCRIPT_PATH] + args, capture_output=True, text=True)
    logging.info(f"Test {args}:\n{result.stdout}")
    assert expected in result.stdout.lower(), f"Prompt attendu non trouvé pour {args}"

if __name__ == "__main__":
    try:
        for args, expected in TESTS:
            run_test(args, expected)
        print("Tous les tests ath-dev-boost sont passés.")
        logging.info("Tous les tests ath-dev-boost sont passés.")
    except AssertionError as e:
        print(f"Erreur : {e}")
        logging.error(f"Erreur : {e}")
        exit(1) 