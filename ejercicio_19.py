while True:
    # mostrar menu
    print("Deportes")
    print("   1. Fútbol")
    print("   2. Baloncesto")
    print("   3. Tenis")
    print("   4. Padel")
    print("   5. Salir")
    # ingresar una opcion
    opcion = int(input("Elija una opción (1-5): "))
    # procesar esa opción
    if opcion == 1:
        print("Fútbol:")
        print(" - Barcelona")
        print(" - Real Madrid")
        print(" - Valencia")
    elif opcion == 2:
        print("Baloncesto:")
        print(" - Valladolid")
        print(" - Real Madrid")
        print(" - Valencia")
    elif opcion == 3:
        print("Tenis:")
        print(" - Barcelona")
        print(" - Real Madrid")
        print(" - Valencia")
    elif opcion == 4:
        print("Padel")
        print(" - Barcelona")
        print(" - Real Madrid")
        print(" - Valencia")
    elif opcion == 5:
        print("Cerrando sesión")
        break;
    else:
        print("Opción no válida")


