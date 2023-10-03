def tribuono (edad, ingreso):
    if edad>16 and ingreso>=1000:
        print("Tienes que tributar")
    else:
        print("No tributas maquina")
        
edad=int(input("Dime tu edad en años: "))
ingreso=int(input("Dime cuanto ganas en euros: "))

tribuono(edad, ingreso)
