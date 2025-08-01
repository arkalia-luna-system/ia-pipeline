#!/usr/bin/env python3
"""
🔍 AUDIT COMPLET DOSSIERS ET SOUS-DOSSIERS
==========================================
Script pour analyser chaque dossier et sous-dossier du projet Athalia.
Vérifie: utilité, implémentation, tests, documentation, intégration.
"""

import ast
from dataclasses import dataclass, field
from pathlib import Path
import sys
from typing import List, Optional

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


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
    """Auditeur complet des dossiers et sous-dossiers"""

    def __init__(self, root_path: Optional[str] = None):
        self.root_path = Path(root_path or Path.cwd())
        self.dossiers: List[Path] = []
        self.results: List[AuditResult] = []

    def analyser_tous_dossiers(self) -> List[AuditResult]:
        """Analyser tous les dossiers et sous-dossiers"""
        print("🔍 ANALYSE COMPLÈTE DE TOUS LES DOSSIERS")
        print("=" * 50)

        # Dossiers principaux à analyser
        dossiers_principaux = [
            "athalia_core",
            "tests",
            "docs",
            "tools",
            "demos",
            "scripts",
            "setup",
            "config",
            "dashboard",
            "data",
            "archive",
            "projects",
            "mon-projet",
            "prompts",
            "templates",
            "bin",
        ]

        results = []

        for dossier_nom in dossiers_principaux:
            dossier_path = self.root_path / dossier_nom
            if dossier_path.exists():
                print(f"\n📁 ANALYSE DU DOSSIER: {dossier_nom}")
                result = self._analyser_dossier_complet(dossier_path, dossier_nom)
                if result:
                    results.append(result)

        # Analyser les sous-dossiers cachés
        print("\n🔍 ANALYSE DES SOUS-DOSSIERS CACHÉS")
        sous_dossiers_caches = self._trouver_sous_dossiers_caches()
        for sous_dossier in sous_dossiers_caches:
            print(f"\n📁 ANALYSE DU SOUS-DOSSIER CACHÉ: {sous_dossier}")
            result = self._analyser_dossier_complet(sous_dossier, sous_dossier.name)
            if result:
                results.append(result)

        self.results = results
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
        elif "demo" in nom_dossier.lower():
            type_dossier = "demos"
        elif "script" in nom_dossier.lower():
            type_dossier = "scripts"
        elif "config" in nom_dossier.lower():
            type_dossier = "config"
        elif "archive" in nom_dossier.lower():
            type_dossier = "archive"
        else:
            type_dossier = "other"

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
        )

    def _analyser_module(self, file_path: Path) -> Optional[ModuleInfo]:
        """Analyser un module Python"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Parser le code
            tree = ast.parse(content)

            # Extraire les fonctions
            fonctions = []
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    fonctions.append(node.name)

            # Extraire les classes
            classes = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)

            # Extraire les imports
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")

            # Extraire le docstring
            docstring = ""
            for node in ast.walk(tree):
                if isinstance(node, ast.Module) and node.body:
                    first_node = node.body[0]
                    if isinstance(first_node, ast.Expr) and isinstance(
                        first_node.value, ast.Str
                    ):
                        docstring = first_node.value.s.split("\n")[0]
                        break

            # Chercher les tests associés
            tests_associes = self._chercher_tests_associes(file_path)

            # Chercher la documentation associée
            documentation_associee = self._chercher_documentation_associee(file_path)

            # Vérifier l'intégration avec l'orchestrateur
            integration_orchestrateur = self._verifier_integration_orchestrateur(
                content, imports
            )

            return ModuleInfo(
                path=file_path,
                nom=file_path.stem,
                taille=len(content.split("\n")),
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
            for test_file in tests_path.rglob(f"test_{nom_module}*.py"):
                tests.append(str(test_file.relative_to(self.root_path)))
            for test_file in tests_path.rglob(f"*{nom_module}*test*.py"):
                tests.append(str(test_file.relative_to(self.root_path)))

        return tests

    def _chercher_documentation_associee(self, file_path: Path) -> List[str]:
        """Chercher la documentation associée à un module"""
        docs = []
        nom_module = file_path.stem

        # Chercher dans le dossier docs
        docs_path = self.root_path / "docs"
        if docs_path.exists():
            for doc_file in docs_path.rglob(f"*{nom_module}*.md"):
                docs.append(str(doc_file.relative_to(self.root_path)))

        return docs

    def _verifier_integration_orchestrateur(
        self, content: str, imports: List[str]
    ) -> bool:
        """Vérifier si le module est intégré dans l'orchestrateur"""
        # Vérifier les imports de l'orchestrateur
        if "unified_orchestrator" in imports or "intelligent_analyzer" in imports:
            return True

        # Vérifier dans le contenu
        if (
            "orchestrator" in content.lower()
            or "intelligent_analyzer" in content.lower()
        ):
            return True

        return False

    def _calculer_score_utilite(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> float:
        """Calculer le score d'utilité"""
        score = 0.0

        # Points pour les fichiers Python
        if dossier_info.fichiers_python:
            score += min(len(dossier_info.fichiers_python) * 0.5, 5.0)

        # Points pour la taille
        if dossier_info.taille_totale > 0:
            score += min(dossier_info.taille_totale / 1000, 2.0)

        # Points pour les types de fichiers
        if dossier_info.fichiers_md:
            score += 1.0
        if dossier_info.fichiers_yaml:
            score += 1.0
        if dossier_info.fichiers_json:
            score += 1.0

        return min(score, 10.0)

    def _calculer_score_implementation(self, modules: List[ModuleInfo]) -> float:
        """Calculer le score d'implémentation"""
        if not modules:
            return 0.0

        score = 0.0

        for module in modules:
            # Points pour les fonctions
            score += min(len(module.fonctions) * 0.2, 2.0)

            # Points pour les classes
            score += min(len(module.classes) * 0.3, 2.0)

            # Points pour la taille
            score += min(module.taille / 100, 2.0)

            # Points pour le docstring
            if module.docstring:
                score += 1.0

        return min(score / len(modules), 10.0)

    def _calculer_score_tests(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> float:
        """Calculer le score des tests"""
        score = 0.0

        # Compter les tests associés
        total_tests = sum(len(module.tests_associes) for module in modules)
        if total_tests > 0:
            score += min(total_tests * 2.0, 5.0)

        # Points pour les fichiers de test dans le dossier
        test_files = [
            f for f in dossier_info.fichiers_python if "test" in f.name.lower()
        ]
        score += min(len(test_files) * 1.0, 5.0)

        return min(score, 10.0)

    def _calculer_score_documentation(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> float:
        """Calculer le score de documentation"""
        score = 0.0

        # Points pour les fichiers markdown
        score += min(len(dossier_info.fichiers_md) * 1.0, 5.0)

        # Points pour la documentation associée
        total_docs = sum(len(module.documentation_associee) for module in modules)
        score += min(total_docs * 1.0, 3.0)

        # Points pour les docstrings
        modules_avec_docstring = sum(1 for module in modules if module.docstring)
        if modules:
            score += (modules_avec_docstring / len(modules)) * 2.0

        return min(score, 10.0)

    def _calculer_score_integration(self, modules: List[ModuleInfo]) -> float:
        """Calculer le score d'intégration"""
        if not modules:
            return 0.0

        modules_integres = sum(
            1 for module in modules if module.integration_orchestrateur
        )
        return (modules_integres / len(modules)) * 10.0

    def _generer_recommandations(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo], score_total: float
    ) -> List[str]:
        """Générer des recommandations"""
        recommandations = []

        if score_total < 5.0:
            recommandations.append("⚠️ Score faible - Nécessite une amélioration")

        if not modules:
            recommandations.append("📝 Aucun module Python trouvé - Vérifier l'utilité")

        if not dossier_info.fichiers_md:
            recommandations.append(
                "📚 Aucune documentation trouvée - Ajouter des fichiers .md"
            )

        total_tests = sum(len(module.tests_associes) for module in modules)
        if total_tests == 0 and modules:
            recommandations.append("🧪 Aucun test associé - Créer des tests")

        modules_sans_docstring = [m for m in modules if not m.docstring]
        if modules_sans_docstring:
            recommandations.append(
                f"📖 {len(modules_sans_docstring)} modules sans docstring - "
                "Ajouter de la documentation"
            )

        modules_non_integres = [m for m in modules if not m.integration_orchestrateur]
        if modules_non_integres:
            recommandations.append(
                f"🔗 {len(modules_non_integres)} modules non intégrés - "
                "Considérer l'intégration"
            )

        return recommandations

    def _chercher_pepites(
        self, dossier_info: DossierInfo, modules: List[ModuleInfo]
    ) -> List[str]:
        """Chercher des pépites dans le dossier"""
        pepites = []

        # Chercher des modules avec beaucoup de fonctionnalités
        for module in modules:
            if len(module.fonctions) > 10 or len(module.classes) > 5:
                pepites.append(
                    f"💎 Module riche: {module.nom} ({len(module.fonctions)} fonctions,"
                    f" {len(module.classes)} classes)"
                )

        # Chercher des modules avec des noms intéressants
        for module in modules:
            nom_lower = module.nom.lower()
            if any(
                mot in nom_lower
                for mot in [
                    "intelligent",
                    "advanced",
                    "smart",
                    "ai",
                    "ml",
                    "neural",
                    "deep",
                ]
            ):
                pepites.append(f"🧠 Module IA: {module.nom}")

        # Chercher des modules avec beaucoup d'imports
        for module in modules:
            if len(module.imports) > 10:
                pepites.append(
                    f"🔗 Module complexe: {module.nom} ({len(module.imports)} imports)"
                )

        # Chercher des fichiers de configuration
        if dossier_info.fichiers_yaml:
            pepites.append(
                f"⚙️ Configuration: {len(dossier_info.fichiers_yaml)} fichiers YAML"
            )

        return pepites

    def generer_rapport(self) -> str:
        """Générer un rapport complet"""
        rapport = []
        rapport.append("# 🔍 AUDIT COMPLET DOSSIERS ET SOUS-DOSSIERS")
        rapport.append("=" * 60)
        rapport.append(f"**Date**: {Path.cwd().name}")
        rapport.append(f"**Total dossiers analysés**: {len(self.results)}")
        rapport.append("")

        # Résumé global
        scores_totaux = [r.score_total for r in self.results]
        if scores_totaux:
            rapport.append(
                "**Score moyen global**:"
                f" {sum(scores_totaux) / len(scores_totaux):.2f}/10"
            )
            rapport.append(f"**Meilleur score**: {max(scores_totaux):.2f}/10")
            rapport.append(f"**Pire score**: {min(scores_totaux):.2f}/10")
        rapport.append("")

        # Détails par dossier
        for result in sorted(self.results, key=lambda x: x.score_total, reverse=True):
            rapport.append(f"## 📁 {result.dossier.nom}")
            rapport.append(f"**Type**: {result.dossier.type_dossier}")
            rapport.append(f"**Score total**: {result.score_total:.2f}/10")
            rapport.append(f"**Modules Python**: {len(result.modules)}")
            rapport.append(f"**Fichiers MD**: {len(result.dossier.fichiers_md)}")
            rapport.append(f"**Sous-dossiers**: {len(result.dossier.sous_dossiers)}")
            rapport.append("")

            # Scores détaillés
            rapport.append("### 📊 Scores détaillés")
            rapport.append(f"- **Utilité**: {result.score_utilite:.2f}/10")
            rapport.append(
                f"- **Implémentation**: {result.score_implementation:.2f}/10"
            )
            rapport.append(f"- **Tests**: {result.score_tests:.2f}/10")
            rapport.append(f"- **Documentation**: {result.score_documentation:.2f}/10")
            rapport.append(f"- **Intégration**: {result.score_integration:.2f}/10")
            rapport.append("")

            # Pépites trouvées
            if result.pepites_trouvees:
                rapport.append("### 💎 Pépites trouvées")
                for pepite in result.pepites_trouvees:
                    rapport.append(f"- {pepite}")
                rapport.append("")

            # Recommandations
            if result.recommandations:
                rapport.append("### 🎯 Recommandations")
                for rec in result.recommandations:
                    rapport.append(f"- {rec}")
                rapport.append("")

            # Modules principaux
            if result.modules:
                rapport.append("### 📦 Modules principaux")
                for module in result.modules[:5]:  # Top 5
                    rapport.append(
                        f"- **{module.nom}**: {len(module.fonctions)} fonctions,"
                        f" {len(module.classes)} classes"
                    )
                rapport.append("")

        return "\n".join(rapport)


def main() -> None:
    """Fonction principale"""
    print("🔍 AUDIT COMPLET DOSSIERS ET SOUS-DOSSIERS")
    print("=" * 50)

    auditor = AuditCompletDossiers()
    results = auditor.analyser_tous_dossiers()

    # Générer le rapport
    rapport = auditor.generer_rapport()

    # Sauvegarder le rapport
    rapport_path = Path("audit_complet_dossiers.md")
    with open(rapport_path, "w", encoding="utf-8") as f:
        f.write(rapport)

    print(f"\n✅ Rapport sauvegardé dans: {rapport_path}")

    # Afficher un résumé
    print("\n📊 RÉSUMÉ EXÉCUTIF:")
    print(f"  📁 Dossiers analysés: {len(results)}")
    if results:
        scores = [r.score_total for r in results]
        print(f"  📈 Score moyen: {sum(scores) / len(scores):.2f}/10")
        print(f"  🏆 Meilleur: {max(scores):.2f}/10")
        print(f"  ⚠️ Pire: {min(scores):.2f}/10")

    # Afficher les pépites
    toutes_pepites = []
    for result in results:
        toutes_pepites.extend(result.pepites_trouvees)

    if toutes_pepites:
        print(f"\n💎 PÉPITES TROUVÉES ({len(toutes_pepites)}):")
        for pepite in toutes_pepites[:10]:  # Top 10
            print(f"  - {pepite}")


if __name__ == "__main__":
    main()
