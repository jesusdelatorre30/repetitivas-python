horas_acum = 0
trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?:"))
sueldo_por_hora = float(input("Introduzca el sueldo por hora:"))
for trabajador in range(1, trabajadores + 1):
	horas_por_semana = int(input("¿Cuántas horas ha trabajado el trabajador %d ?:" % trabajador))
	horas_acum = horas_acum + horas_por_semana
	print("El trabajador %d tiene de sueldo %f" % (trabajador,horas_por_semana*sueldo_por_hora))
print("El pago a los %d trabajadores es: %f" % (trabajadores,horas_acum*sueldo_por_hora))


