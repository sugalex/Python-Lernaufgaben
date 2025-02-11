

"""
#wenn die schrägstriche(backslashes) falsch rum sind, einfach das r vorne hinsetzen, dann korregiert er den fehler
t = open(r"C:\Users/nikol\Desktop\Sonstiges\Text Dokumente\Neues Textdokument (4).txt") #hier muss ein r vorne hin
print(t.read())

t = open(r"C:\Users/nikol\Desktop\Sonstiges\Text Dokumente\Neues Textdokument (4).txt")
print(t.read(10)) # gewünschte anzahl an wiedergegebenen zeichen

t = open(r"C:\Users/nikol\Desktop\Sonstiges\Text Dokumente\Neues Textdokument (4).txt") # nur um die erste zeile auszulesen
print(t.readline())
"""

t = open(r"C:\Users/nikol\Desktop\Sonstiges\Text Dokumente\Neues Textdokument (4).txt") # nur um die erste zeile auszulesen
for zeile in t:
    print(zeile)