# Args und Kwargs (Argumente und Keyword- Argumente)
# um mehrere Argumente zu übernehmen

def aFunction(var, *args, **kwargs):
    '''
    Es muss nicht *args und **kwargs heißen, 
    wichtig sind die Sternchen.
    *args wird als Tupel interpretiert,
    **kwargs als Dictionary.
    '''
    print(f"Das ist die Variable: {var}.")
    print(f"Das ist das Args- Tupel: {args}")
    print(f"Das ist das Kwargs- Dictionary: {kwargs}")
    for value in kwargs.values():
        print(args[0]*value)

aFunction("Var", 5,"m",3.14, kwargs1 = "Hallo", kwargs2 = "Welt")

# Ende Args und Kwargs



# Lambda- Funktionen
# sind kurze, "anonyme" Funktionen
# Sie können an Ort und Stelle geschrieben und ausgeführt werden.


# Beispiele
greater0 = lambda x: x>0    # prüft, ob die Zahl größer 0 ist
mal2 = lambda y: y*2        # verdoppelt die Zahl

print((lambda z: z%2==0)(4))    # prüft, ob die Zahl in der letzten Klammer gerade ist
                                # beachte: z wurde an der Stelle definiert, wo sie gebraucht
                                # wurde

# Ende Lambda



# pass - um Funktionsdefinitionen zunächst offen zu lassen.

def anyFunction():
    pass

# Ende pass



# Verschachtelte Funktionen

def outerFunc(name):    
    def innerFunc():
        return name
    print("Hallo", innerFunc())

outerFunc("Stefan")

# Ende Verschachtelte Funktionen



# Namensräume

x=5                         # globale Variable x 

def scope():
    x=10                    # nichtlokal für Unterfunktionen, lokal scope()
    def glob():
        global x
        print(f"Globale Variable {x}")
    def nonloc():
        nonlocal x          # sucht in der übergeordneten Ebene, aber nicht global
        print(f"Nichtlokale Variable {x}")
    def loc():
        x=15                # lokal für loc() 
        print(f"Lokale Variable {x}")
    glob()                  # gibt die globale Variable aus
    nonloc()                # gibt die nichtlokale Variable aus
    loc()                   # gibt die lokale Variable aus
    
scope()

# Ende Namensräume


# all / any

daten = [0,1,0,5,0,60,74,32,5,6,-4,3,6,8,52,-12,1000]

# all
print("Alle Daten zwischen 0 und 100?")
print(all([(lambda x: x>0 and x<100)(x) for x in daten]))

# any
print("Gibt es Daten gleich 1000 oder drüber?")
print(any([(lambda x: x>=1000)(x) for x in daten]))

# filter
# filtert die Daten aus einer Datenreihe gemäß einer Funktion
daten1 = list(filter(lambda x: x>0 and x<100, daten))   
# übrig bleiben die Daten zwischen 0 und 100.
print(daten1)

daten2 = list(filter(lambda x: x<0 or x>=1000, daten))
# übrig bleiben die Daten kleiner 0 und größergleich 1000
print(daten2)

# map
# map wendet eine Funktion auf eine Datenreihe an
daten3 = list(map(lambda x: x>0 and x<100, daten))
# True, wenn 'daten' zwischen 0 und 100, sonst False
print(daten3)

daten4 = list(map(lambda x: x*2, daten))
# verdoppelt die Daten aus 'daten'
print(daten4)


