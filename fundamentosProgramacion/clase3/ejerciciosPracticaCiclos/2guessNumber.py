
guess = 4
userNumber = 0

while userNumber != guess:
    userNumber = int (input("Ingrese el número entre 0 y 9 que cree es el correcto: "))
    if userNumber < 0 or userNumber > 9:
        print ("El número debe estar entre 0 y 9")
print ("Well guessed!!")