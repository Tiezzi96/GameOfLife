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
- Comandi Play/Stop/Clear per gestire l'interfaccia utente
- Comando per gestire il frame rate
- La creazione e la modifica dello stato da parte dell'utente

### Funzionalità extra
Come funzionalità extra sono state implementate:
- La modifica della griglia, consentendo all'utente di sceglierne la dimensione
- La Cell History, cioè una mappa che tenga traccia della storia di ogni cella

## Download e installazione
Per eseguire il codice è sufficiente effettuare il download del progetto e, una volta scaricato, eseguire il file *main.py*.

## Istruzioni d'Uso
L'interfaccia utente presenta una griglia di dimensione variabile con ai lati i pulsanti per la gestione dello stato:
- **History Grid**: se selezionato mostra sulla griglia la storia delle celle, soddividendole in base al colore. Una cella morta è di colore bianco: appena nata assume un blu chiaro che tende al rosso scuro durante il suo ciclo di vità.
- **Grid Size**: consente di variare le dimensioni della griglia in base alle richieste dell'utente 
- **State**: inizializza lo stato della griglia; è possibile imporstare una figura già pronta o partire dalla griglia vuota e disegnare personalmente un'immagine
- **Play**: avvia l'esecuzione del gioco
- **Clear**: reimposta la griglia al suo stato iniziale che varia a seconda del valore selezionato con **State**
- **Stop**: interrompe l'esecuzione del gioco, abilitando l'utente alla modifica dello stato
- **Frame rate**: consente di impostare manualmente il frame rate del gioco. Di base è impostato ad 1.



