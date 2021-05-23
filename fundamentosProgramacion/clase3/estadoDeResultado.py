
#Pedir al usuario los ingresos
ingresos = float(input('Favor diligenciar sus ingresos: '))

#Pedir al usuario los costos
costos = float (input('Favor ingresar sus costos: '))

#Calcular la utilidad bruta
utilidadBruta = ingresos - costos

#Pedir al usuario los gastos
gastos= float (input('Favor ingresar sus gastos: '))

#Calcular la utilidad operativa
utilidadOperativa = utilidadBruta - gastos

#Calcular el impuesto a la renta
impuestoRento = utilidadOperativa * 0.3

# Calcular utilidad neta
utilidadNeta = utilidadOperativa - impuestoRento

print (f"Su utilidad bruta es: {utilidadBruta}")
print (f"Su utilidad operativa es: {utilidadOperativa}")
print (f"Su utilidad impuesto es: {impuestoRento}")
print (f"Su utilidad neta es: {utilidadNeta}")