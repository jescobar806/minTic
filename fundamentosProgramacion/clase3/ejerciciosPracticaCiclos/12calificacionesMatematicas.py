
countAprove = 0
countFail = 0
notaAprove = 0
notaFail = 0

while True:
    nota = float (input ("Ingrese la nota obtenida, o -1 para salir: "))

    if nota != -1:
        if nota >= 3 and nota <= 5:
            countAprove = countAprove + 1
            notaAprove = notaAprove + nota
        elif nota >= 0 and nota < 3:
            countFail = countFail + 1
            notaFail = notaFail + nota
        else:
            print ("La nota no es correcta!")
    else:
        break
print(f"La cantidad de estudiantes que aprobaron matematicas es {countAprove} con una nota promedio de {notaAprove/countAprove}")
print(f"La cantidad de estudiantes que reprobaron matematicas es {countFail} con una nota promedio de {notaFail/countFail}")
