#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from typing import Dict

logger = logging.getLogger(__name__)


def get_base_templates() -> Dict[str, str]:
    """Retourne les templates de base pour tous les projets."""

    return {
        "api/main.py": (
            '''"""
API principale du projet.
"""

import logging
import json
import os
from flask import Flask, request, jsonify
from typing import Dict, Any

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de santé de l'API."""
    return jsonify({
        'status': 'ok',
        'service': '{{ project_name }}',
        'version': '1.0.0'
    })

@app.route('/api/process', methods=['POST'])
def process_data():
    """Endpoint principal de traitement."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Données manquantes'}), 400

        # Traitement des données
        result = process_request(data)

        return jsonify({
            'status': 'success',
            'result': result,
            'timestamp': '{{ timestamp }}'
        })

    except Exception as e:
        logger.error(f"Erreur traitement: {e}")
        return jsonify({'error': 'Erreur interne'}), 500

def process_request(data: Dict[str, Any]) -> Dict[str, Any]:
    """Traite la requête et retourne le résultat."""
    # Logique de traitement personnalisable
    return {
        'processed': True,
        'input_data': data,
        'message': 'Traitement réussi'
    }

@app.errorhandler(404)
def not_found(error):
    """Gestionnaire d'erreur 404."""
    return jsonify({'error': 'Endpoint non trouvé'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Gestionnaire d'erreur 500."""
    return jsonify({'error': 'Erreur interne du serveur'}), 500

if __name__ == '__main__':
    logger.info("Démarrage de l'API {{ project_name }}")
    app.run(debug=os.getenv('DEBUG', 'false').lower() == 'true', host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
'''
        ),
        "tts/tts.py": (
            '''"""
Module de synthèse vocale.
"""

import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class TTSManager:
    """Gestionnaire de synthèse vocale."""

    def __init__(self):
        self.available_voices = ['fr', 'en', 'es']
        self.default_voice = 'fr'
        self.volume = 0.8

    def synthesize_speech(self, text: str, voice: Optional[str] = None) -> Dict[str, Any]:
        """
        Synthétise du texte en parole.

        Args:
            text: Texte à synthétiser
            voice: Voix à utiliser (optionnel)

        Returns:
            Dict avec les informations de synthèse
        """
        try:
            if not text:
                raise ValueError("Texte manquant")

            voice = voice or self.default_voice
            if voice not in self.available_voices:
                voice = self.default_voice

            # Simulation de synthèse vocale
            audio_data = self._generate_audio(text, voice)

            return {
                'status': 'success',
                'text': text,
                'voice': voice,
                'audio_length': len(audio_data),
                'volume': self.volume
            }

        except Exception as e:
            logger.error(f"Erreur synthèse vocale: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def _generate_audio(self, text: str, voice: str) -> bytes:
        """Génère les données audio (simulation)."""
        # Simulation - en production, utiliser une vraie TTS
        return f"audio_{voice}_{len(text)}".encode()

    def set_volume(self, volume: float):
        """Ajuste le volume (0.0 à 1.0)."""
        self.volume = max(0.0, min(1.0, volume))
        logger.info(f"Volume ajusté à {self.volume}")

    def get_available_voices(self) -> list:
        """Retourne la liste des voix disponibles."""
        return self.available_voices.copy()

# Instance globale
tts_manager = TTSManager()

def main():
    """Test du module TTS."""
    test_text = "Bonjour, ceci est un test de synthèse vocale."
    result = tts_manager.synthesize_speech(test_text, 'fr')
    logger.info(f"Résultat TTS: {result}")

if __name__ == "__main__":
    main()
'''
        ),
        "memory/memory.py": (
            '''"""
Module de gestion mémoire et stockage.
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class MemoryManager:
    """Gestionnaire de mémoire et stockage."""

    def __init__(self, storage_file: str = "memory.json"):
        self.storage_file = storage_file
        self.memory = {}
        self.load_memory()

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> Dict[str, Any]:
        """
        Stocke une valeur avec une clé.

        Args:
            key: Clé de stockage
            value: Valeur à stocker
            ttl: Time to live en secondes (optionnel)

        Returns:
            Dict avec le statut de l'opération
        """
        try:
            timestamp = datetime.now().isoformat()
            self.memory[key] = {
                'value': value,
                'timestamp': timestamp,
                'ttl': ttl
            }

            self.save_memory()
            logger.info(f"Valeur stockée: {key}")

            return {
                'status': 'success',
                'key': key,
                'timestamp': timestamp
            }

        except Exception as e:
            logger.error(f"Erreur stockage: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def get(self, key: str) -> Dict[str, Any]:
        """
        Récupère une valeur par sa clé.

        Args:
            key: Clé de récupération

        Returns:
            Dict avec la valeur ou une erreur
        """
        try:
            if key not in self.memory:
                return {
                    'status': 'error',
                    'error': 'Clé non trouvée'
                }

            item = self.memory[key]

            # Vérifier le TTL
            if item.get('ttl'):
                # Logique de vérification TTL simplifiée
                pass

            return {
                'status': 'success',
                'key': key,
                'value': item['value'],
                'timestamp': item['timestamp']
            }

        except Exception as e:
            logger.error(f"Erreur récupération: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def delete(self, key: str) -> Dict[str, Any]:
        """
        Supprime une valeur par sa clé.

        Args:
            key: Clé à supprimer

        Returns:
            Dict avec le statut de l'opération
        """
        try:
            if key in self.memory:
                del self.memory[key]
                self.save_memory()
                logger.info(f"Valeur supprimée: {key}")
                return {
                    'status': 'success',
                    'key': key
                }
            else:
                return {
                    'status': 'error',
                    'error': 'Clé non trouvée'
                }

        except Exception as e:
            logger.error(f"Erreur suppression: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def load_memory(self):
        """Charge la mémoire depuis le fichier."""
        try:
            with open(self.storage_file, 'r') as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = {}
        except Exception as e:
            logger.error(f"Erreur chargement mémoire: {e}")
            self.memory = {}

    def save_memory(self):
        """Sauvegarde la mémoire dans le fichier."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.memory, f, indent=2)
        except Exception as e:
            logger.error(f"Erreur sauvegarde mémoire: {e}")

# Instance globale
memory_manager = MemoryManager()

def main():
    """Test du module mémoire."""
    # Test de stockage
    result = memory_manager.set('test_key', 'test_value')
    logger.info(f"Stockage: {result}")

    # Test de récupération
    result = memory_manager.get('test_key')
    logger.info(f"Récupération: {result}")

if __name__ == "__main__":
    main()
'''
        ),
    }
