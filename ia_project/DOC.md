# Documentation technique

## Description
Test YAML final

## Modules
- api
- tts
- memory

## Dépendances
- flask
- tts
- memorylib

## Structure
- src/
- tests/
- api/
- prompts/
- README.md
- requirements.txt

## Endpoints/API

### api
- Endpoint : /api/api
- Méthode : POST
- Payload : {"data": "test", "user_id": 1, "mode": "fast"}
- Réponse : {"result": "ok", "details": {"info": "détail"}}

### tts
- Endpoint : /api/tts
- Méthode : POST
- Payload : {"text": "Bonjour", "lang": "fr"}
- Réponse : {"audio": "base64..."}

### memory
- Endpoint : /api/memory
- Méthode : POST
- Payload : {"key": "foo", "value": "bar"}
- Réponse : {"status": "ok"}

---

## Dépendances (Mermaid)
```mermaid
graph TD
    api --> tts
    tts --> memory
```
## Séquence principale (Mermaid)
```mermaid
sequenceDiagram
    participant User
    participant API
    participant Memory
    participant TTS
    User->>API: Requête
    API->>Memory: Lecture/écriture
    API->>TTS: Synthèse
    TTS-->>User: Audio
```