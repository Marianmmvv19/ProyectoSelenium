import pandas as pd
import sqlite3

# Cargar el archivo CSV
csv_file = 'computo.csv'  # Cambia esto por la ruta de tu archivo CSV
data = pd.read_csv(csv_file)

# Agregar la columna 'ruta_imagen' con datos nulos
data['ruta_imagen'] = None  # Agrega la nueva columna con valores NULL

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('votaciones.db')  # Puedes cambiar el nombre del archivo de la base de datos

# Guardar los datos en una tabla llamada 'votaciones'
data.to_sql('votaciones', conn, if_exists='replace', index=False)

# Cerrar la conexión
conn.close()

print("Datos cargados exitosamente en la base de datos SQLite.")
