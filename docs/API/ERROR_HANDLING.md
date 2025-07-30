# 🛡️ Gestion d'Erreurs - Athalia

**Section :** Documentation API - Gestion d'Erreurs  
**Date :** 29 juillet 2025

---

## 🎯 **Vue d'Ensemble**

Système de gestion d'erreurs centralisé et standardisé pour Athalia.

---

## 📋 **Modules de Gestion d'Erreurs**

### **🔢 Codes d'Erreur**

#### `error_codes.py`
**Classes :** `ErrorCode`, `ErrorSeverity`

Système de codes d'erreur standardisés avec niveaux de sévérité.

```python
from athalia_core.error_codes import (
    ErrorCode, ErrorSeverity, 
    get_error_description, get_error_severity,
    format_error_message
)

# Utiliser les codes d'erreur
error_code = ErrorCode.FILE_NOT_FOUND
severity = get_error_severity(error_code)
description = get_error_description(error_code)

# Formater un message d'erreur
message = format_error_message(
    ErrorCode.INVALID_INPUT,
    "Données invalides",
    {"field": "email", "value": "invalid"}
)
```

**Catégories d'erreurs :**

| Catégorie | Plage | Exemples |
|-----------|-------|----------|
| **Générales** | 1000-1999 | `UNKNOWN_ERROR`, `INVALID_INPUT` |
| **Fichiers** | 2000-2999 | `FILE_NOT_FOUND`, `FILE_CORRUPTED` |
| **Modules** | 3000-3999 | `MODULE_NOT_FOUND`, `MODULE_IMPORT_ERROR` |
| **IA** | 4000-4999 | `AI_MODEL_NOT_AVAILABLE`, `AI_RESPONSE_TIMEOUT` |
| **Génération** | 5000-5999 | `GENERATION_FAILED`, `BLUEPRINT_INVALID` |
| **Tests** | 6000-6999 | `TEST_FAILED`, `COVERAGE_BELOW_THRESHOLD` |
| **CI/CD** | 7000-7999 | `CI_PIPELINE_FAILED`, `BUILD_FAILED` |
| **Sécurité** | 8000-8999 | `SECURITY_VIOLATION`, `VULNERABILITY_DETECTED` |
| **Performance** | 9000-9999 | `PERFORMANCE_DEGRADED`, `MEMORY_EXHAUSTED` |

---

### **🎛️ Gestionnaire d'Erreurs**

#### `error_handling.py`
**Classes :** `AthaliaError`, `ErrorHandler`

Système complet de gestion d'erreurs avec logging et callbacks.

```python
from athalia_core.error_handling import (
    AthaliaError, ErrorHandler, 
    get_error_handler, handle_error,
    raise_athalia_error, error_handler, ErrorContext
)

# Créer une erreur personnalisée
error = AthaliaError(
    error_code=ErrorCode.FILE_NOT_FOUND,
    message="Configuration manquante",
    details="config.yml",
    context={"path": "/app/config"}
)

# Utiliser le gestionnaire global
handler = get_error_handler()
summary = handler.get_error_summary()

# Gérer une erreur automatiquement
try:
    # Code qui peut échouer
    pass
except Exception as e:
    athalia_error = handle_error(e, {"context": "validation"})

# Lever une erreur avec gestion automatique
raise_athalia_error(
    ErrorCode.INVALID_CONFIGURATION,
    "Configuration invalide",
    "Section manquante"
)
```

**Fonctionnalités avancées :**

#### **Décorateur de gestion d'erreurs**
```python
@error_handler(ErrorCode.INVALID_INPUT)
def process_data(data):
    # Code qui peut échouer
    return validate_and_process(data)
```

#### **Context Manager**
```python
with ErrorContext(ErrorCode.FILE_ACCESS_DENIED, {"file": "config.yml"}):
    # Code protégé
    config = load_config("config.yml")
```

#### **Callbacks personnalisés**
```python
def on_critical_error(error):
    send_alert(f"Erreur critique: {error}")

handler = get_error_handler()
handler.register_callback(ErrorCode.SECURITY_VIOLATION, on_critical_error)
```

---

## 🚀 **Exemples d'Utilisation**

### **Exemple 1 : Validation de données**
```python
from athalia_core.error_handling import AthaliaError, ErrorCode

def validate_user_data(user_data):
    if not user_data.get('email'):
        raise AthaliaError(
            ErrorCode.MISSING_REQUIRED_PARAMETER,
            "Email requis",
            "Champ email manquant",
            {"user_id": user_data.get('id')}
        )
    
    if not is_valid_email(user_data['email']):
        raise AthaliaError(
            ErrorCode.INVALID_INPUT,
            "Email invalide",
            user_data['email'],
            {"field": "email"}
        )
```

### **Exemple 2 : Gestion de fichiers**
```python
from athalia_core.error_handling import handle_error, ErrorContext

def load_project_config(project_path):
    with ErrorContext(ErrorCode.FILE_NOT_FOUND, {"project": project_path}):
        config_file = Path(project_path) / "config.yml"
        
        if not config_file.exists():
            raise FileNotFoundError(f"Config introuvable: {config_file}")
        
        return yaml.safe_load(config_file.read_text())
```

### **Exemple 3 : Monitoring d'erreurs**
```python
from athalia_core.error_handling import get_error_handler

def generate_error_report():
    handler = get_error_handler()
    summary = handler.get_error_summary()
    
    if summary['has_critical_errors']:
        print("⚠️ Erreurs critiques détectées:")
        for error in summary['critical_error_details']:
            print(f"  - {error['message']} ({error['error_code']})")
    
    return summary
```

---

## 🔗 **Navigation**

- [← Retour à l'index API](INDEX.md)
- [→ Modules principaux](CORE_MODULES.md)
- [→ Configuration](CONFIG_MANAGER.md)

---

*Documentation générée automatiquement par Athalia - 2025-07-29* 