###### LISTEN ######

# 1. Variable als Parameter übergeben

class Beispiel:
    def methode1(self):
        a = "hallo"
        b = " hillo"
        c = a + b
        self.methode2(c)

    def methode2(self, nett):
        print(f"ich bin {nett}")

objekt = Beispiel()
objekt.methode1()

#___________________________________________________________________

class Wurst:
    def methode01(self):
        a = 5
        b = 6
        c = a * b
        return c

    def methode02(self):
        höfflich = self.methode01()
        print(f"Geschafft: {höfflich}")

usage = Wurst()
usage.methode02()

#___________________________________________________________________

#2. Variable als Klassenattribut speichern

class Beispiel_2:
    def methode3(self):
        self.b = "hallo"
        self.c = 6 + 6
        self.methode4()

    def methode4(self):
        print(f"Dein name lautet: {self.b, self.c}")

ausgabe = Beispiel_2()
ausgabe.methode3()

#--------------------------------------------------------------------

#3. Variable als Rückgabewert verwenden

class Beispiel_3:
    def methode5(self):
        return "Hallo"  # Variable zurückgeben

    def methode6(self):
        daten = self.methode5()
        print(f"Dein Auto heisst: {daten}")

lust = Beispiel_3()
lust.methode6()
