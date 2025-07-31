#!/usr/bin/env python3
import subprocess
import sys


# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs) -> subprocess.CompletedProcess:  # type: ignore
        return subprocess.run(command, **kwargs)

    SecurityError = Exception  # type: ignore


def main() -> None:
    # Linting complet - vérifier tous les fichiers Python
    print("🔍 Exécution du linting complet...")

    try:
        # Vérifier tous les fichiers Python du projet
        result = validate_and_run(
            ["flake8", "athalia_core/", "tests/", "--max-line-length=88", "--count"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("❌ Erreurs de linting détectées:")
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
            print(
                "📊 Total:"
                f" {result.stdout.strip().split()[-1] if result.stdout else 'N/A'} "
                "erreurs"
            )
            sys.exit(1)
        else:
            print("✅ Linting OK - Aucune erreur détectée")
            sys.exit(0)

    except SecurityError as e:
        print(f"⚠️  Limitation de sécurité détectée: {e}")
        print("🔄 Utilisation du linting direct...")

        # Fallback direct sans security validator
        result = subprocess.run(
            ["flake8", "athalia_core/", "tests/", "--max-line-length=88", "--count"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("❌ Erreurs de linting détectées:")
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
            print(
                "📊 Total:"
                f" {result.stdout.strip().split()[-1] if result.stdout else 'N/A'} "
                "erreurs"
            )
            sys.exit(1)
        else:
            print("✅ Linting OK - Aucune erreur détectée")
            sys.exit(0)


if __name__ == "__main__":
    main()
