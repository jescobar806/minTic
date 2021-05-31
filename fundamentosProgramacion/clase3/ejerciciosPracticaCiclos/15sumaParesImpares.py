listOfNumbers = []
even = 0
odd = 0
cantidad = int (input("Ingrese la cantidad de números que contendra la lista: "))
contador = 0

while contador < cantidad:
    contador = contador + 1
    number = int(input("Favor ingrese un número: "))
    if number % 2 == 0:
        even = even + number
    else:
        odd = odd + number
print (f"La suma de pares ingresados es: {even} y la suma de impares ingresados es {odd}")