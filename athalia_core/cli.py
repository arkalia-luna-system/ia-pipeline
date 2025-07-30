#!/usr/bin/env python3
"""
Interface CLI pour Athalia avec IA robuste.
"""

import logging
import os
import traceback
from pathlib import Path

import click
import yaml

from .ai_robust import AIModel, RobustAI
from .audit import audit_project_intelligent

# Configuration pour l'internationalisation (i18n) des messages CLI
# Utilisation de gettext pour la traduction des messages utilisateur
# Exemple: _("Message à traduire") pour les chaînes traduisibles


def generate_project(blueprint, output_path, dry_run=False):
    """Génère un projet à partir d'un blueprint"""
    try:
        if dry_run:
            click.echo("🔍 Mode simulation - Aucun fichier créé")
            return True

        # Créer la structure du projet
        project_path = Path(output_path)
        project_path.mkdir(parents=True, exist_ok=True)

        # Créer les fichiers de base
        project_name = blueprint.get("project_name", "my_project")

        # README.md
        readme_content = f"""# {project_name}

{blueprint.get('description', 'Projet généré automatiquement')}

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```python
from {project_name} import main
main()
```
"""

        with open(project_path / "README.md", "w") as f:
            f.write(readme_content)

        # requirements.txt
        dependencies = blueprint.get("dependencies", [])
        if dependencies:
            with open(project_path / "requirements.txt", "w") as f:
                f.write("\n".join(dependencies))

        # main.py
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Projet généré automatiquement
\"\"\"

def main():
    \"\"\"Fonction principale\"\"\"
    print("Hello from {project_name}!")

if __name__ == "__main__":
    main()
"""

        with open(project_path / "main.py", "w") as f:
            f.write(main_content)

        return True

    except Exception as e:
        click.echo(f"❌ Erreur lors de la génération: {e}")
        return False


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Mode verbeux")
def cli(verbose):
    """Athalia-Générateur de projets IA intelligent."""
    if verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)


@cli.command()
@click.argument("idea")
@click.option("--output", "-o", default="./generated_project", help="Dossier de sortie")
@click.option("--dry-run", is_flag=True, help="Mode simulation")
def generate(idea, output, dry_run):
    """Génère un projet complet à partir dune idée."""
    try:
        click.echo(f"🚀 Génération du projet: {idea}")

        if dry_run:
            click.echo("🔍 Mode simulation activé")

        # 1. Générer le blueprint avec lIA robuste
        click.echo("🤖 Génération du blueprint avec IA robuste...")
        ai = RobustAI()
        blueprint = ai.generate_blueprint(idea)

        if not blueprint:
            click.echo("❌ Impossible de générer le blueprint")
            return

        click.echo(f"✅ Blueprint généré: {blueprint.get('project_type', 'Projet')}")

        # 2. Générer le projet complet

        # Créer le dossier de sortie s'il n'existe pas
        os.makedirs(output, exist_ok=True)

        # Variable non utilisée supprimée
        result = generate_project(blueprint, output, dry_run=dry_run)

        if result:
            if not dry_run:
                click.echo(f"✅ Projet généré dans: {output}")
            else:
                click.echo("✅ Simulation terminée")
        else:
            click.echo("❌ Erreur lors de la génération du projet")

    except Exception as e:
        click.echo(f"❌ Erreur: {e}")
        click.echo(f"🔍 Détails: {traceback.format_exc()}")


@cli.command()
@click.argument("project_path")
def audit(project_path):
    """Audit intelligent dun projet existant."""
    try:
        click.echo(f"🔍 Audit du projet: {project_path}")

        results = audit_project_intelligent(project_path)

        click.echo(f"📊 Score global: {results.get('global_score', 0)}/100")
        click.echo(f"📁 Fichiers analysés: {len(results.get('files', []))}")
        click.echo(f"⚠️  Problèmes détectés: {len(results.get('issues', []))}")
        click.echo(f"💡 Suggestions: {len(results.get('suggestions', []))}")

        # Sauvegarder le rapport
        report_path = Path(project_path) / "audit_report.yaml"
        with open(report_path, "w") as f:
            yaml.dump(results, f, default_flow_style=False)

        click.echo(f"📄 Rapport sauvegardé: {report_path}")

    except Exception as e:
        click.echo(f"❌ Erreur: {e}")


@cli.command()
def ai_status():
    """Affiche le statut de lIA robuste."""
    try:
        ai = RobustAI()
        click.echo("🤖 Statut de lIA robuste")
        click.echo("=" * 40)

        # Modèles disponibles
        click.echo(f"📋 Modèles détectés: {len(ai.available_models)}")
        for model in ai.available_models:
            status = "✅" if model != AIModel.MOCK else "🔄"
            click.echo(f"  {status} {model.value}")

        # Chaîne de fallback
        click.echo(f"\n🔄 Chaîne de fallback ({len(ai.fallback_chain)} modèles):")
        for index, model in enumerate(ai.fallback_chain, 1):
            click.echo(f"  {index}. {model.value}")

        # Templates de prompts
        click.echo(f"\n📝 Templates de prompts: {len(ai.prompt_templates)}")
        for context in ai.prompt_templates.keys():
            click.echo(f"  • {context}")

        click.echo("\n✨ IA robuste prête à lemploi!")

    except ImportError:
        click.echo("❌ Module ai_robust non disponible")
    except Exception as e:
        click.echo(f"❌ Erreur: {e}")


@cli.command()
@click.argument("idea")
def test_ai(idea):
    """Teste lIA robuste avec une idée de projet."""
    try:
        ai = RobustAI()
        click.echo(f"🧪 Test IA robuste: {idea}")
        click.echo("=" * 50)

        # Test de génération de blueprint
        click.echo("📋 Génération de blueprint...")
        blueprint = ai.generate_blueprint(idea)

        click.echo("✅ Blueprint généré:")
        click.echo(f"  • Nom: {blueprint.get('project_name', 'N/A')}")
        click.echo(f"  • Type: {blueprint.get('project_type', 'N/A')}")
        click.echo(f"  • Modules: {len(blueprint.get('modules', []))}")
        click.echo(f"  • Dépendances: {len(blueprint.get('dependencies', []))}")

        # Test de revue de code
        click.echo("\n🔍 Test de revue de code...")
        test_code = """
def hello_world():
    print("Hello World")
    return True
"""
        review = ai.review_code(
            code=test_code, filename="test.py", project_type="python", current_score=50
        )

        click.echo("✅ Revue générée:")
        click.echo(f"  • Score: {review.get('score', 'N/A')}")
        click.echo(f"  • Problèmes: {len(review.get('issues', []))}")
        click.echo(f"  • Suggestions: {len(review.get('suggestions', []))}")

        # Test de documentation
        click.echo("\n📚 Test de génération de documentation...")
        doc = ai.generate_documentation(
            project_name="test", project_type="python", modules=["api", "web"]
        )

        click.echo(f"✅ Documentation générée ({len(doc)} caractères)")

        click.echo("\n🎉 Tous les tests IA robuste réussis!")

    except ImportError:
        click.echo("❌ Module ai_robust non disponible")
    except Exception as e:
        click.echo(f"❌ Erreur: {e}")


if __name__ == "__main__":
    cli()
