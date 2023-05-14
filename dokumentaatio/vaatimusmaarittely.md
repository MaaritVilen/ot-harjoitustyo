# TETRIS

## Sovelluksen tarkoitus

Sovellus on klassinen tetris-peli, eli ruudulle putoavat palikat pyritään sjoittaamaan siten että ruutu ei täyty. 
Mikäli ruutu täyttyy palikoista, peli päättyy.

## Toiminnallisuudet:

### Ennen peliä
Pelaaja kirjaa alussa nimensä, jonka jälkeen hän näkee korkeimmat saavuttamansa pisteet aikaisemmissa peleissä. 

### Peli
Pelaaja ohjaa ylhäältä putoavia palikoita ja pyrkii muodostamaan kokoanisia rivejä. Kun rivi on täynnä se poistuu 
pelistä. Pelaaja saa 10 pistettä kustakin poistetusta palikasta. Peli nopeutuu pistemäärän kertyessä. Peli päättyy
kun palikkapino yltää ruudun yläreunaan. 

### Pelin päättyminen
Pelin päätyttyä peli tallentaa saavutetut pisteet mikäli ne ylittävät aikai-
semmat pisteet.


## Jatkokehitys

### Selkeät puutteet
Pelin kehitys jäi kurssin aikana kesken. Pelissä on ainakin seuraavat viat, joita ei ole ehditty korjata:
- Liikutettaessa palikoita sivuttain (x-horisontissa) putoava palikka menee vanohjen palikoiden päälle.
- Rivien poistuminen ruudulta ei ole täydellistä. (Laskennassa on edelleen jokin vika)

### Muita parannus ideoita
Seuraavilla parannuksilla pelistä saa miellyttävämmän:
- Koodi ei ole parasta mahdollista. Koodissa voisi hyödyntää dictionary ominaisutta sekä joissa tapauksissa muodostaa
uusia luokkia ja funktioita
- Palikoiden ohjailu on hieman vaikeaa. Tätä voisi parantaa
- Pelin visuaalisuutta voisi parantaa
