#!/usr/bin/env python3
"""
Athalia Core Metrics Exporter
=============================

Module d'export des métriques en différents formats.
Supporte JSON, Markdown, HTML et CSV.
"""

import csv
import json
from pathlib import Path
from typing import Any, Optional


class MetricsExporter:
    """
    Exporteur de métriques en différents formats.

    Supporte l'export en :
    - JSON (format complet)
    - Markdown (pour README)
    - HTML (pour dashboards)
    - CSV (pour analyse)
    """

    def __init__(self, metrics_data: dict[str, Any]) -> None:
        """
        Initialise l'exporteur avec les données de métriques.

        Args:
            metrics_data: Données des métriques à exporter
        """
        self.metrics_data = metrics_data

    def export_json(self, output_file: str) -> bool:
        """
        Exporte en format JSON.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(self.metrics_data, f, indent=2, ensure_ascii=False)

            return True

        except (OSError, TypeError) as e:
            print(f"Erreur lors de l'export JSON: {e}")
            return False

    def export_markdown_summary(self, output_file: str) -> bool:
        """
        Exporte un résumé en format Markdown pour le README.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            summary = self.metrics_data.get("summary", {})
            collection_info = self.metrics_data.get("collection_info", {})

            content = f"""## 🎯 **Core Metrics** *(Automatically Updated)*

<div align="center">

| **Component** | **Value** | **Status** | **Verified** |
|:-------------:|:---------:|:----------:|:------------:|
| **🐍 Python Files** | `{summary.get("total_python_files", 0):,} modules` | ![Active](https://img.shields.io/badge/status-active-brightgreen) | ✅ **COUNTED** |
| **📝 Lines of Code** | `{summary.get("lines_of_code", 0):,} lines` | ![Maintained](https://img.shields.io/badge/status-maintained-blue) | ✅ **MEASURED** |
| **🧪 Tests** | `{summary.get("collected_tests", 0):,} tests` | ![Tested](https://img.shields.io/badge/status-tested-green) | ✅ **COLLECTED** |
| **🛡️ Security Commands** | `{summary.get("security_commands", 0)} validated` | ![Secure](https://img.shields.io/badge/status-secure-green) | ✅ **TESTED** |
| **📊 HTML Dashboards** | `{summary.get("html_dashboards", 0)} functional` | ![Ready](https://img.shields.io/badge/status-ready-orange) | ✅ **VERIFIED** |
| **🔧 Utility Scripts** | `{summary.get("utility_scripts", 0)} tools` | ![Available](https://img.shields.io/badge/status-available-purple) | ✅ **LISTED** |
| **📚 Documentation** | `{summary.get("documentation_files", 0)} files` | ![Complete](https://img.shields.io/badge/status-complete-yellow) | ✅ **ORGANIZED** |

</div>

*Metrics collected automatically on {collection_info.get("collection_date", "Unknown")} by [Athalia Metrics Collector](data/metrics.json)*
"""

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            return True

        except OSError as e:
            print(f"Erreur lors de l'export Markdown: {e}")
            return False

    def export_full_markdown(self, output_file: str) -> bool:
        """
        Exporte un rapport complet en format Markdown.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            summary = self.metrics_data.get("summary", {})
            collection_info = self.metrics_data.get("collection_info", {})
            python_data = self.metrics_data.get("python_files", {})
            test_data = self.metrics_data.get("tests", {})
            doc_data = self.metrics_data.get("documentation", {})
            dashboard_data = self.metrics_data.get("dashboards", {})
            script_data = self.metrics_data.get("scripts", {})
            security_data = self.metrics_data.get("security", {})

            content = f"""# Athalia Project Metrics Report

**Generated on:** {collection_info.get("collection_date", "Unknown")}
**Collector version:** {collection_info.get("collector_version", "Unknown")}
**Python version:** {collection_info.get("python_version", "Unknown")}

## 🎯 Executive Summary

| **Metric** | **Value** |
|:-----------|:---------:|
| **Total Python Files** | {summary.get("total_python_files", 0):,} |
| **Core Python Files** | {summary.get("core_python_files", 0):,} |
| **Lines of Code** | {summary.get("lines_of_code", 0):,} |
| **Test Files** | {summary.get("test_files", 0):,} |
| **Collected Tests** | {summary.get("collected_tests", 0):,} |
| **Documentation Files** | {summary.get("documentation_files", 0):,} |
| **HTML Dashboards** | {summary.get("html_dashboards", 0):,} |
| **Utility Scripts** | {summary.get("utility_scripts", 0):,} |
| **Security Commands** | {summary.get("security_commands", 0):,} |

## 📊 Detailed Analysis

### 🐍 Python Code Metrics

- **Total Python files:** {python_data.get("count", 0):,}
- **Core application files:** {python_data.get("core_files", 0):,}
- **Test files:** {python_data.get("test_files", 0):,}
- **Total lines of code:** {python_data.get("total_lines", 0):,}

### 🧪 Testing Metrics

- **Test files found:** {test_data.get("test_files_count", 0):,}
- **Test directories:** {test_data.get("test_directories_count", 0):,}
- **Tests collected by pytest:** {test_data.get("collected_tests_count", 0):,}

### 📚 Documentation Metrics

- **Total documentation files:** {doc_data.get("total_files", 0):,}
- **Markdown files:** {doc_data.get("by_format", {}).get("md", 0):,}
- **YAML files:** {doc_data.get("by_format", {}).get("yaml", 0) + doc_data.get("by_format", {}).get("yml", 0):,}
- **Text files:** {doc_data.get("by_format", {}).get("txt", 0):,}

### 📊 Dashboard Metrics

- **HTML dashboards:** {dashboard_data.get("html_dashboards", 0):,}

### 🔧 Script Metrics

- **Total utility scripts:** {script_data.get("total_scripts", 0):,}
- **Python scripts:** {script_data.get("by_type", {}).get("py", 0):,}
- **Shell scripts:** {script_data.get("by_type", {}).get("sh", 0):,}

### 🛡️ Security Metrics

- **Validated security commands:** {security_data.get("validated_commands", 0):,}

## 📈 Quality Indicators

### Test Coverage Ratio
- **Test files vs Core files:** {(test_data.get("test_files_count", 0) / max(python_data.get("core_files", 1), 1)):.2f}
- **Tests per core file:** {(test_data.get("collected_tests_count", 0) / max(python_data.get("core_files", 1), 1)):.2f}

### Documentation Coverage
- **Doc files vs Python files:** {(doc_data.get("total_files", 0) / max(python_data.get("count", 1), 1)):.2f}

## 🔍 Collection Details

- **Project root:** `{self.metrics_data.get("project_root", "Unknown")}`
- **Collection timestamp:** `{self.metrics_data.get("timestamp", "Unknown")}`
- **Excluded patterns:** Cache, virtual environments, build artifacts

---

*This report was generated automatically by the Athalia Metrics Collector.*
*For the latest metrics, see: [`data/metrics.json`](../data/metrics.json)*
"""

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            return True

        except OSError as e:
            print(f"Erreur lors de l'export Markdown complet: {e}")
            return False

    def export_csv(self, output_file: str) -> bool:
        """
        Exporte les métriques principales en format CSV.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            summary = self.metrics_data.get("summary", {})
            collection_info = self.metrics_data.get("collection_info", {})

            # Préparer les données pour CSV
            rows = [
                ["metric", "value", "collection_date"],
                [
                    "total_python_files",
                    summary.get("total_python_files", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "core_python_files",
                    summary.get("core_python_files", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "lines_of_code",
                    summary.get("lines_of_code", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "test_files",
                    summary.get("test_files", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "collected_tests",
                    summary.get("collected_tests", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "documentation_files",
                    summary.get("documentation_files", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "html_dashboards",
                    summary.get("html_dashboards", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "utility_scripts",
                    summary.get("utility_scripts", 0),
                    collection_info.get("collection_date", ""),
                ],
                [
                    "security_commands",
                    summary.get("security_commands", 0),
                    collection_info.get("collection_date", ""),
                ],
            ]

            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(rows)

            return True

        except OSError as e:
            print(f"Erreur lors de l'export CSV: {e}")
            return False

    def export_html_dashboard(self, output_file: str) -> bool:
        """
        Exporte un dashboard HTML interactif.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            summary = self.metrics_data.get("summary", {})
            collection_info = self.metrics_data.get("collection_info", {})

            html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Athalia Project Metrics Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .metric-card {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            border-left: 4px solid #667eea;
            transition: transform 0.2s;
        }}
        .metric-card:hover {{
            transform: translateY(-2px);
        }}
        .metric-title {{
            font-size: 0.9em;
            color: #666;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .metric-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }}
        .metric-description {{
            font-size: 0.9em;
            color: #666;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e9ecef;
        }}
        .status-badge {{
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Athalia Project Metrics</h1>
            <p>Generated on {collection_info.get("collection_date", "Unknown")}</p>
        </div>

        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">🐍 Python Files</div>
                <div class="metric-value">{summary.get("total_python_files", 0):,}</div>
                <div class="metric-description">Total modules in the project <span class="status-badge">COUNTED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">📝 Lines of Code</div>
                <div class="metric-value">{summary.get("lines_of_code", 0):,}</div>
                <div class="metric-description">Total lines across all Python files <span class="status-badge">MEASURED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">🧪 Tests</div>
                <div class="metric-value">{summary.get("collected_tests", 0):,}</div>
                <div class="metric-description">Tests collected by pytest <span class="status-badge">COLLECTED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">🛡️ Security Commands</div>
                <div class="metric-value">{summary.get("security_commands", 0)}</div>
                <div class="metric-description">Validated security commands <span class="status-badge">TESTED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">📊 HTML Dashboards</div>
                <div class="metric-value">{summary.get("html_dashboards", 0)}</div>
                <div class="metric-description">Functional dashboard files <span class="status-badge">VERIFIED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">🔧 Utility Scripts</div>
                <div class="metric-value">{summary.get("utility_scripts", 0)}</div>
                <div class="metric-description">Available automation tools <span class="status-badge">LISTED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">📚 Documentation</div>
                <div class="metric-value">{summary.get("documentation_files", 0)}</div>
                <div class="metric-description">Documentation files <span class="status-badge">ORGANIZED</span></div>
            </div>

            <div class="metric-card">
                <div class="metric-title">📁 Core Files</div>
                <div class="metric-value">{summary.get("core_python_files", 0)}</div>
                <div class="metric-description">Core application modules <span class="status-badge">ANALYZED</span></div>
            </div>
        </div>

        <div class="footer">
            <p>
                🤖 <strong>Automatically generated</strong> by Athalia Metrics Collector v{collection_info.get("collector_version", "Unknown")}
                <br>
                📊 For detailed metrics, see <a href="../data/metrics.json">data/metrics.json</a>
            </p>
        </div>
    </div>

    <script>
        // Auto-refresh every 5 minutes if this is viewed in a live environment
        setTimeout(() => {{
            if (confirm('Update metrics dashboard?')) {{
                window.location.reload();
            }}
        }}, 300000);
    </script>
</body>
</html>"""

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            return True

        except OSError as e:
            print(f"Erreur lors de l'export HTML: {e}")
            return False
