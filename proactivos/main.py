import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Variables globales
tabla_final = pd.DataFrame()
tabla_filtrada = pd.DataFrame()

# Función para cargar los datos y generar la tabla cruzada
def cargar_datos():
    global tabla_final

    # Cargar los archivos Excel
    detalle_por_mac = pd.read_excel("Detalle por MAC.xlsx")
    table_rank_devices = pd.read_excel("table_rank_devices.xlsx")

    # Rellenar celdas vacías con el texto "Sin bloque"
    detalle_por_mac.fillna("Sin bloque", inplace=True)

    # Renombrar columnas para facilitar el cruce de datos
    detalle_por_mac.rename(columns={"MAC": "mac_upper"}, inplace=True)

    # Unir ambas tablas en base a las columnas de MAC
    tabla_cruzada = table_rank_devices.merge(
        detalle_por_mac,
        left_on="mac",
        right_on="mac_upper",
        how="inner"
    )

    # Crear la columna "Direccion completa"
    tabla_cruzada["Direccion completa"] = (
        tabla_cruzada["direccion_calle"].astype(str) + " " + tabla_cruzada["direccion_altura"].astype(str)
    )

    # Seleccionar y reorganizar columnas según la solicitud
    columnas_seleccionadas = [
        "dt_week", "base", "mac", "mac_upper", "observado_saludred", "Zona",
        "Elemento", "Direccion completa", "direccion_calle", "direccion_altura",
        "US", "OFDMA", "DS", "OFDM"
    ]
    tabla_final = tabla_cruzada[columnas_seleccionadas]

# Función para obtener los valores seleccionados en un Listbox
def obtener_seleccionados(listbox):
    seleccionados = [listbox.get(i) for i in listbox.curselection()]
    if "Todos" in seleccionados:
        return None  # Seleccionar todos
    return seleccionados

# Función para actualizar los valores de los Listbox
def actualizar_filtros():
    for col, listbox in zip(["US", "OFDMA", "DS", "OFDM"], [us_listbox, ofdma_listbox, ds_listbox, ofdm_listbox]):
        # Incluir valores únicos y "Todos"
        valores = sorted(tabla_final[col].dropna().unique().tolist())
        valores = ["Todos"] + valores
        listbox.delete(0, tk.END)
        for valor in valores:
            listbox.insert(tk.END, valor)

# Función para aplicar los filtros y actualizar la tabla
def aplicar_filtros():
    global tabla_filtrada
    tabla_filtrada = tabla_final.copy()

    # Aplicar filtros de los listbox
    filtros = {
        "US": obtener_seleccionados(us_listbox),
        "OFDMA": obtener_seleccionados(ofdma_listbox),
        "DS": obtener_seleccionados(ds_listbox),
        "OFDM": obtener_seleccionados(ofdm_listbox)
    }

    for columna, valores in filtros.items():
        if valores is not None:  # Si no se selecciona "Todos"
            tabla_filtrada = tabla_filtrada[tabla_filtrada[columna].isin(valores)]

    # Mostrar mensaje de éxito
    messagebox.showinfo("Filtrado", f"Se aplicaron los filtros. La tabla ahora tiene {len(tabla_filtrada)} filas.")

# Función para guardar el archivo filtrado
def guardar_archivo():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        tabla_filtrada.to_excel(file_path, index=False)
        messagebox.showinfo("Archivo Guardado", f"El archivo filtrado se guardó en:\n{file_path}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cruce iDocsis - CEI")
root.geometry("800x600")

# Crear widgets para los filtros
tk.Label(root, text="Filtros:").pack(pady=10)

frame_filtros = tk.Frame(root)
frame_filtros.pack(pady=10)

# Función corregida para crear listboxes con `grid`
def crear_listbox(parent, label_text, row, col):
    tk.Label(parent, text=label_text).grid(row=row, column=col, padx=5, pady=5)
    listbox = tk.Listbox(parent, selectmode="multiple", height=8, exportselection=False)
    listbox.grid(row=row+1, column=col, padx=5, pady=5)
    return listbox

# Crear listboxes para los filtros
us_listbox = crear_listbox(frame_filtros, "US", 0, 0)
ofdma_listbox = crear_listbox(frame_filtros, "OFDMA", 0, 1)
ds_listbox = crear_listbox(frame_filtros, "DS", 0, 2)
ofdm_listbox = crear_listbox(frame_filtros, "OFDM", 0, 3)

# Botón para aplicar filtros
tk.Button(root, text="Aplicar Filtros", command=aplicar_filtros, bg="lightblue").pack(pady=10)

# Botón para guardar el archivo filtrado
tk.Button(root, text="Guardar Archivo", command=guardar_archivo, bg="lightgreen").pack(pady=10)

# Cargar los datos después de definir los Listbox
cargar_datos()
actualizar_filtros()

# Iniciar la aplicación
root.mainloop()
