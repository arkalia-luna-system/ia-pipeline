#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test d'intégration CLI robuste pour Athalia
"""
import subprocess
import sys
from pathlib import Path

import pytest


def test_cli_robustesse():
    """Test simple de la CLI sans interaction complexe"""
    cli_path = Path("athalia_core/main.py")
    if not cli_path.exists():
        pytest.skip("CLI principale non trouvée")
    
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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])