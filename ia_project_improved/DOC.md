# Documentation technique

## Description
foot

## Modules
- api
- tts
- memory
- auto_mod_8655
- auto_mod_6673

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
- auto_mod_8655/
- auto_mod_6673/

## Endpoints/API
### api
- Endpoint : /api/api
- Méthode : POST
- Payload : {'data': ...}
- Réponse : {'result': ...}
### tts
- Endpoint : /api/tts
- Méthode : POST
- Payload : {'data': ...}
- Réponse : {'result': ...}
### memory
- Endpoint : /api/memory
- Méthode : POST
- Payload : {'data': ...}
- Réponse : {'result': ...}
### auto_mod_8655
- Endpoint : /api/auto_mod_8655
- Méthode : POST
- Payload : {'data': ...}
- Réponse : {'result': ...}
### auto_mod_6673
- Endpoint : /api/auto_mod_6673
- Méthode : POST
- Payload : {'data': ...}
- Réponse : {'result': ...}

## Dépendances (Mermaid)
```mermaid
graph TD
    api --> tts
    tts --> memory
    memory --> auto_mod_8655
    auto_mod_8655 --> auto_mod_6673
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