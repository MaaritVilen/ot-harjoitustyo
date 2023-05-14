# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on yksikerrokseinen. Kaikki luokat on sisällytetty samaan program nimiseen pakkaukseen.


## Käyttöliittymä

Käyttöliittymä sisältää kolme erilaista näkymää:
- Pelin aloitusnäkymä
- Pelinäkymä
- Pelin lopetus näkymä

Näitä ei ole toteutettu omina luokkinaan vaan pelisilmukka määrittelee pelistatuksen mukaan mitä näkymää käyttäjälle
näytetään. 

## Sovelluslogiikka

Peli on toteutettu Pygame-kirjastoa käyttäen. Eri luokkien suhdetta kuvaa seuraava luokka/pakkauskaavio.
![Pakkausrakenne ja luokat ](./kuvat/Kaavio%20Pakkaus_Luokat.JPG)


## Tietojen pysyväistallennus ja Tiedostot

Gaimsettings luokka tallentaa pelaajan nimen ja pisteet CSV tiedostoon.

## Päätoiminnallisuudet

Seuraavassa kuvataan sovelluksen toimintalogiikkaa

### MainBody luokka
Pelisilmukka on sisällytetty kyseiseen luokkaan. Pelisilmukan sisään on rakennettu palikoiden liikkuminen y akselilla,
näppäimistön syötteiden luku ja metodikutsut.

### Pelin aloittaminen

Pelaaja syöttää oman nimensä. Mikäli pelaajan nimi löytyy tiedostosta, näyttää peli pelaajan saavuttamat korkeimmat
pisteet. Pelaaja käynnistää pelin enter painikkeella.

### Uusien palikoiden luominen

Kun pelaaja on käynnistänyt pelin enter-painikkeella. Peli kutsuu new_shape metodia, joka arpoo satunnaiseti
yhden kolmesta vaihtoehtoisesta palikasta. Samalla peli myös kutsuu start_position metodia joka arpoo 
satunnaisti palikan aloituspalikan satunnaisesta kohdasta. Samoja metodeja käytetään pelin aikana uusien 
palikoiden luomiseen ja niiden sijainnin arpomiseen.

### Palikoiden liikkeet ruudulla
Pelaaja voi siirtää palikkaa oikealle ja vasemmalle nuolinäppäimillä. Kun pelaaja painaa jompaa kumpaa nuoli
näppäintä peli kutsuu count_x metodia, joka tarkistaa että palikka pysyy peliruudun sisällä. Pelistä puuttuu tällä 
hetkellä metodi joka tarkistaisi ettei putoava palikka siirry sivusuunnassa vanhojen palikoiden päälle.
Lisäksi pelaaja voi kääntää palikkaa ylös/alas nuolinäppäimillä. Kun jompaa kumpaa näppäintä painetaan, peli kutsuu 
turn_shape metodia.

### Palikoiden pysähtyminen ruudulla
Palikat pysähtyvät ruudulla kun ne saavuttavat pelilaatikon pohjan tai ne osuvat pelissä olevaan vanhaan palikkaan. 
Peli tarkistaa pohjan saavuttamista kutsumalla count_y metodia.
Pelit tarkistaa mahdollisen törmäyksen vanhoihin palikoihin kutsumalla count_old shapes metodia. 

### Rivien poistaminen ruudulta

Aina kun vanha palikka pysähtyy, eli joko saavuttaa pohjan tai törmää vanhoihin palikoihin, ohjelma kutsuu 
check_shapes metodia, joka tarkistaa onko rivi täyttynyt. Mikäli rivi on täyttynyt kyseinen metodi kutsuu
reshape_pieces metodia, joka pienentää olemassa olevia palikoita poistettavan rivin verran. Mikäli rivi on 
täyttynyt check_shapes metodi kutsuu myös reposition pieces metodia, jonka tarkoitus olisi siirtää palikoita
poistetun rivin verran alaspäin. Valitettavasti tätä toiminnallisuutta ei ole ehditty saattaa loppuun.


## MainBody

Pelisilmukka löytyy täältä. Silmukka lukee pelaajan syötteet ja valitsee toiminnan tämän perusteella

## GaimSettings

Täältä löytyy pelin pyörityksessä käytetyt asetukset kuten pelin nopeus. Täällä tapahtuu myös tietojen
pysyväistallennus sillä tallennettava informaatio on varsin pieni, jolloin omaa luokkaa ei sitä varten kannata rakentaa.

## Counting

Peliin liittyy erilaista laskentaa kuten palikoiden sijainti ja liikkeet, rivien poistaminen, pisteiden kertyminen
ja pelin päättyminen. Voi olla että kehityksen edetessä tätä osiota tulee vielä jakaa osiin.

## Shapes

Palikat arvotaan ja muodostetaan täällä.
