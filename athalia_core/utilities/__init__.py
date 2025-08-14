"""
Module d'utilitaires pour Athalia
CLI, dashboard, logging, édition multi-fichiers, onboarding et gestion de projets
"""

try:
    from .cli import CLI
except ImportError:
    CLI = None

try:
    from .dashboard import Dashboard
except ImportError:
    Dashboard = None

try:
    from .generation_backup import GenerationBackup
except ImportError:
    GenerationBackup = None

try:
    from .generation_simple import GenerationSimple
except ImportError:
    GenerationSimple = None

try:
    from .logger_advanced import LoggerAdvanced
except ImportError:
    LoggerAdvanced = None

try:
    from .multi_file_editor import MultiFileEditor
except ImportError:
    MultiFileEditor = None

try:
    from .onboarding import Onboarding
except ImportError:
    Onboarding = None

try:
    from .project_importer import ProjectImporter
except ImportError:
    ProjectImporter = None

try:
    from .ready_check import ReadyCheck
except ImportError:
    ReadyCheck = None

__all__ = [
    "CLI",
    "Dashboard",
    "GenerationBackup",
    "GenerationSimple",
    "LoggerAdvanced",
    "MultiFileEditor",
    "Onboarding",
    "ProjectImporter",
    "ReadyCheck",
]
