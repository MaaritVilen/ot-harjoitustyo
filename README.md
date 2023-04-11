# Kysymys ohjaajalle

Onko ohjaajalla mitään näkemystä miksi ohjelma löytää csv-tiedoston kun ohjelmaa käytetään VCS:n kautta mutta ei löydä kun yritän ajaa ohjelmaa tai testejä komentoriivn kautta?

# Tetris

Kyseessä on klassinen tetris, jossa pelaaja yrittää saada pelin etenemään niin pitkälle kuin mahdollista.
Peliruudun yläreunasta putoilee palikoita kiihtyvällä tahdilla, jotka alaosaan pudotessaan pysähtyvät ja kasaantuvat
pinoksi. Kun pino yltää ruudun yläreunaan, peli päättyy. Pinoa saa madallettua asettelamalla putoavia palikoita siten
ettei riville jää tyhjää tilaa. Kun rivi on täynnä ilman tyhjiä ruutuja, rivi poistuu ja pino madaltuu rivin verran.

## Dokumentaatio
-[Changelog](https://github.com/MaaritVilen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

_[Vaatimusmäärittely](https://github.com/MaaritVilen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

_[Työaikakirjanpito](https://github.com/MaaritVilen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

-[Arkkitehtuuri](https://github.com/MaaritVilen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Käynnistä sovellus komennolla:
`poetry run invoke start`

## Komentorivitoiminnot
### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:
`poetry run invoke start`

### Testaus

Testit suoritetaan komennolla:
`poetry run invoke test`

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
`poetry run invoke coverage-report`

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
`poetry run invoke lint`


