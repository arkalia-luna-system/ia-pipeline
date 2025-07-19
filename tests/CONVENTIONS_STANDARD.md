# 📋 Guide de Standardisation des Tests Athalia

## 🎯 Objectifs
- **Cohérence** dans tous les tests
- **Facilité de maintenance** et évolution
- **Documentation claire** des tests
- **Débogage simplifié**

---

## 📁 Conventions de Nommage

### **Fichiers de Test**
```
test_<module>_<fonctionnalité>.py
```

**Exemples :**
- ✅ `test_audit_intelligent.py`
- ✅ `test_athalia_orchestrator_basic.py`
- ✅ `test_aliases_basic.py`
- ❌ `test_ath_dev_boost.py` → `test_ath_dev_boost_menu.py`
- ❌ `test_ci.py` → `test_ci_consolidated.py`

### **Classes de Test**
```python
class Test<Module><Fonctionnalité>(unittest.TestCase):
```

**Exemples :**
- ✅ `class TestAuditIntelligent(unittest.TestCase):`
- ✅ `class TestOrchestratorBasic(unittest.TestCase):`
- ✅ `class TestAliasesBasic(unittest.TestCase):`
- ❌ `class TestRobustAI:` → `class TestAIRobust(unittest.TestCase):`

### **Fonctions de Test**
```python
def test_<fonctionnalité>_<scenario>():
```

**Exemples :**
- ✅ `def test_audit_intelligent_basic():`
- ✅ `def test_orchestrator_initialization():`
- ✅ `def test_aliases_file_exists():`
- ❌ `def test_ath_dev_boost_script_exists():` → `def test_script_exists():`

---

## 📝 Structure Standard

### **En-tête de Fichier**
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour <module> - <description>
Version: <version>
Auteur: <auteur>
"""

import unittest
import pytest
from pathlib import Path
# ... autres imports
```

### **Classe de Test**
```python
class Test<Module><Fonctionnalité>(unittest.TestCase):
    """Tests pour <description>"""
    
    def setUp(self):
        """Initialisation avant chaque test"""
        # Setup code
        
    def tearDown(self):
        """Nettoyage après chaque test"""
        # Cleanup code
        
    def test_<fonctionnalité>_<scenario>(self):
        """Test <description>"""
        # Arrange
        # Act
        # Assert
```

### **Fonctions de Test Indépendantes**
```python
def test_<fonctionnalité>_<scenario>():
    """Test <description>"""
    # Arrange
    # Act
    # Assert
```

---

## 🔧 Conventions Techniques

### **Imports**
```python
# Standard library
import os
import sys
import unittest
from pathlib import Path

# Third party
import pytest

# Local imports
from athalia_core.module import Class
```

### **Gestion des Erreurs**
```python
def test_with_error_handling(self):
    """Test avec gestion d'erreurs"""
    try:
        result = function_that_might_fail()
        self.assertIsNotNone(result)
    except ImportError:
        self.skipTest("Module non disponible")
    except Exception as e:
        self.fail(f"Erreur inattendue: {e}")
```

### **Messages d'Assertion**
```python
# ✅ Bon
self.assertEqual(actual, expected, f"Valeur attendue: {expected}, obtenue: {actual}")

# ❌ Mauvais
self.assertEqual(actual, expected)
```

### **Setup et Teardown**
```python
def setUp(self):
    """Initialisation avant chaque test"""
    self.temp_dir = tempfile.mkdtemp()
    self.test_file = Path(self.temp_dir) / "test.txt"
    
def tearDown(self):
    """Nettoyage après chaque test"""
    shutil.rmtree(self.temp_dir, ignore_errors=True)
```

---

## 📊 Conventions de Documentation

### **Docstrings de Classes**
```python
class TestModuleFunctionality(unittest.TestCase):
    """Tests pour la fonctionnalité <description>
    
    Cette classe teste les aspects suivants :
    - Fonctionnalité A
    - Fonctionnalité B
    - Gestion d'erreurs
    """
```

### **Docstrings de Méthodes**
```python
def test_specific_functionality(self):
    """Test de la fonctionnalité spécifique
    
    Scénario : <description du scénario>
    Données : <description des données de test>
    Résultat attendu : <description du résultat>
    """
```

---

## 🚨 Conventions de Gestion d'Erreurs

### **Tests avec Dépendances Optionnelles**
```python
def test_optional_module(self):
    """Test d'un module optionnel"""
    try:
        import optional_module
        result = optional_module.function()
        self.assertIsNotNone(result)
    except ImportError:
        self.skipTest("Module optionnel non disponible")
```

### **Tests avec Chemins Invalides**
```python
def test_invalid_path(self):
    """Test avec un chemin invalide"""
    try:
        result = function_with_path("/chemin/inexistant")
        self.assertIsNotNone(result)
    except FileNotFoundError:
        # Erreur attendue
        pass
    except Exception as e:
        self.fail(f"Erreur inattendue: {e}")
```

---

## 📈 Conventions de Performance

### **Tests Lents**
```python
@pytest.mark.slow
def test_slow_operation(self):
    """Test d'opération lente"""
    # Test code
```

### **Tests d'Intégration**
```python
@pytest.mark.integration
def test_integration_scenario(self):
    """Test d'intégration"""
    # Test code
```

### **Tests de CI**
```python
@pytest.mark.ci
def test_ci_essential(self):
    """Test essentiel pour la CI"""
    # Test code
```

---

## 🔍 Conventions de Débogage

### **Logging**
```python
import logging

logger = logging.getLogger(__name__)

def test_with_logging(self):
    """Test avec logging"""
    logger.info("Début du test")
    # Test code
    logger.info("Fin du test")
```

### **Assertions Détaillées**
```python
def test_detailed_assertions(self):
    """Test avec assertions détaillées"""
    result = function()
    
    # Vérifications multiples
    self.assertIsNotNone(result, "Le résultat ne doit pas être None")
    self.assertIsInstance(result, dict, "Le résultat doit être un dictionnaire")
    self.assertIn('key', result, "Le résultat doit contenir la clé 'key'")
    self.assertEqual(result['key'], expected_value, 
                    f"Valeur attendue: {expected_value}, obtenue: {result['key']}")
```

---

## ✅ Checklist de Validation

### **Avant de Commiter un Test**
- [ ] Nom du fichier suit la convention `test_<module>_<fonctionnalité>.py`
- [ ] Nom de la classe suit la convention `Test<Module><Fonctionnalité>`
- [ ] Noms des méthodes suivent la convention `test_<fonctionnalité>_<scenario>`
- [ ] Docstrings présentes et informatives
- [ ] Messages d'assertion détaillés
- [ ] Gestion d'erreurs appropriée
- [ ] Setup/Teardown corrects
- [ ] Imports organisés (standard, third-party, local)
- [ ] Tests passent individuellement
- [ ] Tests passent en groupe

---

## 🎯 Prochaines Actions

1. **Audit des conventions actuelles** ✅
2. **Création du guide de standardisation** ✅
3. **Correction des tests les plus problématiques**
4. **Application des conventions à tous les tests**
5. **Validation et tests finaux** 