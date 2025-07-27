#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module sécurité, audit, scan de secrets, prompts sécurité.
"""

import logging
import os
import re
from pathlib import Path
from typing import Dict, List


def security_audit_project(project_path):
    """Audit de sécurité d'un projet"""
    audit_path = Path(project_path) / 'security_audit.txt'
    issues = []
    patterns = [
        (r'password\s*=\s*["\'][^"\']+["\']', "Mot de passe en clair"),
        (r'sk\s*-?\s*[a-zA-Z0-9]{10,}', "Clé API trouvée"),
        (r'os\.system\(', "Appel système potentiellement dangereux"),
    ]

    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py') or file.endswith('.f(f'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for pattern, message in patterns:
                            if re.search(pattern, content, re.IGNORECASE):
                                if message == "Clé API trouvée":
                                    issues.append(
                                        f"Clé API trouvée dans {file}")
                                else:
                                    issues.append(f"{message} dans {file}")
                except Exception as e:
                    issues.append(f"Erreur lecture {file}: {e}")

    with open(audit_path, 'w', encoding='utf-8') as f:
        for issue in issues:
            f.write(issue + '\n')

    score = 100 if not issues else max(0, 100 - 20 * len(issues))
    is_secure = len(issues) == 0
    return {
        'secure': is_secure,
        'f': is_secure,
        'issues': issues,
        'score': score}
