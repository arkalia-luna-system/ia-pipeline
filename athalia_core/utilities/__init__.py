"""Module utilities pour Athalia"""

from typing import Any

try:
    from .cli import CLI
except ImportError:
    CLI = None

try:
    from .dashboard import Dashboard
except ImportError:
    Dashboard: Any = None

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
    MultiFileEditor: Any = None

try:
    from .onboarding import Onboarding
except ImportError:
    Onboarding = None

try:
    from .project_importer import ProjectImporter
except ImportError:
    ProjectImporter: Any = None

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
