# Guide de Correction des Erreurs de Linting

## 🎯 **Erreurs Récurrentes et Solutions**

### **1. Correction Automatique Rapide**

```bash
# Corriger toutes les erreurs de formatage (W293, E302, E305, E301)
autopep8 --in-place --aggressive --aggressive athalia_core/

# Corriger les lignes trop longues (E501)
autopep8 --in-place --max-line-length=79 athalia_core/
```

### **2. Correction par Type d'Erreur**

#### **W293 - Lignes vides avec espaces**
```bash
# Trouver les fichiers avec W293
flake8 athalia_core/ --select=W293

# Corriger automatiquement
autopep8 --in-place --select=W293 athalia_core/
```

#### **E302/E305 - Espaces entre fonctions/classes**
```bash
# Trouver les erreurs E302/E305
flake8 athalia_core/ --select=E302,E305

# Corriger automatiquement
autopep8 --in-place --select=E302,E305 athalia_core/
```

#### **E501 - Lignes trop longues**
```bash
# Trouver les lignes trop longues
flake8 athalia_core/ --select=E501

# Corriger avec limite de 79 caractères
autopep8 --in-place --max-line-length=79 athalia_core/
```

#### **F841 - Variables inutilisées**
```bash
# Trouver les variables inutilisées
flake8 athalia_core/ --select=F841

# Correction manuelle nécessaire - supprimer ou utiliser la variable
```

### **3. Workflow de Correction Recommandé**

```bash
# Étape 1: Vérifier l'état actuel
flake8 athalia_core/ --select=W293,E302,E305,E501,F841

# Étape 2: Corriger le formatage automatiquement
autopep8 --in-place --aggressive --aggressive athalia_core/

# Étape 3: Corriger les lignes trop longues
autopep8 --in-place --max-line-length=79 athalia_core/

# Étape 4: Vérifier le résultat
flake8 athalia_core/ --select=W293,E302,E305,E501,F841

# Étape 5: Corriger manuellement les F841 restantes
```

### **4. Commandes Utiles**

#### **Vérifier un fichier spécifique**
```bash
flake8 athalia_core/unified_orchestrator.py --select=W293,E302,E305,E501,F841
```

#### **Corriger un fichier spécifique**
```bash
autopep8 --in-place --aggressive --aggressive athalia_core/core/unified_orchestrator.py
```

#### **Voir les erreurs par fichier**
```bash
flake8 athalia_core/ --select=W293,E302,E305,E501,F841 --count
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
alias ath-lint-fix="autopep8 --in-place --aggressive --aggressive athalia_core/ && autopep8 --in-place --max-line-length=79 athalia_core/"

# Vérification rapide
alias ath-lint-check="flake8 athalia_core/ --select=W293,E302,E305,E501,F841"

# Workflow complet
alias ath-lint-clean="ath-lint-fix && ath-lint-check"
```

### **7. Prévention**

#### **Configuration VS Code/Cursor**
Ajoutez dans vos paramètres :
```json
{
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": ["--max-line-length=79"],
    "editor.formatOnSave": true
}
```

#### **Pre-commit Hook**
Installez `pre-commit` et ajoutez :
```yaml
repos:
  - repo: https://github.com/pycqa/autopep8
    rev: v2.0.4
    hooks:
      - id: autopep8
        args: [--max-line-length=79]
```

## 🎯 **Résumé des Commandes Essentielles**

```bash
# Correction complète en une commande
autopep8 --in-place --aggressive --aggressive --max-line-length=79 athalia_core/

# Vérification
flake8 athalia_core/ --select=W293,E302,E305,E501,F841
```

**Utilisez ces commandes au lieu de scripts automatisés pour garder le contrôle !**
