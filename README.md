# DBAdvanced
Oefeningen van het herexamen van Databases Advanced in augustus 2021

## Scraper
Ik heb eerst alle libraries die ik nodig heb geïmporteerd.
Dan heb ik een definitie gemaakt waarin ik alles zal uitvoeren. Deze definitie komt op het einde van mijn code terug.
In de definitie ben ik begonnen met eerst de website die ik gebruik binnen te halen.
Van die website haal ik eerst volledige lijnen met informatie, daaruit ga ik dan de tijd halen en de waarden in Bitcoin & Dollar.
Nadat ik deze informatie heb, ga ik deze in een DataFrame steken en namen geven aan de kolommen.
Als dat is gebeurd, verwijder ik het Dollarteken en de komma's uit de waarden zodat mijn getal ook effectief als getal kan beschouwd worden.
Als mijn Dataframe in orde is, ga ik de rij met maximale waarden eruithalen en deze in een logfile steken.
Ik zorg ook dat mijn definitie één keer per minuut wordt uitgevoerd.
Helemaal op het einde zal ik ervoor zorgen dat mijn definitie wordt uitgevoerd zolang mijn script aan het lopen is.

## MongoDB
Dit bestand is grotendeels gelijk aan de scraper, maar in plaats van het in een bestand te steken, ga ik het opslaan in een Mongo database.
Dit doe ik door eerst de client op te roepen en daarin een database aangemaakt.
In die database heb ik dan een collectie aangemaakt waarin de rijen met de maximale waarden per minuut worden in opgeslagen.
Ook dit script blijft lopen en blijft de definitie één keer per minuut worden uitgevoerd totdat het wordt stopgezet.

## Redis
Ook dit bestand gaat verder op de scraper. In dit geval sla ik het op in een Redis Cache.
Hier ga ik eerst Redis oproepen om dan de rij met maximale waarden als Python Dictionary op te slaan in mijn cache.
Ik heb er ook voor gezorgd dat elke rij na 1 minuut wordt verwijderd uit de cache zodat er dus telkens maar 1 rij in wordt opgeslagen.
En ook hier blijft het script lopen en wordt de definitie één keer per minuut uitgevoerd totdat het wordt stopgezet.
