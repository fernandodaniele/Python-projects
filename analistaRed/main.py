import pandas as pd
from datetime import datetime

# Cargar el archivo Excel
archivo_excel = 'Detalle.xlsx'
df = pd.read_excel(archivo_excel)

# Verificar las columnas del DataFrame original
print(df.columns)

# Crear la tabla de doble entrada
tabla_entrada = df.pivot_table(index='Zona', columns='OFDMA', values='MAC', aggfunc='count', fill_value=0)

# Calcular el total de cada fila
tabla_entrada['total_fila'] = tabla_entrada.sum(axis=1)

# Calcular los porcentajes
tabla_entrada['% OK'] = tabla_entrada['OK'] / tabla_entrada['total_fila'] * 100
tabla_entrada['% PS/CER/CCER'] = tabla_entrada['PS/CER/CCER'] / tabla_entrada['total_fila'] * 100
tabla_entrada['% SCORE'] = tabla_entrada['SCORE'] / tabla_entrada['total_fila'] * 100

# Ordenar las filas por el porcentaje de PS/CER/CCER de mayor a menor
tabla_entrada = tabla_entrada.sort_values(by='% PS/CER/CCER', ascending=False)

# Obtener la fecha actual en formato "DD.MM.YY"
fecha_hoy = datetime.today().strftime('%d.%m.%y')

# Para las primeras 10 filas de la tabla ordenada
for i, (index, row) in enumerate(tabla_entrada.head(10).iterrows()):
    # Obtener el valor de "Zona" y "% PS/CER/CCER"
    elemento = row.name
    porcentaje_ps_cer_ccer = row['% PS/CER/CCER']

    # Obtener la cantidad de PS/CER/CCER (valor en la columna 'PS/CER/CCER')
    ps_cer_ccer_count = row['PS/CER/CCER']

    # Obtener el total de la fila
    total_fila = row['total_fila']

    # Filtrar el DataFrame original para encontrar los MACs correspondientes a este Zona y a 'PS/CER/CCER' en la columna OFDMA
    macs = df[(df['Zona'] == elemento) & (df['OFDMA'] == 'PS/CER/CCER')]['MAC'].tolist()

    # Crear el listado de MACs como una cadena
    listado_macs = ', '.join(macs) if macs else 'Ninguno'

    # Crear el párrafo con la cantidad de PS/CER/CCER y el total
    parrafo = f"SALUD DE RED {elemento}. VERIFICAR INGRESO DE RUIDO. HAY {ps_cer_ccer_count} DE {total_fila} OBSERVADOS POR PS/CER/CCER ({porcentaje_ps_cer_ccer:.2f}%). MACS TESTIGO {listado_macs}. REF DANIELE {fecha_hoy}"

    # Imprimir el párrafo
    print(parrafo)

