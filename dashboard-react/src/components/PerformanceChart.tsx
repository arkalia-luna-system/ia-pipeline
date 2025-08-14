import React from 'react'

interface PerformanceChartProps {
  data: Array<{
    label: string
    value: number
    color: string
  }>
  title: string
}

const PerformanceChart: React.FC<PerformanceChartProps> = ({ data, title }) => {
  const maxValue = Math.max(...data.map(d => d.value))
  
  return (
    <div className="cyber-card">
      <h3 className="text-xl font-bold text-neon-blue mb-4">{title}</h3>
      
      <div className="space-y-3">
        {data.map((item, index) => (
          <div key={index} className="space-y-2">
            <div className="flex justify-between text-sm">
              <span className="text-gray-300">{item.label}</span>
              <span className="text-neon-green font-bold">{item.value}%</span>
            </div>
            
            <div className="w-full bg-gray-700 rounded-full h-3 relative overflow-hidden">
              <div 
                className="h-3 rounded-full transition-all duration-1000 ease-out"
                style={{ 
                  width: `${(item.value / maxValue) * 100}%`,
                  background: `linear-gradient(90deg, ${item.color}, ${item.color}dd)`
                }}
              >
                <div className="h-full w-full bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse"></div>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-6 pt-4 border-t border-border">
        <div className="flex justify-between text-sm text-gray-400">
          <span>Min: {Math.min(...data.map(d => d.value))}%</span>
          <span>Max: {Math.max(...data.map(d => d.value))}%</span>
        </div>
      </div>
    </div>
  )
}

export default PerformanceChart 