class Rechner:
    def zahlen_eingeben(self):
        """Erfragt zwei Zahlen vom Benutzer."""
        while True:
            try: #ermöglicht es dir, Code auszuführen, der potenziell Fehler verursachen könnte, und diese Fehler auf elegante Weise abzufangen, anstatt dass das Programm abrupt abstürzt.
                zahl1 = float(input("Gib die erste Zahl ein: "))
                zahl2 = float(input("Gib die zweite Zahl ein: "))
                return zahl1, zahl2 # Gibt beide Zahlen als Tupel zurück
            except ValueError:
                print("Ungültige Eingabe. Bitte gib Zahlen ein.")


    def addiere_zahlen(self):
        """Addiert die eingegebenen Zahlen und gibt das Ergebnis aus."""
        z1, z2 = self.zahlen_eingeben()  # Ruft zahlen_eingeben auf und entpackt das Tupel
        summe = z1 + z2
        print(f"Die Summe von {z1} und {z2} ist {summe}.")

r = Rechner()
r.addiere_zahlen()

"""

Wann verwendet man try und except (wozu)?

try und except werden verwendet, um:

Programmabstürze zu verhindern: Anstatt dass ein Programm aufgrund eines Fehlers abbricht, kann es den Fehler abfangen und auf angemessene 
Weise darauf reagieren (z. B. eine Fehlermeldung ausgeben, einen Standardwert verwenden oder eine alternative Aktion ausführen).

Robusten Code zu schreiben: Code, der Fehler abfangen kann, ist widerstandsfähiger gegenüber unerwarteten Eingaben oder Situationen.

Die Benutzererfahrung zu verbessern: Durch das Abfangen von Fehlern und das Anzeigen von benutzerfreundlichen Fehlermeldungen wird die Benutzererfahrung verbessert.

"""