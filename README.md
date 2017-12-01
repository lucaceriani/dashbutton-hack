# Dashbutton hack
Script python per rilevare la pressione di un dash button.

## Utilizzo
Il modulo, una volta importato metto a disposizione la classe `dashButton`.

Per inizializzarla è necessario fornire l'[indirizzo MAC](https://it.wikipedia.org/wiki/Indirizzo_MAC)
e la funzione da eseguire che deve riceve come parametro l'oggetto `dashButton`.

Per cominciare a captare le pressioni del dashbutton basta eseguire `<yourButtonObject>.startListening()`
In ogni case è tutto illustrato dall'esempio `example.py`
