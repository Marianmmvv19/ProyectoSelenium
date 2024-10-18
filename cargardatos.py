import sqlite3
import csv

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('datos_electorales.db')
c = conn.cursor()

# Crear tabla si no existe
c.execute('''
CREATE TABLE IF NOT EXISTS elecciones (
    codigo_mesa TEXT,
    descripcion TEXT,
    codigo_pais TEXT,
    nombre_pais TEXT,
    codigo_departamento TEXT,
    nombre_departamento TEXT,
    codigo_provincia TEXT,
    nombre_provincia TEXT,
    codigo_seccion TEXT,
    nombre_municipio TEXT,
    codigo_localidad TEXT,
    nombre_localidad TEXT,
    codigo_recinto TEXT,
    nombre_recinto TEXT,
    numero_mesa TEXT,
    inscritos_habilitados INTEGER,
    mnr INTEGER,
    mas_ips INTEGER,
    libres INTEGER,
    mts INTEGER,
    fri INTEGER,
    voces INTEGER,
    voto_valido INTEGER,
    voto_blanco INTEGER,
    voto_nulo INTEGER,
    voto_emitido INTEGER,
    voto_valido_sistema INTEGER,
    voto_emitido_sistema INTEGER,
    ruta_imagen TEXT
)
''')

# Leer el archivo CSV
with open('ES2022_ALC_SCZ_20241105_191731_4223632839711807990.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        # Añadir un valor por defecto para ruta_imagen
        row['ruta_imagen'] = 'ruta/por/defecto.jpg'  # Puedes personalizar esto
        c.execute('''
        INSERT INTO elecciones (codigo_mesa, descripcion, codigo_pais, nombre_pais, codigo_departamento,
                                nombre_departamento, codigo_provincia, nombre_provincia, codigo_seccion,
                                nombre_municipio, codigo_localidad, nombre_localidad, codigo_recinto,
                                nombre_recinto, numero_mesa, inscritos_habilitados, mnr, mas_ips, libres,
                                mts, fri, voces, voto_valido, voto_blanco, voto_nulo, voto_emitido,
                                voto_valido_sistema, voto_emitido_sistema, ruta_imagen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (row['CODIGO_MESA'], row['DESCRIPCION'], row['CODIGO_PAIS'], row['NOMBRE_PAIS'],
         row['CODIGO_DEPARTAMENTO'], row['NOMBRE_DEPARTAMENTO'], row['CODIGO_PROVINCIA'],
         row['NOMBRE_PROVINCIA'], row['CODIGO_SECCION'], row['NOMBRE_MUNICIPIO'], 
         row['CODIGO_LOCALIDAD'], row['NOMBRE_LOCALIDAD'], row['CODIGO_RECINTO'], 
         row['NOMBRE_RECINTO'], row['NUMERO_MESA'], row['INSCRITOS_HABILITADOS'], 
         row['MNR'], row['MAS-IPSP'], row['LIBRES'], row['MTS'], row['FRI'], 
         row['VOCES'], row['VOTO_VALIDO'], row['VOTO_BLANCO'], row['VOTO_NULO'], 
         row['VOTO_EMITIDO'], row['VOTO_VALIDO_SISTEMA'], row['VOTO_EMITIDO_SISTEMA'],
         row['ruta_imagen']))

# Guardar (commit) los cambios y cerrar la conexión
conn.commit()
conn.close()
print("Datos cargados exitosamente en la base de datos.")
