#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de standardisation CLI pour Athalia
Standardise toutes les interfaces CLI avec un format cohérent
"""

import click
import json
import sys
from datetime import datetime
from typing import Dict, Any, Optional, List
from enum import Enum

class OutputFormat(Enum):
    """Formats de sortie disponibles"""
    TEXT = "text"
    JSON = "json"

class CLIStandard:
    """Classe de standardisation pour les interfaces CLI"""
    
    def __init__(self, script_name: str):
        self.script_name = script_name
        self.verbose = False
        self.output_format = OutputFormat.TEXT
        self.dry_run = False
        
    def setup_common_options(self, func):
        """Décorateur pour ajouter les options communes"""
        func = click.option('--verbose', '-v', is_flag=True, help='Mode verbeux')(func)
        func = click.option('--output', '-o', type=click.Choice(['text', 'json']), 
                          default='text', help='Format de sortie')(func)
        func = click.option('--dry-run', '-d', is_flag=True, help='Mode simulation')(func)
        func = click.option('--config', '-c', type=click.Path(exists=True), 
                          help='Fichier de configuration')(func)
        func = click.option('--quiet', '-q', is_flag=True, help='Mode silencieux')(func)
        return func
    
    def print_success(self, message: str, details: Optional[Dict[str, Any]] = None):
        """Affiche un message de succès"""
        if self.output_format == OutputFormat.JSON:
            result: Dict[str, Any] = {
                "status": "success",
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "script": self.script_name
            }
            if details:
                result["details"] = details
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            click.echo(f"✅ {message}")
            if details and self.verbose:
                for key, value in details.items():
                    click.echo(f"   {key}: {value}")
    
    def print_error(self, message: str, code: str = "E001", details: Optional[Dict[str, Any]] = None):
        """Affiche un message d'erreur"""
        if self.output_format == OutputFormat.JSON:
            result: Dict[str, Any] = {
                "status": "error",
                "code": code,
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "script": self.script_name
            }
            if details:
                result["details"] = details
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            click.echo(f"❌ [{code}] {message}", err=True)
            if details and self.verbose:
                for key, value in details.items():
                    click.echo(f"   {key}: {value}", err=True)
    
    def print_warning(self, message: str, code: str = "W001", details: Optional[Dict[str, Any]] = None):
        """Affiche un message d'avertissement"""
        if self.output_format == OutputFormat.JSON:
            result: Dict[str, Any] = {
                "status": "warning",
                "code": code,
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "script": self.script_name
            }
            if details:
                result["details"] = details
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            click.echo(f"⚠️ [{code}] {message}")
            if details and self.verbose:
                for key, value in details.items():
                    click.echo(f"   {key}: {value}")
    
    def print_info(self, message: str, details: Optional[Dict[str, Any]] = None):
        """Affiche un message d'information"""
        if self.output_format == OutputFormat.JSON:
            result: Dict[str, Any] = {
                "status": "info",
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "script": self.script_name
            }
            if details:
                result["details"] = details
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            click.echo(f"ℹ️ {message}")
            if details and self.verbose:
                for key, value in details.items():
                    click.echo(f"   {key}: {value}")
    
    def print_table(self, headers: List[str], rows: List[List[str]], title: Optional[str] = None):
        """Affiche un tableau formaté"""
        if self.output_format == OutputFormat.JSON:
            result = {
                "status": "success",
                "type": "table",
                "title": title,
                "headers": headers,
                "rows": rows,
                "timestamp": datetime.now().isoformat(),
                "script": self.script_name
            }
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            if title:
                click.echo(f"\n📊 {title}")
            
            # Calculer les largeurs de colonnes
            widths = [len(header) for header in headers]
            for row in rows:
                for i, cell in enumerate(row):
                    widths[i] = max(widths[i], len(str(cell)))
            
            # Afficher l'en-tête
            header_line = " | ".join(header.ljust(widths[i]) for i, header in enumerate(headers))
            click.echo(header_line)
            click.echo("-" * len(header_line))
            
            # Afficher les lignes
            for row in rows:
                row_line = " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row))
                click.echo(row_line)
    
    def confirm_action(self, message: str, default: bool = False) -> bool:
        """Demande confirmation à l'utilisateur"""
        if self.dry_run:
            self.print_info(f"Mode simulation: {message} (serait confirmé)")
            return True
        
        return click.confirm(message, default=default)
    
    def get_input(self, message: str, default: Optional[str] = None) -> str:
        """Demande une entrée à l'utilisateur"""
        if self.dry_run:
            self.print_info(f"Mode simulation: {message} (utiliserait '{default or 'valeur par défaut'}')")
            return default or "valeur par défaut"
        
        return click.prompt(message, default=default)
    
    def select_option(self, message: str, options: List[str], default: Optional[int] = None) -> int:
        """Demande à l'utilisateur de sélectionner une option"""
        if self.dry_run:
            self.print_info(f"Mode simulation: {message} (sélectionnerait l'option {default or 0})")
            return default or 0
        
        click.echo(f"\n{message}")
        for i, option in enumerate(options):
            click.echo(f"{i + 1}. {option}")
        
        while True:
            try:
                choice = click.prompt("Choix", type=int, default=default or 1)
                if 1 <= choice <= len(options):
                    return choice - 1
                else:
                    click.echo(f"❌ Choix invalide. Entrez un nombre entre 1 et {len(options)}")
            except click.Abort:
                sys.exit(1)

def create_cli_group(name: str, help_text: str):
    """Crée un groupe CLI standardisé"""
    @click.group(name=name, help=help_text)
    @click.option('--verbose', '-v', is_flag=True, help='Mode verbeux')
    @click.option('--output', '-o', type=click.Choice(['text', 'json']), 
                  default='text', help='Format de sortie')
    @click.option('--dry-run', '-d', is_flag=True, help='Mode simulation')
    @click.option('--config', '-c', type=click.Path(exists=True), 
                  help='Fichier de configuration')
    @click.option('--quiet', '-q', is_flag=True, help='Mode silencieux')
    @click.pass_context
    def cli_group(ctx, verbose, output, dry_run, config, quiet):
        """Groupe CLI standardisé"""
        ctx.ensure_object(dict)
        ctx.obj['verbose'] = verbose
        ctx.obj['output'] = output
        ctx.obj['dry_run'] = dry_run
        ctx.obj['config'] = config
        ctx.obj['quiet'] = quiet
        
        # Créer l'instance de standardisation
        cli_std = CLIStandard(name)
        cli_std.verbose = verbose
        cli_std.output_format = OutputFormat(output)
        cli_std.dry_run = dry_run
        ctx.obj['cli_std'] = cli_std
    
    return cli_group

def add_common_commands(cli_group):
    """Ajoute les commandes communes à un groupe CLI"""
    
    @cli_group.command()
    @click.pass_context
    def status(ctx):
        """Affiche le statut du système"""
        cli_std = ctx.obj['cli_std']
        
        # Informations de statut
        status_info = {
            "version": "1.0.0",
            "python_version": sys.version,
            "platform": sys.platform,
            "verbose": cli_std.verbose,
            "output_format": cli_std.output_format.value,
            "dry_run": cli_std.dry_run
        }
        
        cli_std.print_success("Statut du système", status_info)
    
    @cli_group.command()
    @click.pass_context
    def config(ctx):
        """Gère la configuration"""
        cli_std = ctx.obj['cli_std']
        
        if cli_std.dry_run:
            cli_std.print_info("Mode simulation: Affichage de la configuration")
        else:
            # Afficher la configuration actuelle
            config_info = {
                "config_file": ctx.obj.get('config'),
                "verbose": cli_std.verbose,
                "output_format": cli_std.output_format.value
            }
            cli_std.print_success("Configuration actuelle", config_info)
    
    @cli_group.command()
    @click.pass_context
    def help(ctx):
        """Affiche l'aide détaillée"""
        cli_std = ctx.obj['cli_std']
        
        help_text = f"""
Aide pour {cli_std.script_name}

Commandes disponibles:
  run     Exécuter l'action principale
  status  Afficher le statut
  config  Gérer la configuration
  help    Afficher cette aide

Options communes:
  --help, -h          Afficher l'aide
  --verbose, -v       Mode verbeux
  --dry-run, -d       Mode simulation
  --config, -c FILE   Fichier de configuration
  --output, -o FORMAT Format de sortie (text/json)
  --quiet, -q         Mode silencieux

Exemples:
  {cli_std.script_name} run --verbose
  {cli_std.script_name} status --output json
  {cli_std.script_name} --dry-run
        """
        
        if cli_std.output_format == OutputFormat.JSON:
            cli_std.print_success("Aide affichée", {"help_text": help_text})
        else:
            click.echo(help_text)

def standardize_cli_script(script_name: str, help_text: str):
    """Décorateur pour standardiser un script CLI"""
    def decorator(func):
        # Créer le groupe CLI
        cli_group = create_cli_group(script_name, help_text)
        
        # Ajouter les commandes communes
        add_common_commands(cli_group)
        
        # Ajouter la commande principale
        @cli_group.command()
        @click.pass_context
        def run(ctx):
            """Exécute l'action principale"""
            return func(ctx)
        
        return cli_group
    
    return decorator

# Exemple d'utilisation
if __name__ == "__main__":
    @standardize_cli_script("ath-test", "Script de test standardisé")
    def main_action(ctx):
        """Action principale du script"""
        cli_std = ctx.obj['cli_std']
        
        cli_std.print_info("Démarrage du script de test")
        
        if cli_std.dry_run:
            cli_std.print_info("Mode simulation activé")
            return
        
        # Logique principale ici
        cli_std.print_success("Test terminé avec succès")
    
    main_action() 