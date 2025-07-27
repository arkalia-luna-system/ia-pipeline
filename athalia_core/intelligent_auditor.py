#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import os
import re
import sys
from datetime import datetime
import ast
import subprocess
import logging

logger = logging.getLogger(__name__)

"""
Module audit intelligent pour Athalia
Analyse automatique complète des projets avec recommandations
"""


class IntelligentAuditor:
    """Auditeur intelligent pour analyse automatique des projets"""

    def __init__(self, project_path: str = None):
        self.project_path = Path(project_path) if project_path else None
        self.audit_results = {}
        self.recommendations = []

    def run(self) -> Dict[str, Any]:
        """Méthode run() pour l'orchestrateur - exécute l'audit"""
        if not self.project_path:
            raise ValueError("project_path doit être défini")
        return self.audit_project(str(self.project_path))

    def audit_project(self, project_path: str) -> Dict[str, Any]:
        """Audit complet d'un projet"""
        self.project_path = Path(project_path)
        self.audit_results = {
            "info": {},
            "code_quality": {},
            "security": {},
            "performance": {},
            "documentation": {},
            "testing": {},
            "structure": {},
            "recommendations": [],
            "score": 0
        }

        logger.info(
            f"🔍 Audit intelligent en cours pour : {self.project_path.name}")

        # Analyses parallèles
        self._analyze_project_info()
        self._analyze_code_quality()
        self._analyze_security()
        self._analyze_performance()
        self._analyze_documentation()
        self._analyze_testing()
        self._analyze_structure()

        # Calcul du score global
        self._calculate_score()

        # Génération des recommandations
        self._generate_recommendations()

        return self.audit_results

    def _analyze_project_info(self):
        """Analyse des informations du projet"""
        info = {
            "name": self.project_path.name,
            "type": self._detect_project_type(),
            "size": self._calculate_project_size(),
            "languages": self._detect_languages(),
            "dependencies": self._detect_dependencies(),
            "last_modified": self._get_last_modified()
        }
        self.audit_results["info"] = info

    def _detect_project_type(self) -> str:
        """Détection automatique du type de projet"""
        files = list(self.project_path.rglob("*"))
        if any(file_handle.name == "package.json" for file_handle in files):
            return "Node.js / JS"
        elif any(file_handle.name == "requirements.txt" for file_handle in files):
            return "Python"
        elif any(file_handle.name == "pom.xml" for file_handle in files):
            return "Java / Maven"
        elif any(file_handle.name == "Cargo.toml" for file_handle in files):
            return "Rust"
        elif any(file_handle.name == "go.mod" for file_handle in files):
            return "Go"
        elif any(file_handle.name == "Dockerfile" for file_handle in files):
            return "Docker"
        else:
            return "Multi-langage/Autre"

    def _calculate_project_size(self) -> Dict[str, int]:
        """Calcul de la taille du projet"""
        total_files = 0
        total_lines = 0
        code_files = 0
        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                total_files += 1
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_handle:
                        lines = len(file_handle.readlines())
                        total_lines += lines
                        if self._is_code_file(file_path):
                            code_files += 1
                except Exception:
                    pass
        return {
            "total_files": total_files,
            "total_lines": total_lines,
            "code_files": code_files
        }

    def _is_code_file(self, file_path: Path) -> bool:
        """Détermine si un fichier est un fichier de code"""
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h',
            '.go', '.rs', '.php', '.rb', '.swift', '.kt', '.scala', '.cs'
        }
        return file_path.suffix.lower() in code_extensions

    def _detect_languages(self) -> List[str]:
        """Détection des langages du projet"""
        languages = set()
        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext == '.py':
                    languages.add('Python')
                elif ext in ['.js', '.jsx']:
                    languages.add('JavaScript')
                elif ext in ['.ts', '.tsx']:
                    languages.add('TypeScript')
                elif ext == '.java':
                    languages.add('Java')
                elif ext == '.go':
                    languages.add('Go')
                elif ext == '.rs':
                    languages.add('Rust')
                elif ext == '.php':
                    languages.add('PHP')
                elif ext == '.rb':
                    languages.add('Ruby')
        return list(languages)

    def _detect_dependencies(self) -> Dict[str, List[str]]:
        """Détection des dépendances du projet"""
        dependencies = {}
        # Python
        req_file = self.project_path / "requirements.txt"
        if req_file.exists():
            try:
                with open(req_file, 'r') as file_handle:
                    deps = [
                        line.strip() for line in file_handle
                        if line.strip() and not line.startswith('#')
                    ]
                    dependencies['python'] = deps
            except Exception:
                pass
        # Node.js
        package_file = self.project_path / "package.json"
        if package_file.exists():
            try:
                with open(package_file, 'r') as file_handle:
                    data = json.load(file_handle)
                    deps = list(data.get('dependencies', {}).keys())
                    dev_deps = list(data.get('devDependencies', {}).keys())
                    dependencies['nodejs'] = deps + dev_deps
            except Exception:
                pass
        return dependencies

    def _get_last_modified(self) -> str:
        """Date de dernière modification"""
        latest = 0
        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                mtime = file_path.stat().st_mtime
                if mtime > latest:
                    latest = mtime
        return datetime.fromtimestamp(latest).strftime("%Y-%m-%d %H:%M:%S")

    def _analyze_code_quality(self):
        """Analyse de la qualité du code"""
        quality = {
            "complexity": self._analyze_complexity(),
            "style": self._analyze_style(),
            "documentation": self._analyze_code_documentation(),
            "naming": self._analyze_naming_conventions()
        }
        self.audit_results["code_quality"] = quality

    def _analyze_complexity(self) -> Dict[str, Any]:
        """Analyse de la complexité du code"""
        complexity_scores = []

        for file_path in self.project_path.rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    tree = ast.parse(file_handle.read())
                    complexity = self._calculate_cyclomatic_complexity(tree)
                    complexity_scores.append(complexity)
            except Exception:
                pass

        if complexity_scores:
            avg_complexity = sum(complexity_scores) / len(complexity_scores)
            max_complexity = max(complexity_scores)
        else:
            avg_complexity = max_complexity = 0

        return {
            "avg_complexity": avg_complexity,
            "max_complexity": max_complexity,
            "status": "✅" if avg_complexity < 10 else "⚠️"
        }

    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calcul de la complexité cyclomatique d'un fichier"""
        complexity = 1  # Base complexity

        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1

        return complexity

    def _analyze_style(self) -> Dict[str, Any]:
        """Analyse du style du code"""
        style_issues = []

        for file_path in self.project_path.rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    lines = file_handle.readlines()
                    for index, line in enumerate(lines, 1):
                        if len(line.rstrip()) > 120:
                            style_issues.append(
                                f"Ligne trop longue: {file_path.name}:{index}"
                            )
                        if line.strip() and not line.startswith('#'):
                            if not line.startswith(
                                    (' ', '\t')) and line.strip():
                                if not any(
                                    keyword in line for keyword in [
                                        'class ', 'def ', 'import ', 'from ']):
                                    style_issues.append(
                                        f"Indentation: {file_path.name}:{index}")
            except Exception:
                pass

        return {
            "issues": style_issues,
            "status": "✅" if len(style_issues) < 10 else "⚠️"
        }

    def _analyze_code_documentation(self) -> Dict[str, Any]:
        """Analyse de la documentation du code"""
        documented_functions = 0
        total_functions = 0

        for file_path in self.project_path.rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    tree = ast.parse(file_handle.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            total_functions += 1
                            if ast.get_docstring(node):
                                documented_functions += 1
            except Exception:
                pass

        coverage = (
            documented_functions
            / total_functions
            * 100) if total_functions > 0 else 0

        return {
            "coverage": coverage,
            "documented_functions": documented_functions,
            "total_functions": total_functions,
            "status": "✅" if coverage > 80 else "⚠️" if coverage < 50 else "✅"
        }

    def _analyze_naming_conventions(self) -> Dict[str, Any]:
        """Analyse des conventions de nommage"""
        issues = []

        for file_path in self.project_path.rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    tree = ast.parse(file_handle.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                                issues.append(
                                    f"Fonction: {node.name} dans {file_path.name}")
                        elif isinstance(node, ast.ClassDef):
                            if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                                issues.append(
                                    f"Classe: {node.name} dans {file_path.name}")
            except Exception:
                pass

        return {
            "issues": issues,
            "status": "✅" if len(issues) < 5 else "⚠️"
        }

    def _analyze_security(self):
        """Analyse de la sécurité"""
        security = {
            "vulnerabilities": self._detect_security_vulnerabilities(),
            "secrets": self._detect_secrets(),
            "permissions": self._analyze_permissions()
        }
        self.audit_results["security"] = security

    def _detect_security_vulnerabilities(self) -> List[str]:
        """Détection des vulnérabilités de sécurité"""
        vulnerabilities = []

        # Recherche de patterns dangereux
        dangerous_patterns = [
            (r'eval\(', "Utilisation de 'eval()'"),
            (r'exec\(', "Utilisation de 'exec()'"),
            (r'os\.system\(', "Utilisation de 'os.system()'"),
            (r'subprocess\.call\(', "Utilisation de 'subprocess.call()'"),
            (r'password\s*=\s*["\'][^"\']+["\']', "Mot de passe en clair"),
            (r'api_key\s*=\s*["\'][^"\']+["\']', "Clé API en clair")
        ]

        for file_path in self.project_path.rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    content = file_handle.read()
                    for pattern, description in dangerous_patterns:
                        if re.search(pattern, content):
                            vulnerabilities.append(
                                f"{description}: {file_path.name}")
            except Exception:
                pass

        return vulnerabilities

    def _detect_secrets(self) -> List[str]:
        """Détection de secrets"""
        secrets = []

        secret_patterns = [
            r'[A-Za-z0-9+/]{40,}={0,2}',  # Base64 long
            r'sk_[A-Za-z0-9]{24}',  # Stripe secret key
            r'AKIA[0-9A-Z]{16}',  # AWS access key
        ]

        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_handle:
                        content = file_handle.read()
                        for pattern in secret_patterns:
                            if re.search(pattern, content):
                                secrets.append(
                                    f"Secret détecté: {file_path.name}")
                                break
                except Exception:
                    pass

        return secrets

    def _analyze_permissions(self) -> Dict[str, Any]:
        """Analyse des permissions des fichiers"""
        sensitive_files = []

        for file_path in self.project_path.rglob("*f"):
            if file_path.is_file():
                try:
                    stat = file_path.stat()
                    if stat.st_mode & 0o777 == 0o777:  # Permissions trop ouvertes
                        sensitive_files.append(str(file_path))
                except Exception:
                    pass

        return {
            "files": sensitive_files,
            "status": "✅" if not sensitive_files else "⚠️"
        }

    def _analyze_performance(self):
        """Analyse de la performance"""
        performance = {
            "file_sizes": self._analyze_file_sizes(),
            "imports": self._analyze_imports(),
            "memory_usage": self._estimate_memory_usage()
        }
        self.audit_results["performance"] = performance

    def _analyze_file_sizes(self) -> Dict[str, Any]:
        """Analyse de la taille des fichiers"""
        large_files = []
        total_size = 0

        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                size = file_path.stat().st_size
                total_size += size
                if size > 1024 * 1024:  # > 1MB
                    large_files.append(
                        f"{file_path.name}: {size / 1024 / 1024:.1f}MB")

        return {
            "total_size_mb": total_size / 1024 / 1024,
            "large_files": large_files,
            "status": "✅" if len(large_files) < 5 else "⚠️"
        }

    def _analyze_imports(self) -> Dict[str, Any]:
        """Analyse des imports"""
        imports = []

        for file_path in self.project_path.rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    tree = ast.parse(file_handle.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                imports.append(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                imports.append(node.module)
            except Exception:
                pass

        return {
            "total_imports": len(imports),
            "unique_imports": len(set(imports)),
            "status": "✅" if len(imports) < 100 else "⚠️"
        }

    def _estimate_memory_usage(self) -> Dict[str, Any]:
        """Estimation de la list_datausage"""
        # Estimation basique basée sur la taille du code
        code_size = 0
        for file_path in self.project_path.rglob("*.py"):
            if file_path.is_file():
                code_size += file_path.stat().st_size

        estimated_memory = code_size * 0.1  # Estimation approximative

        return {
            "estimated_mb": estimated_memory / 1024 / 1024,
            "status": "✅" if estimated_memory < 50 * 1024 * 1024 else "⚠️"
        }

    def _analyze_documentation(self):
        """Analyse de la documentation"""
        docs = {
            "readme": self._check_readme(),
            "api_docs": self._check_api_documentation(),
            "code_docs": self._analyze_code_documentation(),
            "guides": self._check_guides()
        }
        self.audit_results["documentation"] = docs

    def _check_readme(self) -> Dict[str, Any]:
        """Vérification du README"""
        readme_files = list(self.project_path.glob("README*"))

        if readme_files:
            readme = readme_files[0]
            try:
                with open(readme, 'r', encoding='utf-8') as file_handle:
                    content = file_handle.read()
                    has_installation = "installation" in content.lower()
                    has_usage = "usage" in content.lower() or "utilisation" in content.lower()
                    has_license = "license" in content.lower()

                    score = sum([has_installation, has_usage, has_license])

                    return {
                        "exists": True,
                        "score": score,
                        "status": "✅" if score == 3 else "⚠️"
                    }
            except Exception:
                pass

        return {"exists": False, "score": 0, "status": "❌"}

    def _check_api_documentation(self) -> Dict[str, Any]:
        """Vérification de la documentation API"""
        api_docs = []

        for pattern in ["*api*.py", "*api*.py", "docs/*.py", "docs/*.py"]:
            api_docs.extend(self.project_path.glob(pattern))

        return {
            "files": [str(doc) for doc in api_docs],
            "status": "✅" if api_docs else "❌"
        }

    def _check_guides(self) -> Dict[str, Any]:
        """Vérification des guides"""
        guides = []

        for pattern in [
            "*guide*.py",
            "*tutorial*.py",
            "docs / guides/*",
                "docs / tutorials/*py"]:
            guides.extend(self.project_path.glob(pattern))

        return {
            "files": [str(guide) for guide in guides],
            "status": "✅" if guides else "❌"
        }

    def _analyze_testing(self):
        """Analyse des tests"""
        testing = {
            "coverage": self._analyze_test_coverage(),
            "test_files": self._find_test_files(),
            "quality": self._analyze_test_quality()
        }
        self.audit_results["testing"] = testing

    def _analyze_test_coverage(self) -> Dict[str, Any]:
        """Analyse de la couverture de tests"""
        test_files = list(self.project_path.rglob("*test*.py"))
        source_files = list(self.project_path.rglob("*.py"))

        # Exclure les fichiers de test des fichiers source
        source_files = [
            file_handle for file_handle in source_files
            if "test" not in file_handle.name.lower()
        ]

        coverage_ratio = len(test_files) / \
            len(source_files) if source_files else 0

        return {
            "total_test_files": len(test_files),
            "total_source_files": len(source_files),
            "coverage_ratio": coverage_ratio,
            "status": "✅" if coverage_ratio > 0.8 else "⚠️" if coverage_ratio < 0.3 else "✅"}

    def _find_test_files(self) -> List[str]:
        """Trouve les fichiers de tests"""
        test_files = []

        for pattern in ["*test*.py", "*_test.py", "tests/*.py"]:
            test_files.extend(self.project_path.glob(pattern))

        return [str(file_handle) for file_handle in test_files]

    def _analyze_test_quality(self) -> Dict[str, Any]:
        """Analyse de la qualité des tests"""
        quality_issues = []

        for file_path in self.project_path.rglob("*test*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file_handle:
                    content = file_handle.read()
                    if "assert" not in content and "self." not in content:
                        quality_issues.append(
                            f"Pas d'assertions: {file_path.name}")
                    if "def test_" not in content:
                        quality_issues.append(
                            f"Pas de fonctions de test: {file_path.name}")
            except Exception:
                pass

        return {
            "issues": quality_issues,
            "status": "✅" if len(quality_issues) < 3 else "⚠️"
        }

    def _analyze_structure(self):
        """Analyse de la structure du projet"""
        structure = {
            "organization": self._analyze_organization(),
            "naming": self._analyze_structure_naming(),
            "modularity": self._analyze_modularity()
        }
        self.audit_results["structure"] = structure

    def _analyze_organization(self) -> Dict[str, Any]:
        """Analyse de l'organisation des dossiers"""
        directories = [
            dict_data for dict_data in self.project_path.iterdir() if dict_data.is_dir()]

        expected_dirs = ["src", "tests", "docs", "scripts", "data"]
        found_dirs = (dict_data.name for dict_data in directories)

        organization_score = sum(
            1 for dict_data in expected_dirs if dict_data in found_dirs)

        return {
            "score": organization_score,
            "found_dirs": found_dirs,
            "status": "✅ Bien" if organization_score > 3 else "⚠️ À"
        }

    def _analyze_structure_naming(self) -> Dict[str, Any]:
        """Analyse du nommage des fichiers et dossiers"""
        issues = []

        for item in self.project_path.rglob("*"):
            if item.is_file() or item.is_dir():
                name = item.name
                if " " in name:
                    issues.append(f"Espaces dans le nom: {name}")
                if name.startswith(".") and name not in [".py", ".py"]:
                    issues.append(f"Fichier caché: {name}")

        return {
            "issues": issues,
            "status": "✅" if len(issues) < 5 else "⚠️"
        }

    def _analyze_modularity(self) -> Dict[str, Any]:
        """Analyse de la modularité"""
        modules = []

        for file_path in self.project_path.rglob("*.py"):
            if file_path.name == "__init__.py":
                modules.append(str(file_path.parent))

        return {
            "modules": modules,
            "count": len(modules),
            "status": "✅" if len(modules) > 2 else "⚠️"
        }

    def _calculate_score(self):
        """Calcul du score global"""
        scores = []

        # Code quality (30%)
        quality = self.audit_results["code_quality"]
        if quality["complexity"]["status"] == "✅":
            scores.append(30)
        elif quality["complexity"]["status"] == "⚠️":
            scores.append(15)
        else:
            scores.append(0)

        # Security (25%)
        security = self.audit_results["security"]
        if not security["vulnerabilities"] and not security["permissions"]["files"]:
            scores.append(25)
        elif len(security["vulnerabilities"]) < 3:
            scores.append(15)
        else:
            scores.append(5)

        # Documentation (20%)
        docs = self.audit_results["documentation"]
        if docs["readme"]["status"] == "✅":
            scores.append(20)
        elif docs["readme"]["status"] == "⚠️":
            scores.append(10)
        else:
            scores.append(0)

        # Testing (15%)
        testing = self.audit_results["testing"]
        if testing["coverage"]["status"] == "✅":
            scores.append(15)
        elif testing["coverage"]["status"] == "✅":
            scores.append(10)
        else:
            scores.append(5)

        # Structure (10%)
        structure = self.audit_results["structure"]
        if structure["organization"]["status"] == "✅ Bien":
            scores.append(10)
        else:
            scores.append(5)

        self.audit_results["score"] = sum(scores)

    def _generate_recommendations(self):
        """Génération des recommandations"""
        recommendations = []

        # Basé sur le score
        score = self.audit_results["score"]
        if score < 50:
            recommendations.append("🔴 Projet nécessite une refactorisation")
        elif score < 70:
            recommendations.append("🟡 Projet nécessite des améliorations")
        else:
            recommendations.append("🟢 Projet de bonne qualité")

        # Basé sur les analyses
        if self.audit_results["security"]["vulnerabilities"]:
            recommendations.append("🔒 Corriger les vulnérabilités de sécurité")

        if self.audit_results["documentation"]["readme"]["status"] != "✅":
            recommendations.append("📚 Améliorer la documentation")

        if self.audit_results["testing"]["coverage"]["status"] == "⚠️":
            recommendations.append("🧪 Augmenter la couverture de tests")

        if self.audit_results["code_quality"]["complexity"]["status"] == "⚠️":
            recommendations.append("⚡ Réduire la complexité du code")

        if self.audit_results["structure"]["organization"]["status"] == "⚠️ À":
            recommendations.append("📁 Réorganiser la structure du projet")

        self.audit_results["recommendations"] = recommendations

    def generate_report(self) -> str:
        """Génère un rapport d'audit"""
        report = f"""
{'='*60}
🔍 RAPPORT D'AUDIT INTELLIGENT - {self.audit_results['info']['name']}
{'='*60}

📊 SCORE GLOBAL: {self.audit_results['score']}/100

📋 INFORMATIONS PROJET:
   • Type: {self.audit_results['info']['type']}
   • Langages: {', '.join(self.audit_results['info']['languages'])}
   • Taille: {self.audit_results['info']['size']['total_files']} fichiers
   • Dernière modification: {self.audit_results['info']['last_modified']}

🔒 SÉCURITÉ: {len(self.audit_results['security']['vulnerabilities'])} vulnérabilités détectées
📚 DOCUMENTATION: {self.audit_results['documentation']['readme']['status']}
🧪 TESTS: {self.audit_results['testing']['coverage']['status']}
⚡ PERFORMANCE: {self.audit_results['performance']['file_sizes']['status']}
📁 STRUCTURE: {self.audit_results['structure']['organization']['status']}

💡 RECOMMANDATIONS:
"""

        for rec in self.audit_results["recommendations"]:
            report += f"   • {rec}\n"

        report += f"\n{'='*60}\n"

        return report


def main():
    """Point d'entrée"""
    if len(sys.argv) != 2:
        logger.info("Usage: python intelligent_auditor.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        logger.info(f"❌ Le chemin {project_path} n'existe pas")
        sys.exit(1)

    auditor = IntelligentAuditor()
    results = auditor.audit_project(project_path)

    # Affichage du rapport
    logger.info(auditor.generate_report())

    # Sauvegarde du rapport JSON
    report_file = f"audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w', encoding='utf-8') as file_handle:
        json.dump(results, file_handle, indent=2, ensure_ascii=False)

    logger.info(f"📄 Rapport sauvegardé: {report_file}")


if __name__ == "__main__":
    main()
