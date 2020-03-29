import os
import time
for hora in range(0,24): #horas
	for minuto in range(0,60): #minutos
		for segundo in range(0,60): #segundos
			os.system("clear")
			print(hora,":",minuto,":",segundo)
			time.sleep(1) #va sumando 1 s



