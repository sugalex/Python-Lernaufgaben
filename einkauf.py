# 3.versuch methoden verbinden
from ÜBEN.learn_for_schleife import liste


class Einkauf:
    liste = []
    def versuch1(self):
        self.rein_in_die_liste = input("Was rein diggah?: ")
        self.liste.append(self.rein_in_die_liste) # mit .append mit liste verbinde, kann ich diese funktion immer wieder verwenden
        while True:
            noch_was = input("Noch was?: JA/NEIN ").lower()
            if noch_was == "ja":
                noch_mehr = input("Was denn noch: ? ")
                self.liste.append(noch_mehr) # wie hier das beispiel, liste unser hauptfaktor
                continue
            elif noch_was == "nein":
                break
            else:
                print("Error")
        print(f"Deine Liste beinhaltet: {self.liste}")

    def versuch2(self):
        anal_verkehr = input("YEAH babay: ")
        self.liste.append(anal_verkehr)
        print(f"WAAS noch mehr drinne: {self.liste} ")

eingabe = Einkauf()
eingabe.versuch1()
eingabe.versuch2()


# 2, versuch eigene lösung
class Einkauf:
    def versuch1(self):
        liste = []
        rein_in_die_liste = input("Was rein diggah?: ")
        liste.append(rein_in_die_liste) # mit .append mit liste verbinde, kann ich diese funktion immer wieder verwenden
        while True:
            noch_was = input("Noch was?: JA/NEIN ").lower()
            if noch_was == "ja":
                noch_mehr = input("Was denn noch: ? ")
                liste.append(noch_mehr) # wie hier das beispiel, liste unser hauptfaktor
                continue
            elif noch_was == "nein":
                break
            else:
                print("Error")
        print(f"Deine Liste beinhaltet: {liste}")

eingabe = Einkauf()
eingabe.versuch1()



# 1. versuch

class Einkauf:
    def artikel(self):
        beutel = []
        while True:
            eingabe1 = input("Was soll es sein Herr: ")
            beutel.append(eingabe1)

            while True:
                eingabe2 = input("Noch was? JA/NEIN: ").lower()
                if eingabe2 == "ja":
                    break
                elif eingabe2 == "nein":
                    print(f"im beutel ist : {beutel}")
                    return
                else:
                    print("ERROR, nochmal")

angeber = Einkauf()
angeber.artikel()

