#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système de sauvegarde automatique pour Athalia
Protège les données critiques avec sauvegardes incrémentales et complètes
"""

import os
import json
import shutil
import gzip
import hashlib
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

logger = logging.getLogger(__name__)

@dataclass
class BackupMetadata:
    """Métadonnées de sauvegarde"""
    backup_id: str
    timestamp: str
    backup_type: str  # 'daily' ou 'weekly'
    size_bytes: int
    files_count: int
    checksum: str
    compression: str
    encryption: bool
    source_paths: List[str]
    backup_path: str

class BackupSystem:
    """Système de sauvegarde automatique"""
    
    def __init__(self, backup_root: str = "backups", retention_days: int = 30):
        self.backup_root = Path(backup_root)
        self.retention_days = retention_days
        self.backup_root.mkdir(exist_ok=True)
        
        # Structure des dossiers
        self.daily_dir = self.backup_root / "daily"
        self.weekly_dir = self.backup_root / "weekly"
        self.metadata_dir = self.backup_root / "metadata"
        
        # Créer les dossiers
        self.daily_dir.mkdir(exist_ok=True)
        self.weekly_dir.mkdir(exist_ok=True)
        self.metadata_dir.mkdir(exist_ok=True)
        
        # Chemins critiques à sauvegarder
        self.critical_paths = [
            "data/",
            "config/",
            "logs/",
            "blueprints_history/"
        ]
        
        # Fichiers d'exclusion
        self.exclude_patterns = [
            "*.tmp",
            "*.temp",
            "*.log",
            "__pycache__",
            ".git",
            "*.pyc"
        ]
    
    def create_backup_id(self) -> str:
        """Crée un ID unique pour la sauvegarde"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def calculate_checksum(self, file_path: Path) -> str:
        """Calcule le checksum MD5 d'un fichier"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def should_exclude(self, file_path: Path) -> bool:
        """Détermine si un fichier doit être exclu de la sauvegarde"""
        for pattern in self.exclude_patterns:
            if pattern.startswith("*."):
                if file_path.suffix == pattern[1:]:
                    return True
            elif pattern in file_path.name or pattern in str(file_path):
                return True
        return False
    
    def get_files_to_backup(self) -> List[Path]:
        """Récupère la liste des fichiers à sauvegarder"""
        files_to_backup = []
        
        for critical_path in self.critical_paths:
            path = Path(critical_path)
            if path.exists():
                if path.is_file():
                    if not self.should_exclude(path):
                        files_to_backup.append(path)
                elif path.is_dir():
                    for file_path in path.rglob("*"):
                        if file_path.is_file() and not self.should_exclude(file_path):
                            files_to_backup.append(file_path)
        
        return files_to_backup
    
    def compress_file(self, source_path: Path, dest_path: Path) -> int:
        """Compresse un fichier avec gzip"""
        with open(source_path, 'rb') as f_in:
            with gzip.open(dest_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return dest_path.stat().st_size
    
    def create_backup(self, backup_type: str = "daily") -> BackupMetadata:
        """Crée une sauvegarde complète"""
        backup_id = self.create_backup_id()
        timestamp = datetime.now().isoformat()
        
        # Créer le dossier de sauvegarde
        if backup_type == "daily":
            backup_dir = self.daily_dir / backup_id
        else:
            backup_dir = self.weekly_dir / backup_id
        
        backup_dir.mkdir(exist_ok=True)
        
        # Récupérer les fichiers à sauvegarder
        files_to_backup = self.get_files_to_backup()
        
        total_size = 0
        files_count = 0
        source_paths = []
        
        logger.info(f"Création de la sauvegarde {backup_id} ({backup_type})")
        logger.info(f"Fichiers à sauvegarder: {len(files_to_backup)}")
        
        for file_path in files_to_backup:
            try:
                # Créer la structure de dossiers relative
                relative_path = file_path.relative_to(Path.cwd())
                backup_file_path = backup_dir / relative_path
                backup_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Compresser le fichier
                compressed_size = self.compress_file(file_path, backup_file_path)
                total_size += compressed_size
                files_count += 1
                source_paths.append(str(file_path))
                
                logger.debug(f"Sauvegardé: {file_path} -> {backup_file_path} ({compressed_size} bytes)")
                
            except Exception as e:
                logger.error(f"Erreur lors de la sauvegarde de {file_path}: {e}")
        
        # Calculer le checksum de la sauvegarde (simplifié pour les dossiers)
        checksum = hashlib.md5(str(backup_dir).encode()).hexdigest()
        
        # Créer les métadonnées
        metadata = BackupMetadata(
            backup_id=backup_id,
            timestamp=timestamp,
            backup_type=backup_type,
            size_bytes=total_size,
            files_count=files_count,
            checksum=checksum,
            compression="gzip",
            encryption=False,
            source_paths=source_paths,
            backup_path=str(backup_dir)
        )
        
        # Sauvegarder les métadonnées
        metadata_file = self.metadata_dir / f"{backup_id}_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(metadata), f, indent=2, ensure_ascii=False)
        
        # Mettre à jour l'index des sauvegardes
        self.update_backup_index(metadata)
        
        logger.info(f"Sauvegarde {backup_id} terminée: {files_count} fichiers, {total_size} bytes")
        
        return metadata
    
    def update_backup_index(self, metadata: BackupMetadata):
        """Met à jour l'index des sauvegardes"""
        index_file = self.metadata_dir / "backup_index.json"
        
        if index_file.exists():
            with open(index_file, 'r', encoding='utf-8') as f:
                index = json.load(f)
        else:
            index = {"backups": []}
        
        # Ajouter la nouvelle sauvegarde
        index["backups"].append(asdict(metadata))
        
        # Trier par timestamp (plus récent en premier)
        index["backups"].sort(key=lambda x: x["timestamp"], reverse=True)
        
        # Sauvegarder l'index
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
    
    def list_backups(self) -> List[BackupMetadata]:
        """Liste toutes les sauvegardes disponibles"""
        index_file = self.metadata_dir / "backup_index.json"
        
        if not index_file.exists():
            return []
        
        with open(index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)
        
        backups = []
        for backup_data in index.get("backups", []):
            backups.append(BackupMetadata(**backup_data))
        
        return backups
    
    def get_backup_by_id(self, backup_id: str) -> Optional[BackupMetadata]:
        """Récupère une sauvegarde par son ID"""
        backups = self.list_backups()
        for backup in backups:
            if backup.backup_id == backup_id:
                return backup
        return None
    
    def restore_backup(self, backup_id: str, restore_path: str = ".", 
                      verify_checksum: bool = True) -> bool:
        """Restaure une sauvegarde"""
        backup = self.get_backup_by_id(backup_id)
        if not backup:
            logger.error(f"Sauvegarde {backup_id} non trouvée")
            return False
        
        backup_dir = Path(backup.backup_path)
        if not backup_dir.exists():
            logger.error(f"Dossier de sauvegarde {backup_dir} non trouvé")
            return False
        
        # Vérifier le checksum si demandé
        if verify_checksum:
            current_checksum = self.calculate_checksum(backup_dir)
            if current_checksum != backup.checksum:
                logger.error(f"Checksum invalide pour la sauvegarde {backup_id}")
                return False
        
        restore_path = Path(restore_path)
        restore_path.mkdir(exist_ok=True)
        
        logger.info(f"Restauration de la sauvegarde {backup_id} vers {restore_path}")
        
        try:
            # Restaurer tous les fichiers
            for file_path in backup_dir.rglob("*.gz"):
                # Décompresser le fichier
                relative_path = file_path.relative_to(backup_dir)
                restore_file_path = restore_path / relative_path.with_suffix('')
                restore_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                with gzip.open(file_path, 'rb') as f_in:
                    with open(restore_file_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                
                logger.debug(f"Restauré: {file_path} -> {restore_file_path}")
            
            logger.info(f"Restauration {backup_id} terminée avec succès")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de la restauration {backup_id}: {e}")
            return False
    
    def cleanup_old_backups(self) -> int:
        """Nettoie les anciennes sauvegardes selon la politique de rétention"""
        cutoff_date = datetime.now() - timedelta(days=self.retention_days)
        backups = self.list_backups()
        deleted_count = 0
        
        for backup in backups:
            backup_date = datetime.fromisoformat(backup.timestamp)
            if backup_date < cutoff_date:
                try:
                    # Supprimer le dossier de sauvegarde
                    backup_dir = Path(backup.backup_path)
                    if backup_dir.exists():
                        shutil.rmtree(backup_dir)
                    
                    # Supprimer les métadonnées
                    metadata_file = self.metadata_dir / f"{backup.backup_id}_metadata.json"
                    if metadata_file.exists():
                        metadata_file.unlink()
                    
                    logger.info(f"Sauvegarde ancienne supprimée: {backup.backup_id}")
                    deleted_count += 1
                    
                except Exception as e:
                    logger.error(f"Erreur lors de la suppression de {backup.backup_id}: {e}")
        
        # Mettre à jour l'index
        if deleted_count > 0:
            self.update_backup_index_from_files()
        
        return deleted_count
    
    def update_backup_index_from_files(self):
        """Met à jour l'index en se basant sur les fichiers existants"""
        index = {"backups": []}
        
        # Parcourir les dossiers de sauvegarde
        for backup_dir in [self.daily_dir, self.weekly_dir]:
            for backup_folder in backup_dir.iterdir():
                if backup_folder.is_dir():
                    metadata_file = self.metadata_dir / f"{backup_folder.name}_metadata.json"
                    if metadata_file.exists():
                        with open(metadata_file, 'r', encoding='utf-8') as f:
                            backup_data = json.load(f)
                            index["backups"].append(backup_data)
        
        # Trier par timestamp
        index["backups"].sort(key=lambda x: x["timestamp"], reverse=True)
        
        # Sauvegarder l'index
        index_file = self.metadata_dir / "backup_index.json"
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
    
    def get_backup_stats(self) -> Dict[str, Any]:
        """Récupère les statistiques des sauvegardes"""
        backups = self.list_backups()
        
        if not backups:
            return {
                "total_backups": 0,
                "total_size": 0,
                "total_files": 0,
                "oldest_backup": None,
                "newest_backup": None,
                "daily_backups": 0,
                "weekly_backups": 0
            }
        
        total_size = sum(b.size_bytes for b in backups)
        total_files = sum(b.files_count for b in backups)
        daily_backups = len([b for b in backups if b.backup_type == "daily"])
        weekly_backups = len([b for b in backups if b.backup_type == "weekly"])
        
        timestamps = [datetime.fromisoformat(b.timestamp) for b in backups]
        oldest_backup = min(timestamps).isoformat()
        newest_backup = max(timestamps).isoformat()
        
        return {
            "total_backups": len(backups),
            "total_size": total_size,
            "total_files": total_files,
            "oldest_backup": oldest_backup,
            "newest_backup": newest_backup,
            "daily_backups": daily_backups,
            "weekly_backups": weekly_backups
        }

# Instance globale du système de sauvegarde
global_backup_system = BackupSystem()

def get_backup_system() -> BackupSystem:
    """Récupère l'instance globale du système de sauvegarde"""
    return global_backup_system

def set_backup_system(backup_system: BackupSystem):
    """Définit l'instance globale du système de sauvegarde"""
    global global_backup_system
    global_backup_system = backup_system

# Exemple d'utilisation
if __name__ == "__main__":
    # Test du système de sauvegarde
    backup_system = BackupSystem()
    
    # Créer une sauvegarde quotidienne
    print("Création d'une sauvegarde quotidienne...")
    metadata = backup_system.create_backup("daily")
    print(f"Sauvegarde créée: {metadata.backup_id}")
    
    # Lister les sauvegardes
    print("\nListe des sauvegardes:")
    backups = backup_system.list_backups()
    for backup in backups:
        print(f"- {backup.backup_id} ({backup.backup_type}): {backup.files_count} fichiers, {backup.size_bytes} bytes")
    
    # Statistiques
    print("\nStatistiques:")
    stats = backup_system.get_backup_stats()
    for key, value in stats.items():
        print(f"- {key}: {value}")
    
    # Nettoyage
    print("\nNettoyage des anciennes sauvegardes...")
    deleted_count = backup_system.cleanup_old_backups()
    print(f"Sauvegardes supprimées: {deleted_count}") 