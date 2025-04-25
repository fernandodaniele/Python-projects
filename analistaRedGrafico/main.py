import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Cargar el archivo Excel
archivo_excel = 'Detalle por MAC.xlsx'
df = pd.read_excel(archivo_excel)

# Configurar columnas para combinaciones
zonas_columnas = ['Zona', 'Elemento']
bloque_columnas = ['US', 'OFDM', 'DS', 'OFDMA']
problema_columnas = ['PS/CER/CCER', 'SCORE']

# Función para generar tablas basadas en los umbrales seleccionados
def generar_tablas():
    try:
        porcentaje_umbral = float(porcentaje_var.get())
        cantidad_umbral = int(cantidad_var.get())

        resultados = []
        for zona in zonas_columnas:
            for bloque in bloque_columnas:
                for problema in problema_columnas:
                    # Crear tabla dinámica
                    tabla = df.pivot_table(
                        index=zona,
                        columns=bloque,
                        values='MAC',
                        aggfunc='count',
                        fill_value=0
                    )

                    # Calcular totales y porcentajes
                    #tabla['total_fila'] = tabla.sum(axis=1)
                    #if problema in tabla.columns:
                    #    tabla[f'% {problema}'] = (
                    #        tabla[problema] / tabla['total_fila'].replace(0, 1) * 100
                    #    )
                    # Calcular totales y porcentajes
                    tabla['total_fila'] = tabla.sum(axis=1)
                    if problema in tabla.columns:
                        tabla[f'% {problema}'] = (
                                (tabla[problema] / tabla['total_fila'].replace(0, 1) * 100)
                                .astype(int)  # Redondear al entero más cercano
                        )

                    # Aplicar filtros según los umbrales
                    tabla_filtrada = tabla[
                        (tabla[f'% {problema}'] >= porcentaje_umbral) & (tabla[problema] >= cantidad_umbral)
                    ]

                    # Si no hay filas que cumplan el criterio, omitir la tabla
                    if tabla_filtrada.empty:
                        continue

                    # Ordenar la tabla por cantidad
                    tabla_filtrada = tabla_filtrada.sort_values(by=problema, ascending=False)

                    # Formatear el resultado
                    #resultados.append(
                        #f"TABLA PARA ZONA: {zona}, BLOQUE: {bloque}, PROBLEMA: {problema}\n"
                    #    f"{tabla_filtrada}\n"
                    #    f"{'-'*80}\n"
                    #)

                    # Formatear la tabla con el signo % al final de las líneas después de la segunda
                    filas = tabla_filtrada.to_string().splitlines()
                    for i in range(2, len(filas)):  # A partir de la tercera línea
                        filas[i] += " %"  # Agregar el signo %

                    # Combinar las filas formateadas y añadirlas a los resultados
                    resultados.append(
                        f"{'-' * 80}\n"
                        + "\n".join(filas)  # Combinar las filas modificadas
                        + f"\n{'-' * 80}\n"
                    )

        # Mostrar los resultados en el área de texto izquierdo
        resultado_tablas_texto.delete(1.0, tk.END)
        if resultados:
            resultado_tablas_texto.insert(tk.END, "\n".join(resultados))
        else:
            resultado_tablas_texto.insert(tk.END, "No se encontraron tablas que cumplan con los criterios.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


import pandas as pd


# Función para generar informes con todas las combinaciones posibles
def generar_informes():
    try:
        porcentaje_umbral = float(porcentaje_var.get())
        cantidad_umbral = int(cantidad_var.get())

        # Abrir el archivo Excel con pandas
        df_devices = pd.read_excel('table_rank_devices.xlsx')

        # Convertir las columnas a minúsculas para evitar problemas de mayúsculas/minúsculas
        df_devices['mac'] = df_devices['mac'].str.lower()
        df_devices['direccion_calle'] = df_devices['direccion_calle'].fillna('')
        df_devices['direccion_altura'] = df_devices['direccion_altura'].fillna(
            0)  # Asegurarse que dirección_altura tenga valores numéricos

        resultados = []
        fecha_hoy = datetime.today().strftime('%d.%m.%y')
        parrafos = []  # Lista para almacenar párrafos con cantidad

        for zona in zonas_columnas:
            for bloque in bloque_columnas:
                for problema in problema_columnas:
                    # Crear tabla dinámica
                    tabla = df.pivot_table(
                        index=zona,
                        columns=bloque,
                        values='MAC',
                        aggfunc='count',
                        fill_value=0
                    )

                    # Calcular totales y porcentajes
                    tabla['total_fila'] = tabla.sum(axis=1)
                    if problema in tabla.columns:
                        tabla[f'% {problema}'] = (
                                tabla[problema] / tabla['total_fila'].replace(0, 1) * 100
                        )

                    # Aplicar filtros según los umbrales
                    tabla_filtrada = tabla[
                        (tabla[f'% {problema}'] >= porcentaje_umbral) & (tabla[problema] >= cantidad_umbral)
                        ]

                    # Si no hay filas que cumplan el criterio, omitir la tabla
                    if tabla_filtrada.empty:
                        continue

                    # Ordenar la tabla por cantidad y tomar un máximo de 30 filas
                    tabla_filtrada = tabla_filtrada.sort_values(by=problema, ascending=False).head(30)

                    # Formatear el resultado en párrafos
                    for index, row in tabla_filtrada.iterrows():
                        elemento = row.name
                        problema_count = row.get(problema, 0)
                        total_fila = row['total_fila']
                        porcentaje_problema = row.get(f'% {problema}', 0)

                        # Filtrar MACs correspondientes
                        macs_filtrados = df[(df[zona] == elemento) & (df[bloque] == problema)]["MAC"].tolist()

                        # Buscar las direcciones para cada MAC en el archivo Excel
                        macs_con_direccion = []
                        for mac in macs_filtrados:
                            # Convertir MAC a minúsculas para comparar
                            mac_lower = mac.lower()
                            device_info = df_devices[df_devices['mac'] == mac_lower]

                            if not device_info.empty:
                                direccion_calle = device_info['direccion_calle'].iloc[0]
                                direccion_altura = int(
                                    device_info['direccion_altura'].iloc[0])  # Asegurarse que sea un número entero
                                macs_con_direccion.append((mac, direccion_calle, direccion_altura))
                            else:
                                macs_con_direccion.append((mac, 'Dirección no encontrada', ''))

                        # Ordenar primero por direccion_calle, luego por direccion_altura
                        macs_con_direccion.sort(key=lambda x: (x[1], x[2]))

                        # Crear el listado de MACs con direcciones
                        #listado_macs_con_direccion = ', '.join(
                        #    [
                        #        f"{mac} ({direccion_calle} {direccion_altura})" if direccion_calle != 'Dirección no encontrada' else f"{mac} (Dirección no encontrada)"
                        #        for mac, direccion_calle, direccion_altura in macs_con_direccion]
                        #) if macs_filtrados else 'Ninguno'

                        # Crear el listado de direcciones
                        ultima_calle = None
                        direcciones = []
                        for _, direccion_calle, direccion_altura in macs_con_direccion:
                            if direccion_calle == 'Dirección no encontrada':
                                direcciones.append('S/D')
                            elif direccion_calle == ultima_calle:
                                direcciones.append(f"{direccion_altura}")
                            else:
                                direcciones.append(f"{direccion_calle} {direccion_altura}")
                                ultima_calle = direccion_calle

                        listado_direcciones = ', '.join(direcciones)

                        # Crear el listado de MACs
                        listado_macs = ', '.join([mac for mac, _, _ in macs_con_direccion])

                        # Combinar ambos listados
                        listado_macs_con_direccion = f"{listado_direcciones}, {listado_macs}" if macs_filtrados else 'Ninguno'

                        #parrafo = (
                        #    f"SALUD DE RED {elemento}. VERIFICAR BLOQUE {bloque}. "
                        #    f"HAY {int(porcentaje_problema)}% ({int(problema_count)} DE {int(total_fila)}) OBSERVADOS POR {problema}. "
                        #    f"TESTIGOS {listado_macs_con_direccion}. REF DANIELE {fecha_hoy}"
                        #)

                        if bloque in ["OFDMA"] or ["US"] and problema in ["PS/CER/CCER"]:
                            parrafo = (
                                f"SALUD DE RED {elemento}. VERIFICAR RUIDO EN BLOQUE {bloque} DE x HS A x HS. "
                                f"HAY {int(porcentaje_problema)}% ({int(problema_count)} DE {int(total_fila)}) OBSERVADOS. "
                                f"TESTIGOS {listado_macs_con_direccion}. REF DANIELE {fecha_hoy}"
                            )
                        elif bloque in ["OFDMA"] or ["US"] and problema == "SCORE":
                            parrafo = (
                                f"SALUD DE RED {elemento}. CM CON TX ALTO/BAJO - VAR TX - VAR DE SNR - CAIDA DE SNR EN BLOQUE {bloque}."
                                f"HAY {int(porcentaje_problema)}% ({int(problema_count)} DE {int(total_fila)}) OBSERVADOS. "
                                f"TESTIGOS {listado_macs_con_direccion}. REF DANIELE {fecha_hoy}"
                            )
                        elif bloque in ["OFDM"] or ["DS"] and problema == "SCORE":
                            parrafo = (
                                f"SALUD DE RED {elemento}. CM CON RX ALTO/BAJO - MER BAJA - VARIACION DE MER EN BLOQUE {bloque}. "
                                f"HAY {int(porcentaje_problema)}% ({int(problema_count)} DE {int(total_fila)}) OBSERVADOS. "
                                f"TESTIGOS {listado_macs_con_direccion}. REF DANIELE {fecha_hoy}"
                            )
                        else:
                            parrafo = (
                                f"SALUD DE RED {elemento}. VERIFICAR {problema} EN BLOQUE {bloque}. "
                                f"HAY {int(porcentaje_problema)}% ({int(problema_count)} DE {int(total_fila)}) OBSERVADOS. "
                                f"TESTIGOS {listado_macs_con_direccion}. REF DANIELE {fecha_hoy}"
                            )

                        # Almacenar el párrafo y la cantidad
                        parrafos.append((parrafo, problema_count))

        # Ordenar los párrafos por la cantidad de observaciones (de mayor a menor)
        parrafos_ordenados = sorted(parrafos, key=lambda x: x[1], reverse=True)

        # Mostrar los resultados en el área de texto derecho
        resultado_texto.delete(1.0, tk.END)
        if parrafos_ordenados:
            resultado_texto.insert(tk.END, "\n\n".join([parrafo for parrafo, _ in parrafos_ordenados]))
        else:
            resultado_texto.insert(tk.END, "No se encontraron combinaciones que cumplan con los criterios.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Informes de Red")
ventana.geometry("1200x700")

# Dividir la ventana en dos frames
frame_izquierdo = tk.Frame(ventana, padx=10, pady=10)
frame_derecho = tk.Frame(ventana, padx=10, pady=10)
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Widgets en el frame izquierdo
ttk.Label(frame_izquierdo, text="Umbral de % de CM observados:").pack()
porcentaje_var = tk.StringVar(value="10")
porcentaje_entry = ttk.Entry(frame_izquierdo, textvariable=porcentaje_var)
porcentaje_entry.pack()

ttk.Label(frame_izquierdo, text="Umbral de cantidad de CM observados:").pack()
cantidad_var = tk.StringVar(value="3")
cantidad_entry = ttk.Entry(frame_izquierdo, textvariable=cantidad_var)
cantidad_entry.pack()

ttk.Button(frame_izquierdo, text="Generar Tablas", command=generar_tablas).pack(pady=10)

# Área de texto en el frame izquierdo
resultado_tablas_texto = tk.Text(frame_izquierdo, wrap="word")
resultado_tablas_texto.pack(fill=tk.BOTH, expand=True, pady=10)

# Widgets en el frame derecho
resultado_texto = tk.Text(frame_derecho, wrap="word")
resultado_texto.pack(fill=tk.BOTH, expand=True, pady=10)

generar_boton = ttk.Button(frame_derecho, text="Generar Informe", command=generar_informes)
generar_boton.pack(pady=10)

ventana.mainloop()