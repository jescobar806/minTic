
sales = float(input("Ingrese el total de ventas del empleado: "))

if sales < 5000000:
    comision = sales * 0.05
elif sales >= 5000000 and sales < 15000000:
    comision = sales * 0.075
elif sales >= 15000000 and sales < 30000000:
    comision = sales * 0.115
elif sales >= 30000000 and sales < 55000000:
    comision = sales * 0.15
else:
    comision = 3050000 + 0.075 * (sales - 55000000)
print (comision)