#!/bin/zsh

echo "🛑 \033[1mArrêt de tous les processus sauf Cursor...\033[0m"

# Fonction pour arrêter les processus par pattern
kill_processes_except_cursor() {
    local patterns=(
        "athalia_core"
        "athalia_unified"
        "python.*athalia"
        "pytest.*athalia"
        "validation_continue"
        "ollama"
        "docker"
        "node"
        "npm"
        "yarn"
        "python.*test"
        "python.*script"
    )
    
    local killed_count=0
    
    for pattern in "${patterns[@]}"; do
        echo "🔍 Recherche de processus: $pattern"
        
        # Trouver les processus correspondants
        local processes=$(ps aux | grep -E "$pattern" | grep -v grep | grep -v "stop-all-except-cursor" | grep -v "cursor" || true)
        
        if [ -n "$processes" ]; then
            echo "$processes" | while read line; do
                local pid=$(echo "$line" | awk '{print $2}')
                local cmd=$(echo "$line" | awk '{for(i=11;i<=NF;i++) printf "%s ", $i; print ""}')
                
                # Vérifier que ce n'est pas Cursor
                if [[ "$cmd" != *"cursor"* ]] && [[ "$cmd" != *"Cursor"* ]]; then
                    if [ -n "$pid" ] && [ "$pid" != "$$" ]; then
                        echo "🔪 Arrêt de PID $pid: $cmd"
                        if kill -TERM "$pid" 2>/dev/null; then
                            echo "✅ Arrêté: PID $pid"
                            killed_count=$((killed_count + 1))
                        else
                            echo "❌ Impossible d'arrêter: PID $pid"
                        fi
                    fi
                else
                    echo "🛡️  PROTÉGÉ (Cursor): PID $pid"
                fi
            done
        fi
    done
    
    return $killed_count
}

# Arrêter les processus
echo "📋 Arrêt des processus en cours..."
killed=$(kill_processes_except_cursor)

# Attendre un peu
echo "⏳ Attente de 3 secondes pour la terminaison propre..."
sleep 3

# Forcer l'arrêt des processus qui n'ont pas répondu
echo "🔨 Forçage de l'arrêt des processus récalcitrants..."
pkill -f "athalia_core" 2>/dev/null || true
pkill -f "python.*athalia" 2>/dev/null || true
pkill -f "validation_continue" 2>/dev/null || true

echo "✅ Arrêt terminé !"
echo "📊 Processus restants:"
ps aux | grep -E "(athalia|python.*test|validation)" | grep -v grep | grep -v "stop-all-except-cursor" || echo "Aucun processus Athalia restant"

echo "🎯 Cursor reste actif et protégé !" 