# Arkkitehtuurikuvaus

## Rakenne

```mermaid

classDiagram
	MainBody -->GaimSettings
	MainBody -->Shapes
	Mainbody -->Counting
	class MainBody
	class GaimSettings
	class Shapes
	class Counting

```

## MainBody

Pelisilmukka löytyy täältä. Silmukka lukee pelaajan syötteet ja valitsee toiminnan tämän perusteella

## GaimSettings

Täältä löytyy pelin pyörityksessä käytetyt asetukset kuten pelin nopeus. Täällä tapahtuu myös tietojen
pysyväistallennus sillä tallennettava informaatio on varsin pieni, jolloin omaa luokkaa ei sitä varten kannata rakentaa.

## Counting

Peliin liittyy erilaista laskentaa kuten palikoiden sijainti ja liikkeet, rivien poistaminen, pisteiden kertyminen
ja pelin päättyminen. Voi olla että kehityksen edetessä tätä osiota tulee vielä jakaa osiin.
