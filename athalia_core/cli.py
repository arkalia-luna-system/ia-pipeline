"""
Interface CLI pour Athalia avec IA robuste.
"""

import click
import logging
from pathlib import Path
from .generation import generate_project
from .audit import audit_project_intelligent

# TODO: Préparer l'internationalisation (i18n) des messages CLI et prompts utilisateur.

@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Mode verbeux')
def cli(verbose):
    """Athalia - Générateur de projets IA intelligent."""
    if verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

@cli.command()
@click.argument('idea')
@click.option('--output', '-o', default='./generated_project', help='Dossier de sortie')
@click.option('--dry-run', is_flag=True, help='Mode simulation')
def generate(idea, output, dry_run):
    """Génère un projet complet à partir d'une idée."""
    try:
        click.echo(f"🚀 Génération du projet: {idea}")
        
        if dry_run:
            click.echo("🔍 Mode simulation activé")
        
        # 1. Générer le blueprint avec l'IA robuste
        from .generation import generate_blueprint_ia
        click.echo("🤖 Génération du blueprint avec IA robuste...")
        blueprint = generate_blueprint_ia(idea)
        
        if not blueprint:
            click.echo("❌ Impossible de générer le blueprint")
            return
        
        click.echo(f"✅ Blueprint généré: {blueprint.get('project_name', 'Projet')}")
        
        # 2. Générer le projet complet
        from .generation import generate_project
        
        # Créer le dossier de sortie s'il n'existe pas
        import os
        os.makedirs(output, exist_ok=True)
        
        result = generate_project(blueprint, output, dry_run=dry_run)
        
        if not dry_run:
            click.echo(f"✅ Projet généré dans: {output}")
        else:
            click.echo("✅ Simulation terminée")
            
    except Exception as e:
        click.echo(f"❌ Erreur: {e}")
        import traceback
        click.echo(f"🔍 Détails: {traceback.format_exc()}")

@cli.command()
@click.argument('project_path')
def audit(project_path):
    """Audit intelligent d'un projet existant."""
    try:
        click.echo(f"🔍 Audit du projet: {project_path}")
        
        results = audit_project_intelligent(project_path)
        
        click.echo(f"📊 Score global: {results.get('global_score', 0)}/100")
        click.echo(f"📁 Fichiers analysés: {len(results.get('files', []))}")
        click.echo(f"⚠️  Problèmes détectés: {len(results.get('issues', []))}")
        click.echo(f"💡 Suggestions: {len(results.get('suggestions', []))}")
        
        # Sauvegarder le rapport
        report_path = Path(project_path) / "audit_report.yaml"
        import yaml
        with open(report_path, 'w') as f:
            yaml.dump(results, f, default_flow_style=False)
        
        click.echo(f"📄 Rapport sauvegardé: {report_path}")
        
    except Exception as e:
        click.echo(f"❌ Erreur: {e}")

@cli.command()
def ai_status():
    """Affiche le statut de l'IA robuste."""
    try:
        from .ai_robust import robust_ai, AIModel
        
        click.echo("🤖 Statut de l'IA Robuste")
        click.echo("=" * 40)
        
        # Modèles disponibles
        click.echo(f"📋 Modèles détectés: {len(robust_ai.available_models)}")
        for model in robust_ai.available_models:
            status = "✅" if model != AIModel.MOCK else "🔄"
            click.echo(f"  {status} {model.value}")
        
        # Chaîne de fallback
        click.echo(f"\n🔄 Chaîne de fallback ({len(robust_ai.fallback_chain)} modèles):")
        for i, model in enumerate(robust_ai.fallback_chain, 1):
            click.echo(f"  {i}. {model.value}")
        
        # Templates de prompts
        click.echo(f"\n📝 Templates de prompts: {len(robust_ai.prompt_templates)}")
        for context in robust_ai.prompt_templates.keys():
            click.echo(f"  • {context}")
        
        click.echo("\n✨ IA robuste prête à l'emploi!")
        
    except ImportError:
        click.echo("❌ Module ai_robust non disponible")
    except Exception as e:
        click.echo(f"❌ Erreur: {e}")

@cli.command()
@click.argument('idea')
def test_ai(idea):
    """Teste l'IA robuste avec une idée de projet."""
    try:
        from .ai_robust import robust_ai
        
        click.echo(f"🧪 Test IA robuste: {idea}")
        click.echo("=" * 50)
        
        # Test de génération de blueprint
        click.echo("📋 Génération de blueprint...")
        blueprint = robust_ai.generate_blueprint(idea)
        
        click.echo(f"✅ Blueprint généré:")
        click.echo(f"  • Nom: {blueprint.get('project_name', 'N/A')}")
        click.echo(f"  • Type: {blueprint.get('project_type', 'N/A')}")
        click.echo(f"  • Modules: {len(blueprint.get('modules', []))}")
        click.echo(f"  • Dépendances: {len(blueprint.get('dependencies', []))}")
        
        # Test de revue de code
        click.echo("\n🔍 Test de revue de code...")
        test_code = '''
def hello_world():
    print("Hello")
    return True
'''
        review = robust_ai.review_code(
            code=test_code,
            filename="test.py",
            project_type="generic",
            current_score=50
        )
        
        click.echo(f"✅ Revue générée:")
        click.echo(f"  • Score: {review.get('score', 'N/A')}")
        click.echo(f"  • Problèmes: {len(review.get('issues', []))}")
        click.echo(f"  • Suggestions: {len(review.get('suggestions', []))}")
        
        # Test de documentation
        click.echo("\n📚 Test de génération de documentation...")
        doc = robust_ai.generate_documentation(
            project_name="test_project",
            project_type="generic",
            modules=["api", "database"]
        )
        
        click.echo(f"✅ Documentation générée ({len(doc)} caractères)")
        
        click.echo("\n🎉 Tous les tests IA robuste réussis!")
        
    except ImportError:
        click.echo("❌ Module ai_robust non disponible")
    except Exception as e:
        click.echo(f"❌ Erreur: {e}")

if __name__ == '__main__':
    cli() 