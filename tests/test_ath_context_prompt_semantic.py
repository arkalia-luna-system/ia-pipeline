import subprocess
import os
import logging
from datetime import datetime

dir_path = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(dir_path, '../logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f'test_ath_context_prompt_semantic_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

SCRIPT_PATH = os.path.abspath(os.path.join(dir_path, '../agents/ath_context_prompt.py'))
TEST_FILE = os.path.abspath(os.path.join(dir_path, '../test_context/security_vuln.py'))

if __name__ == "__main__":
    result = subprocess.run(['python3', SCRIPT_PATH, TEST_FILE], capture_output=True, text=True)
    logging.info(result.stdout)
    assert "Analyse sécurité" in result.stdout, "Le prompt sécurité n'a pas été détecté par l'analyse sémantique/custom."
    print("Test sémantique/custom passé.") 