# Billions

## Idea

Billions on osakesijoituspeli, jolla leikkimällä voi tutustua osakesijoittamiseen Helsingin pörssissä. Pääpaino ei ole pelillisyydessä, vaan salkkujen onnistumisen vertailussa.

In Billions, you can try your luck at the Helsinki stockmarket, and see what investing in shares is like - giving sums and clicking buttons. For suspense, you have to think you are actually using your own money, or even better, loan money. The game is in English.

## Kuvaus

Peli tarjoaa rekisteröitymisen ja kirjautumisen toiminnot.
Niiden jälkeen pelaaja perustaa salkun, ostaa ja myy osakkeita.

Pelissä on tietokantataulut rekisteröityneille pelaajille, salkuille, osakkeille, transaktioille ja tilastotaulu aiemmille peleille.
Salkun perustettuaan pelaaja antaa päivämäärän, jonka kursseja haluaa tarkastella. Pelaaja saa listan päivän kursseista ja vaihtomääristä. Tämän jälkeen voi joko ostaa osakkeita, myydä ostettuja osakkeita tai tarkastella toista päivämäärää. Oston tai myynnin jälkeen voi hakea samaa tai myöhempää päivää. Ajassa ei voi siirtyä taaksepäin. Osakkeiden myynti tapahtuu vanhimmat ensin -periaatteella, hiukan epärealistisesti siten, että tietyn oston osakkeet myydään kokonaan kerralla.

Peli näyttää päivämäärän mukaan myös salkun sisällön ja sijoitusten hankintahinnan. Lopuksi peli antaa tiedot sijoituksen menestyksestä: salkun arvo, saadut osingot ja myyntituotot, pankkikulut ja verot. Verotuksessa sovelletaan kiinteää 30 %. Inflaation laskemista ei toteuteta toistaiseksi, mutta ajankohtana vuosittainen inflaatio oli pieni, 2020 keskimäärin 0,29 % ja 2021 2,2 %.

Pelatun pelin jälkeen salkku tuhotaan ja tuloksista tallentuu suppea tilasto. Alkusivun galleria näyttää salkkujen prosentuaalisen menestyksen. Sitä voi tarkastella rekisteröitymättä.

Peli sisältää 12 suomalaisten suosikkiosaketta, eli Pörssisäätiön nimeämää "kansanosaketta", pelivuodet 2020-2021.

"Kansanosakkeet": Pörssisäätiö https://www.porssisaatio.fi/blog/statistics/kansanosakkeet/

Kurssitiedot: Nasdaq http://www.nasdaqomxnordic.com/osakkeet/historiallisetkurssitiedot

Osinkotiedot: Taloussanomat osinkokalenteri https://www.is.fi/taloussanomat/osinkokalenteri/alma-media/alma/

# Sovellus loppupalautuksessa

Suurin osa alkuperäisistä tavoitteista saatiin toteutettua. Ideaalitilanteessa aika olisi pidempi ja mukana inflaation vaikutus ja vertailu esim. OMX-indeksiin. Monien toimintojen toteuttaminen osoittautui yllättävän monimutkaiseksi, ja joitain syötetarkistuksia oli viime hetkellä laastaroitava kömpelösti. Yleisimmät virheet saatiin pois, mutta ei ihan kaikkia olennaisia. Tietokantametodit olisivat vielä kaivanneet virtaviivaistamista. Koska SELECT * FROM-kyselyn huonouden syistä ei saatu vastausta kurssilla, referoitiin seuraavaa https://dzone.com/articles/why-you-should-not-use-select-in-sql-query-1. Jäljelle jätettiin pari tuon tyypin kyselyä, jotka eivät riko lähteessä mainittuja periaatteita.

Sovellukseen jäi jonkin verran toistavaa koodia, koska ei ollut aikaa riittävään refaktorointiin. Siinä on myös joitain metodeja ja rakenneratkaisuja, jotka ovat tarpeen jatkokehityksen kannalta, mutta eivät vielä ole käytössä. Tärkeänä on pidetty myös sitä, että koodi pysyy itselle luettavana ja sen vuoksi jossain ei ole käytetty kaikkein eleganteimpia ratkaisuja, vaan sellaisia, joiden kulkua on helppo itse seurata sovelluksen kasvaessa ja monimutkaistuessa.

# Heroku

Sovellus on testattavissa Herokussa. Sillä on testikäyttäjä tester salasanalla tester123. Käyttäjälle on luotu salkku ja ostettu siihen osakkeita. Mutta salkku tietysti katoaa, jos testaaja pelaa pelin loppuun (tai muuttuu pelikelvottomaksi "ajankulun" vuoksi).

[Billions](https://nasdaq-billions.herokuapp.com/)
