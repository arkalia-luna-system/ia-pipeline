#!/usr/bin/env python3
"""
📋 Générateur d'Index Documentation Athalia

Script pour générer automatiquement un index complet
de la documentation du projet Athalia.
"""

import logging
from datetime import datetime
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/maintenance/index_generation.log", mode="a", encoding="utf-8"
        ),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class IndexGenerator:
    """Générateur d'index de documentation"""

    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.docs_path = self.root_path / "docs"
        self.index_structure: dict[str, list[dict[str, str]]] = {
            "main": [],
            "api": [],
            "guides": [],
            "reports": [],
            "audits": [],
            "robotics": [],
            "archives": [],
        }

    def generate_index(self) -> str:
        """Génère un index complet de la documentation"""
        logger.info("📋 Génération de l'index de documentation...")

        # Scanner tous les fichiers Markdown
        self._scan_documentation()

        # Générer l'index principal
        index_content = self._generate_main_index()

        # Sauvegarder l'index
        index_path = self.docs_path / "INDEX.md"
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)

        logger.info(f"📋 Index généré: {index_path}")
        return str(index_path)

    def _scan_documentation(self):
        """Scanne toute la documentation"""
        logger.info("🔍 Scan de la documentation...")

        # Fichiers principaux
        main_files = ["README.md", "INSTALLATION.md", "CHANGELOG.md", "API.md"]

        for file_name in main_files:
            file_path = self.docs_path / file_name
            if file_path.exists():
                self.index_structure["main"].append(
                    {
                        "name": file_name,
                        "path": str(file_path.relative_to(self.docs_path)),
                        "title": self._extract_title(file_path),
                    }
                )

        # API
        api_path = self.docs_path / "API"
        if api_path.exists():
            for md_file in api_path.glob("*.md"):
                self.index_structure["api"].append(
                    {
                        "name": md_file.name,
                        "path": str(md_file.relative_to(self.docs_path)),
                        "title": self._extract_title(md_file),
                    }
                )

        # Guides
        guides_path = self.docs_path / "GUIDES"
        if guides_path.exists():
            for md_file in guides_path.glob("*.md"):
                self.index_structure["guides"].append(
                    {
                        "name": md_file.name,
                        "path": str(md_file.relative_to(self.docs_path)),
                        "title": self._extract_title(md_file),
                    }
                )

        # Rapports
        reports_path = self.docs_path / "REPORTS"
        if reports_path.exists():
            for md_file in reports_path.glob("*.md"):
                self.index_structure["reports"].append(
                    {
                        "name": md_file.name,
                        "path": str(md_file.relative_to(self.docs_path)),
                        "title": self._extract_title(md_file),
                    }
                )

        # Audits
        audits_path = self.docs_path / "audit_dossiers"
        if audits_path.exists():
            for md_file in audits_path.glob("*.md"):
                self.index_structure["audits"].append(
                    {
                        "name": md_file.name,
                        "path": str(md_file.relative_to(self.docs_path)),
                        "title": self._extract_title(md_file),
                    }
                )

        # Robotics
        robotics_path = self.docs_path / "robotics"
        if robotics_path.exists():
            for md_file in robotics_path.glob("*.md"):
                self.index_structure["robotics"].append(
                    {
                        "name": md_file.name,
                        "path": str(md_file.relative_to(self.docs_path)),
                        "title": self._extract_title(md_file),
                    }
                )

    def _extract_title(self, file_path: Path) -> str:
        """Extrait le titre d'un fichier Markdown"""
        try:
            with open(file_path, encoding="utf-8") as f:
                first_line = f.readline().strip()
                if first_line.startswith("# "):
                    return first_line[2:]
                elif first_line.startswith("## "):
                    return first_line[3:]
                else:
                    return file_path.stem.replace("_", " ").title()
        except Exception as e:
            logger.warning(f"Impossible de lire {file_path}: {e}")
            return file_path.stem.replace("_", " ").title()

    def _generate_main_index(self) -> str:
        """Génère le contenu de l'index principal"""
        content = "# 📚 Index de Documentation - Athalia\n\n"
        content += (
            f"**Date de génération:** {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n"
        )
        content += "**Générateur:** Script automatique\n\n"

        # Navigation rapide
        content += "## 🎯 Navigation Rapide\n\n"
        content += "### 📖 **Documentation Principale**\n"
        for item in self.index_structure["main"]:
            content += f"- [{item['title']}]({item['path']})\n"
        content += "\n"

        content += "### 🔧 **API et Développement**\n"
        for item in self.index_structure["api"]:
            content += f"- [{item['title']}]({item['path']})\n"
        content += "\n"

        content += "### 🛠️ **Guides et Best Practices**\n"
        for item in self.index_structure["guides"]:
            content += f"- [{item['title']}]({item['path']})\n"
        content += "\n"

        content += "### 📊 **Rapports et Analyses**\n"
        for item in self.index_structure["reports"]:
            content += f"- [{item['title']}]({item['path']})\n"
        content += "\n"

        content += "### 🔍 **Audits et Tests**\n"
        for item in self.index_structure["audits"]:
            content += f"- [{item['title']}]({item['path']})\n"
        content += "\n"

        content += "### 🤖 **Robotics**\n"
        for item in self.index_structure["robotics"]:
            content += f"- [{item['title']}]({item['path']})\n"
        content += "\n"

        # Structure détaillée
        content += "## 📁 Structure de Documentation\n\n"
        content += "```\n"
        content += "docs/\n"
        content += "├── INDEX.md                    # ← Cet index\n"
        content += "├── README.md                   # Vue d'ensemble\n"
        content += "├── INSTALLATION.md             # Guide d'installation\n"
        content += "├── CHANGELOG.md                # Historique des versions\n"
        content += "├── API.md                      # API principale (légère)\n"
        content += "├── API/                        # API détaillée\n"
        content += "├── REPORTS/                    # Rapports d'analyse\n"
        content += "├── GUIDES/                     # Guides pratiques\n"
        content += "├── audit_dossiers/             # Audits spécifiques\n"
        content += "├── logs_reports/               # Rapports de logs\n"
        content += "└── robotics/                   # Documentation robotique\n"
        content += "```\n\n"

        # Métriques
        total_files = sum(len(items) for items in self.index_structure.values())
        content += "## 📈 Métriques\n\n"
        content += f"- **Total fichiers MD:** {total_files}\n"
        content += (
            "- **Documentation principale:**"
            f" {len(self.index_structure['main'])} fichiers\n"
        )
        content += f"- **API:** {len(self.index_structure['api'])} fichiers\n"
        content += f"- **Guides:** {len(self.index_structure['guides'])} fichiers\n"
        content += f"- **Rapports:** {len(self.index_structure['reports'])} fichiers\n"
        content += f"- **Audits:** {len(self.index_structure['audits'])} fichiers\n"
        content += (
            f"- **Robotics:** {len(self.index_structure['robotics'])} fichiers\n\n"
        )

        # Recherche rapide
        content += "## 🔍 Recherche Rapide\n\n"
        content += "### **Par Thème:**\n"
        content += "- **Installation** → [INSTALLATION.md](INSTALLATION.md)\n"
        content += "- **API** → [API.md](API.md)\n"
        content += "- **Tests** → [GUIDES/TESTING.md](GUIDES/TESTING.md)\n"
        content += "- **Déploiement** → [GUIDES/DEPLOYMENT.md](GUIDES/DEPLOYMENT.md)\n"
        content += (
            "- **Contribution** → [GUIDES/CONTRIBUTING.md](GUIDES/CONTRIBUTING.md)\n\n"
        )

        content += "### **Par Type:**\n"
        content += "- **Guides** → Dossier [GUIDES/](GUIDES/)\n"
        content += "- **Rapports** → Dossier [REPORTS/](REPORTS/)\n"
        content += "- **Audits** → Dossier [audit_dossiers/](audit_dossiers/)\n"
        content += "- **API** → Dossier [API/](API/)\n\n"

        # Prochaines actions
        content += "## 🎯 Prochaines Actions\n\n"
        content += "1. ✅ **Optimisation API.md** - Terminé\n"
        content += "2. ✅ **Mise à jour README** - Terminé\n"
        content += "3. ✅ **Création index** - Terminé\n"
        content += "4. ✅ **Nettoyage archives** - Terminé\n"
        content += "5. ✅ **Validation liens** - Terminé\n\n"

        content += "---\n\n"
        content += "*Index généré automatiquement - Athalia 2025*\n"

        return content

    def generate_section_index(self, section: str) -> str:
        """Génère un index pour une section spécifique"""
        if section not in self.index_structure:
            return ""

        content = f"# 📋 Index {section.title()} - Athalia\n\n"
        content += f"**Date:** {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n\n"

        for item in self.index_structure[section]:
            content += f"- [{item['title']}]({item['path']})\n"

        return content


def main():
    """Fonction principale"""
    generator = IndexGenerator()

    # Générer l'index principal
    index_path = generator.generate_index()

    print(f"📋 Index généré avec succès: {index_path}")
    print(
        "📊 Fichiers indexés:"
        f" {sum(len(items) for items in generator.index_structure.values())}"
    )


if __name__ == "__main__":
    main()
