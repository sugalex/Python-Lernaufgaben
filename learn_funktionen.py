# Die Einleitung einer Funktion erfolgt immer durch das Schlüsselwort def, dahinter kommen der Name
# der Funktion und die Parameter in Klammern. Die - Parameter können dabei entweder optional oder o
# bligatorisch sein, es wird in der Regel aber nur eine bestimmte Anzahl von Argumenten akzeptiert,
# die von einem bestimmten Typ sein müssen. def funktion1 (Parameter1, Parameter2, Parameter3 usw.)

# - Parameter sind Platzhalter für Werte, die du einer Funktion übergeben kannst, damit sie mit diesen Werten arbeiten kann.

########################### F-U-N-K-T-I-O-N-E-N (methoden) #####################################


# Definition einer Funktion mit Parametern
def begruessung(name, alter): # Das Schlüsselwort def leitet die Funktion ein.

    # Diese Funktion nimmt zwei Parameter:
    # - name: Der Name der Person
    # - alter: Das Alter der Person

    print(f"Hallo {name}! Du bist {alter} Jahre alt.")  # Innerhalb der Funktion verwenden wir die Parameter
                                                        # name und alter, um eine Nachricht zu erstellen.


# Aufruf der Funktion mit Argumenten
begruessung("Anna", 25)
begruessung("Tom", 30)




##########################################################################################

class Hallo:
    def begruessung(self):
        name = "anna"
        alter = 16
        print(f"Hallo {name}! Du bist {alter} Jahre alt.")
        return name, alter # Das Schlüsselwort return in Python wird verwendet, um Daten aus einer Funktion zurückzugeben.
                           # Die Methode gibt die beiden Variablen name und alter als Tupel zurück

    def aufwiedersehen(self):
        name, alter = self.begruessung()  # Die Werte name und alter, die durch return zurückgegeben wurden,
                                          # werden den Variablen name und alter in aufwiedersehen zugewiesen.
        print(name, alter)



objekt = Hallo()
objekt.aufwiedersehen()

# habe versucht, aus der ersten funktion begruessung, name und alter in funktion 2 aufwiedersehen hinzuzufügen
# Warum brauchen wir return, um die Werte in aufwiedersehen zu nutzen?
# Ohne return bleiben die Werte name und alter innerhalb von begruessung begrenzt. Das nennt man den
# Gültigkeitsbereich (Scope). Variablen, die innerhalb einer Funktion definiert sind, existieren nur
# während der Ausführung dieser Funktion.