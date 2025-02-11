

zettel = ["hallo", "ich", "bin", "niko"]
print(zettel)

zettel.insert(0,  "HALLI") #neues wort wird nach nummer eingeordnet, die nr verteilt man selber
print(zettel)

zettel.append("NICHT") #wort hinzufügen
print(zettel)

zettel.remove("HALLI" ) #wort löschen
zettel.remove("hallo" )
zettel.remove("NICHT")
print(zettel)

zettel.pop() #automatische rückwärts löschung
zettel.pop()
print(zettel)

a_0 = "hallo"
b_1 = "ich"
c_2 = "bin"
d_3 = "niko"

meine_liste = [a_0, b_1, c_2, d_3]
print(meine_liste)

meine_liste[3] = "Michael"
print(meine_liste)