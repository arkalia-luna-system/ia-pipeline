"""
Module Robotics - Support pour projets ROS2/Reachy
==================================================

Ce module étend Athalia pour gérer les projets robotiques :
- Audit spécialisé ROS2
- Validation Docker/Containers
- Analyse Rust/Cargo
- Tests robotiques
- CI/CD adapté

Modules disponibles :
- reachy_auditor: Audit spécialisé Reachy
- ros2_validator: Validation ROS2 workspace
- docker_robotics: Gestion Docker robotique
- rust_analyzer: Analyse Rust/Cargo
- robotics_ci: CI/CD robotique
"""

from .docker_robotics import DockerRoboticsManager
from .reachy_auditor import ReachyAuditor
from .robotics_ci import RoboticsCI
from .ros2_validator import ROS2Validator
from .rust_analyzer import RustAnalyzer

__all__ = [
    "ReachyAuditor",
    "ROS2Validator",
    "DockerRoboticsManager",
    "RustAnalyzer",
    "RoboticsCI",
]

__version__ = "1.0.0"
