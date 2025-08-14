import { useState, useEffect } from 'react'
import './App.css'
import Navigation from './components/Navigation'
import PerformanceChart from './components/PerformanceChart'
import RealTimeMetrics from './components/RealTimeMetrics'
import SystemHealth from './components/SystemHealth'
import LogViewer from './components/LogViewer'

function App() {
  const [activeTab, setActiveTab] = useState('overview')
  
  const [systemStatus] = useState({
    athalia: 'online',
    ai: 'online',
    tests: 'online',
    security: 'online'
  })

  const [metrics, setMetrics] = useState({
    tests: 1736,
    modules: 22,
    coverage: 98.5,
    performance: 99.2
  })

  const [aiModels] = useState([
    { name: 'Ollama Qwen', status: 'online', performance: 95.8 },
    { name: 'Ollama Mistral', status: 'online', performance: 97.2 },
    { name: 'Ollama LLaVA', status: 'online', performance: 93.4 },
    { name: 'Mock AI', status: 'standby', performance: 100.0 }
  ])

  const performanceData = [
    { label: 'Tests Unitaires', value: 98.5, color: '#00ff88' },
    { label: 'Tests Intégration', value: 95.2, color: '#00d4ff' },
    { label: 'Tests E2E', value: 92.8, color: '#9d00ff' },
    { label: 'Couverture Code', value: 97.1, color: '#ff6b00' }
  ]

  useEffect(() => {
    // Simulation de mises à jour en temps réel
    const interval = setInterval(() => {
      setMetrics(prev => ({
        ...prev,
        tests: prev.tests + Math.floor(Math.random() * 3),
        performance: prev.performance + (Math.random() - 0.5) * 0.2
      }))
    }, 3000)

    return () => clearInterval(interval)
  }, [])

  const renderOverviewTab = () => (
    <>
      {/* Metrics Dashboard */}
      <section className="max-w-7xl mx-auto px-6 mb-12">
        <h2 className="text-4xl font-bold text-center mb-8 neon-text">
          📊 MÉTRIQUES SYSTÈME
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="cyber-card text-center">
            <div className="text-4xl font-bold text-green-500 mb-2">{metrics.tests}</div>
            <p className="text-blue-500">Tests Collectés</p>
          </div>
          
          <div className="cyber-card text-center">
            <div className="text-4xl font-bold text-purple-600 mb-2">{metrics.modules}</div>
            <p className="text-blue-500">Modules Actifs</p>
          </div>
          
          <div className="cyber-card text-center">
            <div className="text-4xl font-bold text-orange-500 mb-2">{metrics.coverage}%</div>
            <p className="text-blue-500">Couverture Tests</p>
          </div>
          
          <div className="cyber-card text-center">
            <div className="text-4xl font-bold text-green-500 mb-2">{metrics.performance}%</div>
            <p className="text-blue-500">Performance</p>
          </div>
        </div>
      </section>

      {/* Action Buttons */}
      <section className="max-w-4xl mx-auto px-6 mb-12 text-center">
        <h2 className="text-3xl font-bold mb-8 neon-text">
          🎮 ACTIONS SYSTÈME
        </h2>
        
        <div className="flex flex-wrap justify-center gap-6">
          <button className="cyber-button">
            🚀 Lancer Tests
          </button>
          
          <button className="cyber-button">
            🧠 Activer IA
          </button>
          
          <button className="cyber-button">
            📊 Générer Rapport
          </button>
          
          <button className="cyber-button">
            🔧 Maintenance
          </button>
        </div>
      </section>
    </>
  )

  const renderAnalyticsTab = () => (
    <section className="max-w-7xl mx-auto px-6 mb-12">
      <h2 className="text-4xl font-bold text-center mb-8 neon-text">
        📈 ANALYTICS AVANCÉS
      </h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <PerformanceChart data={performanceData} title="🎯 PERFORMANCE TESTS" />
        <RealTimeMetrics />
      </div>
    </section>
  )

  const renderSystemTab = () => (
    <section className="max-w-7xl mx-auto px-6 mb-12">
      <h2 className="text-4xl font-bold text-center mb-8 neon-text">
        🏥 SURVEILLANCE SYSTÈME
      </h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <SystemHealth />
        <LogViewer />
      </div>
    </section>
  )

  const renderAITab = () => (
    <section className="max-w-7xl mx-auto px-6 mb-12">
      <h2 className="text-4xl font-bold text-center mb-8 neon-text">
        🧠 MODÈLES IA
      </h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {aiModels.map((model, index) => (
          <div key={model.name} className="cyber-card">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-xl font-bold text-blue-500">{model.name}</h3>
              <div className={`status-indicator ${model.status}`}></div>
            </div>
            
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-gray-400">Performance:</span>
                <span className="text-green-500 font-bold">{model.performance}%</span>
              </div>
              
              <div className="w-full bg-gray-700 rounded-full h-2">
                <div 
                  className="h-2 rounded-full transition-all duration-500"
                  style={{ width: `${model.performance}%` }}
                >
                  <div className="h-full w-full bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse"></div>
                </div>
              </div>
              
              <div className="flex justify-between text-sm text-gray-400">
                <span>Status: {model.status}</span>
                <span>ID: {index + 1}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )

  const renderLogsTab = () => (
    <section className="max-w-7xl mx-auto px-6 mb-12">
      <h2 className="text-4xl font-bold text-center mb-8 neon-text">
        📋 LOGS SYSTÈME
      </h2>
      
      <div className="grid grid-cols-1 gap-8">
        <LogViewer />
      </div>
    </section>
  )

  const renderActiveTab = () => {
    switch (activeTab) {
      case 'overview':
        return renderOverviewTab()
      case 'analytics':
        return renderAnalyticsTab()
      case 'system':
        return renderSystemTab()
      case 'ai':
        return renderAITab()
      case 'logs':
        return renderLogsTab()
      default:
        return renderOverviewTab()
    }
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white overflow-hidden">
      {/* Header Cyberpunk */}
      <header className="text-center py-12 relative">
        <h1 className="text-6xl font-bold neon-text mb-4 animate-float">
          🚀 ATHALIA CORE
        </h1>
        <p className="text-2xl text-blue-500 mb-8 animate-pulse">
          Intelligence Artificielle Ultra-Moderne
        </p>
        
        {/* Status Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto">
          {Object.entries(systemStatus).map(([key, status]) => (
            <div key={key} className="cyber-card text-center">
              <div className={`status-indicator ${status} mx-auto mb-3`}></div>
              <h3 className="text-blue-500 font-bold capitalize">{key}</h3>
              <p className="text-sm text-gray-400">{status}</p>
            </div>
          ))}
        </div>
      </header>

      {/* Navigation */}
      <Navigation activeTab={activeTab} onTabChange={setActiveTab} />

      {/* Content based on active tab */}
      {renderActiveTab()}

      {/* Footer */}
      <footer className="text-center py-8 border-t border-gray-600">
        <p className="text-blue-500">
          🎯 ATHALIA CORE v6.1 - Système d'Intelligence Artificielle Enterprise-Grade
        </p>
        <p className="text-sm text-gray-500 mt-2">
          Développé avec ❤️ et des néons cyberpunk
        </p>
      </footer>
    </div>
  )
}

export default App
