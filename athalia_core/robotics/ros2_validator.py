"""
ROS2 Validator - Validation spécialisée ROS2
============================================

Validation complète des workspaces ROS2:
- Structure workspace
- Packages et dépendances
- Launch files
- URDF/XACRO
- Build system
"""

import ast
from dataclasses import dataclass
import logging
from pathlib import Path
import subprocess
from typing import Dict, List, Optional
import xml.etree.ElementTree as ET


logger = logging.getLogger(__name__)

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


@dataclass
class ROS2PackageInfo:
    """Informations sur un package ROS2"""

    name: str
    path: Path
    package_type: str  # ament_cmake, ament_python, etc.
    dependencies: List[str]
    has_launch: bool
    has_urdf: bool
    has_tests: bool


@dataclass
class ROS2ValidationResult:
    """Résultat de validation ROS2"""

    workspace_valid: bool
    packages: List[ROS2PackageInfo]
    issues: List[str]
    recommendations: List[str]
    build_ready: bool


class ROS2Validator:
    """Validateur spécialisé ROS2"""

    def __init__(self, workspace_path: str):
        self.workspace_path = Path(workspace_path)
        self.src_path = self.workspace_path / "src"
        self.logger = logger

    def validate_workspace(self) -> ROS2ValidationResult:
        """Validation complète du workspace ROS2"""
        self.logger.info(f"🔍 Validation workspace ROS2: {self.workspace_path}")

        issues = []
        recommendations = []
        packages = []

        # Vérifier structure workspace
        if not self.src_path.exists():
            issues.append("Dossier 'src' manquant - structure workspace ROS2 invalide")
            return ROS2ValidationResult(
                workspace_valid=False,
                packages=[],
                issues=issues,
                recommendations=recommendations,
                build_ready=False,
            )

        # Analyser packages
        package_dirs = [d for d in self.src_path.iterdir() if d.is_dir()]

        for package_dir in package_dirs:
            package_info = self._analyze_package(package_dir)
            if package_info:
                packages.append(package_info)

        if not packages:
            issues.append("Aucun package ROS2 valide trouvé dans src/")
            recommendations.append("Créer au moins un package ROS2")

        # Vérifier build system
        build_ready = self._check_build_system()
        if not build_ready:
            issues.append("Build system ROS2 non configuré")
            recommendations.append("Configurer colcon build")

        # Vérifier launch files
        launch_files = list(self.workspace_path.rglob("*.launch.py"))
        if not launch_files:
            recommendations.append("Ajouter des fichiers launch.py pour le déploiement")

        # Vérifier URDF/XACRO
        urdf_files = list(self.workspace_path.rglob("*.urdf"))
        xacro_files = list(self.workspace_path.rglob("*.xacro"))
        if not urdf_files and not xacro_files:
            recommendations.append(
                "Ajouter des fichiers URDF/XACRO pour la description du robot"
            )

        workspace_valid = len(issues) == 0

        return ROS2ValidationResult(
            workspace_valid=workspace_valid,
            packages=packages,
            issues=issues,
            recommendations=recommendations,
            build_ready=build_ready,
        )

    def _analyze_package(self, package_dir: Path) -> Optional[ROS2PackageInfo]:
        """Analyser un package ROS2"""
        package_xml = package_dir / "package.xml"

        if not package_xml.exists():
            self.logger.warning(f"Package.xml manquant dans {package_dir}")
            return None

        try:
            tree = ET.parse(package_xml)
            root = tree.getroot()

            # Extraire nom du package
            name = root.get("name", package_dir.name)

            # Déterminer type de package
            package_type = self._detect_package_type(package_dir)

            # Extraire dépendances
            dependencies = []
            for dep in root.findall(".//depend"):
                dependencies.append(dep.text)

            # Vérifier présence de fichiers importants
            has_launch = (package_dir / "launch").exists() or list(
                package_dir.glob("*.launch.py")
            )
            has_urdf = (
                (package_dir / "urdf").exists()
                or list(package_dir.glob("*.urdf"))
                or list(package_dir.glob("*.xacro"))
            )
            has_tests = (package_dir / "test").exists() or list(
                package_dir.glob("test_*.py")
            )

            return ROS2PackageInfo(
                name=name,
                path=package_dir,
                package_type=package_type,
                dependencies=dependencies,
                has_launch=bool(has_launch),
                has_urdf=bool(has_urdf),
                has_tests=bool(has_tests),
            )

        except Exception as e:
            self.logger.error(f"Erreur analyse package {package_dir}: {e}")
            return None

    def _detect_package_type(self, package_dir: Path) -> str:
        """Détecter le type de package ROS2"""
        if (package_dir / "setup.py").exists():
            return "ament_python"
        elif (package_dir / "CMakeLists.txt").exists():
            return "ament_cmake"
        else:
            return "unknown"

    def _check_build_system(self) -> bool:
        """Vérifier si le build system est configuré"""
        try:
            result = validate_and_run(
                ["colcon", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except (BaseException, SecurityError):
            return False

    def validate_launch_files(self) -> List[Dict]:
        """Valider les fichiers launch"""
        launch_files = list(self.workspace_path.rglob("*.launch.py"))
        results = []

        for launch_file in launch_files:
            try:
                # Vérifier syntaxe Python
                with open(launch_file, "r") as f:
                    ast.parse(f.read())

                # Vérifier imports ROS2
                with open(launch_file, "r") as f:
                    content = f.read()
                    has_launch_import = "from launch import" in content
                    has_launch_ros_import = "from launch_ros" in content

                results.append(
                    {
                        "file": str(launch_file),
                        "valid": True,
                        "has_launch_import": has_launch_import,
                        "has_launch_ros_import": has_launch_ros_import,
                    }
                )

            except Exception as e:
                results.append(
                    {"file": str(launch_file), "valid": False, "error": str(e)}
                )

        return results

    def validate_urdf_files(self) -> List[Dict]:
        """Valider les fichiers URDF/XACRO"""
        urdf_files = list(self.workspace_path.rglob("*.urdf"))
        xacro_files = list(self.workspace_path.rglob("*.xacro"))
        results = []

        for urdf_file in urdf_files + xacro_files:
            try:
                with open(urdf_file, "r") as f:
                    content = f.read()

                # Vérifications basiques
                has_robot_tag = "<robot" in content
                has_link_tags = "<link" in content
                has_joint_tags = "<joint" in content

                results.append(
                    {
                        "file": str(urdf_file),
                        "valid": True,
                        "has_robot_tag": has_robot_tag,
                        "has_link_tags": has_link_tags,
                        "has_joint_tags": has_joint_tags,
                    }
                )

            except Exception as e:
                results.append(
                    {"file": str(urdf_file), "valid": False, "error": str(e)}
                )

        return results

    def generate_validation_report(self, result: ROS2ValidationResult) -> str:
        """Générer rapport de validation"""
        report = f"""
# 🤖 Rapport de Validation ROS2

## 📊 Résumé
- **Workspace Valide**: {'✅' if result.workspace_valid else '❌'}
- **Build Ready**: {'✅' if result.build_ready else '❌'}
- **Packages**: {len(result.packages)}

## 📦 Packages Détectés
"""

        for package in result.packages:
            report += f"""
### {package.name}
- **Type**: {package.package_type}
- **Dépendances**: {len(package.dependencies)}
- **Launch**: {'✅' if package.has_launch else '❌'}
- **URDF**: {'✅' if package.has_urdf else '❌'}
- **Tests**: {'✅' if package.has_tests else '❌'}
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
