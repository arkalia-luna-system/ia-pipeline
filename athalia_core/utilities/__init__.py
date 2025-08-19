"""Module utilities pour Athalia"""

from typing import Any

try:
    from .cli import cli as CLI
except ImportError:
    pass

try:
    from .dashboard import Dashboard
except ImportError:
    pass

try:
    from .generation_backup import generate_project as GenerationBackup
except ImportError:
    pass

try:
    from .generation_simple import generate_project as GenerationSimple
except ImportError:
    pass

try:
    from .logger_advanced import AthaliaLogger as LoggerAdvanced
except ImportError:
    pass

try:
    from .multi_file_editor import MultiFileEditor
except ImportError:
    pass

try:
    from .onboarding import generate_onboarding_md as Onboarding
except ImportError:
    pass

try:
    from .project_importer import ProjectImporter
except ImportError:
    pass

try:
    from .ready_check import check_ready as ReadyCheck
except ImportError:
    pass

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
