# Die for-Schleife ist eine iterative Kontrollstruktur, mit der Sie eine Gruppe von Anweisungen innerhalb eines
# Code-Blocks mit einer bestimmten Anzahl von Wiederholungen oder Argumenten ausführen können. Dazu durchläuft
# die Schleife eine vorgegebene Liste (Kollektion) und greift dabei direkt auf die einzelnen Werte darin zu.
# Aus diesem Grund ist sie auch eng mit Listen assoziiert.

############################ F-O-R  ------  S-C-H-L-E-I-F-E ################################################

for liste in range(4, 11, 2):
    print(liste)


"""

kiste = ["Apfel", "Birne", "Kirsche"]
for frucht in kiste:
    print(f"Ich mag {frucht}")

# so wie ich das verstehe ist die FOR schleife ein rad, das sich solange dreht, bis die gewünschte eingabe getroffen wird.
# mit frucht in kiste, wird jeder gegenstand einzeln aberufen und mit print ausgegeben



anzahl_reihen = 6

for i in range(1, anzahl_reihen + 1):
    leerzeichen = " " * (anzahl_reihen - i )
    sterbe = "*" * (2 * i - 1)
    print(leerzeichen + sterbe)

anzahl_reihen = 6

for i in range(anzahl_reihen):
    print(" " * (anzahl_reihen - i - 1) + "*" * (2 * i + 1))

import time

for i in range(5): # wiederholt in einer schleife 5x den print begriff
    print("Du kann super Programmieren")
    time.sleep(2) #zeitbasiert gibt 5 mal den print befehl raus, die 2 ist das tempo, die 5 von range

for zahl in range(2, 7): # hier wird nur von 2 - 7 gezählt
    print(zahl)

for buchstabe in "ABCD":
    print(buchstabe)

kaninchen = 10
for i in range(9):
     kaninchen = kaninchen + kaninchen // 5
     print(kaninchen)
"""
