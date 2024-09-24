"""Aufgabe 1)
Personen innerhalb einer Liste suchen
Vorgegeben:
Liste mit Namen (Max Mustermann) vorgeben

Hinweis:
for-Schleife
if-Bedingung
String-Methode: startwith(...)
Variablen

Aufgabenteil a:
Eingabe: Exakter Name
Ausgabe: Alle Einträge die passen
Aufgabenteil b:
Eingabe: Anfang eines Namens
Ausgabe: Alle Einträge die passen
Aufgabenteil c:
Eingabe: Anfang eines Namens
Ausgabe: Maximal die ersten drei passenden Einträge
-----------------------------
"""
namen = ["Levi Schneider","Lina Schmitt","Emil Weber","Liam Fischer","Lia Krause",
         "Emilia Hartmann","Anton Meyer","Theo Wagner","Emma Koch","Paul Becker",
         "Leano Schulz","Elias Richter","Jakob Hofmann","Ella Herrmann",
         "Ida Schröder","Samuel Braun","Laura Stein"]

suche_a = "Paul Becker"
suche_b = "Li"
suche_c = "aul"

# LIKE 'aul%'

gefunden = False

# Aufgabenteil a
for name in namen:
    if name==suche_a:
        print(f"Name '{suche_a}' gefunden")
        gefunden = True
if gefunden == False:
    print(f"Name '{suche_a}' nicht gefunden")

# Aufgabenteil b
for name in namen:
    if name.startswith(suche_b):
        print(f"Name beginnend mit '{suche_b}' gefunden: {name}")
        gefunden = True
if gefunden == False:
    print(f"Name beginnend mit '{suche_b}' nicht gefunden")

# Aufgabenteil c
search2list=[]
for name in namen:
    if suche_c in name:
        search2list.append(name)
print(search2list)
""" for i in range(3):              # range(start, stop, step)
    print(search2list[i], end="\t") """




"""
AUFGABE 2)
Standardabweichung berechnen (Stichprobe)
https://datatab.de/tutorial/standardabweichung-varianz-spannweite
Abschnitt: Streuungsmaße mit DATAtab berechnen
Vorgegeben:
Liste mit Zahlen: 1, 3, 10, 5, 6, 1, -3, 12
Hinweis:
for-Schleife
Quadratwurzel ziehen: import math, math.sqrt()
Aufgabenteil a:
Mittelwert E berechnen: 1+3+10+...+12 / length
Aufgabenteil b:
M = (E-x1)^2 + (E-x2)^2 + (E-x2)^2 ....
Aufgabenteil c:
Standardabweichung: math.sqrt( M / (length-1) )
Vergleichsrechnung zur Probe hier:
https://www.standarddeviationcalculator.io/de/standard-deviation-calculator
-----------------------------
"""

zahlen =[1, 3, 10, 5, 6, 1, -3, 12]

summe = 0
for zahl in zahlen:
    summe += zahl

E = summe/len(zahlen)


M=0
for zahl in zahlen:
    M+=(zahl-E)**2

# from math import sqrt
# import math
print("Standardabweichung ist: ", math.sqrt(M/(len(zahlen)-1)))






"""
Aufgabe 3)
Neue Listen aus bestehender Liste erzeugen
Vorgegeben:
Liste mit Zahlen
Hinweis:
for-Schleife
Listen-Methode: append
Vergleichsoperatoren
Modulo-Operator
Aufgabenteil a:
Zwei neue Listen erstellen
Liste 1: mit allen positiven Zahlen
Liste 2: mit allen negativen Zahlen
Aufgabenteil b:
Zwei neue Listen erstellen
Liste 1: mit allen Zahlen die geraden index haben
Liste 2: mit allen Zahlen die ungeraden index haben
Aufgabenteil c:
Vier neue Listen erstellen
Liste 1: enthält die Zahlen mit index 0, 4, 8, ...
Liste 2: enthält die Zahlen mit index 1, 5, 9, ...
Liste 3: enthält die Zahlen mit index 2, 6, 10, ...
Liste 4: enthält die Zahlen mit index 3, 7, 11, ...
Aufgabenteil d:
Neue Liste die jeweils immer vier aufeinanderfolgende Zahlen der Liste aufsummiert enthält
Beispiel Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11]
Beispiel Neuliste = [ 0+1+2+3, 4+5+6+7, 8+9+10+11 ]
Aufgabenteil e:
Beispiel Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Beispiel Neuliste = [0, 1+2, 3+4+5, 6+7+8+9, 10+11+12+13+14]
-----------------------------
"""

# Aufgabenteil a:

zahlenliste=[1,-6,5,8,45,-62,51,22,-35,11,-25,18]
positiv=[]
negativ=[]

for zahl in zahlenliste:
    if zahl > 0:
        positiv.append(zahl)
    elif zahl==0:
        continue
    else:
        negativ.append(zahl)

print(positiv, negativ)


# Aufgabenteil b:

even_I = []
odd_I = []

for index, zahl in enumerate(zahlenliste):
    if index % 2 == 0:
        even_I.append(zahl)
    else:
        odd_I.append(zahl)

print(even_I, odd_I)


# Aufgabenteil c:

L0_4=[]
L1_5=[]
L2_6=[]
L3_7=[]

liste = 0
for zahl in zahlenliste:
    match liste:
        case 0:
            L0_4.append(zahl)
        case 1:
            L1_5.append(zahl)
        case 2:
            L2_6.append(zahl)
        case 3:
            L3_7.append(zahl)

    liste += 1
    if liste == 4:
        liste = 0

print(L0_4, L1_5, L2_6, L3_7)


# Aufgabenteil d:

Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11]
NeueListe=[]
cnt=0
summe=0
for zahl in Ausgangsliste:
    cnt+=1
    summe+=zahl
    if cnt%4==0:
        NeueListe.append(summe)
        summe=0

print(NeueListe)


# Aufgabenteil e:

Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
NeueListe=[]

spannweite = 1
zaehler = 0

summe = 0
for zahl in Ausgangsliste:
    if zaehler < spannweite:
        summe += zahl
        zaehler += 1

    if zaehler == spannweite:
        zaehler = 0
        spannweite += 1
        NeueListe.append(summe)
        summe = 0

print(NeueListe) 





"""
AUFGABE 4)
Taschenrechner- Simulator
Vorgegeben:
Liste mit Zahlen und arithmetischen Operatoren(+,-,*,/): z.B. ["+", 4, "-", 7, "+", 11, "*", 8, "/", 2]
Hinweis:
for-Schleife
if-Bedingung
Variablen
Aufgabenteil a:
Du schaltest den Taschenrechner ein und es erscheint eine 0, dann gibst du nach und nach die Operatoren und Zahlen ein. Nach der Eingabe einer Zahl berechnet der Taschenrechner den neuen Betrag.
"""

eingaben = ["+", 4, "-", 7, "+", 11, "*", 8, "/", 2]

betrag = 0.0
operation = None

for eingabe in eingaben:
    if eingabe == "+" or eingabe == "-" or eingabe == "*" or eingabe == "/":
        operation = eingabe
    else:
        match operation:
            case "+":
                betrag += eingabe
            case "-":
                betrag -= eingabe
            case "*":
                betrag *= eingabe
            case "/":
                betrag /= eingabe   

print(f"Ergebnis: {betrag}")




#5 Erzeuge eine Liste aller durch 3 teilbaren Zahlen bis 100.

teilbar3=[]
for x in range(1,101):
    if x%3==0:
        teilbar3.append(x)
print(teilbar3)

#alternativ

for x in range(1,101):
    if x%3==0:
        print(x, end=" ")

#6 Sortiere die Liste aus 1) so um, dass die erste Hälfte und die zweite Hälfte gegeneinander vertauscht werden.

print()
print(namen)
umsortiert=[]
umsortiert.extend(namen[int(len(namen)/2):] + namen[:int(len(namen)/2)])
print(umsortiert)

# alternativ
print([].extend(namen[int(len(namen)/2):] + namen[:int(len(namen)/2)]))




#7 Führe die Listen [1,2,3,4,5] und [8,7,6,5,4] zusammen und entferne die Duplikate, einmal ohne Beachtung der Reihenfolge, einmal mit Beachtung der Reihenfolge.

liste_a = [1,2,3,4,5]
liste_b = [8,7,6,5,4]

# Reihenfolge aufsteigend/ Originalreihenfolge nicht beachtet
liste_c = list(set(liste_a+liste_b))

print(liste_c)

# Originalreihenfolge beachtet
liste_c = list({}.fromkeys(liste_a + liste_b))

print(liste_c)




#8
"""
Muster aus Zahlen ausgeben:
Schreibe ein Programm, das folgendes Muster ausgibt:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Verwende eine Schleife, um das Muster zu erstellen.
"""

cnt=1
triangle=[]
while(cnt<6):    
    triangle.append(cnt)
    cnt+=1
    for elem in triangle:
        print(elem, end=" ")
    print()