import random
import time
print("--------------------Ruleta rusa--------------------")
jugadores=int(input("¿Cuantos jugadores sois? "))
respuesta= input("¿Quereis jugar todos? (S o N): ").upper()
numeros=[1,2,3,4,5,6]

if(jugadores<=1):
    print("Tiene que haber mas de un jugador")
else:
    while(respuesta=="S" and jugadores>1):
        num1=random.randint(1,len(numeros))
        numeros.pop(num1)
        print(" ")
        time.sleep(3)
        print("Cojes el arma")
        print(" ")
        time.sleep(3)
        print("Te la pones en la cabeza")
        print(" ")
        time.sleep(3)
        print("Y")
        print(" ")
        time.sleep(3)
        print("BANG!!!")
        if(num1!=3):
            time.sleep(5)
            print("Sigues vivo")
            print(" ")
            respuesta= input("¿Quereis seguir jugando? (S o N): ").upper()
        else:
            time.sleep(5)
            print("Has muerto")
            jugadores=jugadores-1
            numeros=[1,2,3,4,5,6]
            if(jugadores>1):
                respuesta= input("¿Quereis seguir jugando? (S o N): ").upper()
            elif(jugadores==1):
                print("Has ganado")
