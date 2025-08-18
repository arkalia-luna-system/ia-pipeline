"""Module utilities pour Athalia"""

from typing import Any

try:
    from .cli import cli as CLI
except ImportError:
    CLI: Any = None

try:
    from .dashboard import Dashboard
except ImportError:
    Dashboard: Any = None

try:
    from .generation_backup import generate_project as GenerationBackup
except ImportError:
    GenerationBackup: Any = None

try:
    from .generation_simple import generate_project as GenerationSimple
except ImportError:
    GenerationSimple: Any = None

try:
    from .logger_advanced import AthaliaLogger as LoggerAdvanced
except ImportError:
    LoggerAdvanced: type[Any] = type("LoggerAdvancedFallback", (), {})

try:
    from .multi_file_editor import MultiFileEditor
except ImportError:
    MultiFileEditor: type[Any] = type("MultiFileEditorFallback", (), {})

try:
    from .onboarding import generate_onboarding_md as Onboarding
except ImportError:
    Onboarding: Any = None

try:
    from .project_importer import ProjectImporter
except ImportError:
    ProjectImporter: type[Any] = type("ProjectImporterFallback", (), {})

try:
    from .ready_check import check_ready as ReadyCheck
except ImportError:
    ReadyCheck: Any = None

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
