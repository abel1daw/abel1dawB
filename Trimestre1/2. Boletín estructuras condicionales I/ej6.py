numero1=int(input("Dame el primer numero "))
numero2=int(input("Dame el segundo numero "))

if numero2%numero1==0 or numero1%numero2==0:
    print("Un numero es multiplo de otro")
else:
    print("Ninguno es multiplo de ninguno")