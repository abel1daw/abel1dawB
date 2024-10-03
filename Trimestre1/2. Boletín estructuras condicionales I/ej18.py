alumnos=int(input("¿Cuantos alumnos van?: "))

if alumnos>=100:
    print("Cada alumno paga 65€")
elif 50<=alumnos<=99:
    print("Cada alumno paga 70€")
elif 30<=alumnos<=49:
    print("Cada alumno paga 95€")
elif 0<alumnos<=29:
    print("Cada alumno paga %s€"%(4000/alumnos))