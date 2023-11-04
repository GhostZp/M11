class Julkaisu:
    def __init__(self, kirja, lehti):
        self.kirja = kirja
        self.lehti = lehti


class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjoittaja):
        self.nimi = nimi
        self.sivut = sivut
        self.kirjoittaja = kirjoittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.sivut}, {self.kirjoittaja}")


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.nimi = nimi
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.toimittaja}")

kirja = Kirja("Hytti n:o 6", 200, "Rosa Liksom")
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()