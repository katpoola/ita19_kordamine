from album import Album
from laul import Laul
from laulja import Laulja

# võtab ja sorteerib kogu info failist
def faili_info(self):
    with open("albumid.txt", "r", encoding="UTF-8") as fail:
        info = list(zip(*(map(str, rida.split(sep="\t")) for rida in fail)))
    return info[self]

# väljastab kõik info failist korrektselt
def väljasta_sisu():
    kogu_info = [esitaja, albumid, aastad, laulude_nimed()]
    for asi in zip(*kogu_info):
        print(*asi, sep="\t")

# korrastab laulude nimed
def laulude_nimed():
    for nimi in faili_info(3):
        laulud.append(nimi.strip())
    return laulud


esitaja = faili_info(0)
albumid = faili_info(1)
aastad = faili_info(2)
laulud = []

# testime laulu objekti loomist
# laul_1 = Laul("Für Oksana", "Nublu")
# print(laul_1.laulja, laul_1.pealkiri)
# laul_2 = Laul("12", "Nublu")
# print(laul_2.laulja, laul_2.pealkiri)
# laul_3 = Laul("Crossandid", "Nublu")
# print(laul_1.laulja, laul_1.pealkiri)
# laul_4 = Laul("Öölaps", "Nublu")
# print(laul_2.laulja, laul_2.pealkiri)

# testime albumi loomist
# album_1 = Album("Uus album 1", 2019, "Nublu")
# lisame laulud albumisse
# album_1.lisa_laul(laul_1)
# album_1.lisa_laul(laul_2)
# testime albumi loomist
# album_2 = Album("Uus album 2", 2019, "Nublu")
# lisame laulud albumisse
# album_2.lisa_laul(laul_3)
# album_2.lisa_laul(laul_4)

# vaatame loodud albumi sisu
# print(album_2.pealkiri)
# for laul in album_2.laulud:
#    print(laul.laulja, laul.pealkiri)

# testime Laulja loomist
# laulja = Laulja("Nublu")
# laulja.lisa_album(album_1)
# laulja.lisa_album(album_2)
# testime albumite sisu
# for album in laulja.albumid:
#    print(album.pealkiri)
#    for laul in album.laulud:
#        print(laul.laulja, laul.pealkiri)
