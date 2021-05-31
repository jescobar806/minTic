winner1 = 0
winner2 = 0
while True:
    movPlayer1= input ("Jugador 1, digite su jugada (R:piedra,P:papel,S:tijeras): ")
    if (movPlayer1 != "R" and movPlayer1 != "P" and movPlayer1 != "S"):
        print ("Jugada incorrecta!")

    movPlayer2= input ("Jugador 2, digite su jugada (R:piedra,P:papel,S:tijeras): ")
    if (movPlayer2 != "R" and movPlayer2 != "P" and movPlayer2 != "S"):
        print ("Jugada incorrecta!")

    if movPlayer1 == "R" and movPlayer2 == "S":
        winner1 = winner1 + 1
    elif movPlayer1 == "R" and movPlayer2 == "P":
        winner2 = winner2 + 1
    elif movPlayer1 == "P" and movPlayer2 == "S":
        winner2 = winner2 + 1
    elif movPlayer1 == "P" and movPlayer2 == "R":
        winner1 = winner1 + 1
    elif movPlayer1 == "S" and movPlayer2 == "R":
        winner2 = winner2 + 1
    elif movPlayer1 == "S" and movPlayer2 == "P":
        winner1 = winner1 + 1
    if winner2 == 3 or winner1 == 3:
        break
if winner1 > winner2:
    print ("Ganó el jugador 1")
elif winner1 < winner2:
    print ("Ganó el jugador 2")
else:
    print("Es un empate")
