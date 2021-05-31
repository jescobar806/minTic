
key = "abcd"

while True:
    userKey = input ("Trata de adivinar la clave, ingresa el valor que crees correcto: ")


    if userKey != key:
        if userKey == "z":
            print ("Noo!! la clave no tiene z, Animo sigue intentando!")
        elif userKey == "e":
            print ("Noo!! la clave no tiene e, Animo sigue intentando!")
        elif userKey == "1":
            print ("Noo!! la clave no tiene números, Animo sigue intentando!")
        else:
            print ("No te dare pistas, Animo sigue intentando!")
    else:
        break