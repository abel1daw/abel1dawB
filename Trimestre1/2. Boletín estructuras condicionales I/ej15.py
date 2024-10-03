base=int(input("Dame la base: "))
exponente=int(input("Dame el exponente: "))

if exponente<0:
    exponente=exponente*-1
    print("1/%s"%base**exponente)
else:
    print(base**exponente)