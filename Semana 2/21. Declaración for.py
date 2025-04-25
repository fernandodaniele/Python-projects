# Python nos permite construir programas que cuenten con repeticiones de un proces en específico.
# Esto tiene múltiples aplicaciones, nos puede ayudar a evaluar los valores dentro de una lista
# o a construir una repetición infinita de tal forma que un proceso de instrucciones siempre
# se encuentre activo. A este tipo de repeticiones se le llama "bucles" y existen dos fundamentales en programación,
# el bucle "for" y el "while". Conoceremos las características, parámetros y aplicaciones de cada uno.
# Comencemos con el bucle for.

# La declaración "for" nos permite construir bucles definiendo una variable inicial y final dentro de sus parámetros

# Vayamos a nuestra computadora para trabajar con el ejemplo de hoy:

for x in [1, 2, 3, 4]:
    print("La posición actual del bucle es:", x)
print("Bucle terminado")

for x in range(1, 5):
    print("La posición actual del bucle es:", x)
print("Bucle terminado")


