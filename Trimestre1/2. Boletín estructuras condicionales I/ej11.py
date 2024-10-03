tipoProducto=input("Dame el tipo del producto (A,B o C): ").upper()
precioOriginal=float(input("Dame el precio del producto: "))

if tipoProducto=="A" and precioOriginal>0:
    print("Su precio sera de %s €"%(precioOriginal*0.93))
elif tipoProducto=="C" or precioOriginal<500 and 0<precioOriginal:
    print("Su precio sera de %s €"%(precioOriginal*0.88))
elif tipoProducto=="B" and 0<precioOriginal:
    print("Su precio sera de %s €"%(precioOriginal*0.91))
else:
    print("Tipo o precio invalido")