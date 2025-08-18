"""Module utilities pour Athalia"""

from typing import Any

try:
    from .cli import cli as CLI
except ImportError:
    CLI = None

try:
    from .dashboard import Dashboard
except ImportError:
    Dashboard: Any = None

try:
    from .generation_backup import generate_project as GenerationBackup
except ImportError:
    GenerationBackup = None

try:
    from .generation_simple import generate_project as GenerationSimple
except ImportError:
    GenerationSimple = None

try:
    from .logger_advanced import AthaliaLogger as LoggerAdvanced
except ImportError:
    LoggerAdvanced = None

try:
    from .multi_file_editor import MultiFileEditor
except ImportError:
    MultiFileEditor: Any = None

try:
    from .onboarding import generate_onboarding_md as Onboarding
except ImportError:
    Onboarding = None

try:
    from .project_importer import ProjectImporter
except ImportError:
    ProjectImporter: Any = None

try:
    from .ready_check import check_ready as ReadyCheck
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
