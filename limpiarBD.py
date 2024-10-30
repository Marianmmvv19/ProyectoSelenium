import sqlite3

def limpiar_ruta_imagen():
    """Limpia el campo ruta_imagen en la tabla votaciones."""
    # Conectar a la base de datos
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()

    try:
        # Actualizar el campo ruta_imagen a una cadena vacía
        cursor.execute("UPDATE votaciones SET ruta_imagen = ''")
        conn.commit()  # Confirmar cambios
        print("Campo ruta_imagen limpiado exitosamente.")
    except Exception as e:
        print(f"Error al limpiar el campo ruta_imagen: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == "__main__":
    limpiar_ruta_imagen()
