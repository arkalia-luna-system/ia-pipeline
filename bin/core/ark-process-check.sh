#!/bin/zsh

echo "🔍 \033[1mAnalyse des processus en cours...\033[0m"

echo "\n📊 \033[1mTOP 10 CPU :\033[0m"
ps aux | sort -nrk 3 | head -n 10

echo "\n🧠 \033[1mTOP 10 RAM :\033[0m"
ps aux | sort -nrk 4 | head -n 10

echo "\n🐍 \033[1mProcessus Python actifs :\033[0m"
ps aux | grep '[p]ython' || echo "Aucun processus Python"

echo "\n🎯 \033[1mProcessus Athalia spécifiques :\033[0m"
ps aux | grep '[a]thalia_core.main' || echo "Aucun processus Athalia main"
ps aux | grep '[v]alidation_continue' || echo "Aucun processus validation continue"

echo "\n🐳 \033[1mProcessus Docker actifs :\033[0m"
docker ps 2>/dev/null || echo "Docker non actif ou non installé"

echo "\n🧠 \033[1mProcessus Ollama actifs :\033[0m"
ps aux | grep '[o]llama' || echo "Ollama non détecté"

echo "\n🔧 \033[1mPorts TCP écoutés :\033[0m"
lsof -nP -iTCP -sTCP:LISTEN | grep -v 'COMMAND'

echo "\n⚠️ \033[1mTape le PID d'un processus à tuer (ou ENTER pour ignorer) :\033[0m"
read pid_to_kill

if [[ -n "$pid_to_kill" ]]; then
  kill -9 $pid_to_kill && echo "✅ Processus $pid_to_kill tué." || echo "❌ Impossible de tuer $pid_to_kill."
else
  echo "👍 Aucun processus tué."
fi

echo "\n🛑 \033[1mOptions de nettoyage rapide :\033[0m"
echo "1. Tuer tous les processus Athalia main"
echo "2. Tuer tous les processus Python athalia_core"
echo "3. Redémarrer proprement Athalia"
echo "4. Quitter"
echo -n "Choix (1-4) : "
read choix_cleanup

case $choix_cleanup in
  1)
    echo "🔪 Tuage de tous les processus Athalia main..."
    pkill -f "athalia_core.main" && echo "✅ Processus Athalia main tués." || echo "❌ Aucun processus trouvé."
    ;;
  2)
    echo "🔪 Tuage de tous les processus athalia_core..."
    pkill -f "athalia_core" && echo "✅ Processus athalia_core tués." || echo "❌ Aucun processus trouvé."
    ;;
  3)
    echo "🔄 Redémarrage propre d'Athalia..."
    pkill -f "athalia_core.main"
    sleep 2
    echo "✅ Athalia arrêté. Relancez manuellement si nécessaire."
    ;;
  4)
    echo "👋 Au revoir !"
    ;;
  *)
    echo "❌ Choix invalide."
    ;;
esac
