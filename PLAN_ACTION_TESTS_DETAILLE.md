# 🎯 Plan d'Action Détaillé - Tests Athalia

**Date :** 15 Janvier 2025  
**Objectif :** Passer de 45% à 85% de couverture  
**Délai :** 6 semaines  
**Standards :** Code propre (Black, Ruff, MyPy)  

---

## 📋 **TÂCHES PRIORITAIRES PAR SEMAINE**

### **🔥 SEMAINE 1-2 : MODULES CRITIQUES**

#### **Jour 1-2 : `generation_backup.py` (PRIORITÉ ABSOLUE)**
- **Fichier :** `tests/unit/modules/test_generation_backup_complete.py`
- **Statut :** ❌ **AUCUN TEST EXISTANT** (489 lignes sans tests)
- **Effort :** 12 heures
- **Template complet :**

```python
#!/usr/bin/env python3
"""
Tests complets pour generation_backup.py
Module critique sans aucun test - PRIORITÉ ABSOLUE
"""

import pytest
import tempfile
import shutil
import json
from pathlib import Path
from unittest.mock import Mock, patch
from athalia_core.generation_backup import (
    backup_project,
    restore_project,
    validate_backup,
    compress_backup,
    create_backup_metadata
)

class TestGenerationBackupComplete:
    """Tests complets pour generation_backup.py"""
    
    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.backup_path = Path(self.temp_dir) / "backups"
        self.project_path.mkdir(parents=True)
        self.backup_path.mkdir(parents=True)
    
    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_backup_project_structure(self):
        """Test sauvegarde complète structure projet."""
        # Créer structure test
        (self.project_path / "src").mkdir()
        (self.project_path / "src" / "main.py").write_text("print('hello')")
        (self.project_path / "tests").mkdir()
        (self.project_path / "README.md").write_text("# Test Project")
        
        # Effectuer sauvegarde
        backup_file = backup_project(str(self.project_path), str(self.backup_path))
        
        # Vérifications
        assert backup_file.exists()
        assert backup_file.suffix == '.tar.gz'
        assert backup_file.stat().st_size > 0
    
    def test_restore_from_backup(self):
        """Test restauration depuis sauvegarde."""
        # Créer et sauvegarder projet
        (self.project_path / "original.txt").write_text("original content")
        backup_file = backup_project(str(self.project_path), str(self.backup_path))
        
        # Supprimer original
        shutil.rmtree(self.project_path)
        
        # Restaurer
        restored_path = restore_project(backup_file, self.temp_dir)
        
        # Vérifier restauration
        assert restored_path.exists()
        assert (restored_path / "original.txt").read_text() == "original content"
    
    def test_backup_validation(self):
        """Test validation intégrité sauvegarde."""
        # Créer sauvegarde valide
        (self.project_path / "test.py").write_text("# Test file")
        backup_file = backup_project(str(self.project_path), str(self.backup_path))
        
        # Valider
        is_valid, errors = validate_backup(backup_file)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_backup_compression(self):
        """Test compression des sauvegardes."""
        # Créer gros fichier
        large_content = "x" * 10000
        (self.project_path / "large.txt").write_text(large_content)
        
        # Sauvegarder avec compression
        backup_file = backup_project(
            str(self.project_path), 
            str(self.backup_path),
            compress=True
        )
        
        # Vérifier compression
        assert backup_file.stat().st_size < len(large_content)
    
    def test_backup_metadata(self):
        """Test métadonnées sauvegarde."""
        backup_file = backup_project(str(self.project_path), str(self.backup_path))
        metadata = create_backup_metadata(backup_file, str(self.project_path))
        
        assert "timestamp" in metadata
        assert "project_path" in metadata
        assert "backup_size" in metadata
        assert metadata["project_path"] == str(self.project_path)
    
    def test_incremental_backup(self):
        """Test sauvegarde incrémentale."""
        # Sauvegarde initiale
        (self.project_path / "file1.txt").write_text("content1")
        backup1 = backup_project(str(self.project_path), str(self.backup_path))
        
        # Ajouter fichier
        (self.project_path / "file2.txt").write_text("content2")
        backup2 = backup_project(
            str(self.project_path), 
            str(self.backup_path),
            incremental=True,
            base_backup=backup1
        )
        
        assert backup2.exists()
        assert backup2.stat().st_size < backup1.stat().st_size
    
    def test_backup_error_handling(self):
        """Test gestion erreurs sauvegarde."""
        # Chemin inexistant
        with pytest.raises(FileNotFoundError):
            backup_project("/path/inexistant", str(self.backup_path))
        
        # Permissions insuffisantes
        readonly_path = Path(self.temp_dir) / "readonly"
        readonly_path.mkdir(mode=0o444)
        
        with pytest.raises(PermissionError):
            backup_project(str(self.project_path), str(readonly_path))
    
    def test_backup_performance(self):
        """Test performance sauvegarde."""
        import time
        
        # Créer projet moyen
        for i in range(100):
            (self.project_path / f"file_{i}.py").write_text(f"# File {i}")
        
        start_time = time.time()
        backup_file = backup_project(str(self.project_path), str(self.backup_path))
        duration = time.time() - start_time
        
        assert duration < 5.0  # Max 5 secondes
        assert backup_file.exists()
```

#### **Jour 3-4 : `logger_advanced.py` (481 lignes)**
- **Fichier :** `tests/unit/utils/test_logger_advanced_complete.py`
- **Statut :** ❌ 10% couverture (inacceptable)
- **Effort :** 10 heures

```python
#!/usr/bin/env python3
"""
Tests complets pour logger_advanced.py
Couverture actuelle: 10% → Objectif: 85%
"""

import pytest
import tempfile
import json
import logging
from pathlib import Path
from unittest.mock import Mock, patch
from athalia_core.logger_advanced import (
    AthaliaLogger,
    setup_performance_logging,
    log_with_context,
    create_structured_log
)

class TestLoggerAdvancedComplete:
    """Tests complets pour logger avancé."""
    
    def setup_method(self):
        """Configuration tests."""
        self.temp_dir = tempfile.mkdtemp()
        self.log_dir = Path(self.temp_dir) / "logs"
        self.log_dir.mkdir()
        self.logger = AthaliaLogger(log_dir=str(self.log_dir))
    
    def test_logger_initialization(self):
        """Test initialisation logger."""
        assert self.logger.log_dir == str(self.log_dir)
        assert self.logger.level == logging.INFO
        assert len(self.logger.handlers) > 0
    
    def test_structured_logging(self):
        """Test logging structuré."""
        log_data = {
            "event": "test_event",
            "user_id": "123",
            "timestamp": "2025-01-15T10:00:00Z"
        }
        
        self.logger.log_structured(log_data)
        
        log_files = list(self.log_dir.glob("*.json"))
        assert len(log_files) > 0
        
        with open(log_files[0]) as f:
            logged_data = json.load(f)
            assert logged_data["event"] == "test_event"
    
    def test_performance_logging(self):
        """Test logging performance."""
        @log_with_context(self.logger)
        def slow_function():
            import time
            time.sleep(0.1)
            return "result"
        
        result = slow_function()
        assert result == "result"
        
        # Vérifier log performance
        perf_logs = list(self.log_dir.glob("*performance*.log"))
        assert len(perf_logs) > 0
    
    def test_log_rotation(self):
        """Test rotation fichiers logs."""
        # Générer beaucoup de logs
        for i in range(1000):
            self.logger.info(f"Log message {i}" * 100)
        
        log_files = list(self.log_dir.glob("*.log*"))
        assert len(log_files) > 1  # Rotation effectuée
    
    def test_log_filtering(self):
        """Test filtrage logs."""
        sensitive_filter = lambda record: "password" not in record.getMessage()
        self.logger.add_filter(sensitive_filter)
        
        self.logger.info("Normal message")
        self.logger.info("password=secret123")
        
        # Vérifier filtrage
        log_content = (self.log_dir / "athalia.log").read_text()
        assert "Normal message" in log_content
        assert "password=secret123" not in log_content
    
    def test_error_context_logging(self):
        """Test logging avec contexte d'erreur."""
        try:
            raise ValueError("Test error")
        except ValueError as e:
            self.logger.log_exception(e, context={"module": "test"})
        
        error_logs = list(self.log_dir.glob("*error*.log"))
        assert len(error_logs) > 0
```

#### **Jour 5 : Setup Standards Qualité**
- **Installation outils :** `black`, `ruff`, `mypy`, `isort`, `bandit`
- **Configuration pre-commit hooks**
- **Validation des 2 premiers tests créés**

### **⚠️ SEMAINE 3-4 : MODULES HAUTE PRIORITÉ**

#### **Jour 1-2 : `security_validator.py` (489 lignes)**
- **Fichier :** `tests/unit/security/test_security_validator_complete.py`
- **Statut :** ❌ 15% couverture
- **Effort :** 14 heures

#### **Jour 3-4 : `intelligent_auditor.py` (810 lignes)**
- **Fichier :** `tests/unit/modules/test_intelligent_auditor_complete.py`
- **Statut :** ❌ 15% couverture (LE PLUS GROS FICHIER SOUS-TESTÉ)
- **Effort :** 16 heures

#### **Jour 5 : `performance_analyzer.py` (580 lignes)**
- **Fichier :** `tests/unit/modules/test_performance_analyzer_complete.py`
- **Statut :** ❌ 20% couverture
- **Effort :** 12 heures

### **📋 SEMAINE 5-6 : FINALISATION**

#### **Amélioration tests existants partiels :**
1. **`pattern_detector.py`** (575 lignes) : 35% → 75%
2. **`auto_tester.py`** (713 lignes) : 40% → 80%
3. **`docker_robotics.py`** (410 lignes) : 40% → 75%
4. **`rust_analyzer.py`** (405 lignes) : 15% → 70%

---

## 🛠️ **STANDARDS QUALITÉ OBLIGATOIRES**

### **Configuration Automatique**

```bash
# 1. Installation outils qualité
pip install black ruff mypy isort bandit pytest-cov pre-commit

# 2. Configuration pre-commit
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        args: [--line-length=88]
  
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]
  
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: [--profile=black]
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
EOF

# 3. Activation
pre-commit install
```

### **Commandes Obligatoires Avant Chaque Commit**

```bash
# Formatage automatique
black athalia_core/ tests/
isort athalia_core/ tests/

# Vérification qualité
ruff check athalia_core/ tests/ --fix
mypy athalia_core/ --ignore-missing-imports

# Sécurité
bandit -r athalia_core/ -f json -o security_report.json

# Tests avec couverture
pytest --cov=athalia_core --cov-report=html --cov-report=term-missing --cov-fail-under=80
```

### **Template Standardisé pour Nouveaux Tests**

```python
#!/usr/bin/env python3
"""
Tests complets pour [MODULE_NAME].py

Couverture: 80%+ lignes, 70%+ branches
Standards: Black + Ruff + MyPy + Bandit
Pytest: Fixtures + Mocks + Parametrize
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from athalia_core.[module_name] import [ClassToTest]


class Test[ModuleName]Complete:
    """Tests complets pour [module_name].py
    
    Requirements:
    - Couverture ligne: >80%
    - Couverture branche: >70%
    - Tests par fonction: min 3 (nominal, erreur, limite)
    - Documentation: docstring obligatoire
    """
    
    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_instance = [ClassToTest](project_path=self.temp_dir)
    
    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    @pytest.fixture
    def sample_data(self):
        """Données de test réutilisables."""
        return {
            "input": "test_value",
            "expected": "expected_result"
        }
    
    def test_initialization(self):
        """Test initialisation classe."""
        assert self.test_instance.project_path == self.temp_dir
        assert hasattr(self.test_instance, 'config')
    
    @pytest.mark.parametrize("input_val,expected", [
        ("normal", "normal_result"),
        ("", "empty_result"),
        ("special_chars_éàç", "special_result"),
    ])
    def test_core_functionality_parametrized(self, input_val, expected):
        """Test fonctionnalité principale avec paramètres."""
        result = self.test_instance.core_method(input_val)
        assert result == expected
    
    def test_core_functionality_success(self, sample_data):
        """Test fonctionnalité principale - cas nominal."""
        # Arrange
        input_data = sample_data["input"]
        expected = sample_data["expected"]
        
        # Act
        result = self.test_instance.core_method(input_data)
        
        # Assert
        assert result == expected
        assert self.test_instance.last_operation == "success"
    
    def test_edge_cases(self):
        """Test cas limites."""
        # Valeur nulle
        with pytest.raises(ValueError, match="Input cannot be None"):
            self.test_instance.core_method(None)
        
        # Valeur vide
        result = self.test_instance.core_method("")
        assert result == ""
        
        # Valeur très longue
        long_input = "x" * 10000
        result = self.test_instance.core_method(long_input)
        assert len(result) <= 1000  # Troncature attendue
    
    def test_error_handling(self):
        """Test gestion d'erreurs."""
        # Erreur TypeError
        with pytest.raises(TypeError):
            self.test_instance.core_method(123)  # String attendu
        
        # Erreur personnalisée
        with pytest.raises(self.test_instance.CustomError):
            self.test_instance.method_that_fails()
    
    def test_performance(self):
        """Test performance."""
        import time
        
        # Test rapidité
        start = time.time()
        result = self.test_instance.fast_method()
        duration = time.time() - start
        
        assert duration < 0.1  # Max 100ms
        assert result is not None
    
    @patch('athalia_core.[module_name].external_dependency')
    def test_external_integration(self, mock_dependency):
        """Test intégration dépendances externes."""
        # Configuration mock
        mock_dependency.return_value = "mocked_response"
        
        # Exécution
        result = self.test_instance.method_with_dependency()
        
        # Vérifications
        assert result == "processed_mocked_response"
        mock_dependency.assert_called_once_with("expected_param")
    
    def test_file_operations(self):
        """Test opérations fichiers."""
        test_file = Path(self.temp_dir) / "test.txt"
        test_content = "Test content"
        
        # Écriture
        self.test_instance.write_file(test_file, test_content)
        assert test_file.exists()
        assert test_file.read_text() == test_content
        
        # Lecture
        content = self.test_instance.read_file(test_file)
        assert content == test_content
    
    def test_state_management(self):
        """Test gestion états internes."""
        # État initial
        assert self.test_instance.state == "initialized"
        
        # Transition
        self.test_instance.start_operation()
        assert self.test_instance.state == "running"
        
        # Finalisation
        self.test_instance.complete_operation()
        assert self.test_instance.state == "completed"
    
    def test_configuration_validation(self):
        """Test validation configuration."""
        # Configuration valide
        valid_config = {"param1": "value1", "param2": 42}
        assert self.test_instance.validate_config(valid_config) is True
        
        # Configuration invalide
        invalid_config = {"param1": None}
        assert self.test_instance.validate_config(invalid_config) is False
    
    @pytest.mark.slow
    def test_heavy_operation(self):
        """Test opération lourde (marqué slow)."""
        result = self.test_instance.heavy_computation()
        assert result is not None
    
    def test_logging_integration(self):
        """Test intégration logging."""
        with patch('athalia_core.[module_name].logger') as mock_logger:
            self.test_instance.method_with_logging()
            mock_logger.info.assert_called()
    
    def test_cleanup_resources(self):
        """Test nettoyage ressources."""
        # Allouer ressources
        self.test_instance.allocate_resources()
        assert self.test_instance.resources_allocated is True
        
        # Nettoyer
        self.test_instance.cleanup()
        assert self.test_instance.resources_allocated is False


# Tests d'intégration
class Test[ModuleName]Integration:
    """Tests d'intégration pour [module_name].py"""
    
    def test_full_workflow(self):
        """Test workflow complet."""
        # Test intégration bout en bout
        pass
    
    def test_multiple_instances(self):
        """Test plusieurs instances simultanées."""
        # Test isolation instances
        pass


# Tests de performance
@pytest.mark.benchmark
class Test[ModuleName]Performance:
    """Tests de performance pour [module_name].py"""
    
    def test_memory_usage(self):
        """Test utilisation mémoire."""
        import tracemalloc
        
        tracemalloc.start()
        # Opération à tester
        tracemalloc.stop()
    
    def test_execution_time(self):
        """Test temps d'exécution."""
        # Benchmarking
        pass
```

---

## 📊 **MÉTRIQUES DE SUIVI**

### **Dashboard Quotidien**

```bash
#!/bin/bash
# Script de métriques quotidiennes

echo "=== MÉTRIQUES ATHALIA - $(date) ==="

# Couverture globale
echo "📊 COUVERTURE:"
pytest --cov=athalia_core --cov-report=term-missing | grep TOTAL

# Qualité code
echo "🛠️ QUALITÉ:"
ruff check athalia_core/ tests/ --statistics
mypy athalia_core/ --ignore-missing-imports | grep "error"

# Sécurité
echo "🔒 SÉCURITÉ:"
bandit -r athalia_core/ -q | grep "Total issues"

# Tests
echo "🧪 TESTS:"
pytest tests/ --tb=no -q | tail -1
```

### **Objectifs Hebdomadaires**

| Semaine | Couverture Cible | Tests Créés | Modules Traités |
|---------|------------------|-------------|-----------------|
| **1-2** | 45% → 60% | 2 complets | `generation_backup`, `logger_advanced` |
| **3-4** | 60% → 70% | 3 complets | `security_validator`, `intelligent_auditor`, `performance_analyzer` |
| **5-6** | 70% → 85% | 4 améliorés | `pattern_detector`, `auto_tester`, `docker_robotics`, `rust_analyzer` |

---

## 🎯 **LIVRAISON FINALE**

### **Critères de Réussite**
- ✅ **85% couverture globale** minimum
- ✅ **Code conforme** : Black + Ruff + MyPy
- ✅ **Sécurité validée** : Bandit sans erreurs critiques
- ✅ **Tests robustes** : Edge cases + Error handling + Performance
- ✅ **Documentation complète** : Docstrings + README à jour

### **Livrables**
1. **6 fichiers de tests complets** créés
2. **4 fichiers de tests** améliorés significativement
3. **Configuration qualité** automatisée
4. **Documentation** mise à jour
5. **Rapport final** avec métriques

---

**🚀 Impact attendu :** Réduction 60% des bugs + Maintenance facilitée + Confiance déploiements