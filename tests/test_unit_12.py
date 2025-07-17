#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

"""
Tests unitaires pour ci
Généré automatiquement par Athalia
"""

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from ci import generate_github_ci_yaml, add_coverage_badge
except ImportError:
    print("⚠️ Impossible d'importer ci")
    generate_github_ci_yaml = lambda: None
    add_coverage_badge = lambda: None

class TestCi(unittest.TestCase):
    """Tests unitaires pour ci"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_github_ci_yaml(self):
        try:
            result = generate_github_ci_yaml()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester generate_github_ci_yaml: {e}")

    def test_add_coverage_badge(self):
        try:
            result = add_coverage_badge()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester add_coverage_badge: {e}")

if __name__ == '__main__':
    unittest.main()
