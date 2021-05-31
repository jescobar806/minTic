
listOfNumbers = []
even = 0
odd = 0

while True:
    number = int(input("Favor ingrese un número, o para dejar de ingresar números ingrese 0: "))
    if number == 0:
        break
    listOfNumbers.append(number)
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print (f"El número de pares ingresados es: {even} y el número de impares ingresados es {odd}")

