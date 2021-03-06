from album import Album
from laul import Laul
from laulja import Laulja
import csv


def väljasta_sisu():
    kogu_info = [tabel]
    for asi in zip(*kogu_info):
        print(*asi, sep="\t")


tabel = []
with open("albumid.txt", "r", encoding="UTF-8") as fail:
    info = csv.reader(fail, delimiter="\t")
    for rida in info:
        tabel.append(rida)

albumid = []
lauljad = []
laulud = []
lauljad_kontroll = []
albumid_kontroll = []

for rida in tabel:
    laul = Laul(rida[3], rida[0])
    laulud.append(laul)

    if rida[0] not in lauljad_kontroll:
        laulja = Laulja(rida[0])
        lauljad.append(laulja)
        lauljad_kontroll.append(laulja.nimi)

    if rida[1] not in albumid_kontroll:
        album = Album(rida[1], rida[2], rida[0])
        laulja.lisa_album(album)
        albumid.append(album)
        albumid_kontroll.append(rida[1])

    album.lisa_laul(laul)

valik = input("1 - Näita tervet muusikakogu ekraanile\n2 - Otsing albumi pealkirja või aasta järgi\n3 - Otsing laulu nime järgi\n4 - Otsing laulja järgi\nValik (1, 2, 3, 4): ")

if valik == "1":
    print("Albumid: ")
    for album in albumid:
        album.näita_laulja_ja_nimi()
        album.näita_laulud()
        print("---------------------------------------")
elif valik == "2":
    otsing = input("Sisestage otsitav album või aasta: ")
    olemas = False
    for album in albumid:
        if otsing.lower() in album.pealkiri.lower() or otsing == album.aasta:
            album.näita_laulja_ja_nimi()
            album.näita_laulud()
            olemas = True
    while olemas == False:
        print("Puudub.")
        break
elif valik == "3":
    otsing = input("Sisestage otsitav laul: ")
    olemas = False
    for album in albumid:
        for laul in album.laulud:
            if otsing.lower() in laul.pealkiri.lower():
                album.näita_laulja_ja_nimi()
                laul.näita_pealkiri()
                olemas = True
    while olemas == False:
        print("Puudub.")
        break
elif valik == "4":
    otsitav = input("Sisestage otsitav laulja: ")
    olemas = False
    for laulja in lauljad:
        if otsitav.lower() in laulja.nimi.lower():
            for album in laulja.albumid:
                album.näita_laulja_ja_nimi()
            olemas = True
    while olemas == False:
        print("Puudub.")
        break
else:
    print("Midagi läks valesti, proovige uuesti.\n --------------------------------- ")
