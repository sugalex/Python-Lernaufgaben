import json


class Inventar:
    def __init__(self):
        self.itembag = []
        self.datei_pfad = "inventar.json"
        self.load_itembag()


    def reinlegen(self):
        items_new = input("Was hast du gefunden ? ").lower()
        self.itembag.append(items_new)
        self.save_itembag()
        print(f"Item {items_new} wurde ins Inventar gelegt")

    def rausnehmen(self):
        items_cut = input("Welches Item benutzen ? ").lower()
        if items_cut in self.itembag:
            self.itembag.remove(items_cut)
            self.save_itembag()
            print(f"Item {items_cut} wurde erfolgreich benutzt!!")
        else:
            print("Kein Item diese, zurück zur auswahl")

    def anzeige(self):
        if self.itembag:
            print(f"Im Inventar hast du folgende dinge \n{self.itembag}")
        else:
            print("Inventar ist leer")

    def save_itembag(self):
        try:
            with open(self.datei_pfad, 'w') as datei:
                json.dump(self.itembag, datei)
            print("Inventar wird gespeichert.")
        except Exception as e:
            print(f"Fehler beim Speichern der Inventar-Daten: {e}")

    def load_itembag(self):
        try:
            with open(self.datei_pfad, 'r') as datei:
                self.itembag = json.load(datei)
            print("Garage-Daten wurden geladen.")
        except FileNotFoundError:
            print("Keine vorhandenen itembag-Daten gefunden. Eine neue itembag wird erstellt.")
            self.itembag = []
        except json.JSONDecodeError:
            print("Fehler beim Lesen der itembag-Daten. Die itembag wird als leer initialisiert.")
            self.itembag = []
        except Exception as e:
            print(f"Unbekannter Fehler beim Laden der itembag-Daten: {e}")
            self.itembag = []

def menu():
    inventar = Inventar()
    while True:
        print(
          "\n Was genau möchtest du tun ? "
          "\n ---1--- Willst du die Items ins Inventar legen ?"
          "\n ---2--- Die Items aus dem Inventar benutzen"
          "\n ---3--- Inventar anzeigen"
          "\n ---4--- Programm beenden"
          )
        auswahl = input("Welche Nummer wählst du ? ")
        if auswahl == "1":
            inventar.reinlegen()
        elif auswahl == "2":
            inventar.rausnehmen()
        elif auswahl == "3":
            inventar.anzeige()
        elif auswahl == "4":
            break


menu()