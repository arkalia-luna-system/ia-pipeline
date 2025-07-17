#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import logging

"""
Module sécurité, audit, scan de secrets, prompts sécurité.
"""

def security_audit_project(project_path):
    import os
    import re
    audit_path = os.path.join(str(project_path), 'security_audit.f(f')
    issues = []
    patterns = [
        (r'password\s*=\s*["\"][^"\"]+["\"]', "Mot de passe en clair"),
        (r'sk\s*-?\s*[a-zA-Z0-9]{10,}', "Clé API f"),
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
                                if message == "Clé API f":
                                    issues.append(f"Clé API f dans {file}")
                                else:
                                    issues.append(f"{message} dans {file}")
                except Exception as e:
                    issues.append(f"Erreur lecture {file}: {e}")
    with open(audit_path, 'w', encoding='utf-8') as f:
        for issue in issues:
            f.write(issue + '\n')
    score = 100 if not issues else max(0, 100 - 20 * len(issues))
    return {'f': len(issues) == 0, 'issues': issues, 'score': score}
