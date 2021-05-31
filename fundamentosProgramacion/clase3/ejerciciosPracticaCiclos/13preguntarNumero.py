suma = 0
while True:
    number = float(input("Ingrese un número: "))
    suma = suma + number
    if number < 0:
        break
print (suma)