# GameOfLife
Questa è una semplice implementazione del gioco [Conway's Game Of Life](https://playgameoflife.com/) realizzata utilizzando linguaggio di programmazione Python 3.8 e le librerie pygame, tkinter. 

## Motivazioni
Il progetto è stato realizzato per il corso di Human Computer Interaction 2020-2021, appartenente al corso di laurea magistrale in Ingegneria informatica dell'Universita degli Studi di Firenze. Game of Life è stato implementato con una GUI che consente di gestire la simulazione, sfruttando le funzionalità che verranno descritte in seguito. L'implementazione del sorgente si è concentrata sullo sviluppare correttamente le funzionalità, mantenere il codice pulito, garantire la correttezza e la completezza delle funzioni implementate. 

## MVC pattern
Il codice è stato elaborato seguendo una delle migliori pratiche per la programmazione di interfacce utente: Model View Controller pattern. 

## Interfaccia Grafica
<img src="https://github.com/Tiezzi96/GameOfLife/blob/main/Grid.png?raw=true" width="75%" />
<img src="https://github.com/Tiezzi96/GameOfLife/blob/main/GridHistory.png?raw=true" width="75%" />

## Funzionalità sviluppate

### Funzionalità di base
La versione base del progetto prevedeva che fossero implementate:
- Una simulazione visuale del gioco
- Comandi Start/Stop/Clear per gestire l'interfaccia utente
- Comando per gestire il frame rate
- La creazione e la modifica dello stato da parte dell'utente

### Funzionalità extra
Come funzionalità extra sono state implementate:
- La modifica della griglia, consentendo all'utente di sceglierne la dimensione
- La Cell History, cioè una mappa che tenga traccia della storia di ogni cella


