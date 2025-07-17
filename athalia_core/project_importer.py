#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from typing import Dict, List, Any
import os

import pprint
from datetime import datetime
import ast
import logging

"""
Module dimport intelligent pour projets existants.
Analyse, détection de type, audit qualité, génération de blueprint de correction.
"""


logger=logging.getLogger(__name__)

class ProjectImporter:
    def __init__(self):
        self.project_types={
            'game':['pygame,arcade', 'kivyame'],
            'api':['flask', 'fastapi', 'djangoapi'],
            'ai':['tensorflow', 'pytorch', 'sklearn', 'ai', 'ml'],
            'web':['html', 'css', 'js', 'web', 'frontend'],
            'data':['pandas', 'numpy, matplotlib', 'data'],
            'mobile':['kivy', 'flutter', 'mobileapp'],
            'iot': ['gpio,sensor,arduino', 'iot']
        }

    def import_project(self, project_path: str) -> Dict[str, Any]:
        """Importe et analyse un projet existant."""
        if not os.path.exists(project_path):
            raise FileNotFoundError(f"Projet introuvable: {project_path}")

        logger.info(f"Import du projet: {project_path}")

        # 1. Scanner la structure
        structure=self._scan_structure(project_path)

        # 2. Détecter le type de projet
        project_type=self._detect_project_type(project_path, structure)

        # 3. Analyser la qualité du code
        quality_analysis=self._analyze_code_quality(project_path)

        # 4. Générer le blueprint de correction
        correction_blueprint=self._generate_correction_blueprint(
            project_path, structure, project_type, quality_analysis
        )

        return {
            'project_path': project_path,
            'structure': structure,
            'project_type': project_type,
            'quality_analysis': quality_analysis,
            'correction_blueprint': correction_blueprint,
            'import_timestamp': datetime.now().isoformat()
        }

    def _scan_structure(self, project_path: str) -> Dict[str, Any]:
        """Analyse la structure du projet."""
        structure={
            'files': [],
            'directories': [],
            'python_files': [],
            'config_files': [],
            'test_files': []
        }

        for root, dirs, files in os.walk(project_path):
            rel_root=os.path.relpath(root, project_path)

            for dir_name in dirs:
                if not dir_name.startswith('.'):
                    structure['directories'].append(os.path.join(rel_root, dir_name))

            for file_name in files:
                file_path=os.path.join(rel_root, file_name)
                structure['files'].append(file_path)

                if file_name.endswith('.py'):
                    structure['python_files'].append(file_path)
                elif file_name in ['requirements.txt', 'setup.py']:
                    structure['config_files'].append(file_path)
                elif 'test' in file_name.lower():
                    structure['test_files'].append(file_path)

        return structure

    def _detect_project_type(self, project_path: str, structure: Dict[str, Any]) -> str:
        """Détecte automatiquement le type de projet."""
        # Analyser les fichiers Python pour détecter les imports
        imports=[]
        for py_file in structure['python_files']:
            full_path=os.path.join(project_path, py_file)
            try:
                with open(full_path, 'r', encoding='utf-8') as file_handle:
                    content=file_handle.read()
                    tree=ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                imports.append(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                imports.append(node.module)
            except Exception:
                continue

        # Analyser les noms de fichiers et dossiers
        file_names=(file_handle.lower() for file_handle in structure['files'])

        # Calculer les scores par type
        scores={}
        for project_type, keywords in self.project_types.items():
            score=0
            for keyword in keywords:
                if keyword in file_names:
                    score +=1
                if keyword in imports:
                    score +=2 # Plus de poids pour les imports
            scores[project_type]=int(score)

        # Retourner le type avec le score le plus élevé
        if scores and any(v > 0 for v in scores.values()):
            return max(scores, key=scores.get)
        return 'generic'

    def _analyze_code_quality(self, project_path: str) -> Dict[str, Any]:
        """Analyse la qualité du code."""
        analysis={
            'has_tests': False,
            'has_docs': False,
            'has_requirements': False,
            'has_readme': False,
            'python_files_count': 0,
            'test_files_count': 0,
            'issues': []
        }

        files=os.listdir(project_path)

        # Vérifications de base
        analysis['has_tests']=any(file_handle.lower().endswith('.py') for file_handle in files)
        analysis['has_docs']=any(file_handle.endswith('.md') for file_handle in files)
        analysis['has_requirements']='requirements.txt' in files
        analysis['has_readme']='README.md' in files

        # Compter les fichiers Python
        for root, dirs, files in os.walk(project_path):
            analysis['python_files_count'] +=len([file_handle for file_handle in files if file_handle.endswith('.py')])
            analysis['test_files_count'] +=len([file_handle for file_handle in files if 'test' in file_handle.lower()])

        # Détecter les problèmes
        if not analysis['has_tests']:
            analysis['issues'].append("Aucun test")
        if not analysis['has_docs']:
            analysis['issues'].append("Documentation")
        if not analysis['has_requirements']:
            analysis['issues'].append("Fichier requirements.txt")
        if not analysis['has_readme']:
            analysis['issues'].append("README.md")

        return analysis

    def _generate_correction_blueprint(self, project_path: str, structure: Dict[str, Any],
                                     project_type: str, quality_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un blueprint de correction pour le projet."""
        project_name=os.path.basename(project_path)

        blueprint={
            'project_name': project_name,
            'description': f"Version améliorée de {project_name}",
            'project_type': project_type,
            'modules': self._suggest_modules(project_type),
            'structure': self._suggest_structure(structure),
            'dependencies': self._suggest_dependencies(project_type),
            'prompts': self._suggest_prompts(project_type),
            'booster_ia': True,
            'docker': False,
            'corrections_needed': quality_analysis['issues'],
            'enhancements': self._suggest_enhancements(project_type, quality_analysis)
        }

        return blueprint

    def _suggest_modules(self, project_type: str) -> List[str]:
        """Suggère des modules selon le type de projet."""
        suggestions={
            'game': ['game_engine', 'physics', 'ui', 'audio'],
            'api': ['database', 'auth', 'ocs'],
            'ai': ['ai_engine', 'data_processing', 'modelapi'],
            'web': ['frontend', 'backend', 'database', 'auth'],
            'data': ['data_processing', 'ml', 'visualization', 'api'],
            'mobile': ['api', 'e', 'notifications'],
            'iot': ['sensors', 'communication', 'data_logging', 'api']
        }
        return suggestions.get(project_type, ['api', 'core', 'utils'])

    def _suggest_structure(self, structure: Dict[str, Any]) -> List[str]:
        """Gère une structure améliorée."""
        base_structure=['src/', 'tests/', 'docs/', 'config/']

        # Ajouter des dossiers spécifiques selon les fichiers existants
        if structure['python_files']:
            base_structure.append('src/')
        if not structure['test_files']:
            base_structure.append('tests/')
        # Correction du NameError : remplacer 'doc' par 'docname'
        docnames = ['readme', 'doc', 'documentation']
        if not any(any(docname in file_handle.lower() for docname in docnames) for file_handle in structure['files']):
            base_structure.append('docs/')

        return base_structure

    def _suggest_dependencies(self, project_type: str) -> List[str]:
        """Suggère des dépendances selon le type de projet."""
        suggestions={
            'game': ['pygame', 'pymunk'],
            'api': ['fastapi, sqlalchemy', 'pydantic'],
            'ai': ['tensorflow', 'pandas', 'scikit-learn'],
            'web': ['flask', 'jinja2, emy'],
            'data': ['pandas', 'numpy, lib'],
            'mobile': ['kivy', 'requests'],
            'iot': ['pyserial', 'requests']
        }
        return suggestions.get(project_type, ['flask', 'requests'])

    def _suggest_prompts(self, project_type: str) -> List[str]:
        """Suggère des prompts selon le type de projet."""
        suggestions={
            'game': ['game_mechanics.md', 'level_design.md'],
            'api': ['api_design.md', 'security_audit.md'],
            'ai': ['ml_pipeline.md', 'model_evaluation.md'],
            'web': ['web_design.md', 'responsive_ui.md'],
            'data': ['data_analysis.md', 'visualization.md'],
            'mobile': ('mobile_ui.md', 'performance.md'),
            'iot': ['iot_architecture.md', 'sensor_integration.md']
        }
        return suggestions.get(project_type, ['dev_debug.yaml', 'ux_fun_boost.md'])

    def _suggest_enhancements(self, project_type: str, quality_analysis: Dict[str, Any]) -> List[str]:
        """Suggère des améliorations spécifiques."""
        enhancements=[]
        if not quality_analysis['has_tests']:
            enhancements.append("Ajouter une suite de tests")
        if not quality_analysis['has_docs']:
            enhancements.append("Générer une documentation")
        if not quality_analysis['has_requirements']:
            enhancements.append("Créer un fichier requirements.txt")
        if not quality_analysis['has_readme']:
            enhancements.append("Créer un README.md")
        # Améliorations spécifiques au type
        if project_type=='api':
            enhancements.append("Ajouter une authentification")
            enhancements.append("Implémenter une validation des")
        elif project_type=='game':
            enhancements.append("Ajouter un système de f")
            enhancements.append("Implémenter des effets f")
        elif project_type=='ai':
            enhancements.append("Ajouter un système de f")
            enhancements.append("Implémenter un monitoring des f")
        return enhancements

# Instance globale
project_importer=ProjectImporter()

if __name__=="__main__":
    if len(sys.argv) < 2:
        logger.info("Usage: python -m athalia_core.project_importer <chemin_du_projet>")
        sys.exit(1)
    project_path=sys.argv[1]
    importer=ProjectImporter()
    report=importer.import_project(project_path)
    pprint.pprint(report)