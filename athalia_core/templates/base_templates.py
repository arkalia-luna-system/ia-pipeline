#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Templates de base pour Athalia
"""
from typing import Dict, Any

def get_base_templates() -> Dict[str, str]:
    """Retourne les templates de base disponibles"""
    return {
        "api/main.py": '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{{ project_name }} - API {{ api_framework | title }}
Auteur: {{ author }}
Version: {{ version }}
"""

import logging
from flask import Flask, request, jsonify
from typing import Dict, Any

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Point de terminaison de santé"""
    return jsonify({"status": "healthy", "service": "{{ project_name }}"})

@app.route('/api/data', methods=['GET'])
def get_data():
    """Récupérer des données"""
    return jsonify({"data": []})

@app.route('/api/data', methods=['POST'])
def create_data():
    """Créer des données"""
    data = request.get_json()
    return jsonify({"message": "Données créées", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port={{ port | default(8000) }})
''',

        "memory/memory.py": '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de mémoire pour le projet.
"""

import logging
import json
from typing import Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class MemoryManager:
    """Gestionnaire de mémoire simple"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.max_size = self.config.get('max_size', 1000)
        self.data = {}
        
        logger.info("Memory Manager initialisé")
    
    def set(self, key: str, value: Any) -> bool:
        """Stocke une valeur"""
        try:
            if len(self.data) >= self.max_size:
                # Supprimer l'entrée la plus ancienne
                oldest_key = next(iter(self.data))
                del self.data[oldest_key]
            
            self.data[key] = value
            logger.debug(f"Valeur stockée pour la clé: {key}")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors du stockage de {key}: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Récupère une valeur"""
        return self.data.get(key, default)
    
    def delete(self, key: str) -> bool:
        """Supprime une valeur"""
        if key in self.data:
            del self.data[key]
            return True
        return False
    
    def clear(self) -> bool:
        """Vide toute la mémoire"""
        self.data.clear()
        logger.info("Mémoire vidée")
        return True
    
    def size(self) -> int:
        """Retourne la taille de la mémoire"""
        return len(self.data)

# Instance globale
memory = MemoryManager()

if __name__ == "__main__":
    # Test du gestionnaire de mémoire
    memory.set("test_key", {"message": "Hello World"})
    value = memory.get("test_key")
    print(f"Valeur récupérée: {value}")
    print(f"Taille de la mémoire: {memory.size()}")
''',

        "tts/tts.py": '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système Text-to-Speech pour le projet.
"""

import logging
import os
from typing import Optional, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)

class TTSManager:
    """Système de synthèse vocale simple"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.language = self.config.get('language', 'fr')
        self.output_dir = Path(self.config.get('output_dir', 'audio_output'))
        self.output_dir.mkdir(exist_ok=True)
        
        logger.info("TTS Manager initialisé")
    
    def text_to_speech(self, text: str, filename: Optional[str] = None) -> Optional[str]:
        """Convertit du texte en audio (simulation)"""
        try:
            if not filename:
                filename = f"speech_{hash(text) % 10000}.txt"
            
            output_path = self.output_dir / filename
            
            # Simulation TTS
            with open(output_path, 'w') as f:
                f.write(f"# Simulation TTS pour: {text}")
            
            logger.info(f"Audio généré: {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Erreur lors de la génération audio: {e}")
            return None
    
    def get_available_languages(self) -> list:
        """Retourne les langues disponibles"""
        return ['fr', 'en', 'es', 'de', 'it', 'pt']
    
    def set_language(self, language: str) -> bool:
        """Change la langue de synthèse"""
        available_languages = self.get_available_languages()
        if language in available_languages:
            self.language = language
            logger.info(f"Langue changée vers: {language}")
            return True
        else:
            logger.warning(f"Langue non supportée: {language}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """Retourne le statut du système TTS"""
        return {
            "engine": "simulation",
            "language": self.language,
            "output_dir": str(self.output_dir),
            "available_languages": self.get_available_languages(),
            "output_files_count": len(list(self.output_dir.glob("*.txt")))
        }

# Instance globale
tts = TTSManager()

if __name__ == "__main__":
    # Test du système TTS
    test_text = "Bonjour, ceci est un test de synthèse vocale."
    result = tts.text_to_speech(test_text, "test_speech.txt")
    
    if result:
        print(f"✅ Audio généré: {result}")
    else:
        print("❌ Erreur lors de la génération audio")
    
    print(f"Statut: {tts.get_status()}")
'''
    }