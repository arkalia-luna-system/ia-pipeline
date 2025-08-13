"""
Plugin d'export Docker
"""


def run():
    """Fonction principale du plugin Docker"""
    return {"message": "Docker export plugin", "status": "success"}


def get_info():
    """Informations sur le plugin"""
    return {
        "name": "Docker Export Plugin",
        "version": "1.0.0",
        "description": "Plugin d'export Docker",
    }
