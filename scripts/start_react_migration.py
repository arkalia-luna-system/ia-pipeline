#!/usr/bin/env python3
"""
🚀 ATHALIA REACT MIGRATION STARTER
Script pour démarrer immédiatement la migration vers React
"""

import os
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration du projet
PROJECT_ROOT = Path(".")
DASHBOARD_REACT_DIR = PROJECT_ROOT / "dashboard-react"
PACKAGE_JSON = DASHBOARD_REACT_DIR / "package.json"
TS_CONFIG = DASHBOARD_REACT_DIR / "tsconfig.json"
VITE_CONFIG = DASHBOARD_REACT_DIR / "vite.config.ts"


def check_prerequisites() -> bool:
    """Vérifie les prérequis pour la migration React."""
    print("🔍 Vérification des prérequis...")

    # Vérifier Node.js
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js installé: {result.stdout.strip()}")
        else:
            print("❌ Node.js non installé")
            return False
    except FileNotFoundError:
        print("❌ Node.js non trouvé dans le PATH")
        return False

    # Vérifier npm
    try:
        result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ npm installé: {result.stdout.strip()}")
        else:
            print("❌ npm non installé")
            return False
    except FileNotFoundError:
        print("❌ npm non trouvé dans le PATH")
        return False

    return True


def create_react_project() -> bool:
    """Crée le projet React avec Vite."""
    print("\n🚀 Création du projet React...")

    if DASHBOARD_REACT_DIR.exists():
        print("⚠️  Le répertoire dashboard-react existe déjà")
        response = input("Voulez-vous le supprimer et recommencer ? (y/N): ")
        if response.lower() == "y":
            import shutil

            shutil.rmtree(DASHBOARD_REACT_DIR)
        else:
            print("❌ Migration annulée")
            return False

    try:
        # Créer le projet avec Vite
        cmd = [
            "npm",
            "create",
            "vite@latest",
            "dashboard-react",
            "--",
            "--template",
            "react-ts",
        ]

        print(f"📋 Commande: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=PROJECT_ROOT, check=True)

        if result.returncode == 0:
            print("✅ Projet React créé avec succès")
            return True
        else:
            print("❌ Erreur lors de la création du projet")
            return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la création du projet: {e}")
        return False


def install_dependencies() -> bool:
    """Installe les dépendances nécessaires."""
    print("\n📦 Installation des dépendances...")

    try:
        # Installer les dépendances de base
        subprocess.run(["npm", "install"], cwd=DASHBOARD_REACT_DIR, check=True)
        print("✅ Dépendances de base installées")

        # Installer les dépendances supplémentaires
        additional_deps = [
            "tailwindcss",
            "postcss",
            "autoprefixer",
            "recharts",
            "@tanstack/react-query",
            "zustand",
            "react-router-dom",
            "@types/node",
        ]

        cmd = ["npm", "install", "--save"] + additional_deps
        subprocess.run(cmd, cwd=DASHBOARD_REACT_DIR, check=True)
        print("✅ Dépendances supplémentaires installées")

        # Installer les dépendances de développement
        dev_deps = [
            "@typescript-eslint/eslint-plugin",
            "@typescript-eslint/parser",
            "eslint",
            "eslint-config-prettier",
            "eslint-plugin-react",
            "eslint-plugin-react-hooks",
            "prettier",
            "husky",
            "lint-staged",
            "vitest",
            "@testing-library/react",
            "@testing-library/jest-dom",
        ]

        cmd = ["npm", "install", "--save-dev"] + dev_deps
        subprocess.run(cmd, cwd=DASHBOARD_REACT_DIR, check=True)
        print("✅ Dépendances de développement installées")

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation: {e}")
        return False


def configure_tailwind() -> bool:
    """Configure Tailwind CSS."""
    print("\n🎨 Configuration de Tailwind CSS...")

    try:
        # Initialiser Tailwind
        subprocess.run(
            ["npx", "tailwindcss", "init", "-p"], cwd=DASHBOARD_REACT_DIR, check=True
        )

        # Configurer tailwind.config.js
        tailwind_config = DASHBOARD_REACT_DIR / "tailwind.config.js"
        if tailwind_config.exists():
            content = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          900: '#1e3a8a',
        },
        success: {
          500: '#10b981',
        },
        warning: {
          500: '#f59e0b',
        },
        danger: {
          500: '#ef4444',
        }
      }
    },
  },
  plugins: [],
}"""

            with open(tailwind_config, "w") as f:
                f.write(content)
            print("✅ Configuration Tailwind créée")

        # Mettre à jour src/index.css
        css_file = DASHBOARD_REACT_DIR / "src" / "index.css"
        if css_file.exists():
            content = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html {
    font-family: 'Inter', system-ui, sans-serif;
  }
}

@layer components {
  .btn-primary {
    @apply bg-primary-500 hover:bg-primary-600 text-white font-medium py-2 px-4 rounded-lg transition-colors;
  }
  
  .btn-secondary {
    @apply bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-lg transition-colors;
  }
  
  .card {
    @apply bg-white rounded-lg shadow-md p-6 border border-gray-200;
  }
}"""

            with open(css_file, "w") as f:
                f.write(content)
            print("✅ Styles Tailwind configurés")

        return True

    except Exception as e:
        print(f"❌ Erreur lors de la configuration Tailwind: {e}")
        return False


def configure_eslint_prettier() -> bool:
    """Configure ESLint et Prettier."""
    print("\n🔧 Configuration ESLint et Prettier...")

    try:
        # Configuration ESLint
        eslint_config = DASHBOARD_REACT_DIR / ".eslintrc.json"
        eslint_content = {
            "env": {"browser": True, "es2021": True},
            "extends": [
                "eslint:recommended",
                "@typescript-eslint/recommended",
                "plugin:react/recommended",
                "plugin:react-hooks/recommended",
                "prettier",
            ],
            "parser": "@typescript-eslint/parser",
            "parserOptions": {
                "ecmaFeatures": {"jsx": True},
                "ecmaVersion": "latest",
                "sourceType": "module",
            },
            "plugins": ["react", "@typescript-eslint"],
            "rules": {
                "react/react-in-jsx-scope": "off",
                "react-hooks/rules-of-hooks": "error",
                "react-hooks/exhaustive-deps": "warn",
                "@typescript-eslint/no-unused-vars": "error",
                "@typescript-eslint/no-explicit-any": "warn",
            },
            "settings": {"react": {"version": "detect"}},
        }

        with open(eslint_config, "w") as f:
            json.dump(eslint_content, f, indent=2)
        print("✅ Configuration ESLint créée")

        # Configuration Prettier
        prettier_config = DASHBOARD_REACT_DIR / ".prettierrc"
        prettier_content = {
            "semi": True,
            "trailingComma": "es5",
            "singleQuote": True,
            "printWidth": 80,
            "tabWidth": 2,
            "useTabs": False,
        }

        with open(prettier_config, "w") as f:
            json.dump(prettier_content, f, indent=2)
        print("✅ Configuration Prettier créée")

        return True

    except Exception as e:
        print(f"❌ Erreur lors de la configuration ESLint/Prettier: {e}")
        return False


def create_project_structure() -> bool:
    """Crée la structure du projet React."""
    print("\n📁 Création de la structure du projet...")

    try:
        src_dir = DASHBOARD_REACT_DIR / "src"

        # Créer les répertoires
        directories = [
            "components/Dashboard",
            "components/Charts",
            "components/UI",
            "components/Common",
            "hooks",
            "services",
            "types",
            "utils",
            "styles",
        ]

        for dir_path in directories:
            full_path = src_dir / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"📁 Créé: {dir_path}")

        # Créer les fichiers de base
        files_to_create = {
            "types/dashboard.ts": (
                """export interface DashboardData {
  id: string;
  name: string;
  type: 'main' | 'analytics' | 'validation' | 'test';
  data: any;
  lastUpdated: string;
}

export interface ChartData {
  labels: string[];
  datasets: {
    label: string;
    data: number[];
    backgroundColor?: string;
    borderColor?: string;
  }[];
}"""
            ),
            "types/analytics.ts": (
                """export interface AnalyticsData {
  performance: {
    cpu: number;
    memory: number;
    responseTime: number;
  };
  metrics: {
    accuracy: number;
    precision: number;
    recall: number;
    f1Score: number;
  };
  timestamp: string;
}"""
            ),
            "types/validation.ts": (
                """export interface ValidationResult {
  id: string;
  status: 'pass' | 'fail' | 'warning';
  message: string;
  details?: any;
  timestamp: string;
}"""
            ),
            "services/api.ts": (
                """import { DashboardData, AnalyticsData, ValidationResult } from '../types';

const API_BASE = '/api';

export const api = {
  async getDashboards(): Promise<DashboardData[]> {
    const response = await fetch(`${API_BASE}/dashboards`);
    return response.json();
  },
  
  async getAnalytics(): Promise<AnalyticsData[]> {
    const response = await fetch(`${API_BASE}/analytics`);
    return response.json();
  },
  
  async getValidationResults(): Promise<ValidationResult[]> {
    const response = await fetch(`${API_BASE}/validation`);
    return response.json();
  }
};"""
            ),
            "hooks/useAthaliaData.ts": (
                """import { useState, useEffect } from 'react';
import { DashboardData } from '../types/dashboard';
import { api } from '../services/api';

export const useAthaliaData = () => {
  const [data, setData] = useState<DashboardData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const result = await api.getDashboards();
        setData(result);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Erreur inconnue');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return { data, loading, error };
};"""
            ),
            "components/UI/Button.tsx": (
                """import React from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger' | 'success';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  children,
  onClick,
  className = ''
}) => {
  const baseClasses = 'font-medium rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2';
  
  const variantClasses = {
    primary: 'bg-primary-500 hover:bg-primary-600 text-white focus:ring-primary-500',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800 focus:ring-gray-500',
    danger: 'bg-danger-500 hover:bg-danger-600 text-white focus:ring-danger-500',
    success: 'bg-success-500 hover:bg-success-600 text-white focus:ring-success-500'
  };
  
  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };
  
  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`;
  
  return (
    <button
      className={classes}
      disabled={disabled || loading}
      onClick={onClick}
    >
      {loading ? 'Chargement...' : children}
    </button>
  );
};"""
            ),
            "components/UI/Card.tsx": (
                """import React from 'react';

interface CardProps {
  title?: string;
  children: React.ReactNode;
  className?: string;
}

export const Card: React.FC<CardProps> = ({
  title,
  children,
  className = ''
}) => {
  return (
    <div className={`card ${className}`}>
      {title && (
        <h3 className="text-lg font-semibold text-gray-900 mb-4">{title}</h3>
      )}
      {children}
    </div>
  );
};"""
            ),
            "components/Dashboard/MainDashboard.tsx": (
                """import React from 'react';
import { Card } from '../UI/Card';
import { Button } from '../UI/Button';
import { useAthaliaData } from '../../hooks/useAthaliaData';

export const MainDashboard: React.FC = () => {
  const { data, loading, error } = useAthaliaData();

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg text-gray-600">Chargement...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg text-red-600">Erreur: {error}</div>
      </div>
    );
  }

  return (
    <div className="p-6">
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Dashboard Athalia IA</h1>
        <p className="text-gray-600 mt-2">Vue d'ensemble des performances et résultats</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card title="Projets IA" className="bg-blue-50">
          <div className="text-2xl font-bold text-blue-600">{data.length}</div>
          <p className="text-blue-800">Projets actifs</p>
        </Card>
        
        <Card title="Performance" className="bg-green-50">
          <div className="text-2xl font-bold text-green-600">98.5%</div>
          <p className="text-green-800">Score moyen</p>
        </Card>
        
        <Card title="Statut" className="bg-yellow-50">
          <div className="text-2xl font-bold text-yellow-600">Actif</div>
          <p className="text-yellow-800">Système opérationnel</p>
        </Card>
      </div>
      
      <div className="mt-8">
        <Card title="Actions rapides">
          <div className="flex gap-4">
            <Button variant="primary">Nouveau projet</Button>
            <Button variant="secondary">Voir analytics</Button>
            <Button variant="success">Lancer audit</Button>
          </div>
        </Card>
      </div>
    </div>
  );
};"""
            ),
            "App.tsx": (
                """import React from 'react';
import { MainDashboard } from './components/Dashboard/MainDashboard';
import './index.css';

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <MainDashboard />
    </div>
  );
}

export default App;"""
            ),
        }

        for file_path, content in files_to_create.items():
            full_path = src_dir / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"📄 Créé: {file_path}")

        return True

    except Exception as e:
        print(f"❌ Erreur lors de la création de la structure: {e}")
        return False


def create_package_scripts() -> bool:
    """Met à jour package.json avec les scripts nécessaires."""
    print("\n📝 Mise à jour des scripts package.json...")

    try:
        package_json_path = DASHBOARD_REACT_DIR / "package.json"

        if package_json_path.exists():
            with open(package_json_path, "r") as f:
                package_data = json.load(f)

            # Ajouter les scripts
            package_data["scripts"].update(
                {
                    "dev": "vite",
                    "build": "tsc && vite build",
                    "preview": "vite preview",
                    "lint": (
                        "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
                    ),
                    "lint:fix": "eslint . --ext ts,tsx --fix",
                    "format": 'prettier --write "src/**/*.{ts,tsx,css,md}"',
                    "test": "vitest",
                    "test:ui": "vitest --ui",
                    "test:coverage": "vitest --coverage",
                }
            )

            # Sauvegarder
            with open(package_json_path, "w") as f:
                json.dump(package_data, f, indent=2)

            print("✅ Scripts package.json mis à jour")
            return True
        else:
            print("❌ package.json non trouvé")
            return False

    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour package.json: {e}")
        return False


def run_initial_build() -> bool:
    """Lance le premier build pour vérifier que tout fonctionne."""
    print("\n🔨 Premier build de vérification...")

    try:
        # Vérifier que le projet se lance
        result = subprocess.run(
            ["npm", "run", "build"],
            cwd=DASHBOARD_REACT_DIR,
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print("✅ Build réussi ! Le projet React est prêt")
            return True
        else:
            print(f"❌ Erreur de build: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Erreur lors du build: {e}")
        return False


def main() -> None:
    """Fonction principale."""
    print("🚀 ATHALIA REACT MIGRATION STARTER")
    print("=" * 60)

    # Vérifier les prérequis
    if not check_prerequisites():
        print("\n❌ Prérequis non satisfaits. Veuillez installer Node.js et npm.")
        return

    # Créer le projet React
    if not create_react_project():
        print("\n❌ Échec de la création du projet React")
        return

    # Installer les dépendances
    if not install_dependencies():
        print("\n❌ Échec de l'installation des dépendances")
        return

    # Configurer Tailwind
    if not configure_tailwind():
        print("\n❌ Échec de la configuration Tailwind")
        return

    # Configurer ESLint et Prettier
    if not configure_eslint_prettier():
        print("\n❌ Échec de la configuration ESLint/Prettier")
        return

    # Créer la structure du projet
    if not create_project_structure():
        print("\n❌ Échec de la création de la structure")
        return

    # Mettre à jour les scripts
    if not create_package_scripts():
        print("\n❌ Échec de la mise à jour des scripts")
        return

    # Premier build
    if not run_initial_build():
        print("\n❌ Échec du premier build")
        return

    # Résumé final
    print("\n" + "=" * 60)
    print("🎉 MIGRATION REACT DÉMARRÉE AVEC SUCCÈS !")
    print(f"📁 Projet créé: {DASHBOARD_REACT_DIR}")
    print("\n📋 PROCHAINES ÉTAPES:")
    print("1. cd dashboard-react")
    print("2. npm run dev")
    print("3. Ouvrir http://localhost:5173")
    print("\n🔧 COMMANDES UTILES:")
    print("- npm run lint        # Vérifier le code")
    print("- npm run format      # Formater le code")
    print("- npm run test        # Lancer les tests")
    print("- npm run build       # Build de production")

    print("\n🚀 Votre projet React est prêt pour la migration des dashboards !")


if __name__ == "__main__":
    main()
