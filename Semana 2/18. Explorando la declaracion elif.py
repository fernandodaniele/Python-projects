# Habrá ocasiones en las que necesitaremos definir más de una condición en nuestro programa.
# Esto nos permitira decirle a la computadora cuál camino tomar dependiendo de los valores
# que se le presenten y por tanto podremos construir programas más complejos.

# Para lograr estos múltiples caminos utilizando varias condiciones necesitamos utilizar la declaración "elif".
# ¿Cómo funciona? bueno, vamos a poner un ejemplo muy simple acompañado de un diagrama de flujo.
# Ahora supongamos que queremos clasificar números, de tal forma que la computadora nos indique cuando tengamos un
# número positivo, un número nulo o uno negativo.
# Para ello podemos ocupar tres tipos de condiciones:
# 1. Si la variable es mayor que cero, entonces le indicaremos a la computadora que imprima "Es un entero positivo".
# 2. Si la variable es igual que cero, entonces el programa nos imprimirá "Es un entero nulo".
# 3. Por último, si el número es menor que cero, entonces imprimirá "Es un entero negativo".
# Para terminar el programa, le indicaremos que imprima la palabra "Fin".

# Entonces, nuestras condiciones son que nuestra variable sea mayor, igual o menor que cero y dependiendo de
# cuál sea el valor de mi variable será la acción que la computadora ejecutará.

# Vayamos a nuestra computadora para construir el programa, en esta ocasión utilizaremos de nuevo la función
# "input".

x = input("Introduce un número: ", )
x = int(x)
if x > 0:
    print("Es un entero positivo")
elif x == 0:
    print("Es un entero nulo")
elif x < 0:
    print("Es un entero negativo")
print("Fin")

## Esta es una manera alternativa para escribir el programa anterior.
x = input("Introduce un número: ", )
x = int(x)
if x > 0:
    print("Es un entero positivo")
elif x == 0:
    print("Es un entero nulo")
else:
    print("Es un entero negativo")
print("Fin")
