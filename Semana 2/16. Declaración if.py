# Las declaraciones en Python son instrucciones en código que utilizamos para decirle a la computadora
# lo que debe de hacer. En esta ocasión, abordaremos las declaraciones que ocupamos en Python para
# indicar una condición en el programa.

# Python nos permite construir programas que cuenten con condiciones, es decir, le podemos decir a la
# computadora qué hacer si ocurre una u otra cosa, o si se nos presenta una variable con un valor u otro.

# La declaración "if" es la condicional que ocupamos para indicar lo anterior. Esto se puede representar a través
# del siguiente diagrama de flujo.

# Supongamos que tenemos una variable cuyo valor es igual a 3 y queremos indicar a la computadora una condición.
# Si la variable es menor que cero, entonces el programa nos imprimirá la frase "Es un número negativo". Por último,
# acabaremos el programa imprimiento la palabra "Fin".

# Vamos a nuestra computadora a escribir esta condicional y explicar la sintaxis de la declaración en Python.

x = -3
if x < 0:
    print("Es un número negativo")
print("Fin")

x = 1
if x < 0:
    print("Es un número negativo")
print("Fin")

Num = input("Ingresa un número: ", )
Num = int(Num)
if Num > 0:
    print("Es un número positivo")
print("Números positivos consultados:", NumPos)
print("Fin")


