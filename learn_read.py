
# r = Read / Lesen
# a = Append / Hinzufügen
# w = Write / Schreiben
# x = Create / Erstellen

f = open("inventar.json", "r") # damit kann man in der Konsole lesen
print(f.read())
f.close()

#f = open("GedichtOriginal.txt", "r") / Hier wir jede 2te Zeile freigelassen.
#for line in f:
#    print(line)


f = open("Gedicht.txt", "a") # Datei öffnen zum Ergänzen
f.write("Hier den Text eingeben, der in die textdatei soll")
f.close()


#f = open("Bitch.txt", "w")  #Datei öffnen zum Schreiben
#f.write("Bitchi Gonzales")
#f.close()  #Diese Zeile öffnet die Datei im Schreibmodus ('w'). Wenn die Datei bereits existiert, wird ihr Inhalt überschrieben. Wenn sie nicht existiert, wird sie neu erstellt.


#f = open("GedichtOriginal.txt", "x")
#f.write("Damit erstellen wir eine neue text datei") / Die Datei wird nur erstellt, wenn es die Datei nicht gibt
#f.close()


