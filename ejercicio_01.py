factorial = 1;
n=int(input("Dime un número:"))
contador = 2;
while contador <= n:
	factorial = factorial * contador;
	contador = contador + 1;
print("El resultado de ",n,"! es", factorial)