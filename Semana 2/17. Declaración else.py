# Otra de las cosas que también podemos hacer en Python es indicar que sucederá si
# no se cumple la condición que asignamos en nuestra declaración.

# Para ello, ocupamos la instrucción "else". Esta declaración sigue casi la misma lógica que la instrucción "if",
# pero con un ligero cambio: No necesita de ningún operador lógico que defina una condición, es decir, no ocupamos
# ningún menor que, mayor que, igual que etc.

# El diagrama para la declaración else sería de la siguiente manera:
# Supongamos que definimos una variable con el valor de menos tres y le pedimos a la computadora que evalúe nuestra variable.
# La condición sería la siguiente: Si nuestra variable es menor que cero, entonces imprimirá "Es un número negativo".
# Si no cumple la condición, entonces, imprimirá la frase "No es un número negativo".
# Como se muestra en el diagrama, ahora si le estamos indicando a la computadora qué hacer si no se llegase a cumplir
# la condición.

# Vamos a nuestra computadora para ver el ejemplo.

x = -3
if x < 0:
    print("Es un número negativo")
else:
    print("No es un número negativo")
print("Fin")


x = 2
if x < 0:
    print("Es un número negativo")
else:
    print("No es un número negativo")
print("Fin")


NumPos = input("Ingresa un número positivo: ", )
NumPos = int(NumPos)
if NumPos > 0:
    print("Bien hecho")
else:
    print("No es un número positivo")
print("Fin")