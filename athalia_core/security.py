"""
Module sécurité, audit, scan de secrets, prompts sécurité.
"""

import os
import logging
import re

def security_audit_project(outdir):
    """
    Audit sécurité du projet : scan de secrets, patterns à risque, dépendances.
    Log les résultats dans security_audit.log.
    """
    patterns = [
        (r'sk-[a-zA-Z0-9]{16,}', 'Clé API potentielle'),
        (r'password\s*=\s*["\"][^"\"]+["\"]', 'Mot de passe en dur'),
        (r'os\.system\(', 'Appel shell potentiellement risqué'),
        (r'subprocess\.run\(', 'Appel shell potentiellement risqué'),
        (r'open\(.+w', 'Ouverture fichier en écriture'),
    ]
    if not os.path.exists(outdir):
        os.makedirs(outdir, exist_ok=True)
    log_path = os.path.join(outdir, 'security_audit.log')
    with open(log_path, 'w') as log:
        for root, dirs, files in os.walk(outdir):
            for f in files:
                if f.endswith('.py'):
                    path = os.path.join(root, f)
                    try:
                        with open(path, 'r', encoding='utf-8', errors='ignore') as code:
                            content = code.read()
                        for pat, label in patterns:
                            for m in re.finditer(pat, content):
                                msg = f"[SECURITY] {label} dans {path} : {m.group(0)}"
                                log.write(msg + '\n')
                                logging.warning(msg)
                    except Exception as e:
                        logging.error(f"Erreur audit sécurité {path} : {e}")
    logging.info(f"Audit sécurité terminé pour {outdir}, voir {log_path}")
