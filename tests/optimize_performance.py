#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'optimisation des performances des tests
Version: 1.0
Auteur: Athalia Team
"""

import os
import sys
import time
import subprocess
from pathlib import Path
from typing import Dict, List

# Standard library imports
import argparse
import tempfile

# Third party imports
try:
    import pytest
except ImportError:
    pytest = None


class TestPerformanceOptimizer:
    """Optimiseur de performances des tests"""
    
    def __init__(self, test_dir: str = "tests"):
        self.test_dir = Path(test_dir)
        self.results = {}
        self.slow_tests = []
        self.fast_tests = []
        
    def analyze_test_performance(self) -> Dict[str, float]:
        """Analyse les performances de tous les tests
        
        Returns:
            Dict avec les temps d'exécution par test
        """
        print("🔍 Analyse des performances des tests...")
        
        # Exécution avec mesure des durées
        cmd = [
            sys.executable, "-m", "pytest", 
            str(self.test_dir), 
            "--durations=0", 
            "-q", 
            "--tb=no"
        ]
        
        start_time = time.time()
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            total_time = time.time() - start_time
            
            # Parse des résultats
            self._parse_durations(result.stdout)
            
            print(f"✅ Analyse terminée en {total_time:.2f}s")
            return self.results
            
        except subprocess.TimeoutExpired:
            print("⏰ Timeout lors de l'analyse des performances")
            return {}
        except Exception as e:
            print(f"❌ Erreur lors de l'analyse: {e}")
            return {}
    
    def _parse_durations(self, output: str):
        """Parse la sortie de pytest --durations"""
        lines = output.split('\n')
        for line in lines:
            if 'passed' in line and 'failed' in line:
                # Ligne de résumé
                continue
            if 'slowest durations' in line:
                # Section des durées
                continue
            if line.strip() and '::' in line and 'PASSED' in line:
                # Ligne de test avec durée
                parts = line.split('::')
                if len(parts) >= 2:
                    test_name = parts[-1].split(' ')[0]
                    duration = self._extract_duration(line)
                    if duration:
                        self.results[test_name] = duration
    
    def _extract_duration(self, line: str) -> float:
        """Extrait la durée d'une ligne de test"""
        try:
            # Cherche le pattern de durée pytest
            if 'PASSED' in line:
                parts = line.split('PASSED')
                if len(parts) > 1:
                    time_part = parts[1].strip()
                    if time_part.startswith('[') and time_part.endswith(']'):
                        time_str = time_part[1:-1]
                        if 's' in time_str:
                            return float(time_str.replace('s', ''))
        except Exception:
            pass
        return 0.0
    
    def identify_slow_tests(self, threshold: float = 1.0) -> List[str]:
        """Identifie les tests lents
        
        Args:
            threshold: Seuil en secondes pour considérer un test comme lent
            
        Returns:
            Liste des tests lents
        """
        self.slow_tests = [
            test for test, duration in self.results.items()
            if duration > threshold
        ]
        
        print(f"🐌 {len(self.slow_tests)} tests lents identifiés (> {threshold}s)")
        return self.slow_tests
    
    def identify_fast_tests(self, threshold: float = 0.1) -> List[str]:
        """Identifie les tests rapides
        
        Args:
            threshold: Seuil en secondes pour considérer un test comme rapide
            
        Returns:
            Liste des tests rapides
        """
        self.fast_tests = [
            test for test, duration in self.results.items()
            if duration < threshold
        ]
        
        print(f"⚡ {len(self.fast_tests)} tests rapides identifiés (< {threshold}s)")
        return self.fast_tests
    
    def generate_optimization_report(self) -> str:
        """Génère un rapport d'optimisation
        
        Returns:
            Contenu du rapport
        """
        report = []
        report.append("# 📊 RAPPORT D'OPTIMISATION DES PERFORMANCES")
        report.append("")
        report.append(f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Tests analysés:** {len(self.results)}")
        report.append("")
        
        # Statistiques générales
        if self.results:
            durations = list(self.results.values())
            avg_duration = sum(durations) / len(durations)
            max_duration = max(durations)
            min_duration = min(durations)
            
            report.append("## 📈 Statistiques générales")
            report.append(f"- **Durée moyenne:** {avg_duration:.3f}s")
            report.append(f"- **Durée maximale:** {max_duration:.3f}s")
            report.append(f"- **Durée minimale:** {min_duration:.3f}s")
            report.append("")
        
        # Tests lents
        if self.slow_tests:
            report.append("## 🐌 Tests lents (> 1s)")
            for test in sorted(self.slow_tests, key=lambda x: self.results.get(x, 0), reverse=True):
                duration = self.results.get(test, 0)
                report.append(f"- `{test}`: {duration:.3f}s")
            report.append("")
        
        # Tests rapides
        if self.fast_tests:
            report.append("## ⚡ Tests rapides (< 0.1s)")
            for test in sorted(self.fast_tests, key=lambda x: self.results.get(x, 0)):
                duration = self.results.get(test, 0)
                report.append(f"- `{test}`: {duration:.3f}s")
            report.append("")
        
        # Recommandations
        report.append("## 💡 Recommandations d'optimisation")
        report.append("")
        
        if self.slow_tests:
            report.append("### Pour les tests lents:")
            report.append("1. **Ajouter des marqueurs de performance:** `@pytest.mark.slow`")
            report.append("2. **Utiliser des mocks** pour les dépendances externes")
            report.append("3. **Optimiser les setup/teardown** avec `@classmethod`")
            report.append("4. **Paralléliser** les tests indépendants")
            report.append("5. **Mettre en cache** les objets coûteux")
            report.append("")
        
        report.append("### Optimisations générales:")
        report.append("1. **Exécuter les tests rapides en premier**")
        report.append("2. **Utiliser `pytest-xdist` pour la parallélisation**")
        report.append("3. **Configurer des timeouts appropriés**")
        report.append("4. **Réduire les I/O inutiles**")
        report.append("5. **Optimiser les imports**")
        
        return "\n".join(report)
    
    def save_report(self, filename: str = "performance_optimization_report.md"):
        """Sauvegarde le rapport d'optimisation
        
        Args:
            filename: Nom du fichier de rapport
        """
        report = self.generate_optimization_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Rapport sauvegardé: {filename}")
    
    def run_fast_tests_only(self) -> bool:
        """Exécute seulement les tests rapides
        
        Returns:
            True si tous les tests rapides passent
        """
        if not self.fast_tests:
            print("⚠️ Aucun test rapide identifié")
            return False
        
        print(f"⚡ Exécution de {len(self.fast_tests)} tests rapides...")
        
        # Créer un fichier temporaire avec les tests rapides
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("import pytest\n\n")
            for test in self.fast_tests:
                f.write(f"pytest.main(['{test}'])\n")
            temp_file = f.name
        
        try:
            result = subprocess.run([sys.executable, temp_file], capture_output=True, text=True)
            success = result.returncode == 0
            
            if success:
                print("✅ Tous les tests rapides ont réussi")
            else:
                print("❌ Certains tests rapides ont échoué")
                print(result.stdout)
                print(result.stderr)
            
            return success
            
        finally:
            os.unlink(temp_file)


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description="Optimiseur de performances des tests")
    parser.add_argument("--test-dir", default="tests", help="Répertoire des tests")
    parser.add_argument("--threshold", type=float, default=1.0, help="Seuil pour les tests lents (s)")
    parser.add_argument("--report", default="performance_optimization_report.md", help="Fichier de rapport")
    parser.add_argument("--fast-only", action="store_true", help="Exécuter seulement les tests rapides")
    
    args = parser.parse_args()
    
    optimizer = TestPerformanceOptimizer(args.test_dir)
    
    # Analyse des performances
    optimizer.analyze_test_performance()
    
    # Identification des tests
    optimizer.identify_slow_tests(args.threshold)
    optimizer.identify_fast_tests(0.1)
    
    # Génération du rapport
    optimizer.save_report(args.report)
    
    # Exécution des tests rapides si demandé
    if args.fast_only:
        optimizer.run_fast_tests_only()


if __name__ == "__main__":
    main() 