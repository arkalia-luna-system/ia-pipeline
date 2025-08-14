/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'neon-blue': '#00d4ff',
        'neon-purple': '#9d00ff',
        'neon-green': '#00ff88',
        'neon-orange': '#ff6b00',
        'dark-bg': '#0a0a0a',
        'card-bg': '#1a1a1a',
        'border': '#333',
      },
      backgroundColor: {
        'card-bg': '#1a1a1a',
        'dark-bg': '#0a0a0a',
      },
      borderColor: {
        'border': '#333',
      },
      animation: {
        'glow': 'glow 2s ease-in-out infinite alternate',
        'slideIn': 'slideIn 0.8s ease-out',
        'float': 'float 3s ease-in-out infinite',
        'pulse': 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        glow: {
          '0%': { textShadow: '0 0 30px rgba(0, 212, 255, 0.5)' },
          '100%': { textShadow: '0 0 50px rgba(0, 212, 255, 0.8)' },
        },
        slideIn: {
          '0%': { transform: 'translateY(50px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        pulse: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.5' },
        },
      },
    },
  },
  plugins: [],
}