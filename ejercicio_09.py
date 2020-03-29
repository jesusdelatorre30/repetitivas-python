base = int(input("Introduzca la base de la potencia:"))
#Nos aseguramos de que el exponente sea positivo
while True:
	exponente = int(input("Introduzca el exponente de la potencia:"))
	if exponente<0:
		print("Lo siento, el exponente debe ser positivo")
	if exponente >= 0:
		break;
potencia = 1
for i in range(1, exponente + 1):
	potencia = potencia * base
print("Potencia:",potencia)



