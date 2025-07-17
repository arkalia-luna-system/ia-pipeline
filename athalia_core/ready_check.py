import os

def check_ready(project_path: str) -> dict:
    """Vérifie la conformité d'un projet généré (fichiers clés, modules, tests)."""
    required_files = ["README.md", "DOC.md", "requirements.txt"]
    required_dirs = ["tests"]
    report = {"ready": True, "missing": []}
    for f in required_files:
        if not os.path.isfile(os.path.join(project_path, f)):
            report["missing"].append(f)
    for d in required_dirs:
        if not os.path.isdir(os.path.join(project_path, d)):
            report["missing"].append(d + "/")
    report["ready"] = len(report["missing"]) == 0
    return report 