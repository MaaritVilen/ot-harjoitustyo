## viikko 2 (kalenteriviikko 13-14)
- Pelisilmukan runko luotu
- Käyttäjä voi syöttää nimensä
- Peli tervehtii käyttäjää
- Alustavia luokkia suunniteltu

## viikko 3 (14-15)
- Peli hakee käyttäjälle edellisen tuloksen tervehtimisen yhteydessä. Erikoista tässä on se että tämä toimii VCS
käytettäessä mutta ei poetry invoke start toiminnolla. Jälkimmäisellä ohjelma ei löydä csv-tiedostoa... 
Ongelma ratkaistavaksi.
- Peli tallentaa tulokse pelin päätteeksi
- Pelin testiympäristöä on kehitetty edelleen. Jäi viime viikolla kesken...
- Pylint asennettu, jostain syystä ei kuitenkaan toimi. Saattanee olla sama ongelma kuin pelin käynnistämisessä 
komentorivin kautta.
## viikko 4 (15-16)
- Peli luo palikoita ja tuo ne ruudulle
- Palikat ovat jatkuvassa liikkessä
- Käyttäjä kykenee siirtämään palikoita oikealla ja vasemmalle
- Palikka pysähtyy alareunaan
## viikko 5 (kalenteriviikko 16-17)
- Pelaaja kykenee kääntämään palikan
- Palikan pysähdyttyä peli luon uuden putoavan palikan yläreunaan
- Vanhat palikat jäävät näkyviin ruudulle
- Palikka ei enää pysähdy alareunaan vaan se pysähtyy edellisen palikan päälle (vaati vielä pientä tarkkuuden lisäystä) 

## Seuraavat parannukset tulee laatia jo tehtyihin funktioihin
- Nimeä syötettäessä käyttäjän tulee kyetä myös poistamaan ja korjaamaan tekstiä
- Aloitusruudun visuaalisuutta tulee kehittää
- Tällä hetkellä palikka siirtyy sivusuunnassa pisteen kerrallaan. Muutetaan kymmeneen pisteeseen, helpottaa
"pudottamista"
- Tarksitetaan pysähtymiskohdan tarkkuus

