class Rechner:
    def addieren(self):
        self.a = 5
        self.b = 6
        self.c = self.a + self.b



class Rechner2:
    def wiederholen(self, anal):
        wert_c = anal.c
        print(f"Der code lautet: {wert_c}")


objekt = Rechner()
objekt.addieren()

objekt_2 = Rechner2()
objekt_2.wiederholen(objekt)