import React, { useState, useEffect } from 'react'

interface HealthMetric {
  id: string
  name: string
  status: 'healthy' | 'warning' | 'critical'
  value: number
  maxValue: number
  description: string
}

const SystemHealth: React.FC = () => {
  const [healthMetrics, setHealthMetrics] = useState<HealthMetric[]>([
    { id: '1', name: 'CPU Load', status: 'healthy', value: 45, maxValue: 100, description: 'Charge processeur' },
    { id: '2', name: 'Memory Usage', status: 'warning', value: 78, maxValue: 100, description: 'Utilisation mémoire' },
    { id: '3', name: 'Disk Space', status: 'healthy', value: 23, maxValue: 100, description: 'Espace disque' },
    { id: '4', name: 'Network Latency', status: 'healthy', value: 12, maxValue: 100, description: 'Latence réseau' },
    { id: '5', name: 'AI Model Load', status: 'critical', value: 95, maxValue: 100, description: 'Charge modèles IA' },
    { id: '6', name: 'Test Queue', status: 'healthy', value: 8, maxValue: 50, description: 'File d\'attente tests' }
  ])

  useEffect(() => {
    const interval = setInterval(() => {
      setHealthMetrics(prev => prev.map(metric => ({
        ...metric,
        value: Math.max(0, Math.min(metric.maxValue, metric.value + (Math.random() - 0.5) * 10)),
        status: (() => {
          const ratio = metric.value / metric.maxValue
          if (ratio > 0.9) return 'critical'
          if (ratio > 0.7) return 'warning'
          return 'healthy'
        })()
      })))
    }, 4000)

    return () => clearInterval(interval)
  }, [])

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'healthy': return 'text-green-500'
      case 'warning': return 'text-orange-500'
      case 'critical': return 'text-red-500'
      default: return 'text-gray-400'
    }
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'healthy': return '✅'
      case 'warning': return '⚠️'
      case 'critical': return '🚨'
      default: return '❓'
    }
  }

  const getProgressColor = (status: string) => {
    switch (status) {
      case 'healthy': return 'bg-green-500'
      case 'warning': return 'bg-orange-500'
      case 'critical': return 'bg-red-500'
      default: return 'bg-gray-500'
    }
  }

  return (
    <div className="cyber-card">
      <h3 className="text-xl font-bold text-blue-500 mb-6 flex items-center">
        🏥 SANTÉ SYSTÈME
        <span className="ml-2 w-3 h-3 bg-green-500 rounded-full animate-pulse"></span>
      </h3>
      
      <div className="space-y-4">
        {healthMetrics.map((metric) => (
          <div key={metric.id} className="space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <span className="text-lg">{getStatusIcon(metric.status)}</span>
                <div>
                  <p className="text-white font-medium">{metric.name}</p>
                  <p className="text-xs text-gray-400">{metric.description}</p>
                </div>
              </div>
              <span className={`font-bold ${getStatusColor(metric.status)}`}>
                {metric.value.toFixed(1)}/{metric.maxValue}
              </span>
            </div>
            
            <div className="w-full bg-gray-700 rounded-full h-2 relative overflow-hidden">
              <div 
                className={`h-2 rounded-full transition-all duration-1000 ease-out ${getProgressColor(metric.status)}`}
                style={{ width: `${(metric.value / metric.maxValue) * 100}%` }}
              >
                <div className="h-full w-full bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse"></div>
              </div>
            </div>
            
            <div className="flex justify-between text-xs text-gray-500">
              <span>Status: {metric.status}</span>
              <span>{((metric.value / metric.maxValue) * 100).toFixed(1)}%</span>
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-6 pt-4 border-t border-gray-600 text-center">
        <p className="text-sm text-blue-500 animate-pulse">
          🔄 Surveillance continue - Mise à jour toutes les 4 secondes
        </p>
      </div>
    </div>
  )
}

export default SystemHealth
