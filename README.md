# Ohjelmisto 1 ja 2 esimerkit

## Kansiot

- moduulikohtaiset esimerkit omissa kansioisan
- `/extra`: python-moduuliesimerkit (koodin jakaminen eri tiedostoihin)

## Client-server-arkkitehtuuri

```mermaid
graph LR

subgraph Client
   A[HTML/CSS/JS user Interface] <-- Event & DOM manipulation --> B
   B[JS client-side Logic] -- HTTP --> C[Request to Server]
end

subgraph Server
   C --> D[Server-side Logic]
   D <-- SQL --> E[(Database)]
   D -- HTTP --> F[Response to Client]

end

F --> B
```

---

Sekvenssikaavio

```mermaid
sequenceDiagram
    participant browser
    participant server as server-side app
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

    browser->>server: GET https://app.example.com/endpoint/resource
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
