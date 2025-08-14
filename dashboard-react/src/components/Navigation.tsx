import React from 'react'

interface NavigationProps {
  activeTab: string
  onTabChange: (tab: string) => void
}

const Navigation: React.FC<NavigationProps> = ({ activeTab, onTabChange }) => {
  const tabs = [
    { id: 'overview', label: '📊 Vue d\'ensemble', icon: '🏠' },
    { id: 'analytics', label: '📈 Analytics', icon: '📊' },
    { id: 'system', label: '🏥 Système', icon: '⚙️' },
    { id: 'ai', label: '🧠 IA', icon: '🤖' },
    { id: 'logs', label: '📋 Logs', icon: '📝' }
  ]

  return (
    <nav className="bg-gray-800 border-b border-gray-600 mb-8">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex space-x-1 overflow-x-auto">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => onTabChange(tab.id)}
              className={`flex items-center space-x-2 px-4 py-3 text-sm font-medium rounded-t-lg transition-all duration-200 whitespace-nowrap ${
                activeTab === tab.id
                  ? 'bg-blue-500 text-black border-b-2 border-blue-500'
                  : 'text-gray-400 hover:text-white hover:bg-gray-700'
              }`}
            >
              <span className="text-lg">{tab.icon}</span>
              <span>{tab.label}</span>
            </button>
          ))}
        </div>
      </div>
    </nav>
  )
}

export default Navigation
