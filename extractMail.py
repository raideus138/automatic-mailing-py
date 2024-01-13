import pandas as pd

def ece(archivo_excel, nombre_columna):
    try:
        df = pd.read_excel(archivo_excel)
        columna = df[nombre_columna].tolist()
        return columna
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None

archivo_excel = 'ruta/del/archivo.xlsx'
nombre_columna = 'NombreDeLaColumna'

contenido_columna = ece(archivo_excel, nombre_columna)

if contenido_columna:
    print(f"Contenido de la columna '{nombre_columna}':")
    for elemento in contenido_columna:
        print(elemento)
else:
    print("No se pudo extraer el contenido de la columna.")
