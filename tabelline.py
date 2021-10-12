import random

def checkInput(strInput, strError) :
    goodinput = False
    while goodinput == False:
        try :
            intInput = int(input(strInput))
            goodinput = True
        except :
            print(strError)
    return(intInput)

def tabellina():
    punti = 0
    
    volte = checkInput("Quanti tentativi? ","inserire un numero")
    
    for i in range(0,volte):
        
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = a * b
        d = None
        
        while c!= d :
            d = checkInput("Quanto fa {0} * {1}? ".format(a,b),"inserire un numero")
            if c == d :
                print("OK")
                punti += 1
            else:
                print("Riprova")
                punti -= 1
    
    print("Alla prossima")
    print("Punteggio finale {0} {1}".format(punti,"bene"))

if __name__ == '__main__' : tabellina()


