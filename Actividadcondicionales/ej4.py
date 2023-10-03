def tresnumerosmayor (numero1, numero2, numero3):
    
    if numero1>numero2 and numero1>numero3:
        print("El primer numero es el mayor")
    elif numero2>numero1 and numero2>numero3:
        print("El segundo numero es el mayor")
    else: print("El tercer numero es el mayor")
    
numero1=int(input("Dime el primer numero: "))
numero2=int(input("Dime el segundo numero: "))
numero3=int(input("Dime el tercer numero: "))
    
tresnumerosmayor(numero1, numero2, numero3)
    