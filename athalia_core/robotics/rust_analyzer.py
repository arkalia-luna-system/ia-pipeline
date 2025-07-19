"""
Rust Analyzer - Analyse spécialisée Rust pour robotique
=======================================================

Analyse des projets Rust dans l'écosystème robotique :
- Validation Cargo.toml
- Dépendances ROS2 Rust
- Optimisations de compilation
- Intégration avec Reachy
"""

import os
import toml
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class CargoDependency:
    """Dépendance Cargo"""
    name: str
    version: str
    features: List[str]
    optional: bool


@dataclass
class RustProjectInfo:
    """Informations sur un projet Rust"""
    name: str
    path: Path
    version: str
    dependencies: List[CargoDependency]
    dev_dependencies: List[CargoDependency]
    build_dependencies: List[CargoDependency]
    has_ros2_deps: bool
    has_robotics_deps: bool
    build_targets: List[str]


@dataclass
class RustAnalysisResult:
    """Résultat d'analyse Rust"""
    projects: List[RustProjectInfo]
    issues: List[str]
    recommendations: List[str]
    build_ready: bool
    optimization_score: float  # 0-100


class RustAnalyzer:
    """Analyseur spécialisé Rust pour robotique"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.logger = logger
        
    def analyze_rust_projects(self) -> RustAnalysisResult:
        """Analyser tous les projets Rust du projet"""
        self.logger.info(f"🔧 Analyse Rust: {self.project_path}")
        
        issues = []
        recommendations = []
        projects = []
        
        # Trouver tous les Cargo.toml
        cargo_files = list(self.project_path.rglob("Cargo.toml"))
        
        if not cargo_files:
            recommendations.append("Considérer l'ajout de composants Rust pour les performances")
            return RustAnalysisResult(
                projects=[],
                issues=issues,
                recommendations=recommendations,
                build_ready=False,
                optimization_score=0.0
            )
        
        self.logger.info(f"📦 {len(cargo_files)} projets Rust détectés")
        
        # Analyser chaque projet
        for cargo_file in cargo_files:
            project_info = self._analyze_cargo_project(cargo_file)
            if project_info:
                projects.append(project_info)
        
        # Vérifier build system
        build_ready = self._check_rust_build_system()
        if not build_ready:
            issues.append("Build system Rust non configuré")
            recommendations.append("Installer Rust et Cargo")
        
        # Calculer score d'optimisation
        optimization_score = self._calculate_optimization_score(projects)
        
        # Vérifications spécifiques robotique
        self._check_robotics_integration(projects, issues, recommendations)
        
        return RustAnalysisResult(
            projects=projects,
            issues=issues,
            recommendations=recommendations,
            build_ready=build_ready,
            optimization_score=optimization_score
        )
    
    def _analyze_cargo_project(self, cargo_file: Path) -> Optional[RustProjectInfo]:
        """Analyser un projet Cargo"""
        try:
            with open(cargo_file, 'r') as f:
                cargo_data = toml.load(f)
            
            package = cargo_data.get('package', {})
            name = package.get('name', cargo_file.parent.name)
            version = package.get('version', '0.0.0')
            
            # Analyser dépendances
            dependencies = self._parse_dependencies(cargo_data.get('dependencies', {}))
            dev_dependencies = self._parse_dependencies(cargo_data.get('dev-dependencies', {}))
            build_dependencies = self._parse_dependencies(cargo_data.get('build-dependencies', {}))
            
            # Vérifier dépendances ROS2/Robotique
            has_ros2_deps = any('ros2' in dep.name.lower() for dep in dependencies)
            has_robotics_deps = any(self._is_robotics_dependency(dep) for dep in dependencies)
            
            # Analyser targets
            build_targets = self._analyze_build_targets(cargo_file.parent)
            
            return RustProjectInfo(
                name=name,
                path=cargo_file.parent,
                version=version,
                dependencies=dependencies,
                dev_dependencies=dev_dependencies,
                build_dependencies=build_dependencies,
                has_ros2_deps=has_ros2_deps,
                has_robotics_deps=has_robotics_deps,
                build_targets=build_targets
            )
            
        except Exception as e:
            self.logger.error(f"Erreur analyse {cargo_file}: {e}")
            return None
    
    def _parse_dependencies(self, deps_dict: Dict) -> List[CargoDependency]:
        """Parser les dépendances Cargo"""
        dependencies = []
        
        for name, dep_info in deps_dict.items():
            if isinstance(dep_info, str):
                # Version simple
                dependencies.append(CargoDependency(
                    name=name,
                    version=dep_info,
                    features=[],
                    optional=False
                ))
            elif isinstance(dep_info, dict):
                # Configuration complète
                dependencies.append(CargoDependency(
                    name=name,
                    version=dep_info.get('version', '0.0.0'),
                    features=dep_info.get('features', []),
                    optional=dep_info.get('optional', False)
                ))
        
        return dependencies
    
    def _is_robotics_dependency(self, dep: CargoDependency) -> bool:
        """Vérifier si c'est une dépendance robotique"""
        robotics_keywords = [
            'ros2', 'dynamixel', 'robot', 'motor', 'servo', 'kinematics',
            'gazebo', 'rviz', 'tf', 'geometry', 'control', 'sensor'
        ]
        
        return any(keyword in dep.name.lower() for keyword in robotics_keywords)
    
    def _analyze_build_targets(self, project_path: Path) -> List[str]:
        """Analyser les targets de build"""
        targets = []
        
        # Vérifier src/main.rs
        if (project_path / "src" / "main.rs").exists():
            targets.append("bin")
        
        # Vérifier src/lib.rs
        if (project_path / "src" / "lib.rs").exists():
            targets.append("lib")
        
        # Vérifier autres binaires
        bin_files = list(project_path.glob("src/bin/*.rs"))
        if bin_files:
            targets.extend([f"bin:{f.stem}" for f in bin_files])
        
        return targets
    
    def _check_rust_build_system(self) -> bool:
        """Vérifier si le build system Rust est configuré"""
        try:
            result = subprocess.run(['cargo', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except:
            return False
    
    def _calculate_optimization_score(self, projects: List[RustProjectInfo]) -> float:
        """Calculer le score d'optimisation"""
        if not projects:
            return 0.0
        
        score = 0.0
        
        for project in projects:
            # Score de base pour chaque projet
            score += 20.0
            
            # Bonus pour dépendances robotiques
            if project.has_robotics_deps:
                score += 15.0
            
            # Bonus pour ROS2
            if project.has_ros2_deps:
                score += 20.0
            
            # Bonus pour lib + bin
            if 'lib' in project.build_targets and 'bin' in project.build_targets:
                score += 10.0
            
            # Bonus pour tests
            if project.dev_dependencies:
                score += 5.0
        
        return min(100.0, score)
    
    def _check_robotics_integration(self, projects: List[RustProjectInfo], 
                                  issues: List[str], recommendations: List[str]):
        """Vérifier l'intégration robotique"""
        
        # Vérifier dépendances ROS2
        ros2_projects = [p for p in projects if p.has_ros2_deps]
        if not ros2_projects:
            recommendations.append("Considérer l'ajout de dépendances ROS2 Rust pour l'intégration")
        
        # Vérifier dépendances robotiques
        robotics_projects = [p for p in projects if p.has_robotics_deps]
        if not robotics_projects:
            recommendations.append("Ajouter des dépendances robotiques (dynamixel, kinematics, etc.)")
        
        # Vérifier optimisations
        for project in projects:
            if not project.dev_dependencies:
                recommendations.append(f"Ajouter des tests pour {project.name}")
            
            if not any('test' in dep.name.lower() for dep in project.dev_dependencies):
                recommendations.append(f"Ajouter des dépendances de test pour {project.name}")
    
    def validate_cargo_toml(self, cargo_file: Path) -> Dict:
        """Valider un fichier Cargo.toml"""
        try:
            with open(cargo_file, 'r') as f:
                cargo_data = toml.load(f)
            
            issues = []
            
            # Vérifier section package
            if 'package' not in cargo_data:
                issues.append("Section [package] manquante")
            else:
                package = cargo_data['package']
                if 'name' not in package:
                    issues.append("Nom du package manquant")
                if 'version' not in package:
                    issues.append("Version du package manquante")
            
            # Vérifier dépendances
            if 'dependencies' not in cargo_data:
                issues.append("Aucune dépendance déclarée")
            
            # Vérifier edition
            if 'edition' not in cargo_data.get('package', {}):
                recommendations = ["Spécifier l'édition Rust (2021 recommandée)"]
            else:
                recommendations = []
            
            return {
                'file': str(cargo_file),
                'valid': len(issues) == 0,
                'issues': issues,
                'recommendations': recommendations
            }
            
        except Exception as e:
            return {
                'file': str(cargo_file),
                'valid': False,
                'issues': [f"Erreur parsing: {e}"],
                'recommendations': []
            }
    
    def generate_rust_report(self, result: RustAnalysisResult) -> str:
        """Générer rapport d'analyse Rust"""
        report = f"""
# 🔧 Rapport d'Analyse Rust

## 📊 État des Projets
- **Projets Rust**: {len(result.projects)}
- **Build Ready**: {'✅' if result.build_ready else '❌'}
- **Score Optimisation**: {result.optimization_score:.1f}/100

## 📦 Projets Détectés
"""
        
        for project in result.projects:
            report += f"""
### {project.name} v{project.version}
- **Chemin**: {project.path}
- **Dépendances**: {len(project.dependencies)}
- **ROS2**: {'✅' if project.has_ros2_deps else '❌'}
- **Robotique**: {'✅' if project.has_robotics_deps else '❌'}
- **Targets**: {', '.join(project.build_targets)}
"""
        
        if result.issues:
            report += "\n## 🚨 Problèmes Détectés\n"
            for issue in result.issues:
                report += f"- {issue}\n"
        
        if result.recommendations:
            report += "\n## 💡 Recommandations\n"
            for rec in result.recommendations:
                report += f"- {rec}\n"
        
        return report
    
    def create_rust_template(self, project_name: str) -> str:
        """Créer un template Cargo.toml pour robotique"""
        template = f"""[package]
name = "{project_name}"
version = "0.1.0"
edition = "2021"
authors = ["Your Name <your.email@example.com>"]
description = "Rust component for Reachy robotics"
license = "MIT"

[dependencies]
# ROS2 Rust bindings
rclrs = "0.1"
ros2_rust = "0.1"

# Robotique
dynamixel-sdk = "0.1"
nalgebra = "0.32"  # Algèbre linéaire
k = "0.1"  # Kinematics

# Utilitaires
serde = {{ version = "1.0", features = ["derive"] }}
tokio = {{ version = "1.0", features = ["full"] }}
log = "0.4"
env_logger = "0.10"

[dev-dependencies]
criterion = "0.5"
mockall = "0.11"

[[bench]]
name = "performance_bench"
harness = false

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
panic = "abort"
"""
        return template 