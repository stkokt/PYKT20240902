# import ...    Modulimporte

# class         Klassendefinitionen

class Auto():
    autocounter=0   # statische Variable/ Klassenvariable
    def printCounter(): # statische Funktion/ Klassenfunktion
        if Auto.autocounter > 1:
            print(f"Es sind {Auto.autocounter} Autos auf den Straßen.") 
        elif Auto.autocounter == 1:
            print("Es ist nur ein Auto auf den Straßen.")  
        else: print("Es sind keine Autos mehr auf den Straßen.")

    def __init__(self, spd, make="Auto", maxP=4):
        self.marke=make
        self.geschwindigkeit=spd
        self.maxPassenger=maxP
        Auto.autocounter+=1

    def __del__(self):
        del self
        Auto.autocounter-=1

    def __add__(self, _):
        return self.maxPassenger + _.maxPassenger
    
    def __gt__(self, _):
        if self.maxPassenger > _.maxPassenger:
            return True
        else: return False

    def __repr__(self):
        return f"Auto {self.marke}, {self.maxPassenger}"
    
    def __str__(self):
        return f"Auto vom Typ {self.marke}"
    
    def tolleFunktion(self):
        print("Ich bin eine tolle Methode.")

    def fahren(self):
        print("Auto fährt.")

class PKW(Auto):
    pass

class LKW(Auto):
    def __init__(self,spd, make="LKW", maxP=1):
        super().__init__(self, spd)
        self.maxLoad=1000


    def fahren(self, p=True):
        if p:
            print("LKW macht BrummBrumm.")
        else:
            Auto.fahren(self)


# def           Funktionsdefinitionen

def tolleFunktion():
    print("Ich bin eine tolle Funktion.")

if __name__ == "__main__":

    bmw=Auto(100)
    bmw.marke="BMW"
    print(bmw.marke)
    trabant=Auto(0, maxP=3)
    print(trabant.marke)
    trabant.marke="Trabant"
    print(trabant.marke)
    print(bmw.marke)
    trabant.marke="trabbi"

    print(trabant.marke)
    bmw.autocounter=3
    print(Auto.autocounter)

    print(Auto.autocounter)

    print(bmw)

    print(bmw>trabant)
    trabant
    Auto.printCounter()
    tolleFunktion()

    bmw={"marke":"BMW", "Geschwindigkeit":100}

    brummi = LKW("Brummi",100)
    brummi.maxLoad = 2000
    print(brummi.maxLoad, Auto.autocounter)

    brummi.fahren(p=False)
    print(LKW.mro()) # Method Resolution Order
    print(type(brummi))










