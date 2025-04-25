# Nombre del archivo de entrada
nombre_archivo = "archivo.txt"

# Lista para almacenar las líneas que cumplen con el criterio
lineas_filtradas = []

# Abrir el archivo en modo lectura
with open(nombre_archivo, 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()

    # Iterar a partir de la segunda línea
    for linea in lineas[1:]:
        # Dividir la línea en columnas usando la tabulación como separador
        columnas = linea.split('\t')

        # Verificar si la segunda columna comienza con "CPA"
        if len(columnas) > 1 and columnas[1].startswith("CPA"):
            # Agregar la línea a la lista de líneas filtradas
            lineas_filtradas.append(linea)

# Nombre del archivo de salida
nombre_archivo_salida = "resultados.txt"

# Abrir el archivo de salida en modo escritura
with open(nombre_archivo_salida, 'w') as archivo_salida:
    # Escribir las líneas filtradas en el archivo de salida
    archivo_salida.writelines(lineas_filtradas)

print("Proceso completado. Las líneas que comienzan con 'CPA' se han guardado en", nombre_archivo_salida)