#!/usr/bin/env python3
"""
Protection contre la création automatique de fichiers de tests
⚠️ DÉSACTIVÉE TEMPORAIREMENT pour éviter la suppression de tests légitimes
"""

from pathlib import Path


def _protect_test_directory():
    """Protège le répertoire tests contre la création automatique de fichiers."""
    # ⚠️ PROTECTION DÉSACTIVÉE TEMPORAIREMENT
    # Le système supprimait des tests légitimes
    print("🛡️ Protection automatique des tests DÉSACTIVÉE")
    print("⚠️ Les fichiers de tests ne seront plus supprimés automatiquement")
    return

    test_dir = Path(__file__).parent

    # Liste des fichiers de tests autorisés
    allowed_files = {
        "__init__.py",
        "__pycache__",
        ".pytest_cache",
        "test_*_complete.py",  # Nos vrais tests
        "test_*.py",  # Tests existants
    }

    # Vérifier les fichiers récents
    for file_path in test_dir.iterdir():
        if file_path.is_file():
            filename = file_path.name

            # Bloquer les fichiers de tests automatiques
            if (
                filename.startswith("test_unit_")
                or filename.startswith("test_integration_")
                or filename.startswith("test_performance_")
            ):
                # Vérifier si c'est un de nos vrais tests
                if not any(
                    pattern.replace("*", "") in filename for pattern in allowed_files
                ):
                    print(
                        "🚫 BLOCAGE: Suppression du fichier de test automatique: "
                        f"{filename}"
                    )
                    try:
                        file_path.unlink()
                    except Exception as e:
                        print(f"❌ Erreur lors de la suppression: {e}")


# Exécuter la protection au chargement du module
_protect_test_directory()
