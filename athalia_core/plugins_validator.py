import importlib.util
import os
import sys
import types

def validate_plugin(plugin_path: str) -> dict:
    """Valide un plugin Python : héritage, méthode run/execute, docstring."""
    result = {"valid": False, "errors": [], "class_name": None}
    if not os.path.exists(plugin_path):
        result["errors"].append("Fichier introuvable")
        return result
    try:
        spec = importlib.util.spec_from_file_location("plugin_module", plugin_path)
        if spec is None or spec.loader is None:
            result["errors"].append("Impossible de charger le module (spec ou loader manquant)")
            return result
        module = importlib.util.module_from_spec(spec)
        sys.modules["plugin_module"] = module
        spec.loader.exec_module(module)
        # Chercher une classe héritant de Plugin
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and "Plugin" in [base.__name__ for base in obj.__bases__]:
                result["class_name"] = name
                # Vérifier la docstring
                if not obj.__doc__ or len(obj.__doc__.strip()) < 5:
                    result["errors"].append("Classe sans docstring")
                # Vérifier la méthode run ou execute
                if not (hasattr(obj, "run") or hasattr(obj, "execute")):
                    result["errors"].append("Classe sans méthode run/execute")
                result["valid"] = len(result["errors"]) == 0
                return result
        result["errors"].append("Aucune classe héritant de Plugin trouvée")
    except Exception as e:
        result["errors"].append(f"Erreur d'import : {e}")
    return result 