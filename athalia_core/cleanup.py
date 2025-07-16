import os
import shutil
import fnmatch
import logging

def clean_old_tests_and_caches(outdir):
    """
    Supprime les anciens fichiers de test non-suffixés et les caches Python dans le projet cible.
    Log chaque suppression pour audit.
    """
    for root, dirs, files in os.walk(outdir):
        # Suppression des fichiers de test non-suffixés
        if os.path.basename(root) == 'tests':
            for f in files:
                if fnmatch.fnmatch(f, 'test_*.py') and not any(f.endswith(suffix) for suffix in ['_booster_ia.py', '_import_github_issues.py']) and '_' not in f[len('test_'):-3]:
                    try:
                        os.remove(os.path.join(root, f))
                        logging.info(f"Suppression fichier de test obsolète : {os.path.join(root, f)}")
                    except Exception as e:
                        logging.warning(f"Erreur suppression {os.path.join(root, f)} : {e}")
        # Suppression des fichiers .pyc
        for f in files:
            if f.endswith('.pyc'):
                try:
                    os.remove(os.path.join(root, f))
                    logging.info(f"Suppression .pyc : {os.path.join(root, f)}")
                except Exception as e:
                    logging.warning(f"Erreur suppression .pyc {os.path.join(root, f)} : {e}")
        # Suppression des dossiers __pycache__
        for d in dirs:
            if d == '__pycache__':
                try:
                    shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                    logging.info(f"Suppression __pycache__ : {os.path.join(root, d)}")
                except Exception as e:
                    logging.warning(f"Erreur suppression __pycache__ {os.path.join(root, d)} : {e}")
