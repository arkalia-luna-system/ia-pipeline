"""Module utilities pour Athalia"""

from typing import Any

try:
    from .cli import cli as CLI
except ImportError:
    CLI: type[Any] = type("CLIFallback", (), {})

try:
    from .dashboard import Dashboard
except ImportError:
    Dashboard: type[Any] = type("DashboardFallback", (), {})

try:
    from .generation_backup import generate_project as GenerationBackup
except ImportError:
    GenerationBackup: type[Any] = type("GenerationBackupFallback", (), {})

try:
    from .generation_simple import generate_project as GenerationSimple
except ImportError:
    GenerationSimple: type[Any] = type("GenerationSimpleFallback", (), {})

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
    Onboarding: type[Any] = type("OnboardingFallback", (), {})

try:
    from .project_importer import ProjectImporter
except ImportError:
    ProjectImporter: type[Any] = type("ProjectImporterFallback", (), {})

try:
    from .ready_check import check_ready as ReadyCheck
except ImportError:
    ReadyCheck: type[Any] = type("ReadyCheckFallback", (), {})

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
