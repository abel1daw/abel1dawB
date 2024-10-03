dosEuros=int(input("¿Cuantas monedas de dos euros tienes?: "))
unEuros=int(input("¿Cuantas monedas de un euro tienes?: "))
cincuentaCent=int(input("¿Cuantas monedas de cincuenta centimos tienes?: "))
veinteCent=int(input("¿Cuantas monedas de veinte centimos tienes?: "))
diezCent=int(input("¿Cuantas monedas de diez centimos tienes?: "))

centimos=(cincuentaCent*50)+(veinteCent*20)+(diezCent*10)
euros=((dosEuros*2)+unEuros)

total=euros+(centimos*0.01)

print(total,"€")