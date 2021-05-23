#Calculadora de propinas
#Pedir el valor de la factura
totalFactura = int(input('Ingrese el valor total de la factura: '))
#Pedir el % de propina a dar
valorPropina= int(input('Ingrese el valor que quiere dar de propina: '))

#Calcular el iva
totalIva = totalFactura * 0.19

#calcular el subtotal de la factura
subTotal= totalFactura - totalIva

#calcular la propina
propina = (subTotal * valorPropina)/100
#Imprimir el valor
print (f"El valor de la propina es : {propina} pesos")
print (f"IVA: {totalIva}")
print (f"Valor total factura: {totalFactura}")
print (f"Valor del subtotal {subTotal}")
print (f"Valor total a pagar {subTotal + totalIva}")