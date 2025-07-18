# Alias Athalia/Arkalia Dev - à sourcer dans votre .bashrc ou .zshrc

# Ouvre un shell IA (continue)
alias ath-chat='continue'

# Nettoie le projet (cache Python, fichiers temporaires, logs)
alias ath-clean='find . \( -name "__pycache__" -o -name ".DS_Store" -o -name "*.log" \) -print0 | xargs -0 rm -rf'

# Menu interactif de prompts IA (debug, UX, audit, test, refactor)
alias ath-dev-boost='bash $(dirname "$BASH_SOURCE")/ath-dev-boost.sh'

# Ouvre Perplexity.ai dans le navigateur
alias ath-perplex='open https://www.perplexity.ai/'

# Lance les tests via Taskfile
alias ath-test='task test'

# Lint le code via Taskfile
alias ath-lint='task lint'

# Build le projet via Taskfile
alias ath-build='task build'

# (À implémenter) Génération rapide de projet/module (script manquant)
# alias ath-new='bash setup/ath-new.sh'

# Lance le prompt contextuel IA (agents/ath_context_prompt.py)
alias ath-smart='python3 $(dirname "$BASH_SOURCE")/../agents/ath_context_prompt.py'