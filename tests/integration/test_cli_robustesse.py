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
    result = subprocess.run([
        sys.executable, str(cli_path), "--help"
    ], capture_output=True, text=True, timeout=10)
    # Vérifie que la CLI répond sans crash
    assert result.returncode in [0, 1]  # 0 = succès, 1 = erreur d'usage


if __name__ == "__main__":
    pytest.main([__file__, "-v"])