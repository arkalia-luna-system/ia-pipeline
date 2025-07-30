#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit Complet des Dossiers - Athalia/Arkalia
Analyse approfondie de tous les dossiers du projet
"""

import ast
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional


@dataclass
class DossierInfo:
    """Informations sur un dossier"""

    path: Path
    nom: str
    type_dossier: str  # 'core', 'tests', 'docs', 'tools', 'archive', etc.
    fichiers_python: List[Path]
    fichiers_md: List[Path]
    fichiers_yaml: List[Path]
    fichiers_json: List[Path]
    sous_dossiers: List[Path]
    taille_totale: int
    description: str = ""


@dataclass
class ModuleInfo:
    """Informations sur un module Python"""

    path: Path
    nom: str
    taille: int
    fonctions: List[str]
    classes: List[str]
    imports: List[str]
    docstring: str = ""
    tests_associes: List[str] = field(default_factory=list)
    documentation_associee: List[str] = field(default_factory=list)
    integration_orchestrateur: bool = False


@dataclass
class AuditResult:
    """Résultat d'audit pour un dossier"""

    dossier: DossierInfo
    modules: List[ModuleInfo]
    score_utilite: float  # 0-10
    score_implementation: float  # 0-10
    score_tests: float  # 0-10
    score_documentation: float  # 0-10
    score_integration: float  # 0-10
    score_total: float  # 0-10
    recommandations: List[str] = field(default_factory=list)
    pepites_trouvees: List[str] = field(default_factory=list)


class AuditCompletDossiers:
    """Audit complet de tous les dossiers du projet"""

    def __init__(self, root_path: Optional[str] = None):
        self.root_path = Path(root_path) if root_path else Path.cwd()
        self.dossiers_principaux = [
            "athalia_core",
            "tests",
            "docs",
            "tools",
            "scripts",
            "config",
        ]

    def analyser_tous_dossiers(self) -> List[AuditResult]:
        """Analyser tous les dossiers principaux"""
        results = []

        # Analyser les dossiers principaux
        for nom_dossier in self.dossiers_principaux:
            dossier_path = self.root_path / nom_dossier
            if dossier_path.exists():
                print(f"🔍 Analyse de {nom_dossier}...")
                result = self._analyser_dossier_complet(dossier_path, nom_dossier)
                if result:
                    results.append(result)

        # Analyser les sous-dossiers cachés
        sous_dossiers_caches = self._trouver_sous_dossiers_caches()
        for dossier_path in sous_dossiers_caches:
            nom_dossier = dossier_path.name
            if not any(nom_dossier in result.dossier.nom for result in results):
                print(f"🔍 Analyse du sous-dossier caché {nom_dossier}...")
                result = self._analyser_dossier_complet(dossier_path, nom_dossier)
                if result:
                    results.append(result)

        return results

    def _trouver_sous_dossiers_caches(self) -> List[Path]:
        """Trouver les sous-dossiers cachés qui pourraient contenir des pépites"""
        sous_dossiers_caches = []

        # Chercher dans athalia_core
        core_path = self.root_path / "athalia_core"
        if core_path.exists():
            for item in core_path.iterdir():
                if item.is_dir() and not item.name.startswith("."):
                    # Vérifier s'il contient des fichiers Python
                    if list(item.rglob("*.py")):
                        sous_dossiers_caches.append(item)

        # Chercher dans tests
        tests_path = self.root_path / "tests"
        if tests_path.exists():
            for item in tests_path.iterdir():
                if item.is_dir() and not item.name.startswith("."):
                    if list(item.rglob("*.py")):
                        sous_dossiers_caches.append(item)

        # Chercher dans tools
        tools_path = self.root_path / "tools"
        if tools_path.exists():
            for item in tools_path.iterdir():
                if item.is_dir() and not item.name.startswith("."):
                    if list(item.rglob("*.py")):
                        sous_dossiers_caches.append(item)

        return sous_dossiers_caches

    def _analyser_dossier_complet(
        self, dossier_path: Path, nom_dossier: str
    ) -> Optional[AuditResult]:
        """Analyser un dossier complet"""
        try:
            # Informations du dossier
            dossier_info = self._analyser_dossier_info(dossier_path, nom_dossier)

            # Analyser les modules Python
            modules = []
            for py_file in dossier_path.rglob("*.py"):
                if py_file.name != "__init__.py" and not py_file.name.startswith("._"):
                    module_info = self._analyser_module(py_file)
                    if module_info:
                        modules.append(module_info)

            # Calculer les scores
            score_utilite = self._calculer_score_utilite(dossier_info, modules)
            score_implementation = self._calculer_score_implementation(modules)
            score_tests = self._calculer_score_tests(dossier_info, modules)
            score_documentation = self._calculer_score_documentation(
                dossier_info, modules
            )
            score_integration = self._calculer_score_integration(modules)

            score_total = (
                score_utilite
                + score_implementation
                + score_tests
                + score_documentation
                + score_integration
            ) / 5

            # Générer recommandations
            recommandations = self._generer_recommandations(
                dossier_info, modules, score_total
            )

            # Chercher des pépites
            pepites = self._chercher_pepites(dossier_info, modules)

            return AuditResult(
                dossier=dossier_info,
                modules=modules,
                score_utilite=score_utilite,
                score_implementation=score_implementation,
                score_tests=score_tests,
                score_documentation=score_documentation,
                score_integration=score_integration,
                score_total=score_total,
                recommandations=recommandations,
                pepites_trouvees=pepites,
            )

        except Exception as e:
            print(f"⚠️ Erreur lors de l'analyse de {dossier_path}: {e}")
            return None

    def _analyser_dossier_info(
        self, dossier_path: Path, nom_dossier: str
    ) -> DossierInfo:
        """Analyser les informations d'un dossier"""
        fichiers_python = list(dossier_path.rglob("*.py"))
        fichiers_md = list(dossier_path.rglob("*.md"))
        fichiers_yaml = list(dossier_path.rglob("*.yaml")) + list(
            dossier_path.rglob("*.yml")
        )
        fichiers_json = list(dossier_path.rglob("*.json"))
        sous_dossiers = [item for item in dossier_path.iterdir() if item.is_dir()]

        # Calculer la taille totale
        taille_totale = sum(f.stat().st_size for f in fichiers_python if f.exists())

        # Déterminer le type de dossier
        if "core" in nom_dossier.lower():
            type_dossier = "core"
        elif "test" in nom_dossier.lower():
            type_dossier = "tests"
        elif "doc" in nom_dossier.lower():
            type_dossier = "docs"
        elif "tool" in nom_dossier.lower():
            type_dossier = "tools"
        elif "script" in nom_dossier.lower():
            type_dossier = "scripts"
        elif "config" in nom_dossier.lower():
            type_dossier = "config"
        else:
            type_dossier = "autre"

        # Générer une description
        description = (
            f"Dossier {type_dossier} avec {len(fichiers_python)} fichiers Python"
        )

        return DossierInfo(
            path=dossier_path,
            nom=nom_dossier,
            type_dossier=type_dossier,
            fichiers_python=fichiers_python,
            fichiers_md=fichiers_md,
            fichiers_yaml=fichiers_yaml,
            fichiers_json=fichiers_json,
            sous_dossiers=sous_dossiers,
            taille_totale=taille_totale,
            description=description,
        )

    def _analyser_module(self, file_path: Path) -> Optional[ModuleInfo]:
        """Analyser un module Python"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Parse le code Python
            tree = ast.parse(content)
            taille = len(content)

            # Extraire les fonctions et classes
            fonctions = []
            classes = []
            imports = []

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    fonctions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    classes.append(node.name)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")

            # Chercher la docstring
            docstring = ast.get_docstring(tree) or ""

            # Chercher les tests et documentation associés
            tests_associes = self._chercher_tests_associes(file_path)
            documentation_associee = self._chercher_documentation_associee(file_path)

            # Vérifier l'intégration avec l'orchestrateur
            integration_orchestrateur = self._verifier_integration_orchestrateur(
                content, imports
            )

            return ModuleInfo(
                path=file_path,
                nom=file_path.name,
                taille=taille,
                fonctions=fonctions,
                classes=classes,
                imports=imports,
                docstring=docstring,
                tests_associes=tests_associes,
                documentation_associee=documentation_associee,
                integration_orchestrateur=integration_orchestrateur,
            )

        except Exception as e:
            print(f"⚠️ Erreur lors de l'analyse de {file_path}: {e}")
            return None

    def _chercher_tests_associes(self, file_path: Path) -> List[str]:
        """Chercher les tests associés à un module"""
        tests = []
        nom_module = file_path.stem

        # Chercher dans le dossier tests
        tests_path = self.root_path / "tests"
        if tests_path.exists():
            for test_file in tests_path.rglob(f"test_{nom_module}.py"):
                tests.append(str(test_file))
            for test_file in tests_path.rglob(f"*{nom_module}*.py"):
                if "test" in test_file.name.lower():
                    tests.append(str(test_file))

        return tests

    def _chercher_documentation_associee(self, file_path: Path) -> List[str]:
        """Chercher la documentation associée à un module"""
        docs = []
        nom_module = file_path.stem

        # Chercher dans le dossier docs
        docs_path = self.root_path / "docs"
        if docs_path.exists():
            for doc_file in docs_path.rglob(f"*{nom_module}*.md"):
                docs.append(str(doc_file))

        return docs

    def _verifier_integration_orchestrateur(
        self, content: str, imports: List[str]
    ) -> bool:
        """Vérifier si le module s'intègre avec l'orchestrateur principal"""
        # Vérifier les imports d'Athalia
        athalia_imports = [imp for imp in imports if "athalia" in imp.lower()]
        return len(athalia_imports) > 0

    def _calculer_score_utilite(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> float:
        """Calculer le score d'utilité du dossier"""
        if not modules:
            return 0.0

        # Critères d'utilité
        nb_fonctions = sum(len(m.fonctions) for m in modules)
        nb_classes = sum(len(m.classes) for m in modules)
        nb_imports_athalia = sum(
            len([imp for imp in m.imports if "athalia" in imp.lower()]) for m in modules
        )

        # Score basé sur la complexité et l'intégration
        score = min(
            10.0,
            (nb_fonctions * 0.5 + nb_classes * 1.0 + nb_imports_athalia * 0.3)
            / len(modules),
        )

        return round(score, 2)

    def _calculer_score_implementation(self, modules: List[ModuleInfo]) -> float:
        """Calculer le score d'implémentation"""
        if not modules:
            return 0.0

        scores = []
        for module in modules:
            # Score basé sur la taille et la complexité
            if module.taille > 0:
                score = min(
                    10.0,
                    (len(module.fonctions) + len(module.classes) * 2)
                    / (module.taille / 1000),
                )
                scores.append(score)

        return round(sum(scores) / len(scores), 2) if scores else 0.0

    def _calculer_score_tests(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> float:
        """Calculer le score de tests"""
        if not modules:
            return 0.0

        modules_avec_tests = sum(1 for m in modules if m.tests_associes)
        score = (modules_avec_tests / len(modules)) * 10.0

        return round(score, 2)

    def _calculer_score_documentation(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> float:
        """Calculer le score de documentation"""
        if not modules:
            return 0.0

        # Score basé sur la documentation des modules
        modules_documentes = sum(1 for m in modules if m.docstring)
        score_modules = (modules_documentes / len(modules)) * 5.0

        # Score basé sur les fichiers de documentation
        score_docs = min(5.0, len(dossier_info.fichiers_md) * 0.5)

        return round(score_modules + score_docs, 2)

    def _calculer_score_integration(self, modules: List[ModuleInfo]) -> float:
        """Calculer le score d'intégration"""
        if not modules:
            return 0.0

        modules_integres = sum(1 for m in modules if m.integration_orchestrateur)
        score = (modules_integres / len(modules)) * 10.0

        return round(score, 2)

    def _generer_recommandations(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo], score_total: float
    ) -> List[str]:
        """Générer des recommandations d'amélioration"""
        recommandations = []

        if score_total < 5.0:
            recommandations.append("🔴 Amélioration majeure nécessaire")
        elif score_total < 7.0:
            recommandations.append("🟡 Amélioration recommandée")
        else:
            recommandations.append("🟢 Dossier en bon état")

        # Recommandations spécifiques
        if len(modules) > 0:
            modules_sans_tests = [m for m in modules if not m.tests_associes]
            if modules_sans_tests:
                recommandations.append(
                    f"📝 Ajouter des tests pour {len(modules_sans_tests)} modules"
                )

            modules_sans_docs = [m for m in modules if not m.docstring]
            if modules_sans_docs:
                recommandations.append(
                    f"📚 Ajouter de la documentation pour {len(modules_sans_docs)} modules"
                )

        return recommandations

    def _chercher_pepites(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> List[str]:
        """Chercher des pépites (fonctionnalités intéressantes)"""
        pepites = []

        for module in modules:
            # Chercher des patterns intéressants
            if len(module.fonctions) > 10:
                pepites.append(
                    f"🚀 Module {module.nom}: {len(module.fonctions)} fonctions (très actif)"
                )

            if len(module.classes) > 5:
                pepites.append(
                    f"🏗️ Module {module.nom}: {len(module.classes)} classes (architecture complexe)"
                )

            if module.integration_orchestrateur:
                pepites.append(f"🔗 Module {module.nom}: Intégré avec l'orchestrateur")

        return pepites

    def generer_rapport(self) -> str:
        """Générer un rapport complet d'audit"""
        results = self.analyser_tous_dossiers()

        rapport = f"""# 📊 Rapport d'Audit Complet des Dossiers - Athalia/Arkalia

**Date:** {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
**Dossiers analysés:** {len(results)}

## 📈 Résultats par Dossier

"""

        for result in results:
            dossier = result.dossier
            rapport += f"""### 📁 {dossier.nom} ({dossier.type_dossier})

**Score total:** {result.score_total:.1f}/10
**Modules:** {len(result.modules)}
**Taille:** {dossier.taille_totale / 1024:.1f} KB

**Scores détaillés:**
- 🎯 Utilité: {result.score_utilite:.1f}/10
- ⚙️ Implémentation: {result.score_implementation:.1f}/10
- 🧪 Tests: {result.score_tests:.1f}/10
- 📚 Documentation: {result.score_documentation:.1f}/10
- 🔗 Intégration: {result.score_integration:.1f}/10

**Recommandations:**
"""
            for rec in result.recommandations:
                rapport += f"- {rec}\n"

            if result.pepites_trouvees:
                rapport += "\n**💎 Pépites trouvées:**\n"
                for pepite in result.pepites_trouvees:
                    rapport += f"- {pepite}\n"

            rapport += "\n"

        # Statistiques globales
        if results:
            scores_totaux = [r.score_total for r in results]
            score_moyen = sum(scores_totaux) / len(scores_totaux)
            rapport += f"""## 📊 Statistiques Globales

**Score moyen:** {score_moyen:.1f}/10
**Meilleur dossier:** {max(results, key=lambda r: r.score_total).dossier.nom} ({max(scores_totaux):.1f}/10)
**Dossier à améliorer:** {min(results, key=lambda r: r.score_total).dossier.nom} ({min(scores_totaux):.1f}/10)

## 🎯 Recommandations Globales

"""

            if score_moyen < 5.0:
                rapport += "🔴 **Action critique nécessaire** - Le projet nécessite une refonte majeure"
            elif score_moyen < 7.0:
                rapport += (
                    "🟡 **Amélioration recommandée** - Quelques ajustements nécessaires"
                )
            else:
                rapport += "🟢 **Excellent état** - Le projet est bien structuré"

        return rapport


def main():
    """Fonction principale"""
    auditor = AuditCompletDossiers()
    rapport = auditor.generer_rapport()

    # Sauvegarder le rapport
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    rapport_file = f"rapport_audit_complet_{timestamp}.md"

    with open(rapport_file, "w", encoding="utf-8") as f:
        f.write(rapport)

    print(f"📄 Rapport sauvegardé: {rapport_file}")
    print("\n" + "=" * 60)
    print(rapport)


if __name__ == "__main__":
    main()
