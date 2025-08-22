# Guide de Correction des Erreurs de Linting - Athalia

**Dernière mise à jour :** 20 Août 2025  
**Version :** v12.0.0  
**Statut :** ✅ ACTIF ET MAINTENU

## 🎯 **Erreurs Récurrentes et Solutions**

### **1. Correction Automatique Rapide**

```bash
# Corriger toutes les erreurs de formatage
black athalia_core/
ruff check athalia_core/ --fix

# Corriger les lignes trop longues
black athalia_core/ --line-length 88
```

### **2. Correction par Type d'Erreur**

#### **E501 - Lignes trop longues**
```bash
# Trouver les lignes trop longues
ruff check athalia_core/ --select E501

# Corriger automatiquement
black athalia_core/
```

#### **F841 - Variables inutilisées**
```bash
# Trouver les variables inutilisées
ruff check athalia_core/ --select F841

# Correction manuelle nécessaire - supprimer ou utiliser la variable
```

#### **E302/E305 - Espaces entre fonctions/classes**
```bash
# Trouver les erreurs E302/E305
ruff check athalia_core/ --select E302,E305

# Corriger automatiquement
black athalia_core/
```

#### **F841 - Variables inutilisées**
```bash
# Trouver les variables inutilisées
ruff check athalia_core/ --select F841

# Correction manuelle nécessaire - supprimer ou utiliser la variable
```

### **3. Workflow de Correction Recommandé**

```bash
# Étape 1: Vérifier l'état actuel
ruff check athalia_core/

# Étape 2: Corriger le formatage automatiquement
black athalia_core/
ruff check athalia_core/ --fix

# Étape 3: Vérifier le résultat
ruff check athalia_core/

# Étape 5: Corriger manuellement les F841 restantes
```

### **4. Commandes Utiles**

#### **Vérifier un fichier spécifique**
```bash
ruff check athalia_core/unified_orchestrator.py
```

#### **Corriger un fichier spécifique**
```bash
black athalia_core/core/unified_orchestrator.py
ruff check athalia_core/core/unified_orchestrator.py --fix
```

#### **Voir les erreurs par fichier**
```bash
ruff check athalia_core/ --count
```

### **5. Correction Manuelle des F841**

Pour les variables inutilisées, vous devez :

1. **Supprimer la variable** si elle n'est pas nécessaire
2. **Utiliser la variable** si elle devrait être utilisée
3. **Préfixer avec underscore** si c'est intentionnel : `_variable`

Exemple :
```python
# Avant (F841)
result = some_function()
print("Done")

# Après (corrigé)
some_function()  # Variable supprimée
print("Done")
```

### **6. Alias Utiles**

Ajoutez ces alias à votre `.bashrc` ou `.zshrc` :

```bash
# Correction rapide de linting
alias ath-lint-fix="black athalia_core/ && ruff check athalia_core/ --fix"

# Vérification rapide
alias ath-lint-check="ruff check athalia_core/"

# Workflow complet
alias ath-lint-clean="ath-lint-fix && ath-lint-check"
```

### **7. Prévention**

#### **Configuration VS Code/Cursor**
Ajoutez dans vos paramètres :
```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "editor.formatOnSave": true
}
```

#### **Pre-commit Hook**
Installez `pre-commit` et ajoutez :
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        args: [--line-length=88]
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]
```

## 🎯 **Résumé des Commandes Essentielles**

```bash
# Correction complète en une commande
black athalia_core/ && ruff check athalia_core/ --fix

# Vérification
ruff check athalia_core/
```

**Utilisez ces commandes au lieu de scripts automatisés pour garder le contrôle !**
