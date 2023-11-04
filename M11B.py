class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def accelerate(self, nopeuden_muutos):
        self.nopeuden_muutos = nopeuden_muutos
        if nopeuden_muutos >= 0:
            loppuarvo = self.nopeus + nopeuden_muutos
            if loppuarvo > self.huippunopeus:
                self.nopeus = self.huippunopeus
            else:
                self.nopeus = loppuarvo

        if nopeuden_muutos < 0:
            loppuarvo = self.nopeus + nopeuden_muutos
            if loppuarvo < 0:
                self.nopeus = 0
            else:
                self.nopeus = loppuarvo

    def kulje(self, hour_count):
        self.hour_count = hour_count
        self.matka += (self.nopeus * hour_count)


class Electric_car(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus=0, matka=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)


class Polttomoottori_auto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, koko, nopeus=0, matka=0):
        self.koko = koko
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)


electric_car = Electric_car("ABC-15", 180, 52.5)
polttomoottori_auto = Polttomoottori_auto("ACD-123", 165, 32.3)

electric_car.accelerate(104)
polttomoottori_auto.accelerate(79)

electric_car.kulje(3)
polttomoottori_auto.kulje(3)

print(electric_car.matka)
print(polttomoottori_auto.matka)