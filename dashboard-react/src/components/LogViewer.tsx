import React, { useState, useEffect, useRef } from 'react'

interface LogEntry {
  id: string
  timestamp: string
  level: 'info' | 'warning' | 'error' | 'success'
  message: string
  source: string
}

const LogViewer: React.FC = () => {
  const [logs, setLogs] = useState<LogEntry[]>([])
  const [filter, setFilter] = useState<'all' | 'info' | 'warning' | 'error' | 'success'>('all')
  const [autoScroll, setAutoScroll] = useState(true)
  const logEndRef = useRef<HTMLDivElement>(null)

  const logMessages: Array<{ level: 'info' | 'warning' | 'error' | 'success', message: string, source: string }> = [
    { level: 'info', message: 'Système ATHALIA initialisé avec succès', source: 'Core' },
    { level: 'success', message: 'Tests unitaires terminés - 1736/1736 passés', source: 'TestRunner' },
    { level: 'info', message: 'Modèle IA Ollama Qwen chargé et opérationnel', source: 'AIEngine' },
    { level: 'warning', message: 'Utilisation mémoire élevée détectée (78%)', source: 'SystemMonitor' },
    { level: 'error', message: 'Échec de connexion à la base de données externe', source: 'Database' },
    { level: 'success', message: 'Rapport de performance généré et sauvegardé', source: 'Reporter' },
    { level: 'info', message: 'Synchronisation des modules terminée', source: 'ModuleManager' },
    { level: 'warning', message: 'Latence réseau détectée (45ms)', source: 'NetworkMonitor' },
    { level: 'success', message: 'Maintenance automatique planifiée pour 02:00', source: 'Scheduler' },
    { level: 'info', message: 'Sauvegarde incrémentale en cours...', source: 'BackupService' }
  ]

  useEffect(() => {
    const interval = setInterval(() => {
      const randomLog = logMessages[Math.floor(Math.random() * logMessages.length)]
      const newLog: LogEntry = {
        id: Date.now().toString(),
        timestamp: new Date().toLocaleTimeString('fr-FR'),
        level: randomLog.level,
        message: randomLog.message,
        source: randomLog.source
      }
      
      setLogs(prev => {
        const newLogs = [...prev, newLog]
        if (newLogs.length > 50) {
          return newLogs.slice(-50)
        }
        return newLogs
      })
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  useEffect(() => {
    if (autoScroll && logEndRef.current) {
      logEndRef.current.scrollIntoView({ behavior: 'smooth' })
    }
  }, [logs, autoScroll])

  const getLevelColor = (level: string) => {
    switch (level) {
      case 'info': return 'text-blue-500'
      case 'warning': return 'text-orange-500'
      case 'error': return 'text-red-500'
      case 'success': return 'text-green-500'
      default: return 'text-gray-400'
    }
  }

  const getLevelIcon = (level: string) => {
    switch (level) {
      case 'info': return 'ℹ️'
      case 'warning': return '⚠️'
      case 'error': return '❌'
      case 'success': return '✅'
      default: return '📝'
    }
  }

  const filteredLogs = logs.filter(log => filter === 'all' || log.level === filter)

  return (
    <div className="cyber-card">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-bold text-blue-500 flex items-center">
          📋 LOGS SYSTÈME
          <span className="ml-2 w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
        </h3>
        
        <div className="flex items-center space-x-2">
          <select 
            value={filter} 
            onChange={(e) => setFilter(e.target.value as 'all' | 'info' | 'warning' | 'error' | 'success')}
            className="bg-gray-800 border border-gray-600 text-white text-sm rounded px-2 py-1"
          >
            <option value="all">Tous</option>
            <option value="info">Info</option>
            <option value="warning">Warning</option>
            <option value="error">Error</option>
            <option value="success">Success</option>
          </select>
          
          <button
            onClick={() => setAutoScroll(!autoScroll)}
            className={`px-3 py-1 text-xs rounded transition-colors ${
              autoScroll ? 'bg-green-500 text-black' : 'bg-gray-700 text-white'
            }`}
          >
            {autoScroll ? 'Auto' : 'Manuel'}
          </button>
        </div>
      </div>
      
      <div className="bg-gray-900 rounded-lg p-3 h-64 overflow-y-auto font-mono text-sm">
        {filteredLogs.length === 0 ? (
          <p className="text-gray-500 text-center py-8">Aucun log à afficher</p>
        ) : (
          filteredLogs.map((log) => (
            <div key={log.id} className="mb-2 p-2 bg-gray-800/50 rounded border-l-2 border-gray-600">
              <div className="flex items-start space-x-2">
                <span className="text-lg">{getLevelIcon(log.level)}</span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center space-x-2 text-xs text-gray-400 mb-1">
                    <span className={getLevelColor(log.level)}>[{log.level.toUpperCase()}]</span>
                    <span>{log.timestamp}</span>
                    <span className="text-purple-500">[{log.source}]</span>
                  </div>
                  <p className="text-white">{log.message}</p>
                </div>
              </div>
            </div>
          ))
        )}
        <div ref={logEndRef} />
      </div>
      
      <div className="mt-4 pt-3 border-t border-gray-600 text-center">
        <p className="text-xs text-gray-500">
          {filteredLogs.length} logs affichés • Filtre: {filter} • Auto-scroll: {autoScroll ? 'ON' : 'OFF'}
        </p>
      </div>
    </div>
  )
}

export default LogViewer
