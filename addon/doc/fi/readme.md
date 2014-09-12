# dropbox #

* Tekijät: Patrick ZAJDA, Filaos ja muut
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa lisää pikanäppäimen Dropboxin tilan ja version ilmoittamiseksi
tai ilmoitusalueella olevan valikon avaamiseksi.  Lisäksi välilehdet
toimivat Asetukset-valintaikkunassa Ctrl+sarkain-, Ctrl+Shift+sarkain- sekä
Ctrl+Page up/down-näppäimillä, ja Peruuta-painike toimii Esc-näppäimellä.

* Pikanäppäin: NVDA+Shift+D
* Ctrl+Alt+T ilmoittaa aktiivisen välilehden.

## Tunnetut ongelmat ##

* Jos välilehtiä vaihdetaan pikanäppäimillä, NVDA ei voi tietää Asetukset-ikkunaa suljettaessa, että välilehtiä ei enää ole.
Tämä on tunnettu NVDA:n ongelma, eikä sitä voida korjata.

## Muutokset versiossa 4.0 ##

* Käännöksiä päivitetty.
* Korjattu Windows 8:n metro-sovelluksen ongelmia.

## Muutokset versiossa 3.1 ##

* Käytetään toista tapaa Peruuta-painikkeen painamiseksi ja välilehtiin
  pääsemiseksi. Kohdistusta ei enää tarvitse siirtää niihin ennen
  pikanäppäinten käyttämistä.
* Kohdistus siirtyy aktiivista välilehteä vaihdettaessa uuteen välilehteen,
  joten sarkainta painettaessa aktiiviseksi tulee sen ensimmäinen kohde sen
  sijaan että pysyttäisiin edellisessä välilehdessä.
* Välilehtiä on nyt mahdollista vaihtaa Asetukset-valintaikkunassa
  painamalla Ctrl+Page up/down. Myös Ctrl+sarkain ja Ctrl+Shift+sarkain
  toimivat edelleen.
* Kaikkien lokalisoitujen manifestitiedostojen pitäisi olla nyt kunnossa.
* Pieniä korjauksia.

## Muutokset versiossa 3.0 ##

* Pieni korjaus  manifest-päätiedostoon (tekijät näytetään oikein).
* Paranneltu pikavalikon havaitsemista painettaessa kolmasti NVDA+Shift+D.
* Esc-näppäin toimii nyt (vain, kun Dropboxia käytetään samalla kielellä
  kuin NVDA:takin).
* Paljon korjauksia koodiin.
* Kaikkien komentojen ohjeet lisätty/päivitetty.
* Uusia kieliä: arabia, brasilianportugali, espanja, galego, hollanti,
  japani, nepali, puola, saksa, slovakki, suomi, tamili, tshekki, turkki,
  unkari, venäjä.

## Muutokset versiossa 2.0 ##

* Uusi kieli: italia
* Pikanäppäimen painaminen kolmesti tai useammin ei aiheuta enää ongelmia
  pikavalikossa oltaessa.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx

[2]: http://addons.nvda-project.org/files/get.php?file=dx-dev
