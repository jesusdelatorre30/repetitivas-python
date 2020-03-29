cont_negativos = 0
cont_positivos = 0
cont_ceros = 0
cantidad_num=int(input("¿Cuántos números vas a introducir?:"))
for i in range(1,cantidad_num + 1):
	print("Número ",i,":",end="");
	num=int(input(""))
	if num>0: #Si el número es mayor que cero, entonces el contador de positivos suma 1
		cont_positivos = cont_positivos + 1
	else:
		if num<0:
			cont_negativos = cont_negativos + 1  #Si el número es menor que cero, entonces el contador de negativos suma 1
		else:
			cont_ceros = cont_ceros + 1 #Si el número es cero, se suma 1 al contador de ceros

print("Números positivos:",cont_positivos);
print("Números negativos:",cont_negativos);
print("Números igual a 0:",cont_ceros);


