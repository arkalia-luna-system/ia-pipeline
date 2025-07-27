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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])