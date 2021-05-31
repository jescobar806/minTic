
number1 = int(input("Ingrese el primer entero del rango: "))
number2 = int(input("Ingrese el segundo entero del rango: "))
suma = 0
for i in range (number1,number2+1):
    suma = suma + i
print (suma)