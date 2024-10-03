letra=input("Dame una letra ").upper()
print(letra)
if letra=="A":
    print("Es primera vocal (%s)"%letra)
elif letra=="E":
    print("Es segunda vocal (%s)"%letra)
elif letra=="I":
    print("Es tercera vocal (%s)"%letra)
elif letra=="O":
    print("Es cuarte vocal (%s)"%letra)
elif letra=="U":
    print("Es quinta vocal (%s)"%letra)
else:
    print("No es una vocal")