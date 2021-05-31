
temperature = float (input("Por favor ingrese la temperatura: "))
if temperature > 95 or temperature < 20:
    tempRange = False
else:
    tempRange = True

if tempRange == True:
    if temperature >= 80:
        print ("Te recomendamos practicar natación")
    elif temperature >= 60 and temperature < 80:
        print ("Te recomendamos practicar tennis")
    elif temperature >= 40 and temperature < 60:
        print ("Te recomendamos practicar golf")
    elif temperature < 40:
        print ("Te recomendamos practicar ski")
else:
    print("Visita nuestras tiendas!!")