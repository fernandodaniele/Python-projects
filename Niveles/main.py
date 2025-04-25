# import tkinter as tk
# from tkinter import filedialog
#
# def leer_archivo(ruta_archivo):
#     # Nombre del archivo de entrada
#     #nombre_archivo = "Niveles_Crudo.txt"
#
#     # Lista para almacenar las líneas que cumplen con el criterio
#     lineas_filtradas = []
#
#     palabras_filtro = ["CPA", "FRA", "VMA", "VNU", "JMA", "COS", "LFA"]
#
#     # Abrir el archivo en modo lectura
#     with open(ruta_archivo, 'r') as archivo:
#
#         # Leer todas las líneas del archivo
#         lineas = archivo.readlines()
#
#         lineas_filtradas.append(lineas[0])
#
#         # Iterar a partir de la segunda línea
#         for linea in lineas[1:]:
#             # Dividir la línea en columnas usando la tabulación como separador
#             columnas = linea.split('\t')
#
#             # Verificar si la segunda columna comienza con "CPA"
#             if len(columnas) > 1 and any(columnas[1].startswith(palabra) for palabra in palabras_filtro):
#                 # Agregar la línea a la lista de líneas filtradas
#                 lineas_filtradas.append(linea)
#
#     # Nombre del archivo de salida
#     nombre_archivo_salida = "niveles.txt"
#
#     # Abrir el archivo de salida en modo escritura
#     with open(nombre_archivo_salida, 'w') as archivo_salida:
#         # Escribir las líneas filtradas en el archivo de salida
#         archivo_salida.writelines(lineas_filtradas)
#
#     mensaje_var.set("Tarea finalizada.\n Se ha creado el archivo " + nombre_archivo_salida)
#
# def abrir_archivo():
#     # Diálogo para seleccionar el archivo
#     ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
#
#     if ruta_archivo:
#         mensaje_var.set("Leyendo el archivo...\nProcesando archivo...\n")
#         ventana.update()
#         # Llama a la función para leer el archivo
#         leer_archivo(ruta_archivo)
#
# # Crear la ventana principal
# ventana = tk.Tk()
# ventana.title("Filtro de niveles HFC Medi Norte")
#
# # Ajustar el tamaño de la ventana
# ventana.geometry("400x200")  # Puedes cambiar las dimensiones según tus preferencias
#
#
# # Variable para almacenar mensajes dinámicos
# mensaje_var = tk.StringVar()
#
# # Crear una etiqueta para mostrar mensajes
# etiqueta_mensaje = tk.Label(ventana, textvariable=mensaje_var)
# etiqueta_mensaje.pack()
#
# # Crear un marco para contener los botones y centrarlos
# marco_botones = tk.Frame(ventana)
# marco_botones.pack(pady=10)  # Espacio en la parte inferior del marco
#
# # Crear un botón para abrir el archivo
# boton_abrir = tk.Button(marco_botones, text="Abrir Archivo", command=abrir_archivo)
# boton_abrir.pack(side=tk.TOP, pady=25)  # Espacio a la izquierda del botón
#
# # Crear un botón para salir
# boton_salir = tk.Button(marco_botones, text="Salir", command=ventana.destroy)
# boton_salir.pack(side=tk.BOTTOM, pady=10)  # Espacio a la derecha del botón
#
# # Iniciar el bucle principal de la interfaz gráfica
# ventana.mainloop()
import tkinter as tk
from tkinter import filedialog

def leer_archivo(ruta_archivo, palabras_filtro):
    lineas_filtradas = []

    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

        lineas_filtradas.append(lineas[0])

        for linea in lineas[1:]:
            columnas = linea.split('\t')

            if len(columnas) > 1 and any(columnas[1].startswith(palabra) for palabra in palabras_filtro):
                lineas_filtradas.append(linea)

    nombre_archivo_salida = "niveles.txt"

    with open(nombre_archivo_salida, 'w') as archivo_salida:
        archivo_salida.writelines(lineas_filtradas)

    mensaje_var.set("Tarea finalizada.\n Se ha creado el archivo " + nombre_archivo_salida)

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    if ruta_archivo:
        mensaje_var.set("Leyendo el archivo...\nProcesando archivo...\n")
        ventana.update()
        palabras_filtro = entrada_palabras_filtro.get().split(",")  # Obtener palabras filtro desde la entrada de texto
        leer_archivo(ruta_archivo, palabras_filtro)

ventana = tk.Tk()
ventana.title("Filtro de niveles HFC Medi Norte")
ventana.geometry("400x250")

mensaje_var = tk.StringVar()
etiqueta_mensaje = tk.Label(ventana, textvariable=mensaje_var)
etiqueta_mensaje.pack()

marco_entrada = tk.Frame(ventana)
marco_entrada.pack(pady=10)

etiqueta_palabras_filtro = tk.Label(marco_entrada, text="HUBs a filtrar (separados por comas):")
etiqueta_palabras_filtro.pack(side=tk.LEFT)

entrada_palabras_filtro = tk.Entry(marco_entrada, width=30)
entrada_palabras_filtro.pack(side=tk.LEFT)

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)

boton_abrir = tk.Button(marco_botones, text="Abrir Archivo", command=abrir_archivo)
boton_abrir.pack(side=tk.TOP, pady=10)

boton_salir = tk.Button(marco_botones, text="Salir", command=ventana.destroy)
boton_salir.pack(side=tk.BOTTOM, pady=10)

ventana.mainloop()