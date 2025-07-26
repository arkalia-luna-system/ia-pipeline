#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 Moniteur de processus Athalia
Surveille et gère les processus athalia_core.main pour éviter les doublons
"""

import psutil
import time
import os
import signal
import logging
from datetime import datetime
from typing import List, Dict, Any

class AthaliaProcessMonitor:
    """Moniteur de processus pour Athalia"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.processes = {}
    
    def find_athalia_processes(self) -> List[Dict[str, Any]]:
        """Trouve tous les processus athalia_core.main"""
        athalia_processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'create_time']):
            try:
                cmdline = proc.info['cmdline']
                if cmdline and 'athalia_core.main' in ' '.join(cmdline):
                    athalia_processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'cmdline': ' '.join(cmdline),
                        'create_time': proc.info['create_time'],
                        'cpu_percent': proc.cpu_percent(),
                        'memory_mb': proc.memory_info().rss / 1024 / 1024
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        return athalia_processes
    
    def kill_duplicate_processes(self, keep_oldest: bool = True) -> int:
        """Tue les processus en double, garde le plus ancien ou le plus récent"""
        processes = self.find_athalia_processes()
        
        if len(processes) <= 1:
            return 0
        
        # Trier par temps de création
        processes.sort(key=lambda x: x['create_time'], reverse=not keep_oldest)
        
        # Garder le premier (plus ancien ou plus récent selon keep_oldest)
        to_kill = processes[1:]
        killed_count = 0
        
        for proc_info in to_kill:
            try:
                proc = psutil.Process(proc_info['pid'])
                proc.terminate()
                time.sleep(0.5)
                
                # Vérifier si le processus est mort
                if proc.is_running():
                    proc.kill()
                
                self.logger.info(f"🔄 Processus {proc_info['pid']} arrêté")
                killed_count += 1
                
            except psutil.NoSuchProcess:
                self.logger.info(f"✅ Processus {proc_info['pid']} déjà arrêté")
                killed_count += 1
            except Exception as e:
                self.logger.error(f"❌ Erreur lors de l'arrêt du processus {proc_info['pid']}: {e}")
        
        return killed_count
    
    def monitor_processes(self, interval: int = 30, max_duration: int = 3600):
        """Surveille les processus en continu"""
        start_time = time.time()
        
        while time.time() - start_time < max_duration:
            processes = self.find_athalia_processes()
            
            if len(processes) > 1:
                self.logger.warning(f"⚠️ {len(processes)} processus athalia_core.main détectés")
                for proc in processes:
                    self.logger.info(f"   PID {proc['pid']}: {proc['cpu_percent']:.1f}% CPU, {proc['memory_mb']:.1f}MB RAM")
                
                killed = self.kill_duplicate_processes()
                if killed > 0:
                    self.logger.info(f"✅ {killed} processus en double arrêtés")
            elif len(processes) == 1:
                proc = processes[0]
                self.logger.info(f"✅ 1 processus actif: PID {proc['pid']} ({proc['cpu_percent']:.1f}% CPU)")
            else:
                self.logger.info("ℹ️ Aucun processus athalia_core.main actif")
            
            time.sleep(interval)
    
    def get_process_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques des processus"""
        processes = self.find_athalia_processes()
        
        if not processes:
            return {
                'count': 0,
                'total_cpu': 0,
                'total_memory': 0,
                'status': 'inactive'
            }
        
        total_cpu = sum(p['cpu_percent'] for p in processes)
        total_memory = sum(p['memory_mb'] for p in processes)
        
        return {
            'count': len(processes),
            'total_cpu': total_cpu,
            'total_memory': total_memory,
            'status': 'active' if len(processes) == 1 else 'duplicate',
            'processes': processes
        }

def main():
    """Fonction principale"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    monitor = AthaliaProcessMonitor()
    
    # Vérifier les processus actuels
    processes = monitor.find_athalia_processes()
    
    if len(processes) > 1:
        print(f"⚠️ {len(processes)} processus athalia_core.main détectés")
        for proc in processes:
            print(f"   PID {proc['pid']}: {proc['cpu_percent']:.1f}% CPU, {proc['memory_mb']:.1f}MB RAM")
        
        response = input("Voulez-vous arrêter les processus en double ? (y/N): ")
        if response.lower() == 'y':
            killed = monitor.kill_duplicate_processes()
            print(f"✅ {killed} processus arrêtés")
    else:
        print("✅ Aucun processus en double détecté")
    
    # Afficher les statistiques
    stats = monitor.get_process_stats()
    print(f"\n📊 Statistiques: {stats['count']} processus, {stats['total_cpu']:.1f}% CPU, {stats['total_memory']:.1f}MB RAM")

if __name__ == "__main__":
    main() 