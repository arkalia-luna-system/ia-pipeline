#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour ready_check.py
"""

import pytest
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from athalia_core.ready_check import ReadyChecker
except ImportError:
    ReadyChecker = None

def test_check_ready_ok():
    """Test que le projet est prêt"""
    if ReadyChecker is None:
        pytest.skip("Module ReadyChecker non disponible")
    
    checker = ReadyChecker(".")
    report = checker.check_ready()
    
    # Vérifier que le rapport contient les clés attendues
    assert "ready" in report or "status" in report, "Rapport invalide"
    if "ready" in report:
        assert report["ready"]
    elif "status" in report:
        assert report["status"] == "ready"

def test_check_ready_missing():
    """Test avec un projet manquant"""
    if ReadyChecker is None:
        pytest.skip("Module ReadyChecker non disponible")
    
    checker = ReadyChecker("/chemin/inexistant")
    report = checker.check_ready()
    
    # Vérifier que le rapport contient les clés attendues
    assert "ready" in report or "status" in report, "Rapport invalide"
    if "ready" in report:
        assert not report["ready"]
    elif "status" in report:
        assert report["status"] != "ready"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])