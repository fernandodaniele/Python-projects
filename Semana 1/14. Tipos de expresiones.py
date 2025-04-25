# Python maneja distintos tipos de expresiones.
# En los videos pasados estuvimos manejando las expresiones numéricas, específicamente las
# de tipo entero y flotante, es decir "int" y "float".
# Además de estas expresiones, Python maneja una variada lista, estas son algunas de las fundamentales:

# Enteros: "int"
# Flotantes: "float"
# Complejos: "complex"
# Cadenas de caracteres "string"
# Booleanas "bool"

# Una de las ventajas de programa en Python es que el lenguaje reconoce automáticamente con qué tipo de expresiones
# estamos trabajando. A diferencia de Python, otros lenguajes requieren que el programador asigne el tipo
# a la expresión que manejará. Python hace esto por nosotors, por lo que nos permite construir código sin
# la necesidad de preocuparnos por definir tipos de expresiones.

# Existe en Python una función que nos permite identificar el tipo de alguna expresión, constante o variable. Esta
# función es la llamada "type()".

# Por ejemplo:

entero = 5
print(type(entero))

flotante = 8.45
print(type(flotante))

cadena_de_caracteres1 = "Azul"
print(type(cadena_de_caracteres1))

cadena_de_caracteres2 = 'Azul'
print(type(cadena_de_caracteres2))

complejo = 3 + 3j
print(type(complejo))

Booleano = (3 == 3)
print(Booleano)
print(type(Booleano))

Booleano = (3 == 5)
print(Booleano)
print(type(Booleano))