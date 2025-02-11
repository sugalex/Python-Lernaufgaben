# Schleifen werden verwendet, um Programmteile wiederholt auszuführen, ohne dafür jedes
# Mal den Code neu schreiben zu müssen.
# while Bedingung = Anweisungsblock
#break beendet nur die Schleife, in der er sich befindet
#return beendet direkt das ganze programm

########################## W-H-I-L-E  ---------  S-C-H-L-E-I-F-E ##################################

class Einkauf:
    def artikel(self):
        beutel = []  # machen einen echten beutel raus
        while True: #äussere schleife, läuft solange bis ein break oder return kommt
            einfuegen1 = input("Was kommt rein Diggah: ")
            beutel.append(einfuegen1) #die eingabe in der konsole wird hier mit.append mit dem beutel verbunden

            while True: #innere schleife, bis break oder return
                einfuegen2 = input("Noch was rein. JA/NEIN: ").lower()
                if einfuegen2 == "ja":
                    break #verlässt die 2te schleife und springt zur ersten
                elif einfuegen2 == "nein":
                    print(f"Hier der Inhalt: {beutel}")
                    return # beendet das programm
                else:
                    print("Error, nochmal") # wenn kein ja oder nein, springt er zu einfuegen2 und bleibt in der inneren schleife

klasse_auswaehlen = Einkauf()
klasse_auswaehlen.artikel()


####################### ohne klasse zum testen ####################################

zaehler = 1
while zaehler < 11: #soll bis 10 gezählt werden
    print(zaehler) #Damit ist die Bedingung zaehler < 11 unwahr (False) und die Schleife wird verlassen.
    zaehler += 1 #hier wird schrittweise ausgewählt, also immer +1 zur 10