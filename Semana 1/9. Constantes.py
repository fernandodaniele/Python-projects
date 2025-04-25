#Ejemplos de constantes
#Se utilizan las palabras en mayusculas
PORT_DB_SERVER = 3307
USER_DB_SERVER = "root"
PASSWORD_DB_SERVER = "123456"
DB_NAME = "cursos"
#Palabras reservadas
import keyword
#Validadción de palabras reservadas
x = keyword.iskeyword('as')
print(x)

y = keyword.iskeyword('s')
print(y)

print(keyword.kwlist)