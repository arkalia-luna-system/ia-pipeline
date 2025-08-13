#!/usr/bin/env python3
"""
Module d'analytics Athalia
"""

from .advanced_analytics import AdvancedAnalytics
from .analytics import (
    AnalyticsEngine,
    analyze_project_metrics,
    generate_analytics_report,
)

__all__ = [
    "AnalyticsEngine",
    "AdvancedAnalytics",
    "analyze_project_metrics",
    "generate_analytics_report",
]
