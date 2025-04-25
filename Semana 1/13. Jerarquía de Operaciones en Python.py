## Al igual que en matemáticas, Python cuenta con una jerarquía al momento de realizar operaicones
## Es decir, el lenguaje sigue un orden definido para efectuar las operaciones que le pidamos.

## El orden es como sigue:

## Por orden de importancia tenemos primero a:

## Paréntesis: ( )
## Potenciación: **
## Multiplicación: *
## División: /
## Suma: +
## Resta: -

# Por lo que el programa siempre buscará primero el operador de paréntesis y si lo encuentra, entonces ejecutará
## la operación que se encuentra entre ellos.

# Después se irá por los demás operadores.

# Veamos un ejemplo

x = 1 + 4 * 2
print(x)

x = 5 ** 2 + 10 * 3
print(x)

x = 20 / 2 - 4 * 6
print(x)

x = 3 * 2 + 5 - (4 + 6) / 2
print(x)

