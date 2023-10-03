def diasdelasemana (diadesemana):
    if (diadesemana=="lunes"):
        print("Que pereza")
    elif (diadesemana=="viernes"):
        print("Hoy ya si")
    elif (diadesemana=="sabado" or diadesemana=="domingo"):
        print("Que buen finde")
    else: 
        print("Ya queda menos para el finde")
        
diadesemana=str(input("Dime un día de la semana en minusculas: "))

diasdelasemana(diadesemana)
        
