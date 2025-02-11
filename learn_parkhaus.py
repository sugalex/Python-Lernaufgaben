#### Bedingte Anweisungen: if, elif, else ####
# if: Führt den Block aus, wenn die Bedingung wahr ist.
# elif: Prüft zusätzliche Bedingungen, wenn die vorherigen if-Bedingungen falsch waren.
# else: Fängt alle anderen Fälle ab, wenn keine der vorherigen Bedingungen erfüllt ist.

class Parkhaus:

    def __init__(self):
        self.garage = []

    def einparken(self):
        einfahrt = input("Welches Auto wurde reingefahren? ")
        self.garage.append(einfahrt)
        print(f"Auto mit Kennzeichen {einfahrt} ist in der Garage")

    def ausparken(self):
        ausfahrt = input("Welches Auto soll ausgeparkt werden? ")
        if ausfahrt in self.garage: # 'if' überprüft, ob das eingegebene Kennzeichen in der garage-Liste vorhanden ist. 'in' wird verwendet, um zu prüfen, ob ein bestimmtes Element in einer Liste ist.
            self.garage.remove(ausfahrt)
            print(f"Auto mit kennzeichen {ausfahrt} ist raus")
        else: #wenn die überprüfung fehl schlägt, dafür brauchen wir einen else befehl, sonst weiss das programm nicht was es machen soll.
            print(f"Auto mit Kennzeichen {ausfahrt} ist nicht in der Garage.")

    def _garage_anzeigen(self):
        if self.garage: # Diese Zeile überprüft, ob die garage-Liste leer ist oder nicht. Im Wesentlichen fragt sie: Gibt es irgendwelche Autos in der Garage?
            print(f"Autos in der Garage {self.garage}")
        else:
            print("Die Garage ist leer.")


def menu():
    parkhaus = Parkhaus()
    while True:
        print("  \nWelche Option möchten Sie nutzen ? "
                "\nDrücke 1 für Einparken"
                "\nDrücke 2 für Ausparken"
                "\nDrücke 3 für Garage anzeigen"
                "\nDrücke 4 Beenden")
        wahl = input("Ihre Wahl: ")

        if wahl == "1":
            parkhaus.einparken()
        if wahl == "2":
            parkhaus.ausparken()
        if wahl == "3":
            parkhaus._garage_anzeigen()
        if wahl == "4":
            print("Programm beendet")
            break
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

menu()





