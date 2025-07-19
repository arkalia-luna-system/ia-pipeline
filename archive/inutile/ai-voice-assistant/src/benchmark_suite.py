#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite de benchmarks pour l'assistant vocal multilingue
Tests de performance, charge, et robustesse
"""

import asyncio
import time
import json
import statistics
from typing import Dict, List, Any
from pathlib import Path
import threading
from concurrent.futures import ThreadPoolExecutor
import psutil
import gc

from voice_assistant import VoiceAssistantInterface, MultilingualVoiceAssistant

class BenchmarkSuite:
    """Suite complète de benchmarks pour l'assistant vocal"""
    
    def __init__(self):
        self.results = {}
        self.interface = None
        self.test_data = self._generate_test_data()
    
    def _generate_test_data(self) -> Dict[str, Any]:
        """Génère des données de test"""
        return {
            'audio_samples': {
                'short': b"short_audio_sample",
                'medium': b"medium_audio_sample" * 10,
                'long': b"long_audio_sample" * 50
            },
            'languages': ['fr-FR', 'en-US', 'es-ES', 'de-DE', 'it-IT', 'pt-BR', 'ja-JP', 'zh-CN'],
            'conversation_flows': [
                ['greeting', 'weather', 'time', 'help'],
                ['help', 'greeting', 'weather'],
                ['time', 'greeting', 'help']
            ]
        }
    
    async def run_all_benchmarks(self) -> Dict[str, Any]:
        """Exécute tous les benchmarks"""
        print("🚀 Démarrage de la suite de benchmarks complète...")
        print("=" * 60)
        
        # Initialisation
        self.interface = VoiceAssistantInterface()
        
        # Benchmarks séquentiels
        await self._benchmark_initialization()
        await self._benchmark_single_requests()
        await self._benchmark_multilingual_support()
        await self._benchmark_conversation_flows()
        
        # Benchmarks de charge
        await self._benchmark_concurrent_requests()
        await self._benchmark_memory_usage()
        await self._benchmark_stress_test()
        
        # Benchmarks de robustesse
        await self._benchmark_error_handling()
        await self._benchmark_recovery()
        
        # Nettoyage
        if self.interface:
            self.interface.assistant.cleanup()
        
        # Génération du rapport final
        final_report = self._generate_final_report()
        
        print("\n" + "=" * 60)
        print("🎉 SUITE DE BENCHMARKS TERMINÉE")
        print("=" * 60)
        
        return final_report
    
    async def _benchmark_initialization(self):
        """Benchmark de l'initialisation"""
        print("\n🔧 Benchmark d'initialisation...")
        
        start_time = time.time()
        interface = VoiceAssistantInterface()
        init_time = time.time() - start_time
        
        self.results['initialization'] = {
            'time': init_time,
            'memory_mb': psutil.Process().memory_info().rss / 1024 / 1024,
            'status': 'success'
        }
        
        print(f"   ✅ Temps d'initialisation: {init_time:.3f}s")
        print(f"   📊 Mémoire utilisée: {self.results['initialization']['memory_mb']:.1f} MB")
        
        interface.assistant.cleanup()
    
    async def _benchmark_single_requests(self):
        """Benchmark des requêtes individuelles"""
        print("\n🎤 Benchmark des requêtes individuelles...")
        
        interface = VoiceAssistantInterface()
        session_id = await interface.start_session("benchmark_user", "fr-FR")
        
        response_times = []
        success_count = 0
        total_requests = 10
        
        for i in range(total_requests):
            start_time = time.time()
            try:
                result = await interface.process_input(session_id, self.test_data['audio_samples']['medium'])
                response_time = time.time() - start_time
                response_times.append(response_time)
                success_count += 1
                
                if i < 3:  # Afficher les 3 premiers résultats
                    print(f"   Requête {i+1}: {response_time:.3f}s - {result['output_text'][:30]}...")
                    
            except Exception as e:
                print(f"   ❌ Erreur requête {i+1}: {e}")
        
        await interface.stop_session(session_id)
        interface.assistant.cleanup()
        
        self.results['single_requests'] = {
            'total_requests': total_requests,
            'successful_requests': success_count,
            'success_rate': (success_count / total_requests) * 100,
            'response_times': response_times,
            'average_response_time': statistics.mean(response_times) if response_times else 0,
            'min_response_time': min(response_times) if response_times else 0,
            'max_response_time': max(response_times) if response_times else 0,
            'std_deviation': statistics.stdev(response_times) if len(response_times) > 1 else 0
        }
        
        print(f"   📊 Succès: {success_count}/{total_requests} ({self.results['single_requests']['success_rate']:.1f}%)")
        print(f"   ⏱️  Temps moyen: {self.results['single_requests']['average_response_time']:.3f}s")
        print(f"   📈 Écart-type: {self.results['single_requests']['std_deviation']:.3f}s")
    
    async def _benchmark_multilingual_support(self):
        """Benchmark du support multilingue"""
        print("\n🌍 Benchmark du support multilingue...")
        
        interface = VoiceAssistantInterface()
        language_results = {}
        
        for language in self.test_data['languages']:
            start_time = time.time()
            session_id = await interface.start_session(f"user_{language}", language)
            session_time = time.time() - start_time
            
            # Test de traitement
            process_start = time.time()
            result = await interface.process_input(session_id, self.test_data['audio_samples']['short'])
            process_time = time.time() - process_start
            
            await interface.stop_session(session_id)
            
            language_results[language] = {
                'session_creation_time': session_time,
                'processing_time': process_time,
                'detected_language': result['language'],
                'confidence': result['confidence']
            }
            
            print(f"   {language}: {process_time:.3f}s (confiance: {result['confidence']:.2f})")
        
        interface.assistant.cleanup()
        
        self.results['multilingual_support'] = {
            'languages_tested': len(self.test_data['languages']),
            'language_results': language_results,
            'average_session_creation': statistics.mean([r['session_creation_time'] for r in language_results.values()]),
            'average_processing_time': statistics.mean([r['processing_time'] for r in language_results.values()]),
            'average_confidence': statistics.mean([r['confidence'] for r in language_results.values()])
        }
        
        print(f"   📊 Temps moyen de traitement: {self.results['multilingual_support']['average_processing_time']:.3f}s")
        print(f"   📈 Confiance moyenne: {self.results['multilingual_support']['average_confidence']:.2f}")
    
    async def _benchmark_conversation_flows(self):
        """Benchmark des flux de conversation"""
        print("\n💬 Benchmark des flux de conversation...")
        
        interface = VoiceAssistantInterface()
        flow_results = []
        
        for i, flow in enumerate(self.test_data['conversation_flows']):
            session_id = await interface.start_session(f"flow_user_{i}", "fr-FR")
            flow_times = []
            flow_success = True
            
            for step in flow:
                start_time = time.time()
                try:
                    result = await interface.process_input(session_id, self.test_data['audio_samples']['short'])
                    step_time = time.time() - start_time
                    flow_times.append(step_time)
                except Exception as e:
                    flow_success = False
                    print(f"   ❌ Erreur dans le flux {i+1}, étape {step}: {e}")
                    break
            
            await interface.stop_session(session_id)
            
            flow_results.append({
                'flow_id': i + 1,
                'steps': len(flow),
                'success': flow_success,
                'total_time': sum(flow_times),
                'average_step_time': statistics.mean(flow_times) if flow_times else 0,
                'step_times': flow_times
            })
            
            print(f"   Flux {i+1}: {len(flow)} étapes, {flow_results[-1]['total_time']:.3f}s")
        
        interface.assistant.cleanup()
        
        self.results['conversation_flows'] = {
            'flows_tested': len(flow_results),
            'successful_flows': sum(1 for f in flow_results if f['success']),
            'flow_results': flow_results,
            'average_flow_time': statistics.mean([f['total_time'] for f in flow_results if f['success']]),
            'average_step_time': statistics.mean([f['average_step_time'] for f in flow_results if f['success']])
        }
        
        print(f"   📊 Flux réussis: {self.results['conversation_flows']['successful_flows']}/{len(flow_results)}")
        print(f"   ⏱️  Temps moyen par flux: {self.results['conversation_flows']['average_flow_time']:.3f}s")
    
    async def _benchmark_concurrent_requests(self):
        """Benchmark des requêtes concurrentes"""
        print("\n⚡ Benchmark des requêtes concurrentes...")
        
        interface = VoiceAssistantInterface()
        session_ids = []
        
        # Créer plusieurs sessions
        for i in range(5):
            session_id = await interface.start_session(f"concurrent_user_{i}", "fr-FR")
            session_ids.append(session_id)
        
        # Test de concurrence
        async def process_concurrent_request(session_id: str, request_id: int):
            start_time = time.time()
            try:
                result = await interface.process_input(session_id, self.test_data['audio_samples']['short'])
                return {
                    'request_id': request_id,
                    'session_id': session_id,
                    'success': True,
                    'response_time': time.time() - start_time,
                    'output_length': len(result['output_text'])
                }
            except Exception as e:
                return {
                    'request_id': request_id,
                    'session_id': session_id,
                    'success': False,
                    'error': str(e),
                    'response_time': time.time() - start_time
                }
        
        # Exécuter 20 requêtes concurrentes
        tasks = []
        for i in range(20):
            session_id = session_ids[i % len(session_ids)]
            task = process_concurrent_request(session_id, i)
            tasks.append(task)
        
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time
        
        # Nettoyer les sessions
        for session_id in session_ids:
            await interface.stop_session(session_id)
        
        interface.assistant.cleanup()
        
        successful_requests = [r for r in results if r['success']]
        
        self.results['concurrent_requests'] = {
            'total_requests': len(results),
            'successful_requests': len(successful_requests),
            'success_rate': (len(successful_requests) / len(results)) * 100,
            'total_time': total_time,
            'throughput': len(results) / total_time,
            'average_response_time': statistics.mean([r['response_time'] for r in successful_requests]) if successful_requests else 0,
            'results': results
        }
        
        print(f"   📊 Requêtes réussies: {len(successful_requests)}/{len(results)} ({self.results['concurrent_requests']['success_rate']:.1f}%)")
        print(f"   ⚡ Débit: {self.results['concurrent_requests']['throughput']:.1f} req/s")
        print(f"   ⏱️  Temps moyen: {self.results['concurrent_requests']['average_response_time']:.3f}s")
    
    async def _benchmark_memory_usage(self):
        """Benchmark de l'utilisation mémoire"""
        print("\n💾 Benchmark de l'utilisation mémoire...")
        
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024
        
        interface = VoiceAssistantInterface()
        
        # Créer plusieurs sessions pour tester la mémoire
        session_ids = []
        memory_samples = []
        
        for i in range(10):
            session_id = await interface.start_session(f"memory_user_{i}", "fr-FR")
            session_ids.append(session_id)
            
            # Mesurer la mémoire après chaque session
            current_memory = process.memory_info().rss / 1024 / 1024
            memory_samples.append(current_memory)
            
            # Traiter quelques requêtes
            for j in range(3):
                await interface.process_input(session_id, self.test_data['audio_samples']['short'])
        
        # Nettoyer
        for session_id in session_ids:
            await interface.stop_session(session_id)
        
        interface.assistant.cleanup()
        
        final_memory = process.memory_info().rss / 1024 / 1024
        
        self.results['memory_usage'] = {
            'initial_memory_mb': initial_memory,
            'final_memory_mb': final_memory,
            'memory_increase_mb': final_memory - initial_memory,
            'memory_samples': memory_samples,
            'peak_memory_mb': max(memory_samples),
            'average_memory_mb': statistics.mean(memory_samples)
        }
        
        print(f"   📊 Mémoire initiale: {initial_memory:.1f} MB")
        print(f"   📈 Mémoire finale: {final_memory:.1f} MB")
        print(f"   📊 Pic mémoire: {self.results['memory_usage']['peak_memory_mb']:.1f} MB")
        print(f"   📊 Augmentation: {self.results['memory_usage']['memory_increase_mb']:.1f} MB")
    
    async def _benchmark_stress_test(self):
        """Test de stress"""
        print("\n🔥 Test de stress...")
        
        interface = VoiceAssistantInterface()
        stress_results = []
        
        # Test avec beaucoup de sessions et requêtes
        session_ids = []
        
        # Créer 20 sessions
        for i in range(20):
            session_id = await interface.start_session(f"stress_user_{i}", "fr-FR")
            session_ids.append(session_id)
        
        # Traiter 100 requêtes réparties sur les sessions
        start_time = time.time()
        success_count = 0
        
        for i in range(100):
            session_id = session_ids[i % len(session_ids)]
            try:
                result = await interface.process_input(session_id, self.test_data['audio_samples']['short'])
                success_count += 1
                
                if i % 20 == 0:  # Rapport intermédiaire
                    elapsed = time.time() - start_time
                    print(f"   Progression: {i+1}/100 ({elapsed:.1f}s)")
                    
            except Exception as e:
                print(f"   ❌ Erreur requête {i+1}: {e}")
        
        total_time = time.time() - start_time
        
        # Nettoyer
        for session_id in session_ids:
            await interface.stop_session(session_id)
        
        interface.assistant.cleanup()
        
        self.results['stress_test'] = {
            'total_requests': 100,
            'successful_requests': success_count,
            'success_rate': (success_count / 100) * 100,
            'total_time': total_time,
            'throughput': 100 / total_time,
            'sessions_used': len(session_ids)
        }
        
        print(f"   📊 Requêtes réussies: {success_count}/100 ({self.results['stress_test']['success_rate']:.1f}%)")
        print(f"   ⚡ Débit: {self.results['stress_test']['throughput']:.1f} req/s")
        print(f"   ⏱️  Temps total: {total_time:.1f}s")
    
    async def _benchmark_error_handling(self):
        """Benchmark de la gestion d'erreurs"""
        print("\n🛡️ Benchmark de la gestion d'erreurs...")
        
        interface = VoiceAssistantInterface()
        error_results = []
        
        # Tests d'erreurs
        error_tests = [
            ("session_invalide", "session_inexistante", b"test"),
            ("audio_vide", "session_valide", b""),
            ("audio_trop_grand", "session_valide", b"x" * 1000000),
            ("session_none", None, b"test"),
            ("audio_none", "session_valide", None)
        ]
        
        session_id = await interface.start_session("error_user", "fr-FR")
        
        for test_name, session, audio_data in error_tests:
            start_time = time.time()
            try:
                if session == "session_valide":
                    test_session = session_id
                else:
                    test_session = session
                
                result = await interface.process_input(test_session, audio_data)
                error_results.append({
                    'test': test_name,
                    'success': True,
                    'response_time': time.time() - start_time,
                    'error': None
                })
                
            except Exception as e:
                error_results.append({
                    'test': test_name,
                    'success': False,
                    'response_time': time.time() - start_time,
                    'error': str(e)
                })
        
        await interface.stop_session(session_id)
        interface.assistant.cleanup()
        
        successful_errors = [r for r in error_results if not r['success']]
        
        self.results['error_handling'] = {
            'tests_performed': len(error_tests),
            'errors_properly_handled': len(successful_errors),
            'error_handling_rate': (len(successful_errors) / len(error_tests)) * 100,
            'average_error_response_time': statistics.mean([r['response_time'] for r in error_results]),
            'error_results': error_results
        }
        
        print(f"   📊 Erreurs gérées: {len(successful_errors)}/{len(error_tests)} ({self.results['error_handling']['error_handling_rate']:.1f}%)")
        print(f"   ⏱️  Temps moyen de gestion d'erreur: {self.results['error_handling']['average_error_response_time']:.3f}s")
    
    async def _benchmark_recovery(self):
        """Benchmark de la récupération"""
        print("\n🔄 Benchmark de la récupération...")
        
        interface = VoiceAssistantInterface()
        recovery_results = []
        
        # Test de récupération après erreur
        session_id = await interface.start_session("recovery_user", "fr-FR")
        
        # Provoquer une erreur
        try:
            await interface.process_input("session_invalide", b"test")
        except:
            pass
        
        # Tester la récupération
        for i in range(5):
            start_time = time.time()
            try:
                result = await interface.process_input(session_id, self.test_data['audio_samples']['short'])
                recovery_results.append({
                    'attempt': i + 1,
                    'success': True,
                    'response_time': time.time() - start_time
                })
            except Exception as e:
                recovery_results.append({
                    'attempt': i + 1,
                    'success': False,
                    'response_time': time.time() - start_time,
                    'error': str(e)
                })
        
        await interface.stop_session(session_id)
        interface.assistant.cleanup()
        
        successful_recoveries = [r for r in recovery_results if r['success']]
        
        self.results['recovery'] = {
            'recovery_attempts': len(recovery_results),
            'successful_recoveries': len(successful_recoveries),
            'recovery_rate': (len(successful_recoveries) / len(recovery_results)) * 100,
            'average_recovery_time': statistics.mean([r['response_time'] for r in successful_recoveries]) if successful_recoveries else 0,
            'recovery_results': recovery_results
        }
        
        print(f"   📊 Récupérations réussies: {len(successful_recoveries)}/{len(recovery_results)} ({self.results['recovery']['recovery_rate']:.1f}%)")
        print(f"   ⏱️  Temps moyen de récupération: {self.results['recovery']['average_recovery_time']:.3f}s")
    
    def _generate_final_report(self) -> Dict[str, Any]:
        """Génère le rapport final des benchmarks"""
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'benchmark_version': '1.0',
            'summary': {
                'total_benchmarks': len(self.results),
                'overall_status': 'completed'
            },
            'detailed_results': self.results,
            'performance_summary': {
                'initialization_time': self.results.get('initialization', {}).get('time', 0),
                'average_response_time': self.results.get('single_requests', {}).get('average_response_time', 0),
                'concurrent_throughput': self.results.get('concurrent_requests', {}).get('throughput', 0),
                'memory_usage_mb': self.results.get('memory_usage', {}).get('peak_memory_mb', 0),
                'stress_test_success_rate': self.results.get('stress_test', {}).get('success_rate', 0),
                'error_handling_rate': self.results.get('error_handling', {}).get('error_handling_rate', 0),
                'recovery_rate': self.results.get('recovery', {}).get('recovery_rate', 0)
            },
            'recommendations': self._generate_recommendations()
        }
        
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """Génère des recommandations basées sur les résultats"""
        recommendations = []
        
        # Analyse des temps de réponse
        avg_response = self.results.get('single_requests', {}).get('average_response_time', 0)
        if avg_response > 1.0:
            recommendations.append("Optimiser les temps de réponse - considérer la mise en cache")
        
        # Analyse de la concurrence
        throughput = self.results.get('concurrent_requests', {}).get('throughput', 0)
        if throughput < 10:
            recommendations.append("Améliorer la gestion de la concurrence - augmenter le pool de threads")
        
        # Analyse de la mémoire
        memory_usage = self.results.get('memory_usage', {}).get('peak_memory_mb', 0)
        if memory_usage > 100:
            recommendations.append("Optimiser l'utilisation mémoire - implémenter le garbage collection")
        
        # Analyse de la robustesse
        error_rate = self.results.get('error_handling', {}).get('error_handling_rate', 0)
        if error_rate < 80:
            recommendations.append("Améliorer la gestion d'erreurs - ajouter plus de validation")
        
        if not recommendations:
            recommendations.append("Performance excellente - système prêt pour la production")
        
        return recommendations
    
    def save_report(self, filename: str = "benchmark_report.json"):
        """Sauvegarde le rapport dans un fichier"""
        report = self._generate_final_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Rapport sauvegardé: {filename}")
        return filename

async def main():
    """Fonction principale pour exécuter les benchmarks"""
    benchmark_suite = BenchmarkSuite()
    report = await benchmark_suite.run_all_benchmarks()
    
    # Afficher le résumé
    print("\n📊 RÉSUMÉ DES PERFORMANCES")
    print("=" * 40)
    summary = report['performance_summary']
    print(f"⏱️  Temps d'initialisation: {summary['initialization_time']:.3f}s")
    print(f"🎤 Temps de réponse moyen: {summary['average_response_time']:.3f}s")
    print(f"⚡ Débit concurrent: {summary['concurrent_throughput']:.1f} req/s")
    print(f"💾 Pic mémoire: {summary['memory_usage_mb']:.1f} MB")
    print(f"🔥 Test de stress: {summary['stress_test_success_rate']:.1f}%")
    print(f"🛡️ Gestion d'erreurs: {summary['error_handling_rate']:.1f}%")
    print(f"🔄 Taux de récupération: {summary['recovery_rate']:.1f}%")
    
    # Afficher les recommandations
    print("\n💡 RECOMMANDATIONS")
    print("=" * 20)
    for rec in report['recommendations']:
        print(f"• {rec}")
    
    # Sauvegarder le rapport
    benchmark_suite.save_report()

if __name__ == "__main__":
    asyncio.run(main()) 