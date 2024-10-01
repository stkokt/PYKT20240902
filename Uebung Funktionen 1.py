# 1.    Quadrat einer Zahl berechnen: Schreibe eine Funktion quadrat(x),
#       die das Quadrat einer Zahl zurückgibt.

print("Aufgabe 1\n")

def quadrat(x):
    return x**2     # alternativ 1: return x*x

print(quadrat(2))

# 2.    Summe von zwei Zahlen: Schreibe eine Funktion summe(a, b), 
#       die die Summe von zwei Zahlen berechnet.

print("\nAufgabe 2\n")

def summe(a, b):
    return a+b      # alternativ: b+a oder sum([a, b])

print(summe("Stefan"," Koschnik"))

# 3.    Länge eines Strings: Schreibe eine Funktion laenge(s), 
#       die die Länge eines Strings zurückgibt.

print("\nAufgabe 3\n")

# Wenn man die Aufgabe penibel wörtlich nimmt, muss man prüfen, 
# ob tatsächlich ein String übergeben wurde.

def laenge(s):
    if type(s) == str:
        return len(s)
    else:
        return ("Sie haben keinen String übergeben.")

# Alternativ:
def laengeA1(s):
    if type(s) == str:
        cnt=0
        for letter in s:
            cnt+=1
        return cnt
    else:
        return ("Sie haben keinen String übergeben.")

#print(laenge("Das ist ein String"))
print(laenge(str(10/10.0)))       # Das ist kein String. Auch die Builtin- Funktion len()würde hier einen Fehler werfen.
#print(laenge([1,2,3]))  # Das auch nicht. Die Builtin- Funktion len() 
                        # hätte hier aber einen Wert zurück geliefert,
                        # würde in der Funktion laenge nicht explizit auf den Typ geprüft werden.
#print(laengeA1("Das ist ein String"))


# 4.    Größere Zahl finden: Schreibe eine Funktion groesser(a, b), 
#       die die größere von zwei Zahlen zurückgibt.

print("\nAufgabe 4\n")

def groesser(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Beide Zahlen sind gleich."
    
print(groesser(10,5))
# Alternative:

def groesserA1(a, b):
    return a if a>b else b if b>a else "Beide gleich groß"

# a>b?a:b Terniärer Operator

    
print(groesser(5,10))
print(groesser(10,10))
print(groesserA1(5,10))
print(groesserA1(10,10))


# 5.    Umwandlung in Großbuchstaben: Schreibe eine Funktion grossbuchstaben(s), 
#       die einen String in Großbuchstaben umwandelt.

print("\nAufgabe 5\n")

def grossbuchstaben(s):
    if type(s) == str:
        return s.upper()
    else:
        return "Du hast keinen String übergeben."




print(grossbuchstaben("Das ist ein String."))
print(grossbuchstaben({"Hallo":"Dictionary"}))


# 6.    Prüfen auf gerade Zahl: Schreibe eine Funktion ist_gerade(n), 
#       die überprüft, ob eine Zahl gerade ist.

print("\nAufgabe 6\n")

def ist_gerade(n):
    if type(n)==int:
        if n%2==0:
            return f"Zahl {n} ist gerade."
        else:
            return f"Zahl {n} ist ungerade."
    return "Übergebener Wert ist keine Ganzzahl."

print(ist_gerade(4))
print(ist_gerade(5))
print(ist_gerade(5.5))


# 7.    Umkehrung eines Strings: Schreibe eine Funktion umkehren(s), 
#       die einen String umkehrt.

print("\nAufgabe 7\n")

def umkehren(s):
    if type(s)==str:
        return s[::-1]
    
# Alternativ:

def umkehrenA1(s):
    if type(s)==str:
        liste=[]
        for letter in s:
            liste.append(letter)
        liste.reverse()
        return "".join(liste)

    
print(umkehren("HAllo"))
print(umkehrenA1("HAllo"))


# 8.    Durchschnitt von drei Zahlen: Schreibe eine Funktion durchschnitt(a, b, c), 
#       die den Durchschnitt von drei Zahlen berechnet.

print("\nAufgabe 8\n")

def durchschnitt(a, b, c):
    return (a+b+c)/3

def durchschnitt(a, b):
    return (a+b)/2

print(durchschnitt(5,8))

print(durchschnitt(5,8,10))

