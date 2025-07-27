#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système de logging avancé pour Athalia/Arkalia
Logging intelligent avec rotation, compression et analyse automatique
"""

import logging
import logging.handlers
import os
import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List
import gzip
import shutil
import threading
from collections import defaultdict, deque


class AthaliaLogger:
    """Système de logging avancé pour Athalia/Arkalia"""

    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        # Créer le dossier archive
        self.archive_dir = self.log_dir / "archive"
        self.archive_dir.mkdir(exist_ok=True)

        # Configuration des loggers
        self.loggers = {}
        self.metrics = defaultdict(deque)
        self.performance_data = {}

        # Initialiser les loggers
        self._setup_loggers()

        # Thread de nettoyage automatique
        self.cleanup_thread = threading.Thread(target=self._cleanup_worker, daemon=True)
        self.cleanup_thread.start()

    def _setup_loggers(self):
        """Configure tous les loggers"""

        # Logger principal
        self.loggers['main'] = self._create_logger(
            'athalia',
            self.log_dir / 'athalia.log',
            logging.INFO
        )

        # Logger de validation
        self.loggers['validation'] = self._create_logger(
            'validation',
            self.log_dir / 'validation.log',
            logging.DEBUG
        )

        # Logger de correction
        self.loggers['correction'] = self._create_logger(
            'correction',
            self.log_dir / 'correction.log',
            logging.DEBUG
        )

        # Logger de performance
        self.loggers['performance'] = self._create_logger(
            'performance',
            self.log_dir / 'performance.log',
            logging.DEBUG
        )

        # Logger d'erreurs
        self.loggers['errors'] = self._create_logger(
            'errors',
            self.log_dir / 'errors.log',
            logging.ERROR
        )

    def _create_logger(self, name: str, log_file: Path, level: int) -> logging.Logger:
        """Crée un logger avec rotation et compression"""

        logger = logging.getLogger(f'athalia.{name}')
        logger.setLevel(level)

        # Éviter les doublons
        if logger.handlers:
            return logger

        # Handler pour fichier avec rotation
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )

        # Format personnalisé
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)

        # Handler pour console (seulement pour les erreurs)
        if name == 'errors':
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.ERROR)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        logger.addHandler(file_handler)
        return logger

    def log_main(self, message: str, level: str = 'INFO', **kwargs):
        """Log dans le logger principal"""
        logger = self.loggers['main']
        extra_data = f" | {json.dumps(kwargs)}" if kwargs else ""
        getattr(logger, level.lower())(f"{message}{extra_data}")

    def log_validation(self, test_name: str, result: Dict[str, Any], duration: float):
        """Log des résultats de validation"""
        logger = self.loggers['validation']

        # Métriques de validation
        self.metrics['validation'].append({
            'timestamp': datetime.now().isoformat(),
            'test_name': test_name,
            'success': result.get('success', False),
            'duration': duration,
            'details': result
        })

        # Garder seulement les 1000 dernières métriques
        if len(self.metrics['validation']) > 1000:
            self.metrics['validation'].popleft()

        logger.info(
            f"VALIDATION | {test_name} | {result.get('succes', False)} | {duration:.2f}s | {result}"
        )

    def log_correction(self, file_path: str, correction_type: str, success: bool,
                      old_content: str, new_content: str, duration: float):
        """Log des corrections automatiques"""
        logger = self.loggers['correction']

        # Métriques de correction
        self.metrics['correction'].append({
            'timestamp': datetime.now().isoformat(),
            'file_path': file_path,
            'type': correction_type,
            'success': success,
            'duration': duration,
            'changes': len(new_content) - len(old_content)
        })

        # Garder seulement les 1000 dernières métriques
        if len(self.metrics['correction']) > 1000:
            self.metrics['correction'].popleft()

        logger.info(f"CORRECTION | {file_path} | {correction_type} | {success} | {duration:.2f}s")

        if not success:
            logger.warning(f"CORRECTION_FAILED | {file_path} | {correction_type}")

    def log_performance(self, operation: str, duration: float, memory_mb: Optional[float] = None,
                       cpu_percent: Optional[float] = None, **kwargs):
        """Log des métriques de performance"""
        logger = self.loggers['performance']

        # Métriques de performance
        perf_data = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'duration': duration,
            'memory_mb': memory_mb,
            'cpu_percent': cpu_percent,
            **kwargs
        }

        self.metrics['performance'].append(perf_data)

        # Garder seulement les 1000 dernières métriques
        if len(self.metrics['performance']) > 1000:
            self.metrics['performance'].popleft()

        logger.info(f"PERFORMANCE | {operation} | {duration:.2f}s | {memory_mb}MB | {cpu_percent}%")

    def log_error(self, error: Exception, context: str = "", **kwargs):
        """Log des erreurs"""
        logger = self.loggers['errors']

        error_data = {
            'timestamp': datetime.now().isoformat(),
            'error_type': type(error).__name__,
            'error_message': str(error),
            'context': context,
            **kwargs
        }

        self.metrics['errors'].append(error_data)

        # Garder seulement les 100 dernières erreurs
        if len(self.metrics['errors']) > 100:
            self.metrics['errors'].popleft()

        logger.error(f"ERROR | {context} | {type(error).__name__} | {str(error)} | {kwargs}")

    def get_validation_stats(self, hours: int = 24) -> Dict[str, Any]:
        """Récupère les statistiques de validation"""
        cutoff = datetime.now() - timedelta(hours=hours)

        recent_metrics = [
            m for m in self.metrics['validation']
            if datetime.fromisoformat(m['timestamp']) > cutoff
        ]

        if not recent_metrics:
            return {'total': 0, 'success_rate': 0, 'avg_duration': 0}

        total = len(recent_metrics)
        success_count = sum(1 for m in recent_metrics if m['success'])
        success_rate = (success_count / total) * 100
        avg_duration = sum(m['duration'] for m in recent_metrics) / total

        return {
            'total': total,
            'success_rate': success_rate,
            'avg_duration': avg_duration,
            'recent_tests': recent_metrics[-10:]  # 10 derniers tests
        }

    def get_correction_stats(self, hours: int = 24) -> Dict[str, Any]:
        """Récupère les statistiques de correction"""
        cutoff = datetime.now() - timedelta(hours=hours)

        recent_metrics = [
            m for m in self.metrics['correction']
            if datetime.fromisoformat(m['timestamp']) > cutoff
        ]

        if not recent_metrics:
            return {'total': 0, 'success_rate': 0, 'avg_duration': 0}

        total = len(recent_metrics)
        success_count = sum(1 for m in recent_metrics if m['success'])
        success_rate = (success_count / total) * 100
        avg_duration = sum(m['duration'] for m in recent_metrics) / total

        # Statistiques par type de correction
        correction_types = defaultdict(list)
        for m in recent_metrics:
            correction_types[m['type']].append(m)

        type_stats = {}
        for corr_type, metrics in correction_types.items():
            type_success = sum(1 for m in metrics if m['success'])
            type_stats[corr_type] = {
                'count': len(metrics),
                'success_rate': (type_success / len(metrics)) * 100
            }

        return {
            'total': total,
            'success_rate': success_rate,
            'avg_duration': avg_duration,
            'type_stats': type_stats,
            'recent_corrections': recent_metrics[-10:]  # 10 dernières corrections
        }

    def get_performance_stats(self, hours: int = 24) -> Dict[str, Any]:
        """Récupère les statistiques de performance"""
        cutoff = datetime.now() - timedelta(hours=hours)

        recent_metrics = [
            m for m in self.metrics['performance']
            if datetime.fromisoformat(m['timestamp']) > cutoff
        ]

        if not recent_metrics:
            return {'total': 0, 'avg_duration': 0}

        # Statistiques par opération
        operations = defaultdict(list)
        for m in recent_metrics:
            operations[m['operation']].append(m)

        op_stats = {}
        for op, metrics in operations.items():
            durations = [m['duration'] for m in metrics]
            op_stats[op] = {
                'count': len(metrics),
                'avg_duration': sum(durations) / len(durations),
                'min_duration': min(durations),
                'max_duration': max(durations)
            }

        all_durations = [m['duration'] for m in recent_metrics]

        return {
            'total': len(recent_metrics),
            'avg_duration': sum(all_durations) / len(all_durations),
            'min_duration': min(all_durations),
            'max_duration': max(all_durations),
            'operation_stats': op_stats
        }

    def get_error_stats(self, hours: int = 24) -> Dict[str, Any]:
        """Récupère les statistiques d'erreurs"""
        cutoff = datetime.now() - timedelta(hours=hours)

        recent_errors = [
            m for m in self.metrics['errors']
            if datetime.fromisoformat(m['timestamp']) > cutoff
        ]

        if not recent_errors:
            return {'total': 0, 'error_types': {}}

        # Statistiques par type d'erreur
        error_types = defaultdict(int)
        for error in recent_errors:
            error_types[error['error_type']] += 1

        return {
            'total': len(recent_errors),
            'error_types': dict(error_types),
            'recent_errors': recent_errors[-10:]  # 10 dernières erreurs
        }

    def _cleanup_worker(self):
        """Thread de nettoyage automatique des logs"""
        while hasattr(self, '_cleanup_active') and self._cleanup_active:
            try:
                self._cleanup_old_logs()
                self._compress_old_logs()
                time.sleep(3600)  # Nettoyer toutes les heures
            except Exception as e:
                self.log_error(e, "cleanup_worker")
                time.sleep(300)  # Attendre 5 minutes en cas d'erreur

    def start_cleanup_worker(self):
        """Démarre le thread de nettoyage"""
        if not hasattr(self, '_cleanup_active') or not self._cleanup_active:
            self._cleanup_active = True
            self._cleanup_thread = threading.Thread(target=self._cleanup_worker, daemon=True)
            self._cleanup_thread.start()
            self.log_main("🧹 Thread de nettoyage démarré")

    def stop_cleanup_worker(self):
        """Arrête le thread de nettoyage"""
        if hasattr(self, '_cleanup_active'):
            self._cleanup_active = False
            self.log_main("🛑 Thread de nettoyage arrêté")

    def _cleanup_old_logs(self):
        """Nettoie les anciens logs"""
        cutoff = datetime.now() - timedelta(days=30)

        for log_file in self.log_dir.glob("*.log.*"):
            try:
                file_time = datetime.fromtimestamp(log_file.stat().st_mtime)
                if file_time < cutoff:
                    log_file.unlink()
                    self.log_main(f"Supprimé ancien log: {log_file.name}")
            except Exception as e:
                self.log_error(e, f"cleanup_logs_{log_file.name}")

    def _compress_old_logs(self):
        """Compresse les logs anciens"""
        cutoff = datetime.now() - timedelta(days=7)

        for log_file in self.log_dir.glob("*.log.*"):
            if log_file.suffix == '.gz':
                continue

            try:
                file_time = datetime.fromtimestamp(log_file.stat().st_mtime)
                if file_time < cutoff:
                    # Compresser le fichier
                    with open(log_file, 'rb') as f_in:
                        with gzip.open(f"{log_file}.gz", 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)

                    # Supprimer l'original
                    log_file.unlink()
                    self.log_main(f"Compressé log: {log_file.name}")
            except Exception as e:
                self.log_error(e, f"compress_logs_{log_file.name}")

    def export_metrics(self, output_file: Optional[str] = None) -> Dict[str, Any]:
        """Exporte toutes les métriques"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = str(self.log_dir / f"metrics_export_{timestamp}.json")

        export_data = {
            'export_timestamp': datetime.now().isoformat(),
            'validation_stats': self.get_validation_stats(),
            'correction_stats': self.get_correction_stats(),
            'performance_stats': self.get_performance_stats(),
            'error_stats': self.get_error_stats(),
            'raw_metrics': dict(self.metrics)
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

        self.log_main(f"Métriques exportées: {output_file}")
        return export_data


# Instance globale du logger
athalia_logger = AthaliaLogger()


# Fonctions de convenance
def log_main(message: str, level: str = 'INFO', **kwargs):
    """Log dans le logger principal"""
    athalia_logger.log_main(message, level, **kwargs)


def log_validation(test_name: str, result: Dict[str, Any], duration: float):
    """Log des résultats de validation"""
    athalia_logger.log_validation(test_name, result, duration)


def log_correction(file_path: str, correction_type: str, success: bool,
                  old_content: str, new_content: str, duration: float):
    """Log des corrections automatiques"""
    athalia_logger.log_correction(file_path, correction_type, success,
                                 old_content, new_content, duration)


def log_performance(operation: str, duration: float, memory_mb: Optional[float] = None,
                   cpu_percent: Optional[float] = None, **kwargs):
    """Log des métriques de performance"""
    athalia_logger.log_performance(operation, duration, memory_mb, cpu_percent, **kwargs)


def log_error(error: Exception, context: str = "", **kwargs):
    """Log des erreurs"""
    athalia_logger.log_error(error, context, **kwargs) 