# LC = List Comprehension


# 1: Die Listen 4_1 und 4_2 enthalten einen gemeinsamen Floatwert. Liste 4_3 soll
# bis zu diesem Wert nur die Werte aus Liste 4_1 und ab diesem Wert nur Werte aus Liste 2 enthalten.
# Tipp: Wandle die Werte in einen String um und wende die String- Methode isdecimal() an. 

print("Aufgabe 1")
liste1_1=[50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 1.1, 100, 101, 102, 103, 104]
liste1_2=[76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 1.1, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148]

ind1_1=0
ind1_2=0
for x in liste1_1:
    if str(x).isdecimal():
        ind1_1=liste1_1.index(x)
for x in liste1_2:
    if str(x).isdecimal():
        ind4_1=liste1_2.index(x)
liste1_3=liste1_1[:ind4_1]+liste1_2[ind1_2:]
print(liste1_3)


# 2 Erzeuge eine Liste bis 100, in der statt einer durch 5 teilbaren Zahl eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [[0],1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

print("Aufgabe 2\n")
import random
liste2=[x for x in range(100)]

tmpList=[]
listeOfFive=[]

for x in liste2:    
    if x%5==0:
        tmpList.append(liste2[x])
        listeOfFive.append(tmpList.copy())  # Hier Kopie statt Original, weil Listen mutable!
    else:
        listeOfFive.append(liste2[x])

print(listeOfFive)

# Alternativ per Funktion und LC:

"""
def listOf5(x):
    tmpList=[]
    if x%5==0:
        for x in range(x+1):
            if x%5==0:
                tmpList.append(x)
        return tmpList
    else:
        return x
    
listeOfFive=[listOf5(x) for x in range(100)]
"""

# 3 Erzeuge ein Liste aus zufälligen 3-stelligen Zahlen (random Modul). Entferne von jeder die erste und die dritte Ziffer und quadriere die mittlere.
# Tipp: Wandle die Werte in einen String und dann in eine Liste um.

print("Aufgabe 3\n")
liste3=[random.randint(100, 999) for x in range(10)]
print(liste3, "\n")
liste3squared=[(int(list(str(x))[1]))**2 for x in liste3]

# liste6squared=[((x-(x//100*100))//10)**2 for x in liste6]     # Alternative Gordon

# alternativ: Funktion schreiben und in LC verwenden
""" def keepMiddleAndSquareIt(num):
    listOfNum=list(str(num)) # str: "345" -> list: ['3','4','5']
    return int(listOfNum[1])**2 # int: 4 ->**2: 16

liste6squared=[keepMiddleAndSquareIt(x) for x in liste6] """

print("\ngeaenderte Liste:\n", liste3squared, "\n")


# 4 Schreibe einen Algorithmus zum Lotto- Spielen (6 aus 49)
# Die Ziehungen sollen n-mal wiederholt werden und dabei die 
# 3er, 4er, 5er und 6er gezählt und im Anschluss ausgegeben werden

import random


lotto=[x for x in range(1, 50)]
tip = [5,18,29,45,37,7]
t3=0
t4=0
t5=0
t6=0
for n in range(1000000):
    ziehung=random.sample(lotto, 6)
    treffer = 0
    for zahl_t in tip:
            if zahl_t in ziehung:
                  treffer+=1
    match treffer:
        case 3:
            t3+=1
        case 4:
            t4+=1
        case 5:
            t5+=1
        case 6:
            t6+=1
print(f"Dreier: {t3}, Vierer: {t4}, Fünfer: {t5}, Sechser: {t6}")

#4 Erzeuge die Liste [[[1,2,3],[4,5,6],[7,8,9]], [10,11,12],[13,14,15],[16,17,18]], [18,20,21],[22,23,24],[25,26,27]]]
#   mittels LC

liste4=[[[i+1+j*3+k*9 for i in range(3)] for j in range(3)] for k in range(3)]
# liste7 = [[i, i+1, i+2] for i in range(1, 28, 3)]     # Alternative Silvio
# liste7=[[[ z+y*3+x*9 for z in range(1,4) ]for y in range(3) ] for x in range(3)]      # Alternative Gordon
print("Aufgabe 7\n")
print(liste4)