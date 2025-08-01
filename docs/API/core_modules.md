# 🛠️ Core Modules - Documentation API

**Date :** 27 juillet 2025
**Statut :** Documentation exhaustive et conforme au code

## 🎯 Vue d'ensemble

Les modules principaux d'Athalia fournissent toutes les fonctionnalités de base pour l'industrialisation, l'audit, l'analyse, la configuration, la CI/CD, la sécurité, l'IA, et la maintenance des projets.

---

## 📁 Modules Disponibles

### 📊 analytics.py
- **Fonctions principales :**
  - `analyze_project(project_path: str) -> dict`
  - `generate_heatmap_data(project_path: str) -> dict`
  - `generate_technical_debt_analysis(project_path: str) -> dict`

### 🕵️ audit.py / intelligent_auditor.py
- **Classe principale :**
  - `IntelligentAuditor`
- **Fonctions principales :**
  - `audit_project_intelligent(project_path: str) -> dict`
  - `generate_audit_report(project_path: str) -> str`

### 🧹 auto_cleaner.py
- **Classe principale :**
  - `AutoCleaner(project_path: str)`
    - `clean_project(dry_run: bool = False) -> dict`
    - `optimize_project_structure(project_path: str) -> dict`

### 📚 auto_documenter.py
- **Classe principale :**
  - `AutoDocumenter(project_path: str, lang: str = 'fr')`
    - `document_project(project_path: str) -> dict`
    - `run() -> dict`

### 🧪 auto_tester.py
- **Classe principale :**
  - `AutoTester(project_path: str)`
    - `generate_tests(project_path: str) -> dict`
    - `run() -> dict`

### 🚀 auto_cicd.py
- **Classe principale :**
  - `AutoCICD()`
    - `setup_cicd(project_path: str) -> dict`

### 🤖 ai_robust.py
- **Classe principale :**
  - `RobustAI()`
    - `generate_blueprint(idea: str, **kwargs) -> dict`
    - `review_code(code: str, filename: str, project_type: str, current_score: int) -> dict`
    - `generate_documentation(project_name: str, project_type: str, modules: list) -> str`

### ⚙️ config_manager.py
- **Fonctions principales :**
  - `load_config(config_path: str) -> dict`
  - `save_config(config: dict, config_path: str) -> bool`
- **Classe :**
  - `ConfigManager(config_file: str)`
    - `get(key: str, default: Any = None) -> Any`
    - `set(key: str, value: Any) -> None`
    - `validate_config(config: dict) -> bool`

### 📈 performance_analyzer.py
- **Classe principale :**
  - `PerformanceAnalyzer(root_path: str = None)`
    - `analyze_project_performance(project_path: str = None) -> PerformanceReport`
    - `get_performance_insights() -> dict`

### 🧩 pattern_detector.py
- **Classe principale :**
  - `PatternDetector(root_path: str = None)`
    - `analyze_project_patterns(project_path: str = None) -> dict`
    - `get_learning_insights() -> dict`

### 🔒 security.py / security_auditor.py
- **Fonctions principales :**
  - `security_audit_project(project_path: str)`
- **Classe :**
  - `SecurityAuditor(project_path: str)`
    - `run() -> dict`

### 🧩 plugins_manager.py / plugins_validator.py
- **Fonctions principales :**
  - `validate_plugin(path)`

### 📦 project_importer.py
- **Classe principale :**
  - `ProjectImporter()`
    - `import_project(project_path: str) -> dict`

### 📝 multi_file_editor.py
- **Classe principale :**
  - `MultiFileEditor(backup_dir: str = ".multi_file_backups")`
    - `backup_file(file_path: str)`
    - `apply_corrections(files: List[str], correction_fn: Callable[[str], str]) -> dict`
    - `rollback()`

### 📊 advanced_analytics.py
- **Fonctions principales :**
  - `analyze_advanced_metrics(project_path: str) -> dict`

### 🏗️ architecture_analyzer.py
- **Classe principale :**
  - `ArchitectureAnalyzer()`
    - `analyze_architecture(project_path: str) -> dict`

### 📝 logger_advanced.py
- **Classe principale :**
  - `LoggerAdvanced()`
    - `setup_logging(level: str, format: str)`

### 🟢 ready_check.py
- **Fonctions principales :**
  - `check_ready(project_path: str) -> dict`

### 🧑‍💻 onboarding.py
- **Fonctions principales :**
  - `generate_onboarding_md(blueprint, outdir)`
  - `generate_onboard_cli(blueprint, outdir)`
  - `generate_onboarding_html_advanced(blueprint, outdir)`

---

## 🔗 Navigation

- [Index API](README.md)
- [Orchestrateur](orchestrator.md)
- [Plugins et Templates](plugins.md)
- [Robotique](robotics.md)

---

*Documentation exhaustive et conforme au code réel, mise à jour le 27/07/2025.*
