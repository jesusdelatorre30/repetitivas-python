import random
intentos = 10;
nsecreto  =  random.randint(1,100);#un número aleatorio
ningresado = int(input("Introduzca un número (de 1 a 100):"))

while nsecreto != ningresado and intentos>1: #Si el numero secreto no es igual al numero ingresado y todavia tenemos intentos, se repite la siguiente estructura
    if nsecreto > ningresado:
        print("Muy bajo, vuelva a intentarlo")
    else: 
        print("Muy alto, vuelva a intentarlo")
    intentos  =  intentos-1;
    print("Le quedan ",intentos," intentos")
    ningresado = int(input("Introduzca un número (de 1 a 100):"))

if num_secreto == num_ingresado: #si el numero secreto es el introducido, realizará la siguiente estructura
    print("Enhorabuena! Usted adivino en ",11-intentos," intentos.")
else:
    print("Lo siento, el numero era: ",num_secreto)
