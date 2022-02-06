# Billions

## Idea

Billions on osakesijoituspeli, jolla leikkimällä voi tutustua osakesijoittamiseen Helsingin pörssissä. Pääpaino ei ole pelillisyydessä, vaan salkkujen onnistumisen vertailussa.

## Kuvaus

Peli tarjoaa rekisteröitymisen ja kirjautumisen toiminnot.
Niiden jälkeen pelaaja perustaa salkun ja ostaa siihen osakkeita.

Pelissä on tietokantataulut rekisteröityneille pelaajille, salkuille, osakkeille ja tilastotaulu aiemmille peleille.
Salkun perustettuaan pelaaja antaa päivämäärän, jonka kursseja haluaa tarkastella. Pelaaja saa listan päivän kursseista ja vaihtomääristä. Tämän jälkeen voi joko ostaa osakkeita, myydä ostettuja osakkeita tai tarkastella toista päivämäärää. Oston tai myynnin jälkeen voi hakea seuraavaa päivää. Ajassa ei voi siirtyä taaksepäin.

Peli näyttää päivämäärän mukaan myös salkun tilanteen: sijoituksen hankintahinnan, päivän arvon ja lisäksi menestyksen suhteessa pörssin indeksiin, jos tämä viimeksimainittu tieto löydetään netistä helposti. Lopuksi peli antaa tiedot sijoituksen menestyksestä: salkun arvo, saadut osingot ja myyntituotot, realisointinetto verrattuna siihen, että rahat olisivat olleet käyttötilillä. Tilin koroksi oletetaan 0 ja verotuksessa sovelletaan kiinteää 30 %. Inflaation vaikutus lasketaan karkeasti vuosi-inflaation perusteella.

Pelatuista peleistä tallentuu suppea tilasto, jossa näkyy ainakin, minkä yritysten osakkeita on ostettu, ja yllä mainitut menestymistiedot.

Peli sisältää aluksi 5 suomalaisten suosikkiosaketta, pelivuodet 2020-2021. Ideaali olisi kaikki 15 Pörssisäätiön nimeämää "kansanosaketta" esim. 10 vuoden ajalta. Kurssit saadaan Nasdaqin datasta.

# Sovelluksen tilanne 2. palautuksessa

Sovelluksen pohja on valmis, mutta tietokantaominaisuuksia ja pelin kulun tarvitsemia ominaisuuksia ei ole vielä toteutettu. Tärkeänä pidettiin tässä vaiheessa rakenteen esille tuomista, eli alkusivulta voi joko rekisteröityä tai kirjautua. Rekisteröitymisen tarkistuksia on toteutettu, mutta kirjautumisen vielä ei. Kirjautumisesta siirrytään osakesalkkusivulle (Portfolio), missä (ominaisuuksien toteutuessa) voidaan luoda tai hakea salkku. Tästä siirrytään päivämääräsivulle, jossa annetaan päivämäärä, jonka kursseja halutaan tarkastella. Salkun tarkastelusivun paikka on vielä harkinnassa - tuleeko se omalle sivulle reitin tähän kohtaan vai päivämääräsivulle.  Päivämääräsivulta siirrytään osakkeen valintaan ja sieltä ostosivulle. Tämän reitin toimivuus oli tässä palautuksessa tärkein tavoite. Listaussivulle tulee vielä paluu takaisin päivämäärän antamiseen.

# Heroku

Sovellus on Herokun ilmoituksen mukaan saatu Herokuun onnistuneesti, mutta sitä ei saatu toimimaan Heroku-osoitteessa, vaikka se toimii paikallisesti. Ongelmaa ei ole vielä onnistuttu korjaamaan.

[Billions](https://nasdaq-billions.herokuapp.com/)
