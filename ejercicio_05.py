while True:
    car=input("Introduce un carácter:")
    if len(car) == 1:
        break
while car !=" ":
    if car.upper() == "A" or car.upper() == "E" or car.upper() == "I" or car.upper() == "O" or car.upper() == "U": # si el caracter es igual a las vocales, entonces es  una vocal
        print("VOCAL")
    else:
        print("NO VOCAL") #Si no, no es vocal
    while True:
        car=input("Introduce un carácter:")
        if len(car) == 1:
            break


