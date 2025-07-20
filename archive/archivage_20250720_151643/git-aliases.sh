#!/bin/bash

# 🚀 Alias Git pour Athalia - Workflow Professionnel

# === Branches ===
alias gb='git branch'
alias gba='git branch -a'
alias gbd='git branch -d'
alias gbD='git branch -D'
alias gco='git checkout'
alias gcob='git checkout -b'
alias gcom='git checkout main'
alias gcod='git checkout develop'

# === Status et Logs ===
alias gs='git status'
alias gl='git log --oneline'
alias gla='git log --oneline --all --graph'
alias gl10='git log --oneline -10'
alias gl20='git log --oneline -20'

# === Workflow quotidien ===
alias gstart='git checkout develop && git pull origin develop'
alias gfeature='git checkout -b feature/'
alias ghotfix='git checkout -b hotfix/'
alias grelease='git checkout -b release/'

# === Commits ===
alias ga='git add .'
alias gc='git commit -m'
alias gca='git commit --amend'
alias gcan='git commit --amend --no-edit'

# === Push/Pull ===
alias gp='git push'
alias gpu='git push -u origin'
alias gpl='git pull'
alias gplo='git pull origin'

# === Merge et Rebase ===
alias gm='git merge'
alias grb='git rebase'
alias grbi='git rebase -i'

# === Nettoyage ===
alias gclean='git branch --merged | grep -v "\*" | xargs -n 1 git branch -d'
alias gclean-remote='git remote prune origin'

# === Utilitaires ===
alias gdiff='git diff'
alias gstash='git stash'
alias gstashp='git stash pop'
alias greset='git reset --hard HEAD'

# === Workflow Athalia ===
alias ath-start='echo "🚀 Démarrage journée Athalia" && git checkout develop && git pull origin develop && echo "✅ Prêt pour le développement"'
alias ath-feature='echo "🎯 Création feature branch" && git checkout -b feature/'
alias ath-test='echo "🧪 Lancement tests" && pytest tests/ --cov=athalia_core --cov-report=term'
alias ath-commit='echo "💾 Commit avec message conventionnel" && git add . && git commit -m'
alias ath-push='echo "📤 Push feature branch" && git push -u origin'
alias ath-merge='echo "🔄 Retour develop et merge" && git checkout develop && git pull origin develop'

# === Aide ===
alias ath-help='echo "🚀 Workflow Athalia - Commandes utiles:" && echo "  ath-start    : Démarrage journée" && echo "  ath-feature  : Nouvelle feature" && echo "  ath-test     : Lancement tests" && echo "  ath-commit   : Commit conventionnel" && echo "  ath-push     : Push feature" && echo "  ath-merge    : Retour develop"'

# === Configuration Git ===
alias git-config='echo "⚙️ Configuration Git recommandée:" && echo "git config --global user.name \"Ton Nom\"" && echo "git config --global user.email \"ton.email@example.com\"" && echo "git config --global core.editor \"code --wait\"" && echo "git config --global init.defaultBranch main"'

echo "🚀 Alias Git Athalia chargés ! Tape 'ath-help' pour voir les commandes." 