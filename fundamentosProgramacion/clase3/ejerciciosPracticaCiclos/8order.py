
numero = []

for i in range (0,4):
    numero.append(int(input("Ingrese un número: ")))
if numero[0] < numero[1] < numero[2] < numero [3]:
        orden = 1
elif numero[0]> numero[1] > numero[2] > numero[3]:
    orden = 2
else:
    orden = 3
if orden == 1:
    print ("Esta ordenado de forma ascendente")
elif orden == 2:
    print ("Esta ordendo de forma descendente")
else:
    print("No tiene orden")
            