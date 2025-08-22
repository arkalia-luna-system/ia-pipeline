#!/usr/bin/env python3
"""
Système WebSocket temps réel pour Athalia
Interface web moderne avec communication bidirectionnelle
"""

import asyncio
import json
import logging
import os
import webbrowser
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import websockets

logger = logging.getLogger(__name__)


@dataclass
class WebSocketMessage:
    """Structure d'un message WebSocket"""

    type: str
    data: Any
    timestamp: str
    sender: str
    session_id: str


class RealtimeWebSocketSystem:
    """Système WebSocket temps réel avec interface web moderne"""

    def __init__(
        self, project_path: str = ".", host: str = "localhost", port: int = 8765
    ):
        self.project_path = Path(project_path)
        self.websocket_dir = self.project_path / "dashboard" / "websocket"
        self.websocket_dir.mkdir(parents=True, exist_ok=True)
        self.host = host
        self.port = port
        self.clients: set[websockets.WebSocketServerProtocol] = set()
        self.message_history: list[WebSocketMessage] = []
        self.max_history = 100

    def generate_websocket_interface(self) -> str:
        """Génère l'interface web WebSocket"""
        websocket_html = self._get_websocket_template()

        # Créer le fichier WebSocket
        websocket_file = self.websocket_dir / "realtime_websocket.html"
        with open(websocket_file, "w", encoding="utf-8") as f:
            f.write(websocket_html)

        logger.info(f"Interface WebSocket générée: {websocket_file}")
        return str(websocket_file)

    def _get_websocket_template(self) -> str:
        """Retourne le template HTML WebSocket"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Temps Réel - Athalia</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}

        .header {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            font-size: 3em;
            color: #667eea;
            margin-bottom: 10px;
            font-weight: 300;
        }}

        .header p {{
            font-size: 1.2em;
            color: #666;
        }}

        .connection-status {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .status-indicator {{
            display: inline-block;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 10px;
            background: #dc3545;
            animation: pulse 2s infinite;
        }}

        .status-indicator.connected {{
            background: #28a745;
            animation: none;
        }}

        @keyframes pulse {{
            0% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
            100% {{ opacity: 1; }}
        }}

        .main-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }}

        .chat-section, .data-section {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .section-title {{
            font-size: 1.5em;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .chat-messages {{
            height: 400px;
            overflow-y: auto;
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 20px;
            background: #f8f9fa;
        }}

        .message {{
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
        }}

        .message.sent {{
            background: #667eea;
            color: white;
            margin-left: auto;
        }}

        .message.received {{
            background: #e9ecef;
            color: #333;
        }}

        .message-header {{
            font-size: 0.8em;
            margin-bottom: 5px;
            opacity: 0.8;
        }}

        .message-content {{
            word-wrap: break-word;
        }}

        .chat-input {{
            display: flex;
            gap: 10px;
        }}

        .chat-input input {{
            flex: 1;
            padding: 12px 15px;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            font-size: 1em;
            outline: none;
            transition: border-color 0.3s ease;
        }}

        .chat-input input:focus {{
            border-color: #667eea;
        }}

        .chat-input button {{
            padding: 12px 20px;
            border: none;
            border-radius: 25px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s ease;
        }}

        .chat-input button:hover {{
            transform: translateY(-2px);
        }}

        .data-display {{
            height: 400px;
            overflow-y: auto;
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 20px;
            background: #f8f9fa;
            font-family: monospace;
            font-size: 0.9em;
        }}

        .data-item {{
            margin-bottom: 10px;
            padding: 8px;
            background: white;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}

        .data-timestamp {{
            color: #666;
            font-size: 0.8em;
        }}

        .data-content {{
            margin-top: 5px;
            color: #333;
        }}

        .controls {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }}

        .btn-primary:hover {{
            transform: translateY(-2px);
        }}

        .btn-secondary {{
            background: #f8f9fa;
            color: #667eea;
            border: 2px solid #667eea;
        }}

        .btn-secondary:hover {{
            background: #667eea;
            color: white;
        }}

        .stats-container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .stats-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .stat-card {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 15px;
        }}

        .stat-number {{
            font-size: 2.5em;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }}

        .stat-description {{
            color: #666;
            font-size: 0.9em;
        }}

        .footer {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            color: #666;
        }}

        @media (max-width: 768px) {{
            .main-content {{
                grid-template-columns: 1fr;
            }}

            .header h1 {{
                font-size: 2em;
            }}

            .chat-input {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔌 WebSocket Temps Réel Athalia</h1>
            <p>Communication bidirectionnelle en temps réel avec votre système</p>
        </div>

        <div class="connection-status">
            <div class="status-indicator" id="statusIndicator"></div>
            <span id="statusText">Déconnecté</span>
            <button class="btn btn-primary" onclick="connectWebSocket()" id="connectBtn">🔌 Se Connecter</button>
            <button class="btn btn-secondary" onclick="disconnectWebSocket()" id="disconnectBtn" style="display: none;">🔌 Se Déconnecter</button>
        </div>

        <div class="stats-container">
            <h2 class="stats-title">📊 Statistiques Temps Réel</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" id="totalMessages">0</div>
                    <div class="stat-description">Messages Reçus</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="activeConnections">0</div>
                    <div class="stat-description">Connexions Actives</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="dataPackets">0</div>
                    <div class="stat-description">Paquets de Données</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="uptime">00:00:00</div>
                    <div class="stat-description">Temps de Connexion</div>
                </div>
            </div>
        </div>

        <div class="main-content">
            <div class="chat-section">
                <h3 class="section-title">💬 Chat Temps Réel</h3>
                <div class="chat-messages" id="chatMessages">
                    <div class="message received">
                        <div class="message-header">Système - {current_time}</div>
                        <div class="message-content">Bienvenue dans le chat temps réel ! Connectez-vous pour commencer.</div>
                    </div>
                </div>
                <div class="chat-input">
                    <input type="text" id="messageInput" placeholder="Tapez votre message..." onkeypress="handleKeyPress(event)">
                    <button onclick="sendMessage()">📤 Envoyer</button>
                </div>
            </div>

            <div class="data-section">
                <h3 class="section-title">📡 Flux de Données</h3>
                <div class="data-display" id="dataDisplay">
                    <div class="data-item">
                        <div class="data-timestamp">{current_time}</div>
                        <div class="data-content">Système initialisé - En attente de connexion WebSocket</div>
                    </div>
                </div>
                <div class="controls">
                    <button class="btn btn-primary" onclick="requestData()">📊 Demander Données</button>
                    <button class="btn btn-secondary" onclick="clearData()">🗑️ Effacer</button>
                    <button class="btn btn-secondary" onclick="exportData()">💾 Exporter</button>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🕒 Dernière mise à jour: <span id="last-update">{current_time}</span></p>
            <p>🔌 Système WebSocket temps réel généré automatiquement par Athalia</p>
        </div>
    </div>

    <script>
        let websocket = null;
        let isConnected = false;
        let messageCount = 0;
        let dataPacketCount = 0;
        let connectionStartTime = null;
        let uptimeInterval = null;

        // Fonction de connexion WebSocket
        function connectWebSocket() {{
            if (isConnected) return;

            try {{
                websocket = new WebSocket('ws://localhost:8765');

                websocket.onopen = function(event) {{
                    isConnected = true;
                    connectionStartTime = new Date();
                    updateConnectionStatus(true);
                    startUptimeCounter();
                    addMessage('Système', 'Connexion WebSocket établie !', 'received');
                    addDataItem('Connexion WebSocket établie', 'success');
                }};

                websocket.onmessage = function(event) {{
                    try {{
                        const data = JSON.parse(event.data);
                        messageCount++;
                        dataPacketCount++;

                        updateStats();
                        addMessage(data.sender || 'Serveur', data.data || 'Message reçu', 'received');
                        addDataItem(`Données reçues: ${{JSON.stringify(data)}}`, 'data');

                    }} catch (e) {{
                        addMessage('Système', `Erreur de parsing: ${{e.message}}`, 'received');
                    }}
                }};

                websocket.onclose = function(event) {{
                    isConnected = false;
                    updateConnectionStatus(false);
                    stopUptimeCounter();
                    addMessage('Système', 'Connexion WebSocket fermée', 'received');
                    addDataItem('Connexion WebSocket fermée', 'warning');
                }};

                websocket.onerror = function(error) {{
                    addMessage('Système', 'Erreur WebSocket', 'received');
                    addDataItem('Erreur WebSocket', 'error');
                }};

            }} catch (e) {{
                addMessage('Système', `Erreur de connexion: ${{e.message}}`, 'received');
            }}
        }}

        // Fonction de déconnexion WebSocket
        function disconnectWebSocket() {{
            if (websocket && isConnected) {{
                websocket.close();
                isConnected = false;
                updateConnectionStatus(false);
                stopUptimeCounter();
                addMessage('Système', 'Déconnexion manuelle', 'received');
            }}
        }}

        // Fonction de mise à jour du statut de connexion
        function updateConnectionStatus(connected) {{
            const statusIndicator = document.getElementById('statusIndicator');
            const statusText = document.getElementById('statusText');
            const connectBtn = document.getElementById('connectBtn');
            const disconnectBtn = document.getElementById('disconnectBtn');

            if (connected) {{
                statusIndicator.classList.add('connected');
                statusText.textContent = 'Connecté';
                connectBtn.style.display = 'none';
                disconnectBtn.style.display = 'inline-block';
            }} else {{
                statusIndicator.classList.remove('connected');
                statusText.textContent = 'Déconnecté';
                connectBtn.style.display = 'inline-block';
                disconnectBtn.style.display = 'none';
            }}
        }}

        // Fonction d'ajout de message
        function addMessage(sender, content, type) {{
            const chatMessages = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${{type}}`;

            const timestamp = new Date().toLocaleTimeString('fr-FR');
            messageDiv.innerHTML = `
                <div class="message-header">${{sender}} - ${{timestamp}}</div>
                <div class="message-content">${{content}}</div>
            `;

            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }}

        // Fonction d'ajout d'élément de données
        function addDataItem(content, type) {{
            const dataDisplay = document.getElementById('dataDisplay');
            const dataItem = document.createElement('div');
            dataItem.className = 'data-item';

            const timestamp = new Date().toLocaleTimeString('fr-FR');
            dataItem.innerHTML = `
                <div class="data-timestamp">${{timestamp}}</div>
                <div class="data-content">${{content}}</div>
            `;

            dataDisplay.appendChild(dataItem);
            dataDisplay.scrollTop = dataDisplay.scrollHeight;
        }}

        // Fonction d'envoi de message
        function sendMessage() {{
            const messageInput = document.getElementById('messageInput');
            const message = messageInput.value.trim();

            if (message && isConnected) {{
                const data = {{
                    type: 'chat',
                    data: message,
                    timestamp: new Date().toISOString(),
                    sender: 'Utilisateur',
                    session_id: 'web_client'
                }};

                websocket.send(JSON.stringify(data));
                addMessage('Vous', message, 'sent');
                messageInput.value = '';
                messageCount++;
                updateStats();

            }} else if (!isConnected) {{
                addMessage('Système', 'Veuillez d\'abord vous connecter', 'received');
            }}
        }}

        // Fonction de gestion des touches
        function handleKeyPress(event) {{
            if (event.key === 'Enter') {{
                sendMessage();
            }}
        }}

        // Fonction de demande de données
        function requestData() {{
            if (isConnected) {{
                const data = {{
                    type: 'request_data',
                    data: 'request',
                    timestamp: new Date().toISOString(),
                    sender: 'Client',
                    session_id: 'web_client'
                }};

                websocket.send(JSON.stringify(data));
                addDataItem('Demande de données envoyée', 'request');

            }} else {{
                addMessage('Système', 'Veuillez d\'abord vous connecter', 'received');
            }}
        }}

        // Fonction d'effacement des données
        function clearData() {{
            const dataDisplay = document.getElementById('dataDisplay');
            dataDisplay.innerHTML = '';
            addDataItem('Données effacées', 'system');
        }}

        // Fonction d'export des données
        function exportData() {{
            const dataDisplay = document.getElementById('dataDisplay');
            const data = dataDisplay.innerText;

            const blob = new Blob([data], {{ type: 'text/plain' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'websocket_data.txt';
            a.click();
            URL.revokeObjectURL(url);

            addDataItem('Données exportées', 'export');
        }}

        // Fonction de mise à jour des statistiques
        function updateStats() {{
            document.getElementById('totalMessages').textContent = messageCount;
            document.getElementById('dataPackets').textContent = dataPacketCount;
        }}

        // Fonction de démarrage du compteur de temps de connexion
        function startUptimeCounter() {{
            if (uptimeInterval) clearInterval(uptimeInterval);

            uptimeInterval = setInterval(() => {{
                if (connectionStartTime) {{
                    const now = new Date();
                    const diff = now - connectionStartTime;
                    const hours = Math.floor(diff / 3600000);
                    const minutes = Math.floor((diff % 3600000) / 60000);
                    const seconds = Math.floor((diff % 60000) / 1000);

                    document.getElementById('uptime').textContent =
                        `${{hours.toString().padStart(2, '0')}}:${{minutes.toString().padStart(2, '0')}}:${{seconds.toString().padStart(2, '0')}}`;
                }}
            }}, 1000);
        }}

        // Fonction d'arrêt du compteur de temps de connexion
        function stopUptimeCounter() {{
            if (uptimeInterval) {{
                clearInterval(uptimeInterval);
                uptimeInterval = null;
            }}
            document.getElementById('uptime').textContent = '00:00:00';
        }}

        // Mise à jour automatique des statistiques
        setInterval(() => {{
            const now = new Date();
            document.getElementById('last-update').textContent = now.toLocaleString('fr-FR');
        }}, 300000);

        // Animation d'entrée des éléments
        document.addEventListener('DOMContentLoaded', function() {{
            const elements = document.querySelectorAll('.chat-section, .data-section, .stats-container');
            elements.forEach((element, index) => {{
                setTimeout(() => {{
                    element.style.opacity = '0';
                    element.style.transform = 'translateY(20px)';
                    element.style.transition = 'all 0.5s ease';

                    setTimeout(() => {{
                        element.style.opacity = '1';
                        element.style.transform = 'translateY(0)';
                    }}, 100);
                }}, index * 100);
            }});
        }});
    </script>
</body>
</html>"""

    async def handle_client(self, websocket, path):
        """Gère la connexion d'un client WebSocket"""
        self.clients.add(websocket)
        logger.info(f"Nouveau client connecté. Total clients: {len(self.clients)}")

        try:
            async for message in websocket:
                try:
                    data = json.loads(message)
                    logger.info(f"Message reçu: {data}")

                    # Créer un message structuré
                    ws_message = WebSocketMessage(
                        type=data.get("type", "unknown"),
                        data=data.get("data", ""),
                        timestamp=datetime.now().isoformat(),
                        sender=data.get("sender", "unknown"),
                        session_id=data.get("session_id", "unknown"),
                    )

                    # Ajouter à l'historique
                    self.message_history.append(ws_message)
                    if len(self.message_history) > self.max_history:
                        self.message_history.pop(0)

                    # Traiter le message selon son type
                    response = await self._process_message(ws_message)

                    # Envoyer la réponse à tous les clients
                    if response:
                        await self._broadcast_message(response)

                except json.JSONDecodeError as e:
                    logger.error(f"Erreur de parsing JSON: {e}")
                    error_msg = WebSocketMessage(
                        type="error",
                        data="Format JSON invalide",
                        timestamp=datetime.now().isoformat(),
                        sender="system",
                        session_id="system",
                    )
                    await websocket.send(json.dumps(asdict(error_msg)))

        except websockets.exceptions.ConnectionClosed:
            logger.info("Client déconnecté")
        finally:
            self.clients.remove(websocket)
            logger.info(f"Client déconnecté. Total clients: {len(self.clients)}")

    async def _process_message(
        self, message: WebSocketMessage
    ) -> WebSocketMessage | None:
        """Traite un message reçu et retourne une réponse optionnelle"""
        if message.type == "chat":
            # Message de chat - pas de réponse nécessaire
            return None

        elif message.type == "request_data":
            # Demande de données
            response_data = {
                "system_status": "online",
                "active_clients": len(self.clients),
                "message_count": len(self.message_history),
                "uptime": "running",
                "timestamp": datetime.now().isoformat(),
            }

            return WebSocketMessage(
                type="data_response",
                data=response_data,
                timestamp=datetime.now().isoformat(),
                sender="system",
                session_id="system",
            )

        elif message.type == "ping":
            # Ping/Pong pour maintenir la connexion
            return WebSocketMessage(
                type="pong",
                data="pong",
                timestamp=datetime.now().isoformat(),
                sender="system",
                session_id="system",
            )

        else:
            # Message de type inconnu
            return WebSocketMessage(
                type="error",
                data=f"Type de message inconnu: {message.type}",
                timestamp=datetime.now().isoformat(),
                sender="system",
                session_id="system",
            )

    async def _broadcast_message(self, message: WebSocketMessage):
        """Envoie un message à tous les clients connectés"""
        if not self.clients:
            return

        message_json = json.dumps(asdict(message))
        await asyncio.gather(
            *[client.send(message_json) for client in self.clients],
            return_exceptions=True,
        )

    async def start_server(self):
        """Démarre le serveur WebSocket"""
        logger.info(f"Démarrage du serveur WebSocket sur ws://{self.host}:{self.port}")

        async with websockets.serve(self.handle_client, self.host, self.port):
            await asyncio.Future()  # Garde le serveur en vie

    def open_websocket_interface(self) -> None:
        """Ouvre l'interface WebSocket dans le navigateur"""
        websocket_file = self.generate_websocket_interface()
        webbrowser.open(f"file://{os.path.abspath(websocket_file)}")
        logger.info(f"Interface WebSocket ouverte: {websocket_file}")

    def get_websocket_summary(self) -> dict[str, Any]:
        """Retourne un résumé du système WebSocket"""
        return {
            "active_connections": len(self.clients),
            "total_messages": len(self.message_history),
            "max_history": self.max_history,
            "host": self.host,
            "port": self.port,
            "status": "running" if self.clients else "idle",
            "last_updated": datetime.now().isoformat(),
        }


def main():
    """Fonction principale pour test du système WebSocket"""
    import sys

    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = "."

    websocket_system = RealtimeWebSocketSystem(project_path)

    if len(sys.argv) > 2 and sys.argv[2] == "server":
        print("🚀 Démarrage du serveur WebSocket...")
        print("Interface disponible sur: http://localhost:8765")
        print("Appuyez sur Ctrl+C pour arrêter")

        try:
            asyncio.run(websocket_system.start_server())
        except KeyboardInterrupt:
            print("\\n🛑 Serveur WebSocket arrêté")
    else:
        websocket_system.open_websocket_interface()


if __name__ == "__main__":
    main()
