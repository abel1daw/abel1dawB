lado1=int(input("Primer lado: "))
lado2=int(input("Segundo lado: "))
lado3=int(input("Tercer lado: "))

if lado1==lado2 and lado1==lado3:
    print("Es triángulo equilátero")
elif lado3**2==lado1**2+lado2**2 or lado2**2==lado3**2+lado1**2 or lado1**2==lado2**2+lado3**2:
    print("Es triángulo rectángulo")
elif (lado1==lado2 and lado1!=lado3) or (lado2==lado3 and lado2!=lado1)or (lado3==lado1 and lado3!=lado1):
    print("Es triángulo isósceles")
else:
    print("Es triángulo escaleno")