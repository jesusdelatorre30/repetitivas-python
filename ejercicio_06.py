n1 = int(input("Introduce el número 1:"))
n2 = int(input("Introduce el número 2:"))
if n1 % 2 == 1: #Si el resto es distinto de 0 entonces es impar
	n1 = n1 + 1;
for n in range(n1, n2 + 1, 2):
		print(n," ",end="")


