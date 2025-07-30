#!/bin/bash
# Alias pour le script de fermeture propre d'Athalia

# Alias principal pour la fermeture propre
alias ath-shutdown='./bin/ath-clean-shutdown'

# Alias alternatifs pour la fermeture
alias ath-close='./bin/ath-clean-shutdown'
alias ath-exit='./bin/ath-clean-shutdown'
alias ath-bye='./bin/ath-clean-shutdown'

# Alias pour le démarrage rapide
alias ath-start='./bin/ath-quick-start'
alias ath-quick='./bin/ath-quick-start'
alias ath-wake='./bin/ath-quick-start'

# Alias pour le workflow complet
alias ath-workflow='./bin/ath-workflow-complete'
alias ath-flow='./bin/ath-workflow-complete'
alias ath-cycle='./bin/ath-workflow-complete'

echo "✅ Alias de fermeture et démarrage créés:"
echo "   ath-shutdown  - Fermeture propre complète"
echo "   ath-start     - Démarrage rapide"
echo "   ath-workflow  - Workflow complet"
echo "   ath-close     - Alias fermeture"
echo "   ath-quick     - Alias démarrage"
echo "   ath-flow      - Alias workflow"
echo ""
echo "💡 Workflow simple: ath-start → travail → ath-shutdown"
echo "💡 Workflow complet: ath-workflow full" 