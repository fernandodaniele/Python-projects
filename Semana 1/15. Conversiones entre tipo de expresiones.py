# Otra de las ventajas de Python es que de manera muy sencilla el lenguaje nos permite realizar:
# 1. Operaciones entre el mismo y distintos tipos de expresiones
# 2. Conversiones de un tipo de expresión a otra de manera muy sencilla.

# Ya abordamos ejemplos de como es que Python nos permite realizar operaciones entre enteros y flotantes.
# por ejemplo:

x = 2 + 1
print(x)
print(type(x))

x = 2 + (5 - 3j)
print(x)
print(type(x))

x = 2 + 1.0
print(x)
print(type(x))

# Ahora veremos el concepto y aplicación de concatenación.

# La concatenación es la unión de dos strings. Esta la podemos realizar mediante el operador de suma entre
# los strings indicados. Veamos un ejemplo.

x = 'Hola ' + 'desde ' + 'México'
print(x)
print(type(x))

# Para que sea posible realizar la concatenación, es necesario que sea de tipo string la expresión que
# se encuentra en la sentencia. Eso quiere decir que si intentamos concatenar un string con un entero, por ejemplo
# Python identificará un error en nuestro código. Vamos a realizarlo como ejemplo

#x = 'Hola' + '2'
#print(x)

# Para realizar conversiones debemos de utilizar la palabra reservada de python con la indica el tipo de expresión
# a manera de función. Por ejemplo:

x = 3
print(x)
print(type(x))

x = float(x)
print(x)
print(type(x))

x = 5.3
print(x)
print(type(x))

x = int(x)
print(x)
print(type(x))

x = '111'
print(x)
print(type(x))

x = int(x)
print(x)
print(type(x))

x = x + 3
print(x)