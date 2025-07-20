# API Documentation - demo-app-ia-complete-v4

## Vue d'ensemble

Cette documentation décrit l'API de demo-app-ia-complete-v4.

## Modules

### main

web - Point d'entrée principal

---

### main

web - API REST avec FastAPI

#### Classes

##### Item

#### Fonctions

##### main

Point d'entrée principal

##### run

Exécute l'application

---

### test_main

Tests pour web

#### Classes

##### TestWeb

Tests pour web

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_root_endpoint()`
- `test_items_endpoint()`
- `test_create_item()`
- `test_main_function()`
- `test_run_function()`
- `test_import()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_root_endpoint

Test de l'endpoint racine

##### test_items_endpoint

Test de l'endpoint items

##### test_create_item

Test de création d'item

##### test_main_function

Test de la fonction main (mocké)

**Paramètres :**

- `mock_uvicorn`

##### test_run_function

Test de la fonction run (mocké)

**Paramètres :**

- `mock_uvicorn`

##### test_import

Test d'import du module principal

---

