#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de nettoyage intelligent des anciennes données d'analyse
"""

import os
import json
import hashlib
import shutil
from datetime import datetime, timedelta
from pathlib import Path
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('logs/athalia.log', mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DataCleaner:
    """Classe pour nettoyer les anciennes données d'analyse"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.archive_dir = self.data_dir / "archive" / datetime.now().strftime("%Y%m%d")
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        
    def get_file_hash(self, file_path):
        """Calcule le hash MD5 d'un fichier"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def find_analysis_files(self):
        """Trouve tous les fichiers d'analyse"""
        pattern = "comprehensive_analysis_*.json"
        return list(self.data_dir.glob(pattern))
    
    def categorize_files(self, files):
        """Catégorise les fichiers par âge et importance"""
        now = datetime.now()
        categories = {
            'recent': [],      # < 1 heure
            'old': [],         # 1 heure - 1 jour
            'very_old': [],    # > 1 jour
            'duplicates': []   # Doublons détectés
        }
        
        file_hashes = {}
        
        for file_path in files:
            # Calculer l'âge du fichier
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            age = now - mtime
            
            # Calculer le hash
            file_hash = self.get_file_hash(file_path)
            
            # Catégoriser par âge
            if age < timedelta(hours=1):
                categories['recent'].append((file_path, mtime, file_hash))
            elif age < timedelta(days=1):
                categories['old'].append((file_path, mtime, file_hash))
            else:
                categories['very_old'].append((file_path, mtime, file_hash))
            
            # Détecter les doublons
            if file_hash in file_hashes:
                categories['duplicates'].append((file_path, mtime, file_hash))
            else:
                file_hashes[file_hash] = file_path
        
        return categories
    
    def archive_important_files(self, files):
        """Archive les fichiers importants"""
        archived_count = 0
        
        for file_path, mtime, file_hash in files:
            # Déterminer si le fichier est important
            is_important = self.is_file_important(file_path, mtime)
            
            if is_important:
                # Créer le nom d'archive
                archive_name = f"archived_{file_path.name}"
                archive_path = self.archive_dir / archive_name
                
                # Copier vers l'archive
                shutil.copy2(file_path, archive_path)
                logger.info(f"📦 Archivé: {file_path.name} -> {archive_path}")
                archived_count += 1
        
        return archived_count
    
    def is_file_important(self, file_path, mtime):
        """Détermine si un fichier est important à archiver"""
        # Règles d'importance
        file_size = file_path.stat().st_size
        
        # Fichiers volumineux (> 50KB) sont importants
        if file_size > 50000:
            return True
        
        # Fichiers récents (< 6 heures) sont importants
        age = datetime.now() - mtime
        if age < timedelta(hours=6):
            return True
        
        # Fichiers avec des noms spécifiques sont importants
        important_patterns = ['athalia-dev-setup', 'demo-app-ia-complete']
        for pattern in important_patterns:
            if pattern in file_path.name:
                return True
        
        return False
    
    def remove_duplicates(self, duplicates):
        """Supprime les fichiers en double"""
        removed_count = 0
        
        for file_path, mtime, file_hash in duplicates:
            try:
                file_path.unlink()
                logger.info(f"🗑️ Supprimé doublon: {file_path.name}")
                removed_count += 1
            except Exception as e:
                logger.error(f"❌ Erreur suppression {file_path.name}: {e}")
        
        return removed_count
    
    def remove_old_files(self, old_files):
        """Supprime les anciens fichiers non importants"""
        removed_count = 0
        
        for file_path, mtime, file_hash in old_files:
            # Vérifier si le fichier est important
            if not self.is_file_important(file_path, mtime):
                try:
                    file_path.unlink()
                    logger.info(f"🗑️ Supprimé ancien: {file_path.name}")
                    removed_count += 1
                except Exception as e:
                    logger.error(f"❌ Erreur suppression {file_path.name}: {e}")
        
        return removed_count
    
    def generate_report(self, categories, archived_count, removed_duplicates, removed_old):
        """Génère un rapport de nettoyage"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_files': sum(len(files) for files in categories.values()),
                'recent_files': len(categories['recent']),
                'old_files': len(categories['old']),
                'very_old_files': len(categories['very_old']),
                'duplicates': len(categories['duplicates']),
                'archived': archived_count,
                'removed_duplicates': removed_duplicates,
                'removed_old': removed_old
            },
            'categories': {
                'recent': [str(f[0]) for f in categories['recent']],
                'old': [str(f[0]) for f in categories['old']],
                'very_old': [str(f[0]) for f in categories['very_old']],
                'duplicates': [str(f[0]) for f in categories['duplicates']]
            }
        }
        
        return report


    def cleanup(self, dry_run=False):
        """Exécute le nettoyage complet"""
        logger.info("🧹 DÉBUT DU NETTOYAGE DES DONNÉES")
        logger.info(f"📁 Dossier de données: {self.data_dir}")
        logger.info(f"📦 Dossier d'archive: {self.archive_dir}")
        
        if dry_run:
            logger.info("🔍 MODE DRY-RUN - Aucun fichier ne sera supprimé")
        
        # Trouver tous les fichiers
        files = self.find_analysis_files()
        logger.info(f"📋 {len(files)} fichiers d'analyse trouvés")
        
        # Catégoriser les fichiers
        categories = self.categorize_files(files)
        
        # Afficher les statistiques
        logger.info(f"📊 Statistiques:")
        logger.info(f"  - Récents (< 1h): {len(categories['recent'])}")
        logger.info(f"  - Anciens (1h-1j): {len(categories['old'])}")
        logger.info(f"  - Très anciens (>1j): {len(categories['very_old'])}")
        logger.info(f"  - Doublons: {len(categories['duplicates'])}")
        
        # Actions de nettoyage
        archived_count = 0
        removed_duplicates = 0
        removed_old = 0
        
        if not dry_run:
            # Archiver les fichiers importants
            important_files = categories['recent'] + categories['old']
            archived_count = self.archive_important_files(important_files)
            
            # Supprimer les doublons
            removed_duplicates = self.remove_duplicates(categories['duplicates'])
            
            # Supprimer les anciens fichiers non importants
            removed_old = self.remove_old_files(categories['very_old'])
        
        # Générer le rapport
        report = self.generate_report(categories, archived_count, removed_duplicates, removed_old)
        
        # Sauvegarder le rapport
        report_file = self.data_dir / f"cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Afficher le résumé
        logger.info("✅ NETTOYAGE TERMINÉ")
        logger.info(f"📦 Fichiers archivés: {archived_count}")
        logger.info(f"🗑️ Doublons supprimés: {removed_duplicates}")
        logger.info(f"🗑️ Anciens supprimés: {removed_old}")
        logger.info(f"📄 Rapport sauvegardé: {report_file}")
        
        return report


def main():
    """Fonction principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Nettoyage intelligent des données d'analyse")
    parser.add_argument("--dry-run", action="store_true", help="Mode simulation")
    parser.add_argument("--data-dir", default="data", help="Dossier de données")
    
    args = parser.parse_args()
    
    # Créer le nettoyeur
    cleaner = DataCleaner(args.data_dir)
    
    # Exécuter le nettoyage
    report = cleaner.cleanup(dry_run=args.dry_run)
    
    # Afficher l'espace libéré
    if not args.dry_run:
        logger.info("💾 Espace disque après nettoyage:")
        os.system(f"du -sh {args.data_dir}")

if __name__ == "__main__":
    main() 