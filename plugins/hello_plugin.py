"""
Plugin de démonstration Hello World
"""

def run():
    """Fonction principale du plugin"""
    return {"message": "Hello from plugin!", "status": "success"}

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "Hello Plugin",
        "version": "1.0.0",
        "description": "Plugin de démonstration"
    } 