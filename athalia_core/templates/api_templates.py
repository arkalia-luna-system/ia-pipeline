"""
Templates API professionnels pour génération de code modulaire.
"""

def get_api_templates():
    """Retourne les templates API enrichis."""
    return {
        "api/main.py": '''"""
API principale du projet {{ project_name }}.
Généré automatiquement par Athalia/Arkalia.
"""

from flask import Flask, request, jsonify, abort
import logging
import os
from typing import Dict, Any
from functools import wraps

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

API_KEY = os.getenv('API_KEY', 'sk-123456')

# Décorateur d'authentification par clé API
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('X-API-KEY')
        if not key or key != API_KEY:
            logger.warning('Clé API manquante ou invalide')
            return jsonify({'error': 'Clé API invalide'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de santé de l'API."""
    return jsonify({
        'status': 'ok',
        'service': '{{ project_name }}',
        'version': '1.0.0'
    })

@app.route('/api/info', methods=['GET'])
@require_api_key
def info():
    """Endpoint d'information sur le projet."""
    return jsonify({
        'project': '{{ project_name }}',
        'description': 'API générée automatiquement',
        'author': 'Athalia/Arkalia',
        'timestamp': '{{ timestamp }}'
    })

@app.route('/api/process', methods=['POST'])
@require_api_key
def process_data():
    """Endpoint principal de traitement avec authentification."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Données manquantes'}), 400
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
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
    } 