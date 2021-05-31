
currentSalary = float (input("Ingrese el salario actual del empleado: "))
performance = int (input("Por favor ingrese 1 si el desempeño del empleado es excelente, 2 si es bueno o 3 si es regular: "))

if performance >= 1 and performance <=3:
    if performance == 1:
        newSalary = currentSalary + currentSalary * 0.06
    elif performance == 2:
        newSalary = currentSalary + currentSalary * 0.04
    else:
        newSalary = currentSalary + currentSalary * 0.015
    print (newSalary)
else:
    print ("El valor ingresado para el desempeño es incorrecto")
