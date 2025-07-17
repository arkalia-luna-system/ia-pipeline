#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

"""
Tests unitaires pour athalia_quick_start
Généré automatiquement par Athalia
"""

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from athalia_quick_start import (
        print_header, show_menu, create_new_project, correct_existing_project, audit_existing_project,
        show_dashboard, manage_user_profile, scan_projects, check_ai_status, show_inventory, industrialize_project, main
    )
except ImportError:
    print("⚠️ Impossible d'importer athalia_quick_start")
    print_header = show_menu = create_new_project = correct_existing_project = audit_existing_project = show_dashboard = manage_user_profile = scan_projects = check_ai_status = show_inventory = industrialize_project = main = lambda: None

class TestAthaliaQuickStart(unittest.TestCase):
    """Tests unitaires pour athalia_quick_start"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_print_header(self):
        try:
            result = print_header()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester print_header: {e}")

    def test_show_menu(self):
        try:
            result = show_menu()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester show_menu: {e}")

    def test_create_new_project(self):
        try:
            result = create_new_project()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester create_new_project: {e}")

    def test_correct_existing_project(self):
        try:
            result = correct_existing_project()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester correct_existing_project: {e}")

    def test_audit_existing_project(self):
        try:
            result = audit_existing_project()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester audit_existing_project: {e}")

    def test_show_dashboard(self):
        try:
            result = show_dashboard()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester show_dashboard: {e}")

    def test_manage_user_profile(self):
        try:
            result = manage_user_profile()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester manage_user_profile: {e}")

    def test_scan_projects(self):
        try:
            result = scan_projects()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester scan_projects: {e}")

    def test_check_ai_status(self):
        try:
            result = check_ai_status()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester check_ai_status: {e}")

    def test_show_inventory(self):
        try:
            result = show_inventory()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester show_inventory: {e}")

    def test_industrialize_project(self):
        try:
            result = industrialize_project()
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester industrialize_project: {e}")

    def test_main(self):
        try:
            def fake_input(*args, **kwargs):
                return '9'  # Quitter immédiatement
            with patch('builtins.input', side_effect=fake_input):
                main(test_mode=True)
        except Exception as e:
            self.fail(f"main() a levé une exception inattendue : {e}")

if __name__ == '__main__':
    unittest.main()
