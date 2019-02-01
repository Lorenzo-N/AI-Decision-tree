# AI-Decision-tree
Elaborato per l’esame finale del corso di Intelligenza Artificiale (2018/19)
##Obiettivo
L'obiettivo di questo elaborato è di implementare l'algoritmo per l'apprendimento di alberi di decisione 
utilizzando l'entropia come misura di impurità e come criteri per terminare la ricorsione 
l'errore di classificazione _p_ e il numero massimo di errori _m_.


##Esecuzione test
Per eseguire il programma si devono selezionare le impostazioni desiderate all'interno del file 
**main.py** ed eseguirlo per visualizzare su terminale i risultati dei test richiesti. 
Il programma carica i 3 data sets e prosegue a seconda della **modalità** selezionata con l'istruzione 
`mode = MODE.PRINT_TABLE`:

* `MODE.PRINT_TABLE` (default): genera due tabelle per ogni data set, la prima al variare di _p_ e la seconda di _m_,
 che contengono il valore del parametro, il tempo utilizzato per eseguire l'algoritmo di apprendimento 
 e gli errori su training e test set. \
 Questa modalità stampa i risultati dei test in un formato leggibile, 
 evidenziando in particolar modo tramite la colorazione dell'output le eventuali variazioni dell'errore sul test set
  al variare dei parametri rispetto all'errore senza terminazione anticipata (parametri a 0): 
  grigio se è uguale, blu se è migliore, giallo se è peggiore di meno dell'1\% e rosso se è peggiore di più dell'1\%.

* `MODE.EXPORT_TABLE`: genera due righe di output per data set, la prima al variare di _p_ e la seconda di _m_,
che contengono il valore del parametro e l'errore sul test set secondo il formato a coppie (x, y).\
Questo output è lo stesso che viene generato nella modalità precedente, 
ma con un diverso formato che risulta difficile alla lettura diretta, ma comodo per esportare i dati verso l'esterno.

* `MODE.PRINT_TREE`: stampa l'intero albero di decisione creato insieme al numero di nodi interni e di foglie, 
il tempo necessario per eseguire l'algoritmo di apprendimento e gli errori su training e test set.\
In questa modalità è possibile selezionare quale tra i 3 data set usare e il valore del parametro _p_ 
oppure del parametro _m_ utilizzato per la creazione dell'albero modificando l'istruzione 
`Test.print_tree(plant, m=0)`.


Essendo i dati riordinati in modo casuale, al momento del caricamento è inoltre possibile impostare
 un seed specifico (di default è 1) tramite `random.seed(1)`, in modo da ottenere dei risultati riproducibili.
 
##Citazioni
La classe _TreePrinter_ all'interno del file **DecisionTree.py** contiene alcuni metodi 
ripresi da https://github.com/jml/tree-format, nel quale sono stati implementati per stampare su terminale 
un albero formato da liste di tuple. I metodi sono stati poi riadattati e modificati per stampare 
l'albero decisionale di questo progetto, composto dalle classi Node e Leaf, aggiungendo alcune funzionalità come
la stampa del numero di nodi e di foglie e la stampa del valore dell'attributo _attr_value_ 
lungo gli archi dell'albero per rendere più chiaro l'albero di decisione.
