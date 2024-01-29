Questo archivio contiene 5 programmi scritti in Python e trattano di fattorizzazione e codifica.



NB: La licenza attribuita a questi programmi è riferita solo all’algoritmo GC57 e non al programma in sé. Questo algoritmo utilizza una particolare sequenza che gli permette di fattorizzare semiprimi molto grandi a tempo zero. I programmi sono più che altro dimostrativi, anche se possono comunque essere usati a difesa dei nostri dati, ma non sono il principale obbiettivo di questo archivio.
Quello che ritengo più importante è la capacità di questo algoritmo a utilizzare chiavi mai utilizzate prima, perché troppo complesse e grandi, per creare una nuovo codice di codifica basato sulla velocità di fattorizzazione ad esso attribuito

Il programma CassaCriptata esegue una codifica su file di testo e utilizza un sistema di scostamento randomizzato utilizzando la chiave dell’algoritmo GC57. E’ un programma molto semplice e la sua caratteristica è quella di prelevare i dati della chiave e degli spostamenti randomizzati da una chiavetta USB esterna.

Il programma CassaCriptata2 è in linea con il programma CassaCriptata con la differenza che utilizza l’algoritmo FERNET  per criptare qualsiasi file gli si sottoponga, e crea un database che verrà poi criptato con il GC57.  Anche in questo caso i dati di codifica e le chiavi si troveranno su una USB.  
A questo programma viene abbinato un programma  attrezzi_cc2 che mi permette di ricodificare tutto l’archivio e anche il database con altre chiavi

Il programma ChatCriptata utilizza la chiave GC57 e ha al suo interno la creazione di chiavi che vengono utilizzate da due computer collegati sulla stessa rete. Lo scambio di chiavi può avvenire in svariati modi e questo permette di avere una connessione sempre aggiornata a nuove chiavi di codifica.. Come nei precedenti programmi i dati delle chiavi si troveranno su USB

Il programma TestCampo crea le chiavi per i due programmi CassaCriptata e CassaCriptata2, e  memorizza i dati sulla chiavetta USB. Nel caso di sostituzione o ricodifica dei dati, nel programma CassaCriptata2,  TestCampo dispone di un salvataggio a parte che crea una nuova chiave in un file S… il quale viene poi utilizzato da attrezzi_cc2 per modificare la codifica sostituendo la chiave vecchia con quella nuova

Questa è una panoramica generica sui programmi caricati ma se avete bisogno di ulteriori chiarimenti potete scrivere in discussione e non mancherò di rispondere.

Inoltre su youtube, a questi indirizzi, troverete due video inerenti a questi programmi, che probabilmente non saranno aggiornati con le versioni caricate qui, ma che vi daranno una idea di come si usano, e inoltre verrà mostrato il funzionamento dell’algoritmo GC57      https://youtu.be/s5Roi4QYOOs   https://youtu.be/Ak5GR7qtKM8      
