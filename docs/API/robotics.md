# 🤖 Robotics - Documentation API

**Date :** 27 juillet 2025
**Statut :** Documentation exhaustive et conforme au code

## 🎯 Vue d'ensemble

Le module Robotics d'Athalia fournit l'intégration avec les systèmes robotiques, notamment Reachy et ROS2, avec des outils spécialisés pour l'audit, la validation, la CI/CD et l'analyse.

---

## 📁 Modules Disponibles

### 🔍 reachy_auditor.py
- **Classe principale :**
  - `ReachyAuditor(project_path: str)`
    - `audit_complete() -> ReachyAuditResult`
    - `generate_report(result: ReachyAuditResult) -> str`
    - `save_report(result: ReachyAuditResult, output_path: Optional[str] = None) -> str`

### 🐳 docker_robotics.py
- **Classe principale :**
  - `DockerRoboticsManager(project_path: str)`
    - `validate_docker_setup() -> DockerValidationResult`
    - `create_reachy_compose_template() -> str`
    - `create_dockerfile_template() -> str`
    - `setup_reachy_environment() -> bool`
    - `run_docker_compose(service: Optional[str] = None) -> bool`

### 🚀 robotics_ci.py
- **Classe principale :**
  - `RoboticsCI(project_path: str)`
    - `create_github_workflow() -> str`
    - `create_docker_compose_ci() -> str`
    - `run_ci_pipeline(config: CIConfig) -> CIResult`
    - `setup_ci_environment() -> bool`

### 🔧 rust_analyzer.py
- **Classe principale :**
  - `RustAnalyzer(project_path: str)`
    - `analyze_rust_projects() -> RustAnalysisResult`
    - `validate_cargo_toml(cargo_file: Path) -> Dict`
    - `create_rust_template(project_name: str) -> str`

### ✅ ros2_validator.py
- **Classe principale :**
  - `ROS2Validator(workspace_path: str)`
    - `validate_workspace() -> ROS2ValidationResult`
    - `validate_launch_files() -> List[Dict]`
    - `validate_urdf_files() -> List[Dict]`

---

## 🔗 Navigation

- [Index API](INDEX.md)
- [Core Modules](core_modules.md)
- [Orchestrateur](orchestrator.md)
- [Plugins et Templates](plugins.md)

---

*Documentation exhaustive et conforme au code réel, mise à jour le 27/07/2025.*
