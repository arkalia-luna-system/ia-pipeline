#!/usr/bin/env python3
import ast
import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

"""
Module audit intelligent pour Athalia
Analyse automatique complète des projets avec recommandations
"""


class IntelligentAuditor:
    """Auditeur intelligent pour analyse automatique des projets"""

    def __init__(self, project_path: str | None = None):
        self.project_path: Path | None = Path(project_path) if project_path else None
        self.audit_results: dict[str, Any] = {}
        self.recommendations: list[str] = []

    def run(self) -> dict[str, Any]:
        """Méthode run() pour lorchestrateur - exécute laudit"""
        if not self.project_path:
            raise ValueError("project_path doit être défini")
        return self.audit_project(str(self.project_path))

    def audit_project(self, project_path: str) -> dict[str, Any]:
        """Audit complet dun projet"""
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
            "score": 0,
        }

        logger.info(f" Audit intelligent en cours pour: {self.project_path.name}")

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

    # Méthodes publiques pour les tests
    def analyze_project_structure(self) -> dict[str, Any]:
        """Analyse la structure du projet"""
        return self.audit_results.get("structure", {})

    def analyze_code_quality(self) -> dict[str, Any]:
        """Analyse la qualité du code"""
        return self.audit_results.get("code_quality", {})

    def analyze_dependencies(self) -> dict[str, Any]:
        """Analyse les dépendances du projet"""
        return self.audit_results.get("info", {}).get("dependencies", {})

    def analyze_security_vulnerabilities(self) -> list[str]:
        """Analyse les vulnérabilités de sécurité"""
        return self.audit_results.get("security", {}).get("vulnerabilities", [])

    def analyze_performance_bottlenecks(self) -> dict[str, Any]:
        """Analyse les goulots d'étranglement de performance"""
        return self.audit_results.get("performance", {})

    def calculate_technical_debt(self) -> float:
        """Calcule la dette technique"""
        code_quality = self.audit_results.get("code_quality", {})
        complexity_score = code_quality.get("complexity", {}).get("score", 0)
        style_score = code_quality.get("style", {}).get("score", 0)
        return float((10 - complexity_score) + (10 - style_score))

    def generate_recommendations(self) -> list[str]:
        """Génère des recommandations d'amélioration"""
        return self.audit_results.get("recommendations", [])

    def audit_code_complexity(self, file_path: str) -> dict[str, Any]:
        """Audite la complexité du code d'un fichier"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
            tree = ast.parse(content)
            complexity = self._calculate_cyclomatic_complexity(tree)
            return {
                "file": file_path,
                "complexity": complexity,
                "score": max(0, 10 - complexity // 5),
            }
        except Exception as e:
            return {"file": file_path, "complexity": 0, "score": 0, "error": str(e)}

    def audit_test_coverage(self) -> dict[str, Any]:
        """Audite la couverture de tests"""
        return self.audit_results.get("testing", {}).get("coverage", {})

    def audit_documentation_quality(self) -> dict[str, Any]:
        """Audite la qualité de la documentation"""
        return self.audit_results.get("documentation", {})

    def detect_code_smells(self) -> list[str]:
        """Détecte les code smells"""
        smells = []
        code_quality = self.audit_results.get("code_quality", {})

        if code_quality.get("complexity", {}).get("score", 0) < 5:
            smells.append("Complexité cyclomatique élevée")

        if code_quality.get("style", {}).get("score", 0) < 5:
            smells.append("Problèmes de style de code")

        return smells

    def analyze_architecture_patterns(self) -> list[str]:
        """Analyse les patterns d'architecture"""
        patterns = []
        structure = self.audit_results.get("structure", {})

        if structure.get("modularity", {}).get("score", 0) > 7:
            patterns.append("Architecture modulaire")

        if structure.get("organization", {}).get("score", 0) > 7:
            patterns.append("Organisation claire")

        return patterns

    def audit_naming_conventions(self) -> dict[str, Any]:
        """Audite les conventions de nommage"""
        return self.audit_results.get("code_quality", {}).get("naming", {})

    def analyze_cyclomatic_complexity(self) -> dict[str, Any]:
        """Analyse la complexité cyclomatique"""
        return self.audit_results.get("code_quality", {}).get("complexity", {})

    def run_full_audit(self) -> dict[str, Any]:
        """Exécute un audit complet"""
        return self.audit_project(str(self.project_path))

    def generate_audit_report(self) -> str:
        """Génère un rapport d'audit"""
        return self.generate_report()

    def _analyze_project_info(self) -> None:
        """Analyse des informations du projet"""
        if self.project_path is not None:
            info = {
                "name": self.project_path.name,
                "type": self._detect_project_type(),
                "size": self._calculate_project_size(),
                "languages": self._detect_languages(),
                "dependencies": self._detect_dependencies(),
                "last_modified": self._get_last_modified(),
            }
            self.audit_results["info"] = info

    def _detect_project_type(self) -> str:
        """Détection automatique du type de projet"""
        if self.project_path is None:
            return "Unknown"

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

    def _calculate_project_size(self) -> dict[str, int]:
        """Calcul de la taille du projet"""
        total_files = 0
        total_lines = 0
        total_size = 0

        if self.project_path is not None:
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file():
                    total_files += 1
                    try:
                        total_size += file_path.stat().st_size
                        if self._is_code_file(file_path):
                            with open(file_path, encoding="utf-8") as f:
                                total_lines += len(f.readlines())
                    except (OSError, UnicodeDecodeError):
                        continue

        return {
            "files": total_files,
            "lines": total_lines,
            "size_bytes": total_size,
            "size_mb": int(round(total_size / (1024 * 1024), 0)),
        }

    def _is_code_file(self, file_path: Path) -> bool:
        """Vérifie si un fichier est un fichier de code"""
        code_extensions = {
            ".py",
            ".js",
            ".ts",
            ".java",
            ".cpp",
            ".c",
            ".h",
            ".hpp",
            ".cs",
            ".php",
            ".rb",
            ".go",
            ".rs",
            ".swift",
            ".kt",
            ".scala",
        }
        return file_path.suffix.lower() in code_extensions

    def _detect_languages(self) -> list[str]:
        """Détecte les langages utilisés dans le projet"""
        languages = set()
        if self.project_path is not None:
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file():
                    ext = file_path.suffix.lower()
                    if ext == ".py":
                        languages.add("Python")
                    elif ext in [".js", ".ts", ".jsx", ".tsx"]:
                        languages.add("JavaScript/TypeScript")
                    elif ext in [".java", ".class"]:
                        languages.add("Java")
                    elif ext in [".cpp", ".c", ".h", ".hpp"]:
                        languages.add("C/C++")
                    elif ext == ".rs":
                        languages.add("Rust")
                    elif ext == ".go":
                        languages.add("Go")
                    elif ext == ".php":
                        languages.add("PHP")
                    elif ext == ".rb":
                        languages.add("Ruby")

        return list(languages)

    def _detect_dependencies(self) -> dict[str, list[str]]:
        """Détecte les dépendances du projet"""
        dependencies: dict[str, list[str]] = {"direct": [], "indirect": []}

        if self.project_path is not None:
            # Python
            requirements_file = self.project_path / "requirements.txt"
            if requirements_file.exists():
                try:
                    with open(requirements_file, encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith("#"):
                                dep = line.split("==")[0].split(">=")[0].split("<=")[0]
                                dependencies["direct"].append(dep)
                except Exception as e:
                    logger.debug(f"Erreur lors de l'analyse des dépendances: {e}")
                    pass

            # Node.js
            package_json = self.project_path / "package.json"
            if package_json.exists():
                try:
                    with open(package_json, encoding="utf-8") as f:
                        data = json.load(f)
                        if "dependencies" in data:
                            dependencies["direct"].extend(
                                list(data["dependencies"].keys())
                            )
                        if "devDependencies" in data:
                            dependencies["direct"].extend(
                                list(data["devDependencies"].keys())
                            )
                except Exception as e:
                    logger.debug(f"Erreur lors de l'analyse des dépendances: {e}")
                    pass

        return dependencies

    def _get_last_modified(self) -> str:
        """Obtient la date de dernière modification"""
        try:
            latest_time: float = 0.0
            if self.project_path is not None:
                for file_path in self.project_path.rglob("*"):
                    if file_path.is_file():
                        mtime = file_path.stat().st_mtime
                        if mtime > latest_time:
                            latest_time = mtime
            return datetime.fromtimestamp(latest_time).isoformat()
        except Exception as e:
            logger.debug(f"Erreur lors du calcul de la dernière modification: {e}")
            return "Inconnu"

    def _analyze_code_quality(self):
        """Analyse de la qualité du code"""
        quality = {
            "complexity": self._analyze_complexity(),
            "style": self._analyze_style(),
            "naming": self._analyze_naming_conventions(),
            "documentation": self._analyze_code_documentation(),
        }
        self.audit_results["code_quality"] = quality

    def _analyze_complexity(self) -> dict[str, Any]:
        """Analyse de la complexité du code"""
        complexity_scores = []
        total_files = 0

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file() and "test" not in py_file.name.lower():
                    total_files += 1
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            content = f.read()
                        tree = ast.parse(content)
                        score = self._calculate_cyclomatic_complexity(tree)
                        complexity_scores.append(score)
                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de complexité: {e}")
                        complexity_scores.append(0)

        if complexity_scores:
            avg_complexity = sum(complexity_scores) / len(complexity_scores)
            max_complexity = max(complexity_scores)
            score = int(max(0, 10 - (avg_complexity / 2)))
        else:
            avg_complexity = 0
            max_complexity = 0
            score = 10

        return {
            "average": round(avg_complexity, 2),
            "max": max_complexity,
            "score": round(score, 2),
            "files_analyzed": total_files,
        }

    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calcule la complexité cyclomatique d'un AST"""
        complexity = 1  # Base complexity

        for node in ast.walk(tree):
            if isinstance(node, ast.If | ast.While | ast.For | ast.AsyncFor):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.With):
                complexity += 1
            elif isinstance(node, ast.Assert):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1

        return complexity

    def _analyze_style(self) -> dict[str, Any]:
        """Analyse du style de code"""
        style_issues = []
        total_files = 0

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file():
                    total_files += 1
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            lines = f.readlines()

                        for i, line in enumerate(lines, 1):
                            if len(line.rstrip()) > 79:
                                style_issues.append(
                                    f"{py_file}:{i} - Ligne trop longue"
                                )
                            if line.endswith(" \n"):
                                style_issues.append(
                                    f"{py_file}:{i} - Espace en fin de ligne"
                                )
                            if line.startswith("import ") and "," in line:
                                style_issues.append(
                                    f"{py_file}:{i} - Import multiple sur une ligne"
                                )

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        score = max(0, 10 - len(style_issues))
        return {
            "issues": style_issues,
            "score": score,
            "files_analyzed": total_files,
        }

    def _analyze_code_documentation(self) -> dict[str, Any]:
        """Analyse de la documentation du code"""
        doc_issues = []
        total_functions = 0
        documented_functions = 0

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file():
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            content = f.read()
                        tree = ast.parse(content)

                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                                total_functions += 1
                                if ast.get_docstring(node):
                                    documented_functions += 1
                                else:
                                    doc_issues.append(
                                        f"{py_file}:{node.lineno} - Fonction sans docstring"
                                    )

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        if total_functions > 0:
            doc_coverage = (documented_functions / total_functions) * 100
            score = round(doc_coverage / 10, 2)
        else:
            doc_coverage = 100
            score = 10

        return {
            "coverage": round(doc_coverage, 2),
            "score": score,
            "total_functions": total_functions,
            "documented_functions": documented_functions,
            "issues": doc_issues,
        }

    def _analyze_naming_conventions(self) -> dict[str, Any]:
        """Analyse des conventions de nommage"""
        naming_issues = []
        total_names = 0
        compliant_names = 0

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file():
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            content = f.read()
                        tree = ast.parse(content)

                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                total_names += 1
                                if node.name.replace("_", "").islower():
                                    compliant_names += 1
                                else:
                                    naming_issues.append(
                                        f"{py_file}:{node.lineno} - Nom de fonction non conforme: {node.name}"
                                    )
                            elif isinstance(node, ast.ClassDef):
                                total_names += 1
                                if node.name[0].isupper():
                                    compliant_names += 1
                                else:
                                    naming_issues.append(
                                        f"{py_file}:{node.lineno} - Nom de classe non conforme: {node.name}"
                                    )

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        if total_names > 0:
            compliance_rate = (compliant_names / total_names) * 100
            score = round(compliance_rate / 10, 2)
        else:
            compliance_rate = 100
            score = 10

        return {
            "compliance_rate": round(compliance_rate, 2),
            "score": score,
            "total_names": total_names,
            "compliant_names": compliant_names,
            "issues": naming_issues,
        }

    def _analyze_security(self):
        """Analyse de sécurité"""
        security = {
            "vulnerabilities": self._detect_security_vulnerabilities(),
            "secrets": self._detect_secrets(),
            "permissions": self._analyze_permissions(),
        }
        self.audit_results["security"] = security

    def _detect_security_vulnerabilities(self) -> list[str]:
        """Détecte les vulnérabilités de sécurité"""
        vulnerabilities = []

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file():
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            content = f.read()

                        # Détection de patterns dangereux
                        dangerous_patterns = [
                            (r"eval\s*\(", "Utilisation de eval()"),
                            (r"exec\s*\(", "Utilisation de exec()"),
                            (
                                r"subprocess\.call.*shell=True",
                                "Subprocess avec shell=True",
                            ),
                            (r"pickle\.loads", "Utilisation de pickle.loads"),
                            (r"yaml\.load\(", "Utilisation de yaml.load()"),
                        ]

                        for pattern, description in dangerous_patterns:
                            if re.search(pattern, content):
                                vulnerabilities.append(f"{py_file}: {description}")

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        return vulnerabilities

    def _detect_secrets(self) -> list[str]:
        """Détecte les secrets exposés"""
        secrets = []

        if self.project_path is not None:
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and file_path.suffix in [
                    ".py",
                    ".env",
                    ".txt",
                    ".md",
                ]:
                    try:
                        with open(file_path, encoding="utf-8") as f:
                            content = f.read()

                        # Patterns de secrets
                        secret_patterns = [
                            r"password\s*=\s*['\"][^'\"]+['\"]",
                            r"secret\s*=\s*['\"][^'\"]+['\"]",
                            r"api_key\s*=\s*['\"][^'\"]+['\"]",
                            r"token\s*=\s*['\"][^'\"]+['\"]",
                        ]

                        for pattern in secret_patterns:
                            if re.search(pattern, content, re.IGNORECASE):
                                secrets.append(f"{file_path}: Secret potentiel détecté")
                                break

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        return secrets

    def _analyze_permissions(self) -> dict[str, Any]:
        """Analyse des permissions de fichiers"""
        permission_issues = []

        if self.project_path is not None:
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file():
                    try:
                        stat = file_path.stat()
                        mode = stat.st_mode & 0o777

                        if mode & 0o777 == 0o777:  # Permissions trop ouvertes
                            permission_issues.append(
                                f"{file_path}: Permissions trop ouvertes (777)"
                            )
                        elif (
                            mode & 0o200 == 0o200 and mode & 0o020 == 0o020
                        ):  # Écriture groupe et autres
                            permission_issues.append(
                                f"{file_path}: Permissions d'écriture trop ouvertes"
                            )

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        return {
            "issues": permission_issues,
            "score": max(0, 10 - len(permission_issues)),
        }

    def _analyze_performance(self):
        """Analyse de performance"""
        performance = {
            "file_sizes": self._analyze_file_sizes(),
            "imports": self._analyze_imports(),
            "memory_usage": self._estimate_memory_usage(),
        }
        self.audit_results["performance"] = performance

    def _analyze_file_sizes(self) -> dict[str, Any]:
        """Analyse de la taille des fichiers"""
        file_sizes = []

        if self.project_path is not None:
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and self._is_code_file(file_path):
                    try:
                        size = file_path.stat().st_size
                        file_sizes.append(size)
                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        if file_sizes:
            avg_size = sum(file_sizes) / len(file_sizes)
            max_size = max(file_sizes)
            score = max(
                0, 10 - (max_size / (1024 * 100))
            )  # Pénaliser les gros fichiers
        else:
            avg_size = 0
            max_size = 0
            score = 10

        return {
            "average_size": round(avg_size, 2),
            "max_size": max_size,
            "score": round(score, 2),
        }

    def _analyze_imports(self) -> dict[str, Any]:
        """Analyse des imports"""
        import_issues = []
        total_imports = 0

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file():
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            content = f.read()
                        tree = ast.parse(content)

                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                total_imports += len(node.names)
                                for alias in node.names:
                                    if alias.name.startswith("_"):
                                        import_issues.append(
                                            f"{py_file}: Import de module privé: {alias.name}"
                                        )
                            elif isinstance(node, ast.ImportFrom):
                                total_imports += 1
                                if node.module and node.module.startswith("_"):
                                    import_issues.append(
                                        f"{py_file}: Import de module privé: {node.module}"
                                    )

                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        return {
            "total_imports": total_imports,
            "issues": import_issues,
            "score": max(0, 10 - len(import_issues)),
        }

    def _estimate_memory_usage(self) -> dict[str, Any]:
        """Estime l'usage mémoire"""
        total_lines = 0

        if self.project_path is not None:
            for py_file in self.project_path.rglob("*.py"):
                if py_file.is_file():
                    try:
                        with open(py_file, encoding="utf-8") as f:
                            total_lines += len(f.readlines())
                    except Exception as e:
                        logger.debug(f"Erreur lors de l'analyse de fichier: {e}")
                        continue

        # Estimation: ~1KB par 100 lignes
        estimated_memory = total_lines / 100

        return {
            "estimated_memory_kb": round(estimated_memory, 2),
            "total_lines": total_lines,
        }

    def _analyze_documentation(self):
        """Analyse de la documentation"""
        documentation = {
            "readme": self._check_readme(),
            "api_docs": self._check_api_documentation(),
            "guides": self._check_guides(),
        }
        self.audit_results["documentation"] = documentation

    def _check_readme(self) -> dict[str, Any]:
        """Vérifie la qualité du README"""
        if self.project_path is None:
            return {
                "exists": False,
                "score": 0,
                "issues": ["Chemin de projet non défini"],
            }

        readme_files = list(self.project_path.glob("README*"))

        if not readme_files:
            return {"exists": False, "score": 0, "issues": ["README manquant"]}

        readme_file = readme_files[0]
        try:
            with open(readme_file, encoding="utf-8") as f:
                content = f.read()

            score = 5  # Score de base
            issues = []

            # Vérifications
            if len(content) < 100:
                issues.append("README trop court")
                score -= 2

            if "## Installation" not in content:
                issues.append("Section Installation manquante")
                score -= 1

            if "## Utilisation" not in content:
                issues.append("Section Utilisation manquante")
                score -= 1

            if "## Tests" not in content:
                issues.append("Section Tests manquante")
                score -= 1

            return {
                "exists": True,
                "score": max(0, score),
                "issues": issues,
                "size": len(content),
            }

        except Exception as e:
            logger.debug(f"Erreur lors de la lecture du README: {e}")
            return {"exists": True, "score": 0, "issues": ["Erreur de lecture"]}

    def _check_api_documentation(self) -> dict[str, Any]:
        """Vérifie la documentation API"""
        if self.project_path is None:
            return {"exists": False, "score": 0}

        api_docs = list(self.project_path.rglob("*api*"))
        api_docs.extend(list(self.project_path.rglob("*docs*")))

        if not api_docs:
            return {"exists": False, "score": 0}

        return {"exists": True, "score": 7}

    def _check_guides(self) -> dict[str, Any]:
        """Vérifie les guides de développement"""
        if self.project_path is None:
            return {"exists": False, "score": 0}

        guides = list(self.project_path.rglob("*guide*"))
        guides.extend(list(self.project_path.rglob("*tutorial*")))

        if not guides:
            return {"exists": False, "score": 0}

        return {"exists": True, "score": 8}

    def _analyze_testing(self):
        """Analyse des tests"""
        testing = {
            "coverage": self._analyze_test_coverage(),
            "files": self._find_test_files(),
            "quality": self._analyze_test_quality(),
        }
        self.audit_results["testing"] = testing

    def _analyze_test_coverage(self) -> dict[str, Any]:
        """Analyse de la couverture de tests"""
        if self.project_path is None:
            return {"coverage": 0, "score": 0, "test_files": 0, "source_files": 0}

        test_files = list(self.project_path.rglob("*test*.py"))
        test_files.extend(list(self.project_path.rglob("tests/*.py")))

        source_files = list(self.project_path.rglob("*.py"))
        source_files = [f for f in source_files if "test" not in f.name.lower()]

        if not source_files:
            return {"coverage": 100, "score": 10, "test_files": len(test_files)}

        coverage = (len(test_files) / len(source_files)) * 100 if source_files else 0
        score = min(10, coverage / 10)

        return {
            "coverage": round(coverage, 2),
            "score": round(score, 2),
            "test_files": len(test_files),
            "source_files": len(source_files),
        }

    def _find_test_files(self) -> list[str]:
        """Trouve les fichiers de test"""
        test_files = []
        if self.project_path is not None:
            for file_path in self.project_path.rglob("*test*.py"):
                if file_path.is_file():
                    test_files.append(str(file_path))
        return test_files

    def _analyze_test_quality(self) -> dict[str, Any]:
        """Analyse de la qualité des tests"""
        test_files = self._find_test_files()
        quality_score = 0

        if self.project_path is not None:
            for test_file in test_files:
                try:
                    with open(test_file, encoding="utf-8") as f:
                        content = f.read()

                    # Vérifications de qualité
                    if "def test_" in content:
                        quality_score += 1
                    if "import pytest" in content:
                        quality_score += 1
                    if "assert" in content:
                        quality_score += 1
                    if "setup_method" in content or "teardown_method" in content:
                        quality_score += 1

                except Exception as e:
                    logger.debug(f"Erreur gérée: {e}")
                    continue

        if test_files:
            avg_quality = quality_score / len(test_files)
            score = min(10, avg_quality * 2.5)
        else:
            score = 0

        return {
            "score": round(score, 2),
            "test_files": len(test_files),
        }

    def _analyze_structure(self):
        """Analyse de la structure du projet"""
        structure = {
            "organization": self._analyze_organization(),
            "naming": self._analyze_structure_naming(),
            "modularity": self._analyze_modularity(),
        }
        self.audit_results["structure"] = structure

    def _analyze_organization(self) -> dict[str, Any]:
        """Analyse de l'organisation du projet"""
        score = 5
        issues = []

        # Vérifier la présence de dossiers standards
        standard_dirs = ["src", "tests", "docs", "config"]
        if self.project_path is not None:
            for dir_name in standard_dirs:
                if (self.project_path / dir_name).exists():
                    score += 1
                else:
                    issues.append(f"Dossier {dir_name} manquant")

        return {
            "score": min(10, score),
            "issues": issues,
        }

    def _analyze_structure_naming(self) -> dict[str, Any]:
        """Analyse du nommage de la structure"""
        score = 5
        issues = []

        if self.project_path is not None:
            for item in self.project_path.iterdir():
                if item.is_dir():
                    name = item.name
                    if name.startswith("."):
                        issues.append(f"Dossier caché: {name}")
                    elif " " in name:
                        issues.append(f"Nom avec espaces: {name}")
                    elif name.lower() != name and name.upper() != name:
                        issues.append(f"Nom mixte: {name}")

        score = max(0, score - len(issues))
        return {
            "score": score,
            "issues": issues,
        }

    def _analyze_modularity(self) -> dict[str, Any]:
        """Analyse de la modularité"""
        if self.project_path is None:
            return {"score": 0, "issues": ["Chemin de projet non défini"]}

        py_files = list(self.project_path.rglob("*.py"))
        init_files = [f for f in py_files if f.name == "__init__.py"]

        if len(py_files) > 0:
            modularity_score = len(init_files) / len(py_files) * 10
        else:
            modularity_score = 0

        return {
            "score": round(modularity_score, 2),
            "total_files": len(py_files),
            "init_files": len(init_files),
        }

    def _calculate_score(self):
        """Calcule le score global du projet"""
        scores = []

        # Récupérer tous les scores
        for category in [
            "code_quality",
            "security",
            "performance",
            "documentation",
            "testing",
            "structure",
        ]:
            category_data = self.audit_results.get(category, {})
            if isinstance(category_data, dict):
                for key, value in category_data.items():
                    if isinstance(value, dict) and "score" in value:
                        scores.append(value["score"])
                    elif key == "score":
                        scores.append(value)

        if scores:
            self.audit_results["score"] = round(sum(scores) / len(scores), 2)
            # Ajouter global_score pour la compatibilité avec les tests
            self.audit_results["global_score"] = self.audit_results["score"]
        else:
            self.audit_results["score"] = 0
            self.audit_results["global_score"] = 0

    def _generate_recommendations(self):
        """Génère des recommandations d'amélioration"""
        recommendations = []
        score = self.audit_results.get("score", 0)

        if score < 5:
            recommendations.append("Amélioration urgente de la qualité du code")
            recommendations.append("Ajout de tests unitaires")
            recommendations.append("Documentation du projet")

        if score < 7:
            recommendations.append("Révision de l'architecture")
            recommendations.append("Optimisation des performances")

        if score < 8:
            recommendations.append("Amélioration de la sécurité")
            recommendations.append("Standardisation du style de code")

        self.audit_results["recommendations"] = recommendations

    def generate_report(self) -> str:
        """Génère un rapport d'audit complet"""
        score = self.audit_results.get("score", 0)

        if self.project_path is None:
            project_name = "Projet inconnu"
        else:
            project_name = self.project_path.name

        report = f"""# Rapport d'Audit Intelligent - {project_name}

## Score Global: {score}/10

## Résumé des Analyses

### Informations du Projet
{self._format_section(self.audit_results.get("info", {}))}

### Qualité du Code
{self._format_section(self.audit_results.get("code_quality", {}))}

### Sécurité
{self._format_section(self.audit_results.get("security", {}))}

### Performance
{self._format_section(self.audit_results.get("performance", {}))}

### Documentation
{self._format_section(self.audit_results.get("documentation", {}))}

### Tests
{self._format_section(self.audit_results.get("testing", {}))}

### Structure
{self._format_section(self.audit_results.get("structure", {}))}

## Recommandations
"""
        for rec in self.audit_results.get("recommendations", []):
            report += f"- {rec}\n"

        return report

    def _format_section(self, data: dict) -> str:
        """Formate une section du rapport"""
        if not data:
            return "Aucune donnée disponible\n"

        formatted = ""
        for key, value in data.items():
            if isinstance(value, dict):
                formatted += f"\n#### {key.title()}\n"
                for sub_key, sub_value in value.items():
                    formatted += f"- {sub_key}: {sub_value}\n"
            elif isinstance(value, list):
                formatted += f"\n#### {key.title()}\n"
                for item in value:
                    formatted += f"- {item}\n"
            else:
                formatted += f"- {key}: {value}\n"

        return formatted


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(description="Auditeur intelligent pour projets")
    parser.add_argument("project_path", help="Chemin vers le projet à auditer")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport")

    args = parser.parse_args()

    auditor = IntelligentAuditor(args.project_path)
    auditor.run()

    report = auditor.generate_report()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Rapport sauvegardé dans {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
