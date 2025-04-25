# El bucle while nos permite utilizar de una condicional para entrar en un conjunto de repeticiones.
# Si la condiconal cumple, entonces el programa ejecutará lo escrito en la sangría debajo del while y seguirá
# ejecutándose hasta que la condición sea falsa, entonces el programa saldrá del bucle.
# Si no se cumple, entonces el programa ignorará el contenido dentro del bucle
# y continuará evaluando las demás líneas de código.

# Veamos el ejemplo:

x = 1
while x <= 4:
    print("Iteración número:", x)
    x = x + 1
print("Iteración terminada")
