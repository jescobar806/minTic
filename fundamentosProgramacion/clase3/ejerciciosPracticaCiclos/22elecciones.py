
contCandidato1= 0
contCandidato2= 0

while True:
    voto = int (input("Su voto es por el candidato 1 o 2, o ingrese 0 para salir: "))
    if voto != 1 and voto != 2 and voto !=0:
        print ("Candidato invalido")
    elif voto == 1:
        contCandidato1 = contCandidato1 + 1
    elif voto == 2:
        contCandidato2 = contCandidato2 + 1
    else:
        break
if contCandidato2 > contCandidato1:
    print("el ganador es el candidato 2")
elif contCandidato1 > contCandidato2:
    print ("El ganador es el candidato 1")
else:
    print ("Es un empate, esto se jodio!0")
