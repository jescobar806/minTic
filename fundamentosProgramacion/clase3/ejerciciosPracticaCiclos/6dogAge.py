
dogAge = float (input ("Ingrese la edad del perro en años: "))

if dogAge > 2:
    humanAge = (dogAge - 2) * 4 + (2 * 10.5)
else:
    humanAge = dogAge * 10.5
print (f"La edad de su perro en años humanos es: {humanAge}")