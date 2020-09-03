from album import Album
from laul import Laul
# testime laulu objekti loomist
laul_1 = Laul("Für Oksana", "Nublu")
print(laul_1.laulja, laul_1.pealkiri)
laul_2 = Laul("12", "Nublu")
print(laul_2.laulja, laul_2.pealkiri)
# testime albumi loomist
album = Album("Uus album", 2019, "Nublu")
# lisame laulud albumisse
album.laulud.append(laul_1)
album.laulud.append(laul_2)
# vaatame loodud albumi sisu
for laul in album.laulud:
    print(laul.laulja, laul.pealkiri)