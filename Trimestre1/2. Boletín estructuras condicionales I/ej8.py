estadoCivil=input("Cual es tu estado civil  (S-Soltero, C-Casado, V-Viudo o D-Divorciado): ").upper()
edad=input(int("Dame tu edad "))

if estadoCivil=="S" or estadoCivil=="D" and 0<=edad<35:
    print("Tu porcentaje de retención es de un 12%")
elif 50<=edad<=200:
    print("Tu porcentaje de retención es de un 8.5%")
elif estadoCivil=="V" or estadoCivil=="C" and edad<35:
    print("Tu porcentaje de retención es de un 11.3%")
else:
    print("Tu porcentaje de retención es de un 10.5%")