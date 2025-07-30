#!/usr/bin/env python3
import subprocess
import sys

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import validate_and_run, SecurityError
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):  # type: ignore
        return subprocess.run(command, **kwargs)
    SecurityError = Exception  # type: ignore


def main():
    # Linting simplifié - vérifier seulement les fichiers principaux
    print("🔍 Exécution du linting simplifié...")
    
    # Vérifier seulement les fichiers principaux du projet
    main_files = [
        "athalia_core/cli.py",
        "athalia_core/main.py",
        "tests/test_cli_complete.py",
        "tests/test_ci_robust.py"
    ]
    
    all_ok = True
    
    for file_path in main_files:
        try:
            result = validate_and_run([
                "flake8", 
                file_path,
                "--ignore=E128,E501,W503",
                "--max-line-length=120"
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Erreurs dans {file_path}:")
                if result.stdout:
                    print(result.stdout)
                all_ok = False
            else:
                print(f"✅ {file_path} - OK")
                
        except Exception as e:
            print(f"⚠️  Impossible de vérifier {file_path}: {e}")
            all_ok = False
    
    if all_ok:
        print("✅ Linting OK")
        sys.exit(0)
    else:
        print("❌ Erreurs de linting détectées")
        sys.exit(1)


if __name__ == "__main__":
    main()
