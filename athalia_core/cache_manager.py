#!/usr/bin/env python3
"""
Module cache_manager pour Athalia
Gestion du cache avec persistance et optimisation
"""

import gzip
import hashlib
import json
import logging
import pickle
import time
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import yaml

logger = logging.getLogger(__name__)


class CacheManager:
    """Gestionnaire de cache avec persistance"""

    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_config = self.load_cache_config()
        self.cache_stats = {"hits": 0, "misses": 0, "total_entries": 0, "total_size": 0}

    def load_cache_config(self, config_path: Optional[str] = None) -> Dict[str, Any]:
        """Charge la configuration du cache"""
        default_config = {
            "max_size_mb": 100,
            "ttl_hours": 24,
            "compression": False,
            "encryption": False,
            "backup_enabled": True,
            "cleanup_interval_hours": 6,
            "serialization_format": "json",
        }

        if config_path:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    user_config = yaml.safe_load(f)
                    default_config.update(user_config)
            except Exception as e:
                logger.warning(
                    f"Impossible de charger la configuration {config_path}: {e}"
                )

        return default_config

    def set_cache(
        self,
        key: str,
        value: Any,
        ttl_seconds: Optional[int] = None,
        compress: bool = False,
        encrypt: bool = False,
        format: str = "json",
    ) -> bool:
        """Met une valeur en cache"""
        try:
            if not key or not key.strip():
                logger.error("Clé de cache invalide")
                return False

            if value is None:
                logger.error("Valeur de cache invalide")
                return False

            # Préparer les données
            cache_data = {
                "value": value,
                "timestamp": time.time(),
                "ttl": ttl_seconds or (self.cache_config["ttl_hours"] * 3600),
                "compressed": compress,
                "encrypted": encrypt,
                "format": format,
            }

            # Sérialiser les données
            if format == "json":
                serialized_data = json.dumps(cache_data, default=str).encode("utf-8")
            elif format == "pickle":
                serialized_data = pickle.dumps(cache_data)
            else:
                logger.error(f"Format de sérialisation non supporté: {format}")
                return False

            # Compresser si demandé
            if compress:
                serialized_data = gzip.compress(serialized_data)

            # Chiffrer si demandé
            if encrypt:
                # Chiffrement simple pour l'exemple
                key_hash = hashlib.md5(key.encode()).hexdigest()
                serialized_data = self._simple_encrypt(serialized_data, key_hash)

            # Sauvegarder dans le fichier
            cache_file = self.cache_dir / f"{key}.cache"
            with open(cache_file, "wb") as f:
                f.write(serialized_data)

            # Mettre à jour les statistiques
            self.cache_stats["total_entries"] += 1
            self.cache_stats["total_size"] += len(serialized_data)

            return True

        except Exception as e:
            logger.error(f"Erreur mise en cache {key}: {e}")
            return False

    def get_cache(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache"""
        try:
            cache_file = self.cache_dir / f"{key}.cache"

            if not cache_file.exists():
                self.cache_stats["misses"] += 1
                return None

            # Lire le fichier
            with open(cache_file, "rb") as f:
                serialized_data = f.read()

            # Déchiffrer si nécessaire
            if self._is_encrypted(serialized_data):
                key_hash = hashlib.md5(key.encode()).hexdigest()
                serialized_data = self._simple_decrypt(serialized_data, key_hash)

            # Décompresser si nécessaire
            if self._is_compressed(serialized_data):
                serialized_data = gzip.decompress(serialized_data)

            # Désérialiser
            try:
                # Essayer JSON d'abord (format par défaut)
                try:
                    cache_data = json.loads(serialized_data.decode("utf-8"))
                except (json.JSONDecodeError, UnicodeDecodeError):
                    # Sinon essayer pickle
                    try:
                        cache_data = pickle.loads(serialized_data)
                    except (pickle.UnpicklingError, EOFError):
                        logger.error(
                            f"Impossible de désérialiser les données pour {key}"
                        )
                        return None
            except Exception as e:
                logger.error(f"Erreur désérialisation {key}: {e}")
                return None

            # Vérifier l'expiration
            if self._is_expired(cache_data):
                self.delete_cache(key)
                self.cache_stats["misses"] += 1
                return None

            # Mettre à jour les statistiques
            self.cache_stats["hits"] += 1

            return cache_data["value"]

        except Exception as e:
            logger.error(f"Erreur récupération cache {key}: {e}")
            self.cache_stats["misses"] += 1
            return None

    def delete_cache(self, key: str) -> bool:
        """Supprime une entrée du cache"""
        try:
            cache_file = self.cache_dir / f"{key}.cache"

            if cache_file.exists():
                # Mettre à jour les statistiques
                file_size = cache_file.stat().st_size
                self.cache_stats["total_entries"] -= 1
                self.cache_stats["total_size"] -= file_size

                cache_file.unlink()
                return True

            return False

        except Exception as e:
            logger.error(f"Erreur suppression cache {key}: {e}")
            return False

    def clear_all_cache(self) -> bool:
        """Nettoie tout le cache"""
        try:
            cache_files = list(self.cache_dir.glob("*.cache"))

            for cache_file in cache_files:
                try:
                    cache_file.unlink()
                except Exception as e:
                    logger.warning(f"Impossible de supprimer {cache_file}: {e}")

            # Réinitialiser les statistiques
            self.cache_stats = {
                "hits": 0,
                "misses": 0,
                "total_entries": 0,
                "total_size": 0,
            }

            return True

        except Exception as e:
            logger.error(f"Erreur nettoyage cache: {e}")
            return False

    def get_cache_keys(self) -> List[str]:
        """Récupère toutes les clés du cache"""
        try:
            cache_files = list(self.cache_dir.glob("*.cache"))
            keys = []

            for cache_file in cache_files:
                key = cache_file.stem  # Nom du fichier sans extension
                if self.is_cache_valid(key):
                    keys.append(key)

            return keys

        except Exception as e:
            logger.error(f"Erreur récupération clés cache: {e}")
            return []

    def get_cache_size(self) -> int:
        """Calcule la taille totale du cache"""
        try:
            total_size = 0
            cache_files = list(self.cache_dir.glob("*.cache"))

            for cache_file in cache_files:
                total_size += cache_file.stat().st_size

            return total_size

        except Exception as e:
            logger.error(f"Erreur calcul taille cache: {e}")
            return 0

    def is_cache_valid(self, key: str) -> bool:
        """Vérifie si une entrée du cache est valide"""
        try:
            cache_file = self.cache_dir / f"{key}.cache"

            if not cache_file.exists():
                return False

            # Lire les métadonnées
            with open(cache_file, "rb") as f:
                serialized_data = f.read()

            # Déchiffrer si nécessaire
            if self._is_encrypted(serialized_data):
                key_hash = hashlib.md5(key.encode()).hexdigest()
                serialized_data = self._simple_decrypt(serialized_data, key_hash)

            # Décompresser si nécessaire
            if self._is_compressed(serialized_data):
                serialized_data = gzip.decompress(serialized_data)

            # Désérialiser
            try:
                # Essayer JSON d'abord (format par défaut)
                try:
                    cache_data = json.loads(serialized_data.decode("utf-8"))
                except (json.JSONDecodeError, UnicodeDecodeError):
                    # Sinon essayer pickle
                    try:
                        cache_data = pickle.loads(serialized_data)
                    except (pickle.UnpicklingError, EOFError):
                        # Dernier essai avec gestion d'erreur
                        return False
            except (OSError, IOError):
                return False

            return not self._is_expired(cache_data)

        except Exception as e:
            logger.error(f"Erreur validation cache {key}: {e}")
            return False

    def get_cache_stats(self) -> Dict[str, Any]:
        """Récupère les statistiques du cache"""
        try:
            # Calculer les statistiques actuelles
            current_keys = self.get_cache_keys()
            current_size = self.get_cache_size()

            stats = {
                "total_entries": len(current_keys),
                "total_size": current_size,
                "hits": self.cache_stats["hits"],
                "misses": self.cache_stats["misses"],
                "hit_rate": self.calculate_hit_rate(),
                "max_size_mb": self.cache_config["max_size_mb"],
                "ttl_hours": self.cache_config["ttl_hours"],
            }

            return stats

        except Exception as e:
            logger.error(f"Erreur statistiques cache: {e}")
            return {}

    def calculate_hit_rate(self) -> float:
        """Calcule le taux de hit du cache"""
        total_requests = self.cache_stats["hits"] + self.cache_stats["misses"]

        if total_requests == 0:
            return 0.0

        return self.cache_stats["hits"] / total_requests

    def backup_cache(self, backup_path: str) -> bool:
        """Sauvegarde le cache"""
        try:
            cache_data = {}
            cache_keys = self.get_cache_keys()

            for key in cache_keys:
                value = self.get_cache(key)
                if value is not None:
                    cache_data[key] = value

            with open(backup_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, default=str, indent=2)

            return True

        except Exception as e:
            logger.error(f"Erreur sauvegarde cache: {e}")
            return False

    def restore_cache(self, backup_path: str) -> bool:
        """Restaure le cache depuis une sauvegarde"""
        try:
            with open(backup_path, "r", encoding="utf-8") as f:
                cache_data = json.load(f)

            for key, value in cache_data.items():
                self.set_cache(key, value)

            return True

        except Exception as e:
            logger.error(f"Erreur restauration cache: {e}")
            return False

    def cleanup_expired_entries(self) -> int:
        """Nettoie les entrées expirées"""
        try:
            cleaned_count = 0
            cache_keys = self.get_cache_keys()

            for key in cache_keys:
                if not self.is_cache_valid(key):
                    if self.delete_cache(key):
                        cleaned_count += 1

            return cleaned_count

        except Exception as e:
            logger.error(f"Erreur nettoyage entrées expirées: {e}")
            return 0

    def cleanup_by_size_limit(self, max_size_mb: Optional[int] = None) -> int:
        """Nettoie le cache par limite de taille"""
        try:
            if max_size_mb is None:
                max_size_mb = self.cache_config["max_size_mb"]

            max_size_bytes = max_size_mb * 1024 * 1024
            current_size = self.get_cache_size()

            if current_size <= max_size_bytes:
                return 0

            # Récupérer les fichiers avec leur taille et date de modification
            cache_files = []
            for cache_file in self.cache_dir.glob("*.cache"):
                stat = cache_file.stat()
                cache_files.append(
                    {"file": cache_file, "size": stat.st_size, "mtime": stat.st_mtime}
                )

            # Trier par date de modification (plus ancien en premier)
            cache_files.sort(key=lambda x: x["mtime"])

            cleaned_count = 0
            current_size = self.get_cache_size()

            for cache_file_info in cache_files:
                if current_size <= max_size_bytes:
                    break

                key = cache_file_info["file"].stem
                if self.delete_cache(key):
                    cleaned_count += 1
                    current_size -= cache_file_info["size"]

            return cleaned_count

        except Exception as e:
            logger.error(f"Erreur nettoyage par taille: {e}")
            return 0

    def _is_expired(self, cache_data: Dict[str, Any]) -> bool:
        """Vérifie si les données du cache sont expirées"""
        try:
            timestamp = cache_data.get("timestamp", 0)
            ttl = cache_data.get("ttl", 0)

            current_time = time.time()
            return (current_time - timestamp) > ttl

        except (KeyError, TypeError, ValueError) as cache_error:
            logger.warning(
                f"Erreur lors de la vérification d'expiration du cache: {cache_error}"
            )
            return True

    def _is_compressed(self, data: bytes) -> bool:
        """Vérifie si les données sont compressées"""
        if len(data) < 2:
            return False

        # Vérifier la signature gzip (0x1f 0x8b)
        if data.startswith(b"\x1f\x8b"):
            return True

        # Vérifier la signature zlib
        if data.startswith(b"\x78\x9c") or data.startswith(b"\x78\xda"):
            return True

        # Essayer de décompresser comme dernier recours
        try:
            gzip.decompress(data)
            return True
        except (OSError, ValueError):
            return False

    def _is_encrypted(self, data: bytes) -> bool:
        """Vérifie si les données sont chiffrées"""
        # Vérifier si les données commencent par JSON ou pickle
        if len(data) == 0:
            return False

        # Vérifier d'abord si c'est compressé
        if self._is_compressed(data):
            return False

        # JSON commence par '{'
        if data.startswith(b"{"):
            return False

        # Pickle commence par des bytes spécifiques
        if data.startswith(b"\x80"):
            return False

        # Si ce n'est ni JSON ni pickle ni compressé, c'est probablement chiffré
        return True

    def _simple_encrypt(self, data: Union[str, bytes], key: str) -> bytes:
        """Chiffrement simple pour l'exemple"""
        if isinstance(data, str):
            data = data.encode()

        key_bytes = key.encode()
        encrypted = bytearray()

        for i, byte in enumerate(data):
            key_byte = key_bytes[i % len(key_bytes)]
            encrypted.append(byte ^ key_byte)

        return bytes(encrypted)

    def _simple_decrypt(self, data: bytes, key: str) -> bytes:
        """Déchiffrement simple pour l'exemple"""
        return self._simple_encrypt(data, key)  # XOR est symétrique


def cache_function(cache_dir: str = ".cache", ttl_seconds: Optional[int] = None):
    """Décorateur pour mettre en cache une fonction"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_manager = CacheManager(cache_dir)

            # Créer une clé unique basée sur la fonction et ses arguments
            key_parts = [func.__name__]
            key_parts.extend([str(arg) for arg in args])
            key_parts.extend([f"{k}={v}" for k, v in sorted(kwargs.items())])
            cache_key = hashlib.md5("|".join(key_parts).encode()).hexdigest()

            # Essayer de récupérer du cache
            cached_result = cache_manager.get_cache(cache_key)
            if cached_result is not None:
                return cached_result

            # Exécuter la fonction
            result = func(*args, **kwargs)

            # Mettre en cache
            cache_manager.set_cache(cache_key, result, ttl_seconds=ttl_seconds)

            return result

        return wrapper

    return decorator


def clear_cache(cache_dir: str = ".cache") -> bool:
    """Fonction utilitaire pour nettoyer le cache"""
    cache_manager = CacheManager(cache_dir)
    return cache_manager.clear_all_cache()


def get_cache_stats(cache_dir: str = ".cache") -> Dict[str, Any]:
    """Fonction utilitaire pour obtenir les statistiques du cache"""
    cache_manager = CacheManager(cache_dir)
    return cache_manager.get_cache_stats()
