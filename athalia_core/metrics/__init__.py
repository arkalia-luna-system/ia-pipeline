#!/usr/bin/env python3
"""
Athalia Core Metrics Module
==========================

Module de collecte et d'analyse des métriques du projet Athalia.
Fournit des métriques fiables et automatiques pour le tableau de bord.

Classes principales:
    - MetricsCollector: Collecte des métriques du projet
    - MetricsExporter: Export des métriques en différents formats
    - MetricsValidator: Validation des métriques collectées

Usage:
    from athalia_core.metrics import MetricsCollector

    collector = MetricsCollector(project_root=".")
    metrics = collector.collect_all_metrics()
    print(f"Python files: {metrics['python_files']['count']}")
"""

from .collector import MetricsCollector
from .exporter import MetricsExporter
from .validator import MetricsValidator

__all__ = ["MetricsCollector", "MetricsExporter", "MetricsValidator"]

__version__ = "1.0.0"
__author__ = "Athalia Development Team"
