while True:
    x = input("Escribe un número: ", )
    if x == "Finalizar":
        break
    x = int(x)
    if x > 0:
        print("Es un entero positivo")
    elif x == 0:
        print("Es un entero nulo")
    elif x < 0:
        print("Es un entero negativo")
    else:
        print("Respuesta no válida, intenta de nuevo")
    print("Escribe ""Finalizar"" para terminar el programa")
print("Fin del programa, gracias por participar")