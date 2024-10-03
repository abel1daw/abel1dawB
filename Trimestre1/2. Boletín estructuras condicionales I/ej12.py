num1=int(input("Dame un numero "))
caracter=(input("Dame un caracter "))
num2=int(input("Dame otro numero "))

if caracter=="+":
    print(num1+num2)
elif caracter=="*":
    print(num1*num2)
elif caracter=="-":
    print(num1-num2)
elif caracter=="/":
    print(num1/num2)
elif caracter=="%":
    print(num1%num2)
else:
    print(("%s"+caracter+"%s")%(num1,num2))