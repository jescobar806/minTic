
numberOfPeople = int (input("Por favor indique el número de personas: "))
edad = 0
for i in range (0,numberOfPeople):
    edad = edad + int (input ("Por favor ingrese la edad de la persona: "))
print (f"El promedio de edad es: {edad/numberOfPeople}")