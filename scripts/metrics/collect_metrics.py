#!/usr/bin/env python3
"""
Athalia Metrics Collection Script
=================================

Script principal de collecte automatique des métriques du projet Athalia.
Utilisé par la CI/CD pour générer des métriques fiables et traçables.

Usage:
    python scripts/metrics/collect_metrics.py [OPTIONS]

Options:
    --output-dir DIR    Répertoire de sortie (défaut: data/)
    --json-only         Générer seulement le fichier JSON
    --validate          Valider les métriques collectées
    --verbose           Mode verbeux
    --help              Afficher cette aide

Sorties générées:
    - data/metrics.json        : Métriques complètes en JSON
    - data/metrics.md          : Résumé pour README
    - data/metrics_full.md     : Rapport complet
    - data/metrics.csv         : Données pour analyse
    - dashboard/metrics.html   : Dashboard HTML
"""

import argparse
import sys
from pathlib import Path
from typing import Any

# Ajouter le chemin du projet pour les imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from athalia_core.metrics import MetricsCollector, MetricsExporter, MetricsValidator
except ImportError as e:
    print(f"❌ Erreur d'import des modules de métriques: {e}")
    print("📍 Assurez-vous que le module athalia_core.metrics est disponible.")
    sys.exit(1)


class MetricsCollectionScript:
    """
    Script de collecte de métriques avec interface en ligne de commande.

    Orchestre la collecte, validation et export des métriques du projet.
    """

    def __init__(self, project_root: str = ".") -> None:
        """
        Initialise le script de collecte.

        Args:
            project_root: Chemin racine du projet
        """
        self.project_root = Path(project_root).resolve()
        self.collector = MetricsCollector(str(self.project_root))
        self.validator = MetricsValidator()
        self.verbose = False

    def print_header(self) -> None:
        """Affiche l'en-tête du script."""
        print("=" * 70)
        print("🔢 ATHALIA METRICS COLLECTOR")
        print("=" * 70)
        print(f"📂 Project root: {self.project_root}")
        print("🕒 Collection starting...")
        print()

    def print_success(self, message: str) -> None:
        """Affiche un message de succès."""
        print(f"✅ {message}")

    def print_warning(self, message: str) -> None:
        """Affiche un avertissement."""
        print(f"⚠️  {message}")

    def print_error(self, message: str) -> None:
        """Affiche une erreur."""
        print(f"❌ {message}")

    def print_info(self, message: str) -> None:
        """Affiche une information en mode verbeux."""
        if self.verbose:
            print(f"ℹ️  {message}")

    def collect_metrics(self) -> dict[str, Any]:
        """
        Collecte toutes les métriques du projet.

        Returns:
            Dictionnaire avec les métriques collectées
        """
        self.print_info("Début de la collecte des métriques...")

        try:
            metrics_data = self.collector.collect_all_metrics()
            self.print_success("Collecte des métriques terminée")

            # Afficher un résumé
            summary = metrics_data.get("summary", {})
            self.print_info("Résumé des métriques collectées:")
            self.print_info(
                f"  - Fichiers Python: {summary.get('total_python_files', 0)}"
            )
            self.print_info(f"  - Lignes de code: {summary.get('lines_of_code', 0):,}")
            self.print_info(f"  - Tests collectés: {summary.get('collected_tests', 0)}")
            self.print_info(
                f"  - Documentation: {summary.get('documentation_files', 0)}"
            )

            return metrics_data

        except Exception as e:
            self.print_error(f"Erreur lors de la collecte: {e}")
            raise

    def validate_metrics(self, metrics_data: dict[str, Any]) -> bool:
        """
        Valide les métriques collectées.

        Args:
            metrics_data: Métriques à valider

        Returns:
            True si les métriques sont valides
        """
        self.print_info("Validation des métriques...")

        try:
            is_valid, errors, warnings = self.validator.validate_metrics(metrics_data)

            if errors:
                self.print_error(f"Erreurs de validation trouvées ({len(errors)}):")
                for error in errors:
                    self.print_error(f"  - {error}")

            if warnings:
                self.print_warning(f"Avertissements trouvés ({len(warnings)}):")
                for warning in warnings:
                    self.print_warning(f"  - {warning}")

            if is_valid:
                self.print_success("Validation des métriques réussie")
            else:
                self.print_error("Validation des métriques échouée")

            return is_valid

        except Exception as e:
            self.print_error(f"Erreur lors de la validation: {e}")
            return False

    def export_metrics(
        self, metrics_data: dict[str, Any], output_dir: str, json_only: bool = False
    ) -> bool:
        """
        Exporte les métriques dans différents formats.

        Args:
            metrics_data: Métriques à exporter
            output_dir: Répertoire de sortie
            json_only: Si True, génère seulement le fichier JSON

        Returns:
            True si tous les exports ont réussi
        """
        self.print_info("Export des métriques...")

        try:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            exporter = MetricsExporter(metrics_data)
            success_count = 0
            total_exports = 1 if json_only else 5

            # Export JSON (toujours généré)
            json_file = output_path / "metrics.json"
            if exporter.export_json(str(json_file)):
                self.print_success(f"JSON exporté: {json_file}")
                success_count += 1
            else:
                self.print_error(f"Échec export JSON: {json_file}")

            if not json_only:
                # Export Markdown pour README
                md_file = output_path / "metrics.md"
                if exporter.export_markdown_summary(str(md_file)):
                    self.print_success(f"Markdown résumé exporté: {md_file}")
                    success_count += 1
                else:
                    self.print_error(f"Échec export Markdown résumé: {md_file}")

                # Export Markdown complet
                full_md_file = output_path / "metrics_full.md"
                if exporter.export_full_markdown(str(full_md_file)):
                    self.print_success(f"Markdown complet exporté: {full_md_file}")
                    success_count += 1
                else:
                    self.print_error(f"Échec export Markdown complet: {full_md_file}")

                # Export CSV
                csv_file = output_path / "metrics.csv"
                if exporter.export_csv(str(csv_file)):
                    self.print_success(f"CSV exporté: {csv_file}")
                    success_count += 1
                else:
                    self.print_error(f"Échec export CSV: {csv_file}")

                # Export HTML Dashboard
                dashboard_dir = self.project_root / "dashboard"
                dashboard_dir.mkdir(exist_ok=True)
                html_file = dashboard_dir / "metrics.html"
                if exporter.export_html_dashboard(str(html_file)):
                    self.print_success(f"Dashboard HTML exporté: {html_file}")
                    success_count += 1
                else:
                    self.print_error(f"Échec export HTML: {html_file}")

            success_rate = success_count / total_exports
            if success_rate == 1.0:
                self.print_success(
                    f"Tous les exports réussis ({success_count}/{total_exports})"
                )
                return True
            elif success_rate >= 0.5:
                self.print_warning(
                    f"Exports partiellement réussis ({success_count}/{total_exports})"
                )
                return True
            else:
                self.print_error(
                    f"Échec de la majorité des exports ({success_count}/{total_exports})"
                )
                return False

        except Exception as e:
            self.print_error(f"Erreur lors de l'export: {e}")
            return False

    def run(self, args: argparse.Namespace) -> int:
        """
        Exécute le script de collecte avec les arguments donnés.

        Args:
            args: Arguments de ligne de commande

        Returns:
            Code de sortie (0 = succès, 1 = erreur)
        """
        self.verbose = args.verbose

        try:
            self.print_header()

            # Collecte des métriques
            metrics_data = self.collect_metrics()

            # Validation optionnelle
            if args.validate:
                if not self.validate_metrics(metrics_data):
                    self.print_error("Arrêt à cause d'erreurs de validation")
                    return 1

            # Export des métriques
            if not self.export_metrics(metrics_data, args.output_dir, args.json_only):
                self.print_error("Échec de l'export des métriques")
                return 1

            # Résumé final
            print()
            print("=" * 70)
            summary = metrics_data.get("summary", {})
            print("🎉 COLLECTE TERMINÉE AVEC SUCCÈS")
            print(f"📊 Fichiers Python: {summary.get('total_python_files', 0):,}")
            print(f"📝 Lignes de code: {summary.get('lines_of_code', 0):,}")
            print(f"🧪 Tests: {summary.get('collected_tests', 0):,}")
            print(f"📚 Documentation: {summary.get('documentation_files', 0):,}")
            print(f"📂 Sortie: {args.output_dir}")
            print("=" * 70)

            return 0

        except KeyboardInterrupt:
            self.print_error("Collecte interrompue par l'utilisateur")
            return 1
        except Exception as e:
            self.print_error(f"Erreur inattendue: {e}")
            if self.verbose:
                import traceback

                traceback.print_exc()
            return 1


def create_argument_parser() -> argparse.ArgumentParser:
    """
    Crée le parseur d'arguments en ligne de commande.

    Returns:
        Parser configuré
    """
    parser = argparse.ArgumentParser(
        description="Collecte automatique des métriques du projet Athalia",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python scripts/metrics/collect_metrics.py
  python scripts/metrics/collect_metrics.py --output-dir /tmp/metrics
  python scripts/metrics/collect_metrics.py --json-only --validate
  python scripts/metrics/collect_metrics.py --verbose

Fichiers générés:
  - data/metrics.json        : Données complètes en JSON
  - data/metrics.md          : Résumé pour README
  - data/metrics_full.md     : Rapport détaillé
  - data/metrics.csv         : Format tableur
  - dashboard/metrics.html   : Dashboard interactif
        """,
    )

    parser.add_argument(
        "--output-dir",
        default="data",
        help="Répertoire de sortie pour les fichiers de métriques (défaut: data)",
    )

    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Générer seulement le fichier JSON (plus rapide)",
    )

    parser.add_argument(
        "--validate", action="store_true", help="Valider les métriques collectées"
    )

    parser.add_argument("--verbose", action="store_true", help="Affichage verbeux")

    return parser


def main() -> int:
    """
    Point d'entrée principal du script.

    Returns:
        Code de sortie
    """
    parser = create_argument_parser()
    args = parser.parse_args()

    # Initialiser le script avec le répertoire racine du projet
    script = MetricsCollectionScript(str(PROJECT_ROOT))

    return script.run(args)


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
