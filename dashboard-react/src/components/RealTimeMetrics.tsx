import React, { useState, useEffect } from 'react'

interface Metric {
  id: string
  name: string
  value: number
  unit: string
  trend: 'up' | 'down' | 'stable'
  status: 'online' | 'warning' | 'error'
}

const RealTimeMetrics: React.FC = () => {
  const [metrics, setMetrics] = useState<Metric[]>([
    { id: '1', name: 'CPU Usage', value: 67, unit: '%', trend: 'up', status: 'online' },
    { id: '2', name: 'Memory', value: 84, unit: '%', trend: 'stable', status: 'warning' },
    { id: '3', name: 'Network', value: 92, unit: 'Mbps', trend: 'up', status: 'online' },
    { id: '4', name: 'Disk I/O', value: 45, unit: 'MB/s', trend: 'down', status: 'online' },
    { id: '5', name: 'AI Response', value: 156, unit: 'ms', trend: 'down', status: 'online' },
    { id: '6', name: 'Test Success', value: 98.7, unit: '%', trend: 'up', status: 'online' }
  ])

  useEffect(() => {
    const interval = setInterval(() => {
      setMetrics(prev => prev.map(metric => ({
        ...metric,
        value: metric.value + (Math.random() - 0.5) * 10,
        trend: Math.random() > 0.5 ? 'up' : 'down'
      })))
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  const getTrendIcon = (trend: string) => {
    switch (trend) {
      case 'up': return '📈'
      case 'down': return '📉'
      default: return '➡️'
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'online': return 'text-neon-green'
      case 'warning': return 'text-neon-orange'
      case 'error': return 'text-red-500'
      default: return 'text-gray-400'
    }
  }

  return (
    <div className="cyber-card">
      <h3 className="text-xl font-bold text-neon-blue mb-6 flex items-center">
        📊 MÉTRIQUES TEMPS RÉEL
        <span className="ml-2 w-3 h-3 bg-neon-green rounded-full animate-pulse"></span>
      </h3>
      
      <div className="space-y-4">
        {metrics.map((metric) => (
          <div key={metric.id} className="flex items-center justify-between p-3 bg-gray-800/50 rounded-lg border border-border">
            <div className="flex items-center space-x-3">
              <span className="text-lg">{getTrendIcon(metric.trend)}</span>
              <div>
                <p className="text-white font-medium">{metric.name}</p>
                <p className="text-sm text-gray-400">{metric.unit}</p>
              </div>
            </div>
            
            <div className="text-right">
              <p className={`text-xl font-bold ${getStatusColor(metric.status)}`}>
                {metric.value.toFixed(1)}
              </p>
              <p className="text-xs text-gray-500 capitalize">{metric.status}</p>
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-6 pt-4 border-t border-border text-center">
        <p className="text-sm text-neon-blue animate-pulse">
          🔄 Mise à jour automatique toutes les 2 secondes
        </p>
      </div>
    </div>
  )
}

export default RealTimeMetrics 