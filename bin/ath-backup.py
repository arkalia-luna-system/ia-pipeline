#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script CLI standardisé pour les sauvegardes Athalia
Utilise le système de standardisation CLI
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from athalia_core.cli_standard import standardize_cli_script, CLIStandard
from athalia_core.backup_system import get_backup_system, BackupSystem
from athalia_core.error_codes import ErrorCode

@standardize_cli_script("ath-backup", "Système de sauvegarde automatique Athalia")
def main_action(ctx):
    """Action principale du script de sauvegarde"""
    cli_std = ctx.obj['cli_std']
    backup_system = get_backup_system()
    
    cli_std.print_info("Système de sauvegarde Athalia")
    
    if cli_std.dry_run:
        cli_std.print_info("Mode simulation activé")
        
        # Afficher ce qui serait fait
        files_to_backup = backup_system.get_files_to_backup()
        cli_std.print_info(f"Fichiers qui seraient sauvegardés: {len(files_to_backup)}")
        
        for file_path in files_to_backup[:5]:  # Afficher les 5 premiers
            cli_std.print_info(f"  - {file_path}")
        
        if len(files_to_backup) > 5:
            cli_std.print_info(f"  ... et {len(files_to_backup) - 5} autres fichiers")
        
        return
    
    # Menu principal
    options = [
        "Créer une sauvegarde quotidienne",
        "Créer une sauvegarde hebdomadaire",
        "Lister les sauvegardes existantes",
        "Restaurer une sauvegarde",
        "Nettoyer les anciennes sauvegardes",
        "Afficher les statistiques"
    ]
    
    choice = cli_std.select_option("Choisissez une action:", options)
    
    try:
        if choice == 0:  # Sauvegarde quotidienne
            cli_std.print_info("Création d'une sauvegarde quotidienne...")
            metadata = backup_system.create_backup("daily")
            cli_std.print_success(
                f"Sauvegarde quotidienne créée: {metadata.backup_id}",
                {
                    "files_count": metadata.files_count,
                    "size_bytes": metadata.size_bytes,
                    "backup_path": metadata.backup_path
                }
            )
            
        elif choice == 1:  # Sauvegarde hebdomadaire
            cli_std.print_info("Création d'une sauvegarde hebdomadaire...")
            metadata = backup_system.create_backup("weekly")
            cli_std.print_success(
                f"Sauvegarde hebdomadaire créée: {metadata.backup_id}",
                {
                    "files_count": metadata.files_count,
                    "size_bytes": metadata.size_bytes,
                    "backup_path": metadata.backup_path
                }
            )
            
        elif choice == 2:  # Lister les sauvegardes
            cli_std.print_info("Récupération de la liste des sauvegardes...")
            backups = backup_system.list_backups()
            
            if not backups:
                cli_std.print_warning("Aucune sauvegarde trouvée")
                return
            
            # Préparer les données pour le tableau
            headers = ["ID", "Type", "Date", "Fichiers", "Taille (MB)"]
            rows = []
            
            for backup in backups[:10]:  # Limiter à 10 sauvegardes
                date = backup.timestamp[:10]  # Date seulement
                size_mb = backup.size_bytes / (1024 * 1024)
                rows.append([
                    backup.backup_id,
                    backup.backup_type,
                    date,
                    str(backup.files_count),
                    f"{size_mb:.1f}"
                ])
            
            cli_std.print_table(headers, rows, "Sauvegardes disponibles")
            
        elif choice == 3:  # Restaurer une sauvegarde
            cli_std.print_info("Récupération de la liste des sauvegardes...")
            backups = backup_system.list_backups()
            
            if not backups:
                cli_std.print_error("Aucune sauvegarde disponible pour restauration")
                return
            
            # Afficher les sauvegardes disponibles
            backup_options = []
            for backup in backups:
                date = backup.timestamp[:10]
                backup_options.append(f"{backup.backup_id} ({backup.backup_type}) - {date}")
            
            backup_choice = cli_std.select_option("Choisissez une sauvegarde à restaurer:", backup_options)
            selected_backup = backups[backup_choice]
            
            # Demander le chemin de restauration
            restore_path = cli_std.get_input(
                "Chemin de restauration (défaut: ./restore):",
                default="./restore"
            )
            
            # Confirmation
            if cli_std.confirm_action(
                f"Restaurer la sauvegarde {selected_backup.backup_id} vers {restore_path} ?"
            ):
                cli_std.print_info("Restauration en cours...")
                success = backup_system.restore_backup(selected_backup.backup_id, restore_path)
                
                if success:
                    cli_std.print_success(
                        f"Sauvegarde {selected_backup.backup_id} restaurée avec succès",
                        {"restore_path": restore_path}
                    )
                else:
                    cli_std.print_error(
                        f"Échec de la restauration de {selected_backup.backup_id}",
                        code=ErrorCode.PROCESSING_FAILED.value
                    )
            
        elif choice == 4:  # Nettoyer les anciennes sauvegardes
            if cli_std.confirm_action(
                f"Supprimer les sauvegardes de plus de {backup_system.retention_days} jours ?"
            ):
                cli_std.print_info("Nettoyage des anciennes sauvegardes...")
                deleted_count = backup_system.cleanup_old_backups()
                
                if deleted_count > 0:
                    cli_std.print_success(
                        f"Nettoyage terminé: {deleted_count} sauvegardes supprimées"
                    )
                else:
                    cli_std.print_info("Aucune sauvegarde ancienne à supprimer")
            
        elif choice == 5:  # Statistiques
            cli_std.print_info("Calcul des statistiques...")
            stats = backup_system.get_backup_stats()
            
            if stats["total_backups"] == 0:
                cli_std.print_warning("Aucune sauvegarde trouvée")
                return
            
            # Afficher les statistiques
            cli_std.print_success("Statistiques des sauvegardes", {
                "Total sauvegardes": stats["total_backups"],
                "Sauvegardes quotidiennes": stats["daily_backups"],
                "Sauvegardes hebdomadaires": stats["weekly_backups"],
                "Total fichiers": stats["total_files"],
                "Taille totale (MB)": f"{stats['total_size'] / (1024 * 1024):.1f}",
                "Plus ancienne": stats["oldest_backup"][:10],
                "Plus récente": stats["newest_backup"][:10]
            })
    
    except Exception as e:
        cli_std.print_error(
            f"Erreur lors de l'opération: {str(e)}",
            code=ErrorCode.SYSTEM_INTERNAL_ERROR.value,
            details={"operation": options[choice]}
        )

if __name__ == "__main__":
    main_action() 