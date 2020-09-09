class Laul:
    """
    Klass Laul

    klassi omadused (Atributes)
    pealkiri (str) - laulu pealkiri
    laulja (str) - laulu esitaja (artist)
    """
    def __init__(self, pealkiri, laulja):
        self.pealkiri = pealkiri
        self.laulja = laulja

    def näita(self):
        print("\t"+self.laulja+' "'+self.pealkiri+'"')

    def näita_pealkiri(self):
        print("\t"+'"'+self.pealkiri+'"')
