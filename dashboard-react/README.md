# 🚀 Dashboard React ATHALIA

**Dashboard moderne et interactif pour le système ATHALIA Core - Intelligence Artificielle Enterprise-Grade**

## ✨ Fonctionnalités

### 🎯 **Interface Cyberpunk Moderne**
- Design futuriste avec couleurs néon et animations fluides
- Thème sombre optimisé pour la surveillance système
- Interface responsive et adaptative

### 📊 **Sections Principales**
1. **🏠 Vue d'ensemble** - Métriques système et actions rapides
2. **📈 Analytics** - Graphiques de performance et métriques temps réel
3. **🏥 Système** - Surveillance santé système et logs
4. **🧠 IA** - Statut des modèles d'intelligence artificielle
5. **📋 Logs** - Visualisation des logs système en temps réel

### 🔄 **Fonctionnalités Temps Réel**
- Mise à jour automatique des métriques
- Surveillance continue de la santé système
- Logs en streaming avec filtrage intelligent
- Indicateurs de statut visuels

## 🛠️ Technologies

- **React 19** - Interface utilisateur moderne
- **TypeScript** - Code type-safe et robuste
- **Vite** - Build tool ultra-rapide
- **Tailwind CSS 3** - Framework CSS utilitaire
- **PostCSS** - Traitement CSS avancé

## 🚀 Installation et Démarrage

### Prérequis
- Node.js 18+ 
- npm ou yarn

### Installation
```bash
# Cloner le projet
git clone <repository-url>
cd dashboard-react

# Installer les dépendances
npm install

# Lancer le serveur de développement
npm run dev
```

### Scripts Disponibles
```bash
npm run dev          # Serveur de développement
npm run build        # Build de production
npm run preview      # Prévisualisation du build
npm run lint         # Vérification du code
```

## 📁 Structure du Projet

```
dashboard-react/
├── src/
│   ├── components/          # Composants React
│   │   ├── App.tsx         # Composant principal
│   │   ├── Navigation.tsx  # Navigation par onglets
│   │   ├── PerformanceChart.tsx    # Graphiques
│   │   ├── RealTimeMetrics.tsx     # Métriques temps réel
│   │   ├── SystemHealth.tsx        # Santé système
│   │   └── LogViewer.tsx           # Visualiseur de logs
│   ├── index.css           # Styles Tailwind et personnalisés
│   └── main.tsx            # Point d'entrée
├── tailwind.config.js      # Configuration Tailwind CSS
├── postcss.config.js       # Configuration PostCSS
└── package.json            # Dépendances et scripts
```

## 🎨 Composants Principaux

### `App.tsx`
- Interface principale avec navigation par onglets
- Gestion de l'état global de l'application
- Rendu conditionnel des sections

### `Navigation.tsx`
- Navigation entre les différentes sections
- Indicateurs visuels de l'onglet actif
- Design responsive et accessible

### `PerformanceChart.tsx`
- Graphiques de performance avec barres animées
- Calcul automatique des valeurs min/max
- Couleurs dynamiques et transitions fluides

### `RealTimeMetrics.tsx`
- Métriques système en temps réel
- Indicateurs de tendance (📈📉➡️)
- Mise à jour automatique toutes les 2 secondes

### `SystemHealth.tsx`
- Surveillance de la santé du système
- Indicateurs visuels (✅⚠️🚨)
- Barres de progression animées

### `LogViewer.tsx`
- Visualisation des logs système
- Filtrage par niveau (info, warning, error, success)
- Auto-scroll et navigation manuelle

## 🎭 Styles et Animations

### Classes CSS Personnalisées
```css
.cyber-card      /* Cartes avec bordure et ombre */
.cyber-button    /* Boutons avec effets hover */
.neon-text       /* Texte avec dégradé néon */
.status-indicator /* Indicateurs de statut */
```

### Animations CSS
- `animate-glow` - Effet de lueur pulsante
- `animate-slideIn` - Apparition en slide
- `animate-float` - Flottement subtil
- `animate-pulse` - Pulsation continue

## 🔧 Configuration

### Tailwind CSS
Le projet utilise Tailwind CSS v3 avec une configuration personnalisée :
- Couleurs néon personnalisées
- Animations CSS personnalisées
- Composants utilitaires

### PostCSS
Configuration optimisée avec :
- Tailwind CSS
- Autoprefixer
- Optimisations de production

## 📱 Responsive Design

- **Mobile First** - Optimisé pour les petits écrans
- **Grid System** - Layouts adaptatifs
- **Breakpoints** - Adaptation automatique aux différentes tailles

## 🚀 Déploiement

### Build de Production
```bash
npm run build
```

### Prévisualisation
```bash
npm run preview
```

### Déploiement
Les fichiers générés dans `dist/` peuvent être déployés sur n'importe quel serveur web statique.

## 🔍 Développement

### Ajout de Nouveaux Composants
1. Créer le composant dans `src/components/`
2. Importer dans `App.tsx`
3. Ajouter dans la navigation appropriée
4. Tester avec `npm run dev`

### Modification des Styles
- Utiliser les classes Tailwind CSS
- Ajouter des styles personnalisés dans `index.css`
- Respecter la convention de nommage

## 🐛 Dépannage

### Erreurs Courantes
- **Port déjà utilisé** : Changer le port dans `vite.config.ts`
- **Classes CSS non reconnues** : Vérifier la configuration Tailwind
- **Erreurs TypeScript** : Vérifier les types et interfaces

### Logs de Développement
- Console du navigateur pour les erreurs JavaScript
- Terminal pour les erreurs de build
- Vérifier la configuration PostCSS

## 📄 Licence

Ce projet fait partie du système ATHALIA Core et est soumis aux mêmes conditions de licence.

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Commiter les changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

---

**🎯 ATHALIA CORE v6.1 - Système d'Intelligence Artificielle Enterprise-Grade**

*Développé avec ❤️ et des néons cyberpunk*
