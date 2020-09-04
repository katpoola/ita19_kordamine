class Laulja:
    """
    Klass Laulja

    klassi omadused (Atributes)
    nimi (str) - esitaja nimi
    tekitab esitajale oma albumi

    lisa_album() - tekitab albumi ja lisab albumite hulka
    album (str) - albumi nimi
    """
    def __init__(self, nimi):
        self.nimi = nimi
        self.albumid = []

    def lisa_album(self, album):
        self.albumid.append(album)
