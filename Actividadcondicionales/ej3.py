def dosnumero (numero1, numero2):
    
    if numero1<numero2:
        print("el primero es menor")
    elif numero1==numero2:
        print("Son iguales")
    else:
        print("el segundo es menor")
        
numero1=int(input("Dime un número:"))
numero2=int(input("Dime otro número:"))

dosnumero(numero1, numero2)
