
alfabeto = input("Ingrese el alfabeto a evaluar: ")
for i in range (0,len(alfabeto)):
    if alfabeto[i] != "a" and alfabeto[i] != "e" and alfabeto[i] != "i" and alfabeto[i] != "o" and alfabeto[i] != "u":
        print (alfabeto[i],"Consonante")
    else:
        print (alfabeto[i], "Vocal") 