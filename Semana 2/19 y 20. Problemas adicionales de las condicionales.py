# Una consideración importante al momento de utilizar la declaración "elif" es que nuestro programa se saldrá del
# bucle una vez que encuentre la condicional verdadera para nuestra variable.
# Volvamos al primer ejemplo: Recuerda que nuestro programa evalua linea por linea las instrucciones.
# Si nosotros ingresamos el número 0, nuestro programa evaluará la primer condicional como falsa e ignorará
# su contenido. Después, evaluará la segunda condicional como verdadera, por tanto ejecutará lo escrito
# en esta condicional y una vez terminado ignorará evaluar el número en la tercera condicional, dirigiéndose
# hasta la última instrucción. Lo mismo sucede si evaluáramos con algún número mayor a cero, como el 5.
# Nuestro programa evaulará la primer condición como verdadera y ejecutará lo contenido en esta condicional, ignornado después
# las otras dos y dirigiéndose hasta la última instrucción.

# Tomando lo anterior, te presento el siguiente programa:

x = input("Escribe un número entero: ",)
x = int(x)
if x > 10:
    print("Se ejecutó la primer condicional")
elif x > 0:
    print("Se ejecutó la segunda condicional")
elif x >= 5:
    print("Se ejecutó la tercer condicional")
else:
    print("Se ejecutó la cuarta condicional")
print("Fin")

# La pregunta sería, ¿Habrá alguna condicional que nunca se ejecutará?
# Piénsalo y nos vemos en el siguiente video.
