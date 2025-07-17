"""
Module d'audit intelligent pour analyser la qualité des projets générés.
Analyse le code, détecte la dette technique, et propose des améliorations.
"""

import os
import re
import ast
import logging
import json
from datetime import datetime
from typing import Dict, List, Tuple, Any
from collections import defaultdict

class ProjectAuditor:
    """Auditeur intelligent de projets générés."""
    
    def __init__(self, project_path: str):
        self.project_path = project_path
        self.issues: List[str] = []
        self.suggestions: List[str] = []
        self.metrics: Dict[str, Any] = {}
        self.score = 0
        
    def audit_project(self) -> Dict[str, Any]:
        """Audit complet du projet."""
        logging.info(f"🔍 Audit intelligent du projet: {self.project_path}")
        
        if not os.path.exists(self.project_path):
            return {"error": f"Projet non trouvé: {self.project_path}"}
        
        # Analyses
        self._analyze_structure()
        self._analyze_code_quality()
        self._analyze_tests()
        self._analyze_documentation()
        self._analyze_security()
        self._analyze_performance()
        self._calculate_score()
        
        return self._generate_report()
    
    def _analyze_structure(self):
        """Analyse la structure du projet."""
        structure_issues = []
        structure_score = 100
        
        # Vérifier les dossiers essentiels
        essential_dirs = ['src', 'tests', 'docs', 'api']
        missing_dirs = []
        for dir_name in essential_dirs:
            if not os.path.exists(os.path.join(self.project_path, dir_name)):
                missing_dirs.append(dir_name)
                structure_score -= 15
        
        if missing_dirs:
            structure_issues.append(f"Dossiers manquants: {', '.join(missing_dirs)}")
            self.suggestions.append(f"Créer les dossiers: {', '.join(missing_dirs)}")
        
        # Vérifier les fichiers essentiels
        essential_files = ['README.md', 'requirements.txt', 'main.py']
        missing_files = []
        for file_name in essential_files:
            if not os.path.exists(os.path.join(self.project_path, file_name)):
                missing_files.append(file_name)
                structure_score -= 10
        
        if missing_files:
            structure_issues.append(f"Fichiers manquants: {', '.join(missing_files)}")
            self.suggestions.append(f"Créer les fichiers: {', '.join(missing_files)}")
        
        # Vérifier la cohérence des modules
        modules = self._find_modules()
        if not modules:
            structure_issues.append("Aucun module Python trouvé")
            structure_score -= 20
        else:
            structure_issues.append(f"Modules trouvés: {', '.join(modules)}")
        
        self.issues.extend(structure_issues)
        self.metrics['structure_score'] = max(0, structure_score)
    
    def _analyze_code_quality(self):
        """Analyse la qualité du code Python."""
        code_issues = []
        code_score = 100
        total_lines = 0
        total_functions = 0
        total_classes = 0
        
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Analyse AST
                        tree = ast.parse(content)
                        file_metrics = self._analyze_python_file(tree, content)
                        
                        total_lines += file_metrics['lines']
                        total_functions += file_metrics['functions']
                        total_classes += file_metrics['classes']
                        
                        # Détecter les problèmes
                        if file_metrics['lines'] < 10:
                            code_issues.append(f"{file}: Code trop court ({file_metrics['lines']} lignes)")
                            code_score -= 5
                        
                        if file_metrics['functions'] == 0:
                            code_issues.append(f"{file}: Aucune fonction définie")
                            code_score -= 10
                        
                        if 'TODO' in content or 'FIXME' in content:
                            code_issues.append(f"{file}: Contient TODO/FIXME")
                            code_score -= 5
                        
                        if 'print(' in content and 'logging' not in content:
                            code_issues.append(f"{file}: Utilise print() au lieu de logging")
                            code_score -= 5
                            self.suggestions.append(f"Remplacer print() par logging dans {file}")
                        
                        # Détecter les patterns à risque
                        if 'os.system(' in content or 'subprocess.run(' in content:
                            code_issues.append(f"{file}: Appel shell potentiellement risqué")
                            code_score -= 10
                        
                        if 'password' in content.lower() and 'input(' in content:
                            code_issues.append(f"{file}: Saisie de mot de passe en clair")
                            code_score -= 15
                        
                    except Exception as e:
                        code_issues.append(f"{file}: Erreur d'analyse - {e}")
                        code_score -= 20
        
        self.metrics['total_lines'] = total_lines
        self.metrics['total_functions'] = total_functions
        self.metrics['total_classes'] = total_classes
        self.metrics['code_score'] = max(0, code_score)
        
        if code_issues:
            self.issues.extend(code_issues)
        
        # Suggestions basées sur l'analyse
        if total_functions < 3:
            self.suggestions.append("Ajouter plus de fonctions pour une meilleure modularité")
        
        if total_classes < 1:
            self.suggestions.append("Utiliser des classes pour une meilleure organisation")
    
    def _analyze_python_file(self, tree: ast.AST, content: str) -> Dict[str, int]:
        """Analyse un fichier Python avec AST."""
        lines = len(content.split('\n'))
        functions = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
        classes = len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])
        
        return {
            'lines': lines,
            'functions': functions,
            'classes': classes
        }
    
    def _analyze_tests(self):
        """Analyse la couverture de tests."""
        test_issues = []
        test_score = 100
        
        test_files = []
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.startswith('test_') or file.endswith('_test.py'):
                    test_files.append(file)
        
        if not test_files:
            test_issues.append("Aucun fichier de test trouvé")
            test_score -= 50
            self.suggestions.append("Créer des tests unitaires")
        else:
            test_issues.append(f"Fichiers de test: {', '.join(test_files)}")
        
        # Vérifier la présence de pytest
        requirements_file = os.path.join(self.project_path, 'requirements.txt')
        if os.path.exists(requirements_file):
            with open(requirements_file, 'r') as f:
                content = f.read()
                if 'pytest' not in content:
                    test_issues.append("pytest manquant dans requirements.txt")
                    test_score -= 20
                    self.suggestions.append("Ajouter pytest aux dépendances")
        
        self.metrics['test_score'] = max(0, test_score)
        if test_issues:
            self.issues.extend(test_issues)
    
    def _analyze_documentation(self):
        """Analyse la documentation."""
        doc_issues = []
        doc_score = 100
        
        doc_files = ['README.md', 'DOC.md', 'ONBOARDING.md']
        missing_docs = []
        
        for doc_file in doc_files:
            doc_path = os.path.join(self.project_path, doc_file)
            if not os.path.exists(doc_path):
                missing_docs.append(doc_file)
                doc_score -= 25
            else:
                # Vérifier la taille du fichier
                with open(doc_path, 'r') as f:
                    content = f.read()
                    if len(content) < 100:
                        doc_issues.append(f"{doc_file}: Documentation trop courte")
                        doc_score -= 10
        
        if missing_docs:
            doc_issues.append(f"Documentation manquante: {', '.join(missing_docs)}")
            self.suggestions.append(f"Créer la documentation: {', '.join(missing_docs)}")
        
        # Vérifier les docstrings dans le code
        python_files = self._find_python_files()
        files_without_docstrings = 0
        
        for py_file in python_files:
            try:
                with open(py_file, 'r') as f:
                    content = f.read()
                if '"""' not in content and "'''" not in content:
                    files_without_docstrings += 1
            except:
                pass
        
        if files_without_docstrings > 0:
            doc_issues.append(f"{files_without_docstrings} fichiers sans docstrings")
            doc_score -= files_without_docstrings * 5
            self.suggestions.append("Ajouter des docstrings aux fonctions et classes")
        
        self.metrics['doc_score'] = max(0, doc_score)
        if doc_issues:
            self.issues.extend(doc_issues)
    
    def _analyze_security(self):
        """Analyse la sécurité."""
        security_issues = []
        security_score = 100
        
        # Patterns de sécurité à détecter
        security_patterns = [
            (r'sk-[a-zA-Z0-9]{16,}', 'Clé API potentielle exposée'),
            (r'password\s*=\s*["\'][^"\']+["\']', 'Mot de passe en dur'),
            (r'secret\s*=\s*["\'][^"\']+["\']', 'Secret en dur'),
            (r'api_key\s*=\s*["\'][^"\']+["\']', 'Clé API en dur'),
            (r'eval\(', 'Utilisation de eval() dangereuse'),
            (r'exec\(', 'Utilisation de exec() dangereuse'),
            (r'__import__\(', 'Import dynamique potentiellement risqué'),
        ]
        
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        for pattern, description in security_patterns:
                            if re.search(pattern, content):
                                security_issues.append(f"{file}: {description}")
                                security_score -= 15
                                self.suggestions.append(f"Supprimer {description} de {file}")
                    
                    except Exception as e:
                        security_issues.append(f"{file}: Erreur d'analyse sécurité - {e}")
        
        self.metrics['security_score'] = max(0, security_score)
        if security_issues:
            self.issues.extend(security_issues)
    
    def _analyze_performance(self):
        """Analyse la performance."""
        perf_issues = []
        perf_score = 100
        
        # Détecter les patterns de performance
        perf_patterns = [
            (r'for.*in.*range\(.*\):', 'Boucle range() - considérer enumerate()'),
            (r'\.append\(.*\)', 'Utilisation de append() - considérer list comprehension'),
            (r'import \*', 'Import wildcard - importer spécifiquement'),
        ]
        
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        for pattern, description in perf_patterns:
                            if re.search(pattern, content):
                                perf_issues.append(f"{file}: {description}")
                                perf_score -= 5
                    
                    except Exception as e:
                        perf_issues.append(f"{file}: Erreur d'analyse performance - {e}")
        
        self.metrics['perf_score'] = max(0, perf_score)
        if perf_issues:
            self.issues.extend(perf_issues)
    
    def _calculate_score(self):
        """Calcule le score global du projet."""
        scores = [
            self.metrics.get('structure_score', 0),
            self.metrics.get('code_score', 0),
            self.metrics.get('test_score', 0),
            self.metrics.get('doc_score', 0),
            self.metrics.get('security_score', 0),
            self.metrics.get('perf_score', 0),
        ]
        
        self.score = sum(scores) / len(scores)
        self.metrics['global_score'] = self.score
    
    def _generate_report(self) -> Dict[str, Any]:
        """Génère le rapport d'audit complet."""
        return {
            'project_path': self.project_path,
            'audit_date': datetime.now().isoformat(),
            'global_score': self.score,
            'metrics': self.metrics,
            'issues': self.issues,
            'suggestions': self.suggestions,
            'summary': self._generate_summary()
        }
    
    def _generate_summary(self) -> str:
        """Génère un résumé de l'audit."""
        if self.score >= 80:
            grade = "🟢 EXCELLENT"
        elif self.score >= 60:
            grade = "🟡 BON"
        elif self.score >= 40:
            grade = "🟠 MOYEN"
        else:
            grade = "🔴 CRITIQUE"
        
        return f"""
=== AUDIT PROJET {os.path.basename(self.project_path)} ===
Score global: {self.score:.1f}/100 {grade}

📊 Métriques:
- Structure: {self.metrics.get('structure_score', 0)}/100
- Code: {self.metrics.get('code_score', 0)}/100
- Tests: {self.metrics.get('test_score', 0)}/100
- Documentation: {self.metrics.get('doc_score', 0)}/100
- Sécurité: {self.metrics.get('security_score', 0)}/100
- Performance: {self.metrics.get('perf_score', 0)}/100

📈 Statistiques:
- Lignes de code: {self.metrics.get('total_lines', 0)}
- Fonctions: {self.metrics.get('total_functions', 0)}
- Classes: {self.metrics.get('total_classes', 0)}

🚨 Problèmes détectés: {len(self.issues)}
💡 Suggestions: {len(self.suggestions)}
"""
    
    def _find_modules(self) -> List[str]:
        """Trouve les modules Python dans le projet."""
        modules = []
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    rel_path = os.path.relpath(os.path.join(root, file), self.project_path)
                    modules.append(rel_path)
        return modules
    
    def _find_python_files(self) -> List[str]:
        """Trouve tous les fichiers Python du projet."""
        python_files = []
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

def calculate_base_score(code: str) -> int:
    """Calcule un score de base pour le code."""
    score = 100
    
    # Pénalités basiques
    if len(code.strip()) == 0:
        return 0
    
    # Vérifier la présence de docstrings
    if '"""' not in code and "'''" not in code:
        score -= 10
    
    # Vérifier la présence de commentaires
    if '#' not in code:
        score -= 5
    
    # Vérifier la longueur des lignes
    lines = code.split('\n')
    long_lines = sum(1 for line in lines if len(line) > 120)
    score -= min(long_lines * 2, 20)
    
    # Vérifier les imports
    if 'import' not in code and 'from' not in code:
        score -= 5
    
    return max(score, 0)

def analyze_code_issues(code: str) -> List[str]:
    """Analyse basique des problèmes de code."""
    issues = []
    
    # Vérifications basiques
    if 'print(' in code and 'logging' not in code:
        issues.append("Utilisation de print() au lieu de logging")
    
    if 'except:' in code:
        issues.append("Exception trop générique - spécifier le type")
    
    if 'pass' in code:
        issues.append("Bloc pass détecté - implémenter la logique")
    
    if len(code.split('\n')) > 200:
        issues.append("Fichier très long - considérer la modularisation")
    
    return issues

def generate_basic_suggestions(code: str) -> List[str]:
    """Génère des suggestions basiques d'amélioration."""
    suggestions = []
    
    if 'logging' not in code:
        suggestions.append("Ajouter des logs pour le debugging")
    
    if 'def ' in code and '"""' not in code:
        suggestions.append("Ajouter des docstrings aux fonctions")
    
    if 'class ' in code and '"""' not in code:
        suggestions.append("Ajouter des docstrings aux classes")
    
    if 'test' not in code.lower():
        suggestions.append("Ajouter des tests unitaires")
    
    return suggestions

def audit_code_quality(file_path: str, project_type: str = "generic") -> Dict[str, Any]:
    """Audit de qualité du code avec IA robuste."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Calculer un score de base
        base_score = calculate_base_score(code)
        
        # Utiliser l'IA robuste pour la revue
        try:
            from .ai_robust import robust_ai
            review = robust_ai.review_code(
                code=code,
                filename=os.path.basename(file_path),
                project_type=project_type,
                current_score=base_score
            )
            
            if 'error' not in review:
                return {
                    'file': file_path,
                    'score': review.get('score', base_score),
                    'issues': review.get('issues', []),
                    'suggestions': review.get('suggestions', []),
                    'improvements': review.get('improvements', []),
                    'ai_review': True
                }
        except ImportError:
            logging.warning("IA robuste non disponible pour la revue de code")
        
        # Fallback vers analyse basique
        return {
            'file': file_path,
            'score': base_score,
            'issues': analyze_code_issues(code),
            'suggestions': generate_basic_suggestions(code),
            'improvements': [],
            'ai_review': False
        }
        
    except Exception as e:
        logging.error(f"Erreur audit code {file_path}: {e}")
        return {
            'file': file_path,
            'score': 0,
            'issues': [f"Erreur d'analyse: {e}"],
            'suggestions': [],
            'improvements': [],
            'ai_review': False
        }

def audit_project_intelligent(project_path: str) -> Dict[str, Any]:
    """Fonction principale d'audit intelligent."""
    auditor = ProjectAuditor(project_path)
    return auditor.audit_project()

def generate_audit_report(project_path: str, output_file: str | None = None) -> str:
    """Génère un rapport d'audit et le sauvegarde."""
    audit_result = audit_project_intelligent(project_path)
    
    if output_file is None:
        output_file = os.path.join(project_path, 'audit_report.json')
    
    # Sauvegarder le rapport JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audit_result, f, indent=2, ensure_ascii=False)
    
    # Générer le rapport texte
    text_report = audit_result['summary']
    text_report += "\n\n🚨 PROBLÈMES DÉTECTÉS:\n"
    for i, issue in enumerate(audit_result['issues'], 1):
        text_report += f"{i}. {issue}\n"
    
    text_report += "\n💡 SUGGESTIONS D'AMÉLIORATION:\n"
    for i, suggestion in enumerate(audit_result['suggestions'], 1):
        text_report += f"{i}. {suggestion}\n"
    
    # Sauvegarder le rapport texte
    text_output_file = output_file.replace('.json', '.txt')
    with open(text_output_file, 'w', encoding='utf-8') as f:
        f.write(text_report)
    
    logging.info(f"Rapport d'audit généré: {output_file}")
    return text_report 