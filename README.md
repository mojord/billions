# Billions

## Idea

Billions on osakesijoituspeli, jolla leikkimällä voi tutustua osakesijoittamiseen Helsingin pörssissä. Pääpaino ei ole pelillisyydessä, vaan salkkujen onnistumisen vertailussa.

## Kuvaus

Peli tarjoaa rekisteröitymisen ja kirjautumisen toiminnot.
Niiden jälkeen pelaaja perustaa salkun ja ostaa siihen osakkeita.

Pelissä on tietokantataulut rekisteröityneille pelaajille, salkuille, osakkeille, transaktioille ja tilastotaulu aiemmille peleille.
Salkun perustettuaan pelaaja antaa päivämäärän, jonka kursseja haluaa tarkastella. Pelaaja saa listan päivän kursseista ja vaihtomääristä. Tämän jälkeen voi joko ostaa osakkeita, myydä ostettuja osakkeita tai tarkastella toista päivämäärää. Oston tai myynnin jälkeen voi hakea samaa tai myöhempää päivää. Ajassa ei voi siirtyä taaksepäin. Osakkeiden myynti tapahtuu vanhimmat ensin -periaatteella, hiukan epärealistisesti siten, että tietyn oston osakkeet myydään kokonaan kerralla.

Peli näyttää päivämäärän mukaan myös salkun tilanteen ja sijoitusten hankintahinnan. Lopuksi peli antaa tiedot sijoituksen menestyksestä: salkun arvo, saadut osingot ja myyntituotot, pankkikulut ja verot. Verotuksessa sovelletaan kiinteää 30 %. Inflaation laskemista ei toteuteta toistaiseksi, mutta ajankohtana ne olivat pienet, 2020 keskimäärin 0,29 % ja 2021 2,2 %.

Pelatuista peleistä tallentuu suppea tilasto, jossa näkyy ainakin, minkä yritysten osakkeita on ostettu, ja yllä mainitut menestymistiedot.

Peli sisältää aluksi 5 suomalaisten suosikkiosaketta, pelivuodet 2020-2021. Ideaali olisi kaikki 15 Pörssisäätiön nimeämää "kansanosaketta" esim. 10 vuoden ajalta. Kurssit saadaan Nasdaqin datasta.

# Sovelluksen tilanne 2. palautuksessa

Sovelluksen pohja on valmis, mutta tietokantaominaisuuksia ja pelin kulun tarvitsemia ominaisuuksia ei ole vielä toteutettu. Tärkeänä pidettiin tässä vaiheessa rakenteen esille tuomista, eli alkusivulta voi joko rekisteröityä tai kirjautua. Rekisteröitymisen tarkistuksia on toteutettu, mutta kirjautumisen vielä ei. Kirjautumisesta siirrytään osakesalkkusivulle (Portfolio), missä (ominaisuuksien toteutuessa) voidaan luoda tai hakea salkku. Tästä siirrytään päivämääräsivulle, jossa annetaan päivämäärä, jonka kursseja halutaan tarkastella. Salkun tarkastelusivun paikka on vielä harkinnassa - tuleeko se omalle sivulle reitin tähän kohtaan vai päivämääräsivulle.  Päivämääräsivulta siirrytään osakkeen valintaan ja sieltä ostosivulle. Tämän reitin toimivuus oli tässä palautuksessa tärkein tavoite. Listaussivulle tulee vielä paluu takaisin päivämäärän antamiseen.

# Sovelluksen tilanne 3. palautuksessa

Sovellus on pääosin valmis. Sovelluksella on valmiina "lammas"-niminen käyttäjä, jolle on luotu salkku, ja tehty ostoja ja myyntejä. Kirjautumisen tarkistuksia ei vieläkään toteutettu, koska nämä kuuluvat helppoihin toteutettaviin ja haittaavat kehitysvaiheen testaamista. Sovellukseen voi siten vielä kirjautua rekisteröimättömällä käyttäjällä ja tyhjällä salasanalla, mikä ei toki ole valmiin sovelluksen ominaisuus. Valmiissa sovelluksessa osakesalkku ja transaktiot tuhotaan gameover-vaiheessa, ja vertailtavaksi tallennetaan suppeat tilastot. Tätä ei kuitenkaan vielä ehditty toteuttaa, minkä vuoksi uuden salkun luominen samalle käyttäjälle ei vielä toimi. Toteuttamatta on lisäksi salkun loppuarvon ja osinkojen laskeminen (minkä vuoksi tilastot eivät anna kaikkia lukuja oikein) sekä joitain virheen tuottamisia. Ulkoasun ominaisuudet ovat tässä vaiheessa lähinnä kokeiluja. Loppuviilauksessa toteutetaan puuttuvat toiminnot ja parannellaan tulostuksia ja ulkoasua.

# Heroku

Sovellus on testattavissa Herokussa:

[Billions](https://nasdaq-billions.herokuapp.com/)
