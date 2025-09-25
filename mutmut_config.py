"""
Configuration Mutmut pour Athalia
Tests de mutation pour améliorer la qualité des tests
"""

import os


def init(mutmut_config):
    """Configuration initiale de mutmut"""
    mutmut_config.total = 0
    mutmut_config.surviving = 0
    mutmut_config.skipped = 0
    mutmut_config.killed = 0
    mutmut_config.timeout = 0
    mutmut_config.survivors = []
    mutmut_config.skipped_mutants = []
    mutmut_config.killed_mutants = []
    mutmut_config.timeout_mutants = []


def pre_mutation(context):
    """Avant chaque mutation"""
    context.filename = context.filename
    context.line = context.line
    context.index = context.index


def post_mutation(context):
    """Après chaque mutation"""
    pass


def should_skip(context):
    """Détermine si une mutation doit être ignorée"""
    # Ignorer les fichiers de test
    if "test_" in context.filename or "tests/" in context.filename:
        return True

    # Ignorer les fichiers de configuration
    if any(
        skip in context.filename for skip in ["__init__.py", "setup.py", "conftest.py"]
    ):
        return True

    # Ignorer les fichiers de documentation
    if any(skip in context.filename for skip in ["docs/", "README", ".md"]):
        return True

    return False


def timeout(context):
    """Timeout pour les tests de mutation"""
    return 60  # 60 secondes


def command(context):
    """Commande pour exécuter les tests"""
    return f"python -m pytest {context.filename} -xvs --tb=short"
