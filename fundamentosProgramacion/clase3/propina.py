
#Calculadora de propinas
#Pedir el valor de la factura
totalFactura = int(input('Ingrese el valor total de la factura: '))
#Pedir el % de propina a dar
valorPropina= int(input('Ingrese el valor que quiere dar de propina: '))
#calcular la propina
propina = (totalFactura * valorPropina)/100
#Imprimir el valor
print (f"El valor de la propina es : {propina} pesos")