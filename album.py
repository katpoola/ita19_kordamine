class Album:
    """
    Klass Album

    klassi omadused (Atributes)
    pealkiri (str) - laulu nimi
    aasta (str/int) - albumi loomis aasta
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
