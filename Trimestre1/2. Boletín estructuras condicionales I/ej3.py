numero=int(input("Dame un numero "))

if numero%2==0 and not numero%3==0:
    print("El número %s es múltiplo de 2"%(numero))
elif numero%3==0 and not numero%2==0:
    print("El número %s es múltiplo de 3"%(numero))
elif numero%3==0 and numero%2==0:
    print("El número %s es múltiplo de 2 y de 3"%(numero))