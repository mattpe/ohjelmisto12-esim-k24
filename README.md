# Ohjelmisto 1 ja 2 esimerkit

## Kansiot

- moduulikohtaiset esimerkit omissa kansioisan
- `/extra`: python-moduuliesimerkit (koodin jakaminen eri tiedostoihin)

## Client-server-arkkitehtuuri

```mermaid
graph TD

subgraph Client
   A[HTML/CSS/JS user Interface] <-- Event & DOM manipulation --> B
   B[JS client-side Logic] --> C[Request to Server]
end

subgraph Server
   D <-- SQL --> E[(Database)]
   D --> F[Response to Client]
end

C -- HTTP --> D[Server-side Logic]
F -- HTTP --> B
```

---

Sekvenssikaavio

```mermaid
sequenceDiagram
    participant browser
    participant server as server-side app (flask)
    participant db as database

    browser->>server: GET https://app.example.com/
    activate server
    server-->>browser: (200 OK) HTML document
    deactivate server

    browser->>server: GET https://app.example.com/app.js
    activate server
    server-->>browser: the JavaScript file
    deactivate server

    activate browser
    Note right of browser: The browser starts executing the JS code that fetches some data from the server

    browser->>server: GET https://app.example.com/resource/endpoint
    deactivate browser
    activate server
    server->>db: SQL query
    activate db
    db-->>server: result set
    deactivate db
    server-->>browser: [{ "content": "Hello world!", "date": "2023-1-1" }, ... ]
    deactivate server

    Note right of browser: The browser executes the callback function that renders the notes

```
