# 🚀 ATHALIA CORE - Dashboard React

Un dashboard moderne et cyberpunk pour le système ATHALIA, construit avec React, TypeScript, Vite et Tailwind CSS v4.

## ✨ Fonctionnalités

### 🏠 Vue d'ensemble
- **Statut système en temps réel** : ATHALIA, IA, Tests, Sécurité
- **Métriques clés** : Tests collectés, Modules actifs, Couverture, Performance
- **Actions système** : Lancer tests, Activer IA, Générer rapport, Maintenance

### 📈 Analytics
- **Graphiques de performance** : Tests unitaires, intégration, E2E, Couverture
- **Métriques temps réel** : CPU, Mémoire, Réseau, Disk I/O, IA Response

### 🏥 Surveillance Système
- **Santé système** : CPU Load, Memory Usage, Disk Space, Network Latency
- **Indicateurs visuels** : Healthy (✅), Warning (⚠️), Critical (🚨)

### 🧠 Modèles IA
- **Statut des modèles** : Ollama Qwen, Mistral, LLaVA, Mock AI
- **Métriques de performance** : Temps de réponse, Charge, Disponibilité

### 📋 Logs Système
- **Logs en temps réel** : Info, Warning, Error, Success
- **Filtrage par niveau** : Tous, Info, Warning, Error, Success
- **Auto-scroll** : Mise à jour automatique toutes les 2 secondes

## 🛠️ Technologies

- **Frontend** : React 19 + TypeScript
- **Build Tool** : Vite 7
- **Styling** : Tailwind CSS v4 + PostCSS
- **Architecture** : Composants modulaires avec hooks React

## 🚀 Installation et Démarrage

### Prérequis
- Node.js 18+ 
- npm ou yarn

### Installation
```bash
# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm run dev

# Construire pour la production
npm run build

# Linter le code
npm run lint

# Prévisualiser la build
npm run preview
```

## 📁 Structure du Projet

```
src/
├── components/           # Composants React
│   ├── Navigation.tsx   # Navigation par onglets
│   ├── PerformanceChart.tsx  # Graphiques de performance
│   ├── RealTimeMetrics.tsx   # Métriques temps réel
│   ├── SystemHealth.tsx      # Santé système
│   └── LogViewer.tsx         # Visualiseur de logs
├── App.tsx              # Composant principal
├── App.css              # Styles CSS personnalisés
├── index.css            # Styles Tailwind CSS
└── main.tsx             # Point d'entrée
```

## 🎨 Design System

### Couleurs Cyberpunk
- **Neon Blue** : `#00d4ff` - Éléments principaux
- **Neon Purple** : `#9d00ff` - Accents et highlights
- **Neon Green** : `#00ff88` - Succès et indicateurs positifs
- **Neon Orange** : `#ff6b00` - Avertissements
- **Dark Background** : `#0a0a0a` - Arrière-plan principal
- **Card Background** : `#1a1a1a` - Arrière-plan des cartes

### Animations
- **Glow** : Effet de lueur néon
- **SlideIn** : Animation d'entrée
- **Float** : Effet de flottement
- **Pulse** : Pulsation continue

### Composants CSS
- **`.cyber-card`** : Cartes avec style cyberpunk
- **`.cyber-button`** : Boutons avec effets hover
- **`.neon-text`** : Texte avec gradient néon
- **`.status-indicator`** : Indicateurs de statut

## 🔧 Configuration

### Tailwind CSS v4
Le projet utilise Tailwind CSS v4 avec une configuration personnalisée dans `tailwind.config.js` :

```javascript
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: { /* Couleurs personnalisées */ },
      animation: { /* Animations personnalisées */ },
      keyframes: { /* Keyframes pour animations */ }
    }
  }
}
```

### PostCSS
Configuration PostCSS avec `@tailwindcss/postcss` et `autoprefixer` :

```javascript
export default {
  plugins: {
    '@tailwindcss/postcss': {},
    autoprefixer: {},
  }
}
```

## 📱 Responsive Design

Le dashboard est entièrement responsive avec :
- **Mobile First** : Design optimisé pour mobile
- **Grid System** : Layouts adaptatifs avec CSS Grid
- **Breakpoints** : Adaptation automatique selon la taille d'écran

## 🚀 Déploiement

### Build de Production
```bash
npm run build
```

### Serveur de Production
```bash
npm run preview
```

## 🔍 Développement

### Structure des Composants
Chaque composant suit une structure cohérente :
- Interface TypeScript pour les props
- Hooks React pour l'état et les effets
- Classes Tailwind CSS pour le styling
- Gestion des événements et interactions

### Gestion d'État
- **État local** : `useState` pour les composants individuels
- **Effets** : `useEffect` pour les mises à jour en temps réel
- **Références** : `useRef` pour les interactions DOM

## 🎯 Roadmap

- [ ] **Intégration API** : Connexion aux services ATHALIA réels
- [ ] **WebSocket** : Mises à jour en temps réel via WebSocket
- [ ] **Tests** : Tests unitaires et d'intégration
- [ ] **PWA** : Support Progressive Web App
- [ ] **Thèmes** : Système de thèmes multiples
- [ ] **Internationalisation** : Support multi-langues

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

Pour toute question ou problème :
- Ouvrir une issue sur GitHub
- Consulter la documentation
- Contacter l'équipe de développement

---

**🎯 ATHALIA CORE v6.1** - Système d'Intelligence Artificielle Enterprise-Grade
Développé avec ❤️ et des néons cyberpunk
