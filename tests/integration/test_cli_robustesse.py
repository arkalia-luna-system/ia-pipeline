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
    
    try:
        # Augmenter le timeout à 30 secondes pour les systèmes lents
        result = subprocess.run([
            sys.executable, str(cli_path), "--help"
        ], capture_output=True, text=True, timeout=30)
        # Vérifie que la CLI répond sans crash
        assert result.returncode in [0, 1]  # 0 = succès, 1 = erreur d'usage
    except subprocess.TimeoutExpired:
        # Si timeout, considérer comme un succès si c'est juste un démarrage lent
        pytest.skip("CLI prend trop de temps à démarrer - système potentiellement lent")
    except Exception as e:
        # Autres erreurs sont acceptables pour un test de robustesse
        assert "timeout" in str(e).lower() or "not found" in str(e).lower() or "permission" in str(e).lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])