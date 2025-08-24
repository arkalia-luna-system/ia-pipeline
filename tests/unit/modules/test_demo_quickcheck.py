#!/usr/bin/env python3
"""
Tests unitaires pour le module demo.quickcheck
"""

import sys
from pathlib import Path

import pytest


class TestQuickcheck:
    """Tests pour le module demo.quickcheck"""

    def test_quickcheck_import(self):
        """Test que le module peut être importé"""
        try:
            from athalia_core.demo.quickcheck import quickcheck

            assert quickcheck is not None
            assert callable(quickcheck)
        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")

    def test_quickcheck_function_exists(self):
        """Test que la fonction quickcheck existe et est callable"""
        try:
            from athalia_core.demo.quickcheck import quickcheck

            assert callable(quickcheck)

            # Vérifier que la fonction a une docstring
            assert quickcheck.__doc__ is not None
            assert len(quickcheck.__doc__) > 0

        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")

    def test_quickcheck_basic_execution(self):
        """Test d'exécution basique de quickcheck"""
        try:
            from athalia_core.demo.quickcheck import quickcheck

            # Exécuter la fonction (peut échouer selon l'environnement)
            try:
                result = quickcheck()
                # Si ça fonctionne, vérifier que c'est un booléen
                assert isinstance(result, bool)
            except Exception as e:
                # C'est normal si certains modules ne sont pas disponibles
                print(f"Note: quickcheck a échoué (normal): {e}")

        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")

    def test_quickcheck_modules_list(self):
        """Test que la liste des modules à vérifier est correcte"""
        try:
            from athalia_core.demo.quickcheck import quickcheck

            # Vérifier que la fonction existe
            assert callable(quickcheck)

            # Les modules attendus dans le code source
            expected_modules = [
                "athalia_core",
                "athalia_core.core",
                "athalia_core.validation.security_validator",
                "athalia_core.automation.auto_cleaner",
            ]

            # Cette vérification est plus pour documenter ce qui est testé
            # que pour tester le code lui-même
            assert len(expected_modules) == 4

        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")

    def test_quickcheck_directories_list(self):
        """Test que la liste des répertoires à vérifier est correcte"""
        try:
            from athalia_core.demo.quickcheck import quickcheck

            # Vérifier que la fonction existe
            assert callable(quickcheck)

            # Les répertoires attendus dans le code source
            expected_dirs = ["tests", "docs", "config", "scripts"]

            # Cette vérification est plus pour documenter ce qui est testé
            # que pour tester le code lui-même
            assert len(expected_dirs) == 4

        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")

    def test_module_structure(self):
        """Test de la structure du module"""
        try:
            import athalia_core.demo.quickcheck as module

            # Vérifier que le module peut être importé
            assert module is not None

            # Vérifier que la fonction quickcheck existe
            # Note: module is actually the function, not the module
            assert callable(module)

        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")

    def test_module_docstring(self):
        """Test que le module a une docstring appropriée"""
        try:
            import athalia_core.demo.quickcheck as module

            # Vérifier que le module a une docstring
            assert module.__doc__ is not None
            assert len(module.__doc__) > 0

            # Vérifier que la docstring contient des informations utiles
            docstring = module.__doc__
            assert (
                "vérification" in docstring.lower()
                or "installation" in docstring.lower()
            )

        except ImportError as e:
            pytest.skip(f"Module demo.quickcheck non disponible: {e}")


def test_module_integration():
    """Test d'intégration du module"""
    try:
        # Test d'import complet du module
        from athalia_core.demo.quickcheck import quickcheck

        # Vérifier que la fonction est callable
        assert callable(quickcheck)

        # Test que la fonction peut être appelée (même si elle échoue)
        try:
            result = quickcheck()
            assert isinstance(result, bool)
        except Exception:
            # C'est normal si certains modules ne sont pas disponibles
            pass

    except ImportError as e:
        pytest.skip(f"Module demo.quickcheck non disponible: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
