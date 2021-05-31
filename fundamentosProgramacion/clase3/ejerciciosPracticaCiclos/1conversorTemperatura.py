
temperatura = (input("Ingrese 1 si desea convertir de Fº a Cº o 2 si desea convertir de Cº a Fº: "))
grados = int (input ("Favor ingrese el valor de la temperatura a convertir: "))

if temperatura == 1:
    gradosResultantes = (grados * 9/5) + 32
    print (f"La temperatura dada en ºF es : {gradosResultantes} ºC")
else:
    gradosResultantes = (grados -32) *5/9
    print (f"La temperatura dada en ºC es : {gradosResultantes} ºF")
