tiempo=int(input("¿Cuantos tiempo a durado la llamada?: "))
dia=input("Que dia es (L-M-X-J-V-S-D): ").upper()
if dia=="L" or dia=="M" or dia=="X" or dia=="J" or dia=="V" or dia=="S" or dia=="D" and tiempo>=0:
    
    if tiempo<=5:
        valor=1
    elif 5<tiempo<=8:
        valor=1.80
    elif 9<=tiempo<=10:
        valor=2.50
    elif 10<tiempo:
        valor=2.50+(tiempo-10)*0.50

    if dia=="D":
            print("Paga %s€"%(valor+valor*0.03))
    else:
        turno=input("Es turno de mañana o de tarde (M-T): ").upper()

        if turno=="M":
            print("Paga %s€"%(valor+valor*0.15))
        elif turno=="T":
            print("Paga %s€"%(valor+valor*0.10))

else:
    print("Datos invalidos")