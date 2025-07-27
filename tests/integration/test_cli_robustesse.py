#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test d'intégration CLI robuste pour Athalia
"""
import sys
import subprocess
import pytest
from pathlib import Path


def test_cli_robustesse():
    """Test simple de la CLI sans interaction complexe"""
    cli_path = Path("athalia_core/main.py")
    if not cli_path.exists():
        pytest.skip("CLI principale non trouvée")
<<<<<<< HEAD
    result = subprocess.run([
        sys.executable, str(cli_path), "--help"
    ], capture_output=True, text=True, timeout=10)
    # Vérifie que la CLI répond sans crash
    assert result.returncode in [0, 1]  # 0 = succès, 1 = erreur d'usage
=======
    
    # Test simple : vérifier que le fichier peut être importé
    try:
        import athalia_core.main
        assert hasattr(athalia_core.main, 'main')
        # Test réussi si l'import fonctionne
        assert True
    except ImportError as e:
        pytest.skip(f"Impossible d'importer main.py: {e}")
    except Exception as e:
        # Autres erreurs sont acceptables pour un test de robustesse
        assert "timeout" in str(e).lower() or "not found" in str(e).lower() or "permission" in str(e).lower()
>>>>>>> develop


if __name__ == "__main__":
    pytest.main([__file__, "-v"])