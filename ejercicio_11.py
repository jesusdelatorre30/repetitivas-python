es_primo = True
numero_es_primo = int(input("Introduzca un número para comprobar si es primo:"))
for num in range(2, numero_es_primo):
	if numero_es_primo % num == 0: #Un número es primo si es divisible entre él mismo y la unidad
		es_primo = False
if es_primo:
	print("Es Primo")
else:
	print("No es Primo")

