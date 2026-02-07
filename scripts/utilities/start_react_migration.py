#!/usr/bin/env python3
"""
🚀 ATHALIA REACT MIGRATION STARTER
Script pour démarrer immédiatement la migration vers React
"""

import json
import subprocess
from pathlib import Path

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

        # Installer les dépendances supplémentaires
        additional_deps = [
            "tailwindcss",
            "autoprefixer",
            "postcss",
            "@types/node",
            "eslint",
            "prettier",
            "@typescript-eslint/eslint-plugin",
            "@typescript-eslint/parser",
            "eslint-config-prettier",
            "eslint-plugin-prettier",
        ]

        for dep in additional_deps:
            print(f"📦 Installation de {dep}...")
            subprocess.run(
                ["npm", "install", "--save-dev", dep],
                cwd=DASHBOARD_REACT_DIR,
                check=True,
            )

        print("✅ Toutes les dépendances installées")
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
            ["npx", "tailwindcss", "init", "-p"],
            cwd=DASHBOARD_REACT_DIR,
            check=True,
        )

        # Configurer tailwind.config.js
        tailwind_config = DASHBOARD_REACT_DIR / "tailwind.config.js"
        if tailwind_config.exists():
            with open(tailwind_config, "w", encoding="utf-8") as f:
                f.write("""/** @type {import('tailwindcss').Config} */
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
          600: '#2563eb',
          700: '#1d4ed8',
          900: '#1e3a8a',
        },
        secondary: {
          50: '#f8fafc',
          500: '#64748b',
          600: '#475569',
          700: '#334155',
          900: '#0f172a',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
""")

        # Configurer src/index.css
        css_file = DASHBOARD_REACT_DIR / "src" / "index.css"
        if css_file.exists():
            with open(css_file, "w", encoding="utf-8") as f:
                f.write("""@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

@layer base {
  html {
    font-family: 'Inter', system-ui, sans-serif;
  }

  body {
    @apply bg-gray-50 text-gray-900;
  }

  code {
    font-family: 'JetBrains Mono', monospace;
  }
}

@layer components {
  .btn-primary {
    @apply bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200;
  }

  .btn-secondary {
    @apply bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-lg transition-colors duration-200;
  }

  .card {
    @apply bg-white rounded-xl shadow-sm border border-gray-200 p-6;
  }

  .input-field {
    @apply w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent;
  }
}""")

        print("✅ Tailwind CSS configuré")
        return True

    except Exception as e:
        print(f"❌ Erreur lors de la configuration de Tailwind: {e}")
        return False


def configure_eslint_prettier() -> bool:
    """Configure ESLint et Prettier."""
    print("\n🔧 Configuration d'ESLint et Prettier...")

    try:
        # Configuration ESLint
        eslint_config = DASHBOARD_REACT_DIR / ".eslintrc.cjs"
        with open(eslint_config, "w", encoding="utf-8") as f:
            f.write("""module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
    'plugin:prettier/recommended',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parser: '@typescript-eslint/parser',
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': [
      'warn',
      { allowConstantExport: true },
    ],
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'prefer-const': 'error',
    'no-var': 'error',
  },
}
""")

        # Configuration Prettier
        prettier_config = DASHBOARD_REACT_DIR / ".prettierrc"
        with open(prettier_config, "w", encoding="utf-8") as f:
            f.write("""{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
""")

        print("✅ ESLint et Prettier configurés")
        return True

    except Exception as e:
        print(f"❌ Erreur lors de la configuration d'ESLint/Prettier: {e}")
        return False


def create_project_structure() -> bool:
    """Crée la structure du projet React."""
    print("\n📁 Création de la structure du projet...")

    try:
        # Créer les dossiers
        src_dir = DASHBOARD_REACT_DIR / "src"
        components_dir = src_dir / "components"
        pages_dir = src_dir / "pages"
        hooks_dir = src_dir / "hooks"
        utils_dir = src_dir / "utils"
        types_dir = src_dir / "types"
        assets_dir = src_dir / "assets"

        for directory in [
            components_dir,
            pages_dir,
            hooks_dir,
            utils_dir,
            types_dir,
            assets_dir,
        ]:
            directory.mkdir(parents=True, exist_ok=True)

        # Créer les composants de base
        components = {
            "Button.tsx": (
                """import React from 'react';

interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  onClick?: () => void;
  disabled?: boolean;
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  onClick,
  disabled = false,
  className = '',
}) => {
  const baseClasses = 'font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2';

  const variantClasses = {
    primary: 'bg-primary-600 hover:bg-primary-700 text-white focus:ring-primary-500',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800 focus:ring-gray-500',
    outline: 'border border-gray-300 hover:bg-gray-50 text-gray-700 focus:ring-gray-500',
  };

  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`;

  return (
    <button
      className={classes}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};
"""
            ),
            "Card.tsx": (
                """import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  padding?: 'sm' | 'md' | 'lg';
}

export const Card: React.FC<CardProps> = ({
  children,
  className = '',
  padding = 'md',
}) => {
  const paddingClasses = {
    sm: 'p-4',
    md: 'p-6',
    lg: 'p-8',
  };

  const classes = `bg-white rounded-xl shadow-sm border border-gray-200 ${paddingClasses[padding]} ${className}`;

  return (
    <div className={classes}>
      {children}
    </div>
  );
};
"""
            ),
            "Input.tsx": (
                """import React from 'react';

interface InputProps {
  label?: string;
  placeholder?: string;
  value: string;
  onChange: (value: string) => void;
  type?: 'text' | 'email' | 'password' | 'number';
  error?: string;
  className?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  placeholder,
  value,
  onChange,
  type = 'text',
  error,
  className = '',
}) => {
  const inputClasses = `w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
    error ? 'border-red-500' : 'border-gray-300'
  } ${className}`;

  return (
    <div className="space-y-1">
      {label && (
        <label className="block text-sm font-medium text-gray-700">
          {label}
        </label>
      )}
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className={inputClasses}
      />
      {error && (
        <p className="text-sm text-red-600">{error}</p>
      )}
    </div>
  );
};
"""
            ),
        }

        for filename, content in components.items():
            file_path = components_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        # Créer les pages de base
        pages = {
            "Home.tsx": (
                """import React from 'react';
import { Card } from '../components/Card';
import { Button } from '../components/Button';

export const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Bienvenue sur Athalia Dashboard
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Interface moderne et intuitive pour gérer votre projet Athalia
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              🚀 Démarrage Rapide
            </h3>
            <p className="text-gray-600 mb-4">
              Commencez rapidement avec les fonctionnalités essentielles
            </p>
            <Button variant="primary">
              Commencer
            </Button>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              📊 Analytics
            </h3>
            <p className="text-gray-600 mb-4">
              Suivez les performances et métriques de votre projet
            </p>
            <Button variant="secondary">
              Voir les stats
            </Button>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              ⚙️ Configuration
            </h3>
            <p className="text-gray-600 mb-4">
              Personnalisez votre environnement de développement
            </p>
            <Button variant="outline">
              Configurer
            </Button>
          </Card>
        </div>
      </div>
    </div>
  );
};
"""
            ),
            "Dashboard.tsx": (
                """import React from 'react';
import { Card } from '../components/Card';

export const Dashboard: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">
            Tableau de bord
          </h1>
          <p className="text-gray-600 mt-2">
            Vue d'ensemble de votre projet Athalia
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-8">
          <Card padding="sm">
            <div className="text-center">
              <div className="text-2xl font-bold text-primary-600">153</div>
              <div className="text-sm text-gray-600">Modules</div>
            </div>
          </Card>

          <Card padding="sm">
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">24,243</div>
              <div className="text-sm text-gray-600">Lignes de code</div>
            </div>
          </Card>

          <Card padding="sm">
            <div className="text-center">
              <div className="text-2xl font-bold text-blue-600">1,696</div>
              <div className="text-sm text-gray-600">Tests</div>
            </div>
          </Card>

          <Card padding="sm">
            <div className="text-center">
              <div className="text-2xl font-bold text-purple-600">85%</div>
              <div className="text-sm text-gray-600">Couverture</div>
            </div>
          </Card>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <Card>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">
              Activité Récente
            </h3>
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                <span className="text-sm text-gray-600">
                  Tests unitaires passés avec succès
                </span>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                <span className="text-sm text-gray-600">
                  Nouveau module ajouté
                </span>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-yellow-500 rounded-full"></div>
                <span className="text-sm text-gray-600">
                  Mise à jour de la documentation
                </span>
              </div>
            </div>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">
              Prochaines Actions
            </h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">
                  Optimiser les performances
                </span>
                <span className="text-xs text-gray-500">Demain</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">
                  Ajouter de nouveaux tests
                </span>
                <span className="text-xs text-gray-500">Cette semaine</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">
                  Mettre à jour les dépendances
                </span>
                <span className="text-xs text-gray-500">Prochaine semaine</span>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};
"""
            ),
        }

        for filename, content in pages.items():
            file_path = pages_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        # Créer les hooks personnalisés
        hooks = {
            "useLocalStorage.ts": (
                """import { useState, useEffect } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error setting localStorage:', error);
    }
  };

  return [storedValue, setValue] as const;
}
"""
            ),
            "useDebounce.ts": (
                """import { useState, useEffect } from 'react';

export function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}
"""
            ),
        }

        for filename, content in hooks.items():
            file_path = hooks_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        # Créer les types TypeScript
        types = {
            "index.ts": (
                """export interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
  avatar?: string;
}

export interface Project {
  id: string;
  name: string;
  description: string;
  status: 'active' | 'paused' | 'completed';
  createdAt: Date;
  updatedAt: Date;
}

export interface Metric {
  name: string;
  value: number;
  unit: string;
  trend: 'up' | 'down' | 'stable';
  change: number;
}

export interface Notification {
  id: string;
  type: 'info' | 'success' | 'warning' | 'error';
  title: string;
  message: string;
  timestamp: Date;
  read: boolean;
}
"""
            ),
        }

        for filename, content in types.items():
            file_path = types_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        # Créer les utilitaires
        utils = {
            "formatDate.ts": (
                """export function formatDate(date: Date): string {
  return new Intl.DateTimeFormat('fr-FR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(date);
}

export function formatRelativeTime(date: Date): string {
  const now = new Date();
  const diffInSeconds = Math.floor((now.getTime() - date.getTime()) / 1000);

  if (diffInSeconds < 60) return 'À l\'instant';
  if (diffInSeconds < 3600) return `Il y a ${Math.floor(diffInSeconds / 60)} min`;
  if (diffInSeconds < 86400) return `Il y a ${Math.floor(diffInSeconds / 3600)}h`;
  if (diffInSeconds < 2592000) return `Il y a ${Math.floor(diffInSeconds / 86400)}j`;

  return formatDate(date);
}
"""
            ),
            "validation.ts": (
                r"""export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

export function isValidPassword(password: string): boolean {
  return password.length >= 8;
}

export function sanitizeInput(input: string): string {
  return input.trim().replace(/[<>]/g, '');
}
"""
            ),
        }

        for filename, content in utils.items():
            file_path = utils_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        print("✅ Structure du projet créée")
        return True

    except Exception as e:
        print(f"❌ Erreur lors de la création de la structure: {e}")
        return False


def create_package_scripts() -> bool:
    """Crée les scripts package.json personnalisés."""
    print("\n📝 Configuration des scripts package.json...")

    try:
        package_path = DASHBOARD_REACT_DIR / "package.json"
        if package_path.exists():
            with open(package_path, encoding="utf-8") as f:
                package_data = json.load(f)

            # Ajouter les scripts personnalisés
            package_data["scripts"].update(
                {
                    "dev": "vite",
                    "build": "tsc && vite build",
                    "preview": "vite preview",
                    "lint": (
                        "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
                    ),
                    "lint:fix": "eslint . --ext ts,tsx --fix",
                    "format": "prettier --write .",
                    "type-check": "tsc --noEmit",
                    "test": "vitest",
                    "test:ui": "vitest --ui",
                    "test:coverage": "vitest --coverage",
                }
            )

            with open(package_path, "w", encoding="utf-8") as f:
                json.dump(package_data, f, indent=2)

        print("✅ Scripts package.json configurés")
        return True

    except Exception as e:
        print(f"❌ Erreur lors de la configuration des scripts: {e}")
        return False


def run_initial_build() -> bool:
    """Lance le build initial pour vérifier que tout fonctionne."""
    print("\n🔨 Build initial...")

    try:
        # Vérifier TypeScript
        subprocess.run(
            ["npm", "run", "type-check"],
            cwd=DASHBOARD_REACT_DIR,
            check=True,
        )

        # Build de production
        subprocess.run(
            ["npm", "run", "build"],
            cwd=DASHBOARD_REACT_DIR,
            check=True,
        )

        print("✅ Build initial réussi")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du build initial: {e}")
        return False


def main() -> None:
    """Fonction principale."""
    print("🚀 ATHALIA REACT MIGRATION STARTER")
    print("=" * 60)

    # Vérifier les prérequis
    if not check_prerequisites():
        print("❌ Prérequis non satisfaits")
        return

    # Créer le projet React
    if not create_react_project():
        print("❌ Échec de la création du projet")
        return

    # Installer les dépendances
    if not install_dependencies():
        print("❌ Échec de l'installation des dépendances")
        return

    # Configurer Tailwind
    if not configure_tailwind():
        print("❌ Échec de la configuration de Tailwind")
        return

    # Configurer ESLint et Prettier
    if not configure_eslint_prettier():
        print("❌ Échec de la configuration d'ESLint/Prettier")
        return

    # Créer la structure du projet
    if not create_project_structure():
        print("❌ Échec de la création de la structure")
        return

    # Configurer les scripts
    if not create_package_scripts():
        print("❌ Échec de la configuration des scripts")
        return

    # Build initial
    if not run_initial_build():
        print("❌ Échec du build initial")
        return

    # Succès
    print("\n" + "=" * 60)
    print("🎉 MIGRATION REACT TERMINÉE AVEC SUCCÈS !")
    print("\n📋 Prochaines étapes:")
    print("1. cd dashboard-react")
    print("2. npm run dev")
    print("3. Ouvrir http://localhost:5173")
    print("\n🔧 Commandes utiles:")
    print("- npm run lint        # Vérifier le code")
    print("- npm run format      # Formater le code")
    print("- npm run build       # Build de production")
    print("- npm run preview     # Prévisualiser le build")


if __name__ == "__main__":
    main()
