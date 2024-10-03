numero1=float(input("Dame el primero de los cuatro numeros "))
numero2=float(input("Dame el segundo de los cuatro numeros "))
numero3=float(input("Dame el tercero de los cuatro numeros "))
numero4=float(input("Dame el cuarto de los cuatro numeros "))

total=numero1+numero2+numero3+numero4
contador=0
numerosMay=""
if numero1 > total/4:
    numerosMay="%s "%numero1
    contador+=1
if numero2 > total/4:
    numerosMay=numerosMay+"%s "%numero2
    contador+=1
if numero3 > total/4:
    numerosMay=numerosMay+"%s "%numero3
    contador+=1
if numero4 > total/4:
    numerosMay=numerosMay+"%s "%numero4
    contador+=1

print("Numeros: %s, %s, %s, %s ⇒ La media es %s y hay %s número/s superior a la media: %s"%(numero1,numero2,numero3,numero4,total/4,contador,numerosMay))
