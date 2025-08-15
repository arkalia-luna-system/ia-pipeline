#!/usr/bin/env python3
"""
Script de nettoyage des logs volumineux
Optimise l'espace disque en compressant et nettoyant les anciens logs
"""

import gzip
import logging
import shutil
from datetime import datetime, timedelta
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def cleanup_logs():
    """Nettoie et optimise les logs"""
    logs_dir = Path("logs")
    if not logs_dir.exists():
        logger.info("Dossier logs non trouvé")
        return

    # Statistiques avant nettoyage
    total_size_before = sum(
        f.stat().st_size for f in logs_dir.rglob("*") if f.is_file()
    )
    logger.info(
        f"Taille totale avant nettoyage: {total_size_before / (1024**3):.2f} GB"
    )

    # 1. Compresser les anciens logs volumineux
    compress_old_logs(logs_dir)

    # 2. Supprimer les logs trop anciens (> 30 jours)
    remove_old_logs(logs_dir, days=30)

    # 3. Nettoyer les fichiers ._* (macOS)
    cleanup_macos_files(logs_dir)

    # Statistiques après nettoyage
    total_size_after = sum(f.stat().st_size for f in logs_dir.rglob("*") if f.is_file())
    space_saved = total_size_before - total_size_after
    logger.info(f"Taille totale après nettoyage: {total_size_after / (1024**3):.2f} GB")
    logger.info(f"Espace libéré: {space_saved / (1024**3):.2f} GB")


def compress_old_logs(logs_dir: Path):
    """Compresse les anciens logs volumineux"""
    logger.info("Compression des anciens logs...")

    # Logs à compresser (plus de 50MB)
    large_logs = []
    for log_file in logs_dir.glob("*.log.*"):
        if log_file.is_file() and log_file.stat().st_size > 50 * 1024 * 1024:  # 50MB
            large_logs.append(log_file)

    for log_file in large_logs:
        try:
            # Créer le fichier compressé
            compressed_file = log_file.with_suffix(log_file.suffix + ".gz")
            if not compressed_file.exists():
                with open(log_file, "rb") as f_in:
                    with gzip.open(compressed_file, "wb") as f_out:
                        shutil.copyfileobj(f_in, f_out)

                # Supprimer l'original
                log_file.unlink()
                logger.info(f"Compressé: {log_file.name} -> {compressed_file.name}")
        except Exception as e:
            logger.error(f"Erreur lors de la compression de {log_file}: {e}")


def remove_old_logs(logs_dir: Path, days: int):
    """Supprime les logs trop anciens"""
    logger.info(f"Suppression des logs de plus de {days} jours...")

    cutoff_date = datetime.now() - timedelta(days=days)
    removed_count = 0

    for log_file in logs_dir.rglob("*.log.*"):
        if log_file.is_file():
            try:
                # Vérifier la date de modification
                mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
                if mtime < cutoff_date:
                    log_file.unlink()
                    removed_count += 1
                    logger.info(f"Supprimé (trop ancien): {log_file.name}")
            except Exception as e:
                logger.error(f"Erreur lors de la suppression de {log_file}: {e}")

    logger.info(f"Logs anciens supprimés: {removed_count}")


def cleanup_macos_files(logs_dir: Path):
    """Nettoie les fichiers macOS cachés"""
    logger.info("Nettoyage des fichiers macOS cachés...")

    removed_count = 0
    for hidden_file in logs_dir.rglob("._*"):
        if hidden_file.is_file():
            try:
                hidden_file.unlink()
                removed_count += 1
            except Exception as e:
                logger.error(f"Erreur lors de la suppression de {hidden_file}: {e}")

    logger.info(f"Fichiers macOS supprimés: {removed_count}")


def optimize_log_rotation():
    """Optimise la rotation des logs"""
    logger.info("Optimisation de la rotation des logs...")

    # Créer un fichier de configuration pour logrotate si possible
    logrotate_config = """
# Configuration logrotate pour Athalia
/Volumes/T7/athalia-dev-setup/logs/*.log {
    daily
    rotate 3
    compress
    delaycompress
    missingok
    notifempty
    create 644 athalia staff
    postrotate
        # Redémarrer les services si nécessaire
        echo "Logs rotés: $(date)"
    endscript
}
"""

    try:
        with open("logs/logrotate.conf", "w") as f:
            f.write(logrotate_config)
        logger.info("Configuration logrotate créée")
    except Exception as e:
        logger.error(f"Erreur lors de la création de logrotate.conf: {e}")


if __name__ == "__main__":
    logger.info("🧹 Début du nettoyage des logs Athalia...")

    try:
        cleanup_logs()
        optimize_log_rotation()
        logger.info("✅ Nettoyage des logs terminé avec succès")
    except Exception as e:
        logger.error(f"❌ Erreur lors du nettoyage: {e}")
        exit(1)
