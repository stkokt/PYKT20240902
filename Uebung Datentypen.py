"""
1.String-Konkatenation:
•Speichere deinen Vor- und Nachnamen in zwei separaten Variablen.
•Verbinde die beiden Variablen zu einem vollständigen Namen und gib diesen aus.

2.String-Slicing:
•Speichere das Wort “Python” in einer Variablen.
•Gib die ersten drei Buchstaben und die letzten drei Buchstaben des Wortes separat aus.

3.String-Formatierung:
•Erstelle einen String, der eine Adresse enthält, und formatiere ihn so, dass er in mehreren
Zeilen ausgegeben wird.
•Gebe den Satz „Jedes Wort beginnt mit einem Großbuchstaben“ so aus, dass jedes Wort 
mit einem Großbuchstaben beginnt.

4.Zeichen zählen:
•Schreibe ein Programm, das die Anzahl der Vorkommen jedes Vokals in dem String 
"jklhfpogisdhfpoehniodffvjdsnvjksdhpfuerifhsdiaewaerwkeräjmbälklnnnmopnbhjbhasieu" 
zählt.
• Finde heraus, an welcher Stelle jeder Vokal das erste Mal und das letzte Mal erscheint.

5.Wörter zählen:
•Schreibe ein Programm, das die Anzahl der Wörter in einem gegebenen Satz zählt.
•Beispiel: “Das ist ein Beispieltext.” sollte 4 Wörter ergeben.

"""

# Aufgabe 1

vorname = "Stefan"
nachname = "Koschnik"

print(vorname, nachname)
print(vorname + " " + nachname)

# Aufgabe 2

wort = "Python"
# Erste 3 Buchstaben

print(wort[0:3])
print(wort[:3])



# Letzte 3 Buchstaben

print(wort[3:len(wort)])
print(wort[3:])

# Jeden 2. Buchstaben

print(wort[0::2])   # Parameter in der eckigen Klammer: [start, stop, step]

# Aufgabe 3/1

PLZ = "12345"
Stadt = "Musterstadt"
StrasseHnr = "Bahnhofstraße 7"

print(vorname, nachname,"\n\n",StrasseHnr,"\n",PLZ, Stadt)

# oder
print()
print(vorname, nachname)
print()
print(StrasseHnr)
print(PLZ, Stadt)

# Aufgabe 3/2

satz ="Jedes Wort beginnt mit einem Großbuchstaben"
print(satz.title())

# Aufgabe 4

buchstabensalat = "jklhfpogisdhfpoehniodffvjdsnvjksdhpfuerifhsdiaewaerwkeräjmbälklnnnmopnbhjbhasieu"

print("Der Vokal 'a' erscheint", buchstabensalat.count("a"), "mal. \
Das erste Mal am Index", buchstabensalat.find("a"), \
", das letzte Mal am Index", buchstabensalat.rfind("a"))

print("Der Vokal 'e' erscheint", buchstabensalat.count("e"), "mal. \
Das erste Mal am Index", buchstabensalat.find("e"), \
", das letzte Mal am Index", buchstabensalat.rfind("e"))

print("Der Vokal 'i' erscheint", buchstabensalat.count("i"), "mal. \
Das erste Mal am Index", buchstabensalat.find("i"), \
", das letzte Mal am Index", buchstabensalat.rfind("i"))

print("Der Vokal 'o' erscheint", buchstabensalat.count("o"), "mal. \
Das erste Mal am Index", buchstabensalat.find("o"), \
", das letzte Mal am Index", buchstabensalat.rfind("o"))

print("Der Vokal 'u' erscheint", buchstabensalat.count("u"), "mal. \
Das erste Mal am Index", buchstabensalat.find("u"), \
", das letzte Mal am Index", buchstabensalat.rfind("u"))

# Aufgabe 5

satz2 = "Das ist ein Beispieltext."

print("Satz2 enthält ", len(satz2.split()) , "Worte.")

satz3 = "Das ist ein ,  Beispieltext."
satz3_1 = satz3.split()

print(len(satz3_1))

satz3_1.remove(",")

print(len(satz3_1))