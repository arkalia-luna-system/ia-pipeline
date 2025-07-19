#!/bin/bash

# Athalia Advanced Project Generator
# Générateur de projets ultra-performant avec benchmarks automatiques

set -e

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Fonction d'aide
show_help() {
    echo -e "${BLUE}🚀 ATHALIA ADVANCED PROJECT GENERATOR${NC}"
    echo ""
    echo "Usage: ath-generate-advanced [OPTIONS] <IDÉE_PROJET>"
    echo ""
    echo "Options:"
    echo "  -o, --output DIR     Dossier de sortie (défaut: ./generated_project)"
    echo "  -d, --dry-run        Mode simulation (pas de fichiers créés)"
    echo "  -i, --industrialize  Industrialiser automatiquement après génération"
    echo "  -b, --benchmark      Générer des benchmarks automatiques"
    echo "  -p, --performance    Tests de performance complets"
    echo "  -s, --security       Audit de sécurité automatique"
    echo "  -t, --type TYPE      Type de projet spécifique (api, web, mobile, ai, data, iot)"
    echo "  -c, --complexity     Complexité (simple, medium, complex)"
    echo "  -h, --help           Afficher cette aide"
    echo ""
    echo "Types de projets supportés:"
    echo "  • API REST avec sécurité avancée"
    echo "  • Application web progressive (PWA)"
    echo "  • Application mobile cross-platform"
    echo "  • Système d'IA avec ML"
    echo "  • Dashboard analytics temps réel"
    echo "  • Système IoT avec capteurs"
    echo "  • Plateforme e-commerce complète"
    echo "  • Système de gestion d'entreprise"
    echo "  • Jeu multijoueur en temps réel"
    echo "  • Bot IA conversationnel"
    echo ""
    echo "Exemples:"
    echo "  ath-generate-advanced 'API REST sécurisée avec JWT et rate limiting' -t api -s"
    echo "  ath-generate-advanced 'Dashboard analytics temps réel' -t web -b -p"
    echo "  ath-generate-advanced 'App mobile de fitness avec IA' -t mobile -i"
}

# Variables par défaut
OUTPUT_DIR="./generated_project"
DRY_RUN=false
INDUSTRIALIZE=false
BENCHMARK=false
PERFORMANCE=false
SECURITY=false
PROJECT_TYPE="auto"
COMPLEXITY="medium"
PROJECT_IDEA=""

# Parsing des arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -d|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -i|--industrialize)
            INDUSTRIALIZE=true
            shift
            ;;
        -b|--benchmark)
            BENCHMARK=true
            shift
            ;;
        -p|--performance)
            PERFORMANCE=true
            shift
            ;;
        -s|--security)
            SECURITY=true
            shift
            ;;
        -t|--type)
            PROJECT_TYPE="$2"
            shift 2
            ;;
        -c|--complexity)
            COMPLEXITY="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}❌ Option inconnue: $1${NC}"
            show_help
            exit 1
            ;;
        *)
            PROJECT_IDEA="$1"
            shift
            ;;
    esac
done

# Vérification des arguments
if [[ -z "$PROJECT_IDEA" ]]; then
    echo -e "${RED}❌ Erreur: Vous devez spécifier une idée de projet${NC}"
    echo ""
    show_help
    exit 1
fi

# Affichage du header
echo -e "${BLUE}🚀============================================================🚀${NC}"
echo -e "${BLUE}🌟 ATHALIA ADVANCED PROJECT GENERATOR - Création ULTRA-PERFORMANTE${NC}"
echo -e "${BLUE}🌟 Génération intelligente avec benchmarks et tests automatiques${NC}"
echo -e "${BLUE}🚀============================================================🚀${NC}"
echo ""

echo -e "${CYAN}📋 Idée de projet:${NC} $PROJECT_IDEA"
echo -e "${CYAN}📁 Dossier de sortie:${NC} $OUTPUT_DIR"
echo -e "${CYAN}🔍 Mode simulation:${NC} $([ "$DRY_RUN" = true ] && echo "Oui" || echo "Non")"
echo -e "${CYAN}🏭 Industrialisation:${NC} $([ "$INDUSTRIALIZE" = true ] && echo "Oui" || echo "Non")"
echo -e "${CYAN}📊 Benchmarks:${NC} $([ "$BENCHMARK" = true ] && echo "Oui" || echo "Non")"
echo -e "${CYAN}⚡ Tests performance:${NC} $([ "$PERFORMANCE" = true ] && echo "Oui" || echo "Non")"
echo -e "${CYAN}🔒 Audit sécurité:${NC} $([ "$SECURITY" = true ] && echo "Oui" || echo "Non")"
echo -e "${CYAN}🏷️ Type projet:${NC} $PROJECT_TYPE"
echo -e "${CYAN}📈 Complexité:${NC} $COMPLEXITY"
echo ""

# Vérification de l'environnement
echo -e "${YELLOW}🔍 Vérification de l'environnement avancé...${NC}"

# Vérifier que Python est disponible
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 n'est pas installé${NC}"
    exit 1
fi

# Vérifier que le module athalia_core est disponible
if ! python3 -c "import athalia_core" &> /dev/null; then
    echo -e "${RED}❌ Module athalia_core non disponible${NC}"
    echo -e "${YELLOW}💡 Assurez-vous d'être dans le répertoire racine d'Athalia${NC}"
    exit 1
fi

# Vérifier les outils de benchmark
if [[ "$BENCHMARK" = true ]]; then
    if ! command -v pytest &> /dev/null; then
        echo -e "${YELLOW}⚠️  pytest non installé - installation automatique...${NC}"
        pip3 install pytest pytest-benchmark
    fi
fi

echo -e "${GREEN}✅ Environnement vérifié${NC}"
echo ""

# Génération du projet avec options avancées
echo -e "${PURPLE}🤖 Génération du projet avec IA robuste et options avancées...${NC}"

# Construire la commande avec options avancées
CMD="python3 -m athalia_core.cli generate \"$PROJECT_IDEA\" --output \"$OUTPUT_DIR\""

if [[ "$DRY_RUN" = true ]]; then
    CMD="$CMD --dry-run"
fi

if [[ "$PROJECT_TYPE" != "auto" ]]; then
    CMD="$CMD --type $PROJECT_TYPE"
fi

if [[ "$COMPLEXITY" != "medium" ]]; then
    CMD="$CMD --complexity $COMPLEXITY"
fi

# Exécuter la génération
if eval "$CMD"; then
    echo -e "${GREEN}✅ Projet généré avec succès !${NC}"
else
    echo -e "${RED}❌ Erreur lors de la génération${NC}"
    exit 1
fi

echo ""

# Industrialisation automatique si demandée
if [[ "$INDUSTRIALIZE" = true && "$DRY_RUN" = false ]]; then
    echo -e "${PURPLE}🏭 Lancement de l'industrialisation automatique...${NC}"
    
    if python3 athalia_unified.py "$OUTPUT_DIR" --action complete; then
        echo -e "${GREEN}✅ Industrialisation terminée !${NC}"
    else
        echo -e "${YELLOW}⚠️  Industrialisation terminée avec des avertissements${NC}"
    fi
    
    echo ""
fi

# Tests de performance si demandés
if [[ "$PERFORMANCE" = true && "$DRY_RUN" = false ]]; then
    echo -e "${PURPLE}⚡ Lancement des tests de performance...${NC}"
    
    cd "$OUTPUT_DIR"
    
    # Tests de performance avec pytest-benchmark
    if command -v pytest &> /dev/null; then
        if python3 -m pytest --benchmark-only --benchmark-sort=mean 2>/dev/null; then
            echo -e "${GREEN}✅ Tests de performance terminés !${NC}"
        else
            echo -e "${YELLOW}⚠️  Tests de performance terminés avec des avertissements${NC}"
        fi
    fi
    
    cd - > /dev/null
    echo ""
fi

# Audit de sécurité si demandé
if [[ "$SECURITY" = true && "$DRY_RUN" = false ]]; then
    echo -e "${PURPLE}🔒 Lancement de l'audit de sécurité...${NC}"
    
    if python3 athalia_unified.py "$OUTPUT_DIR" --action security-audit; then
        echo -e "${GREEN}✅ Audit de sécurité terminé !${NC}"
    else
        echo -e "${YELLOW}⚠️  Audit de sécurité terminé avec des avertissements${NC}"
    fi
    
    echo ""
fi

# Benchmarks automatiques si demandés
if [[ "$BENCHMARK" = true && "$DRY_RUN" = false ]]; then
    echo -e "${PURPLE}📊 Génération de benchmarks automatiques...${NC}"
    
    # Créer le script de benchmark
    BENCHMARK_SCRIPT="$OUTPUT_DIR/run_benchmarks.py"
    cat > "$BENCHMARK_SCRIPT" << 'EOF'
#!/usr/bin/env python3
"""
Benchmarks automatiques pour le projet généré
"""
import time
import subprocess
import json
from pathlib import Path
from datetime import datetime

def run_benchmark(name, command, timeout=30):
    """Exécute un benchmark"""
    print(f"🔍 Benchmark: {name}")
    start = time.time()
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout)
        duration = time.time() - start
        return {
            'name': name,
            'duration': duration,
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr
        }
    except subprocess.TimeoutExpired:
        return {
            'name': name,
            'duration': timeout,
            'success': False,
            'output': '',
            'error': 'Timeout'
        }

def main():
    print("🚀 Lancement des benchmarks automatiques...")
    
    benchmarks = [
        ('Import du projet', 'python3 -c "import sys; sys.path.append(\".\"); import main"'),
        ('Tests unitaires', 'python3 -m pytest tests/ -v --tb=short'),
        ('Linting', 'python3 -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'),
        ('Type checking', 'python3 -m mypy . --ignore-missing-imports'),
        ('Documentation', 'python3 -c "import main; help(main)"'),
    ]
    
    results = []
    for name, command in benchmarks:
        result = run_benchmark(name, command)
        results.append(result)
        status = "✅" if result['success'] else "❌"
        print(f"   {status} {name}: {result['duration']:.2f}s")
    
    # Générer le rapport
    report = {
        'timestamp': datetime.now().isoformat(),
        'project_name': Path.cwd().name,
        'benchmarks': results,
        'summary': {
            'total_benchmarks': len(results),
            'successful_benchmarks': sum(1 for r in results if r['success']),
            'total_duration': sum(r['duration'] for r in results),
            'average_duration': sum(r['duration'] for r in results) / len(results) if results else 0
        }
    }
    
    # Sauvegarder le rapport
    with open('benchmark_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 Rapport sauvegardé: benchmark_report.json")
    print(f"📈 Résumé: {report['summary']['successful_benchmarks']}/{report['summary']['total_benchmarks']} benchmarks réussis")

if __name__ == '__main__':
    main()
EOF

    chmod +x "$BENCHMARK_SCRIPT"
    
    # Exécuter les benchmarks
    cd "$OUTPUT_DIR"
    if python3 run_benchmarks.py; then
        echo -e "${GREEN}✅ Benchmarks générés avec succès !${NC}"
    else
        echo -e "${YELLOW}⚠️  Benchmarks terminés avec des avertissements${NC}"
    fi
    cd - > /dev/null
    
    echo ""
fi

# Affichage des résultats
echo -e "${BLUE}📊 RÉSULTATS DE LA GÉNÉRATION AVANCÉE${NC}"
echo -e "${BLUE}========================================${NC}"

if [[ "$DRY_RUN" = false ]]; then
    if [[ -d "$OUTPUT_DIR" ]]; then
        echo -e "${GREEN}📁 Projet créé dans: $OUTPUT_DIR${NC}"
        
        # Lister les fichiers créés
        echo -e "${CYAN}📄 Fichiers générés:${NC}"
        find "$OUTPUT_DIR" -type f \( -name "*.py" -o -name "*.md" -o -name "*.yaml" -o -name "*.json" -o -name "*.txt" \) | while read -r file; do
            echo -e "  • ${file#$OUTPUT_DIR/}"
        done
        
        # Afficher le contenu du README si il existe
        if [[ -f "$OUTPUT_DIR/README.md" ]]; then
            echo ""
            echo -e "${CYAN}📖 README généré:${NC}"
            echo -e "${YELLOW}$(head -20 "$OUTPUT_DIR/README.md")${NC}"
            if [[ $(wc -l < "$OUTPUT_DIR/README.md") -gt 20 ]]; then
                echo -e "${YELLOW}... (voir le fichier complet pour plus de détails)${NC}"
            fi
        fi
        
        # Afficher les rapports générés
        if [[ -f "$OUTPUT_DIR/benchmark_report.json" ]]; then
            echo ""
            echo -e "${CYAN}📊 Rapport de benchmark:${NC}"
            echo -e "${YELLOW}   Fichier: benchmark_report.json${NC}"
        fi
        
        echo ""
        echo -e "${GREEN}🎉 Votre projet ultra-performant est prêt !${NC}"
        echo ""
        echo -e "${BLUE}🚀 PROCHAINES ÉTAPES:${NC}"
        echo -e "  cd $OUTPUT_DIR"
        echo -e "  python3 main.py"
        echo ""
        
        if [[ "$BENCHMARK" = true ]]; then
            echo -e "${BLUE}📊 POUR LANCER LES BENCHMARKS:${NC}"
            echo -e "  cd $OUTPUT_DIR"
            echo -e "  python3 run_benchmarks.py"
            echo ""
        fi
        
        if [[ "$INDUSTRIALIZE" = false ]]; then
            echo -e "${YELLOW}💡 Pour industrialiser le projet:${NC}"
            echo -e "  python3 athalia_unified.py $OUTPUT_DIR --action complete"
        fi
        
    else
        echo -e "${RED}❌ Erreur: Le dossier de sortie n'a pas été créé${NC}"
    fi
else
    echo -e "${GREEN}✅ Simulation terminée avec succès${NC}"
    echo -e "${YELLOW}💡 Pour créer le projet réel, relancez sans --dry-run${NC}"
fi

echo ""
echo -e "${BLUE}🚀============================================================🚀${NC}"
echo -e "${BLUE}🌟 ATHALIA ADVANCED - Votre assistant IA ultra-performant${NC}"
echo -e "${BLUE}🚀============================================================🚀${NC}" 