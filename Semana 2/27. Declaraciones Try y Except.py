while True:
    x = input("Escribe un número: ", )
    if x == "Finalizar":
        break
    try:
        x = int(x)
        if x > 0:
            print("Es un entero positivo")
        elif x == 0:
            print("Es un entero nulo")
        elif x < 0:
            print("Es un entero negativo")
        print("Escribe ""Finalizar"" para terminar el programa")
    except:
        print("Respuesta no válida, intenta de nuevo")
print("Fin del programa, gracias por participar")