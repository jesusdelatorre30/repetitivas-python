suma = 0
contador =0

# Con el mientras si el primer número es 0 no va a entrar en el bucle
n=int(input("Número (0 para salir):"))
while n != 0:
	suma = suma + n
	contador = contador + 1
	num=int(input("Número (0 para salir):"))

# Si cont=0 no puedo realizar la división
if cont > 0:
	media = suma / contador
else:
	media = 0

print("Suma de los números introducidos:",suma)
print("Media de los números introducidos:",media)

