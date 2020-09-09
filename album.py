class Album:
    """
    Klass Album

    klassi omadused (Atributes)
    pealkiri (str) - laulu nimi
    aasta (str) - albumi loomise aasta
    laulja (str) - esitaja
    seob andmed omavahel

    lisa_laul() - lisab laulu albumisse
    laul (str) - laulu nimi
    """
    def __init__(self, pealkiri, aasta, laulja):
        self.pealkiri = pealkiri
        self.aasta = aasta
        self.laulja = laulja
        self.laulud = []

    def lisa_laul(self, laul):
        self.laulud.append(laul)

    def näita_laulja_ja_nimi(self):
        print(self.laulja+":\n - "+self.pealkiri+" ["+self.aasta+"] -")

    def näita_laulud(self):
        for laul in self.laulud:
            laul.näita_pealkiri()

    def näita_pealkiri(self):
        print(self.pealkiri)
