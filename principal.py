import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sqlite3

def configurar_controlador():
    """Configura y devuelve el controlador de Firefox."""
    driver = webdriver.Firefox()
    return driver

def abrir_sitio_web(driver, url):
    """Abre el sitio web especificado."""
    driver.get(url)
    time.sleep(5)  # Esperar unos segundos para cargar la página

def hacer_click_boton_actas(driver):
    """Hace clic en el botón ACTAS."""
    print('Click en el botón ACTAS')
    try:
        actas_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'ACTAS')]"))
        )
        actas_button.click()
    except Exception as e:
        print(f"Error al hacer clic en el botón ACTAS: {e}")
        driver.quit()
        exit()

def seleccionar_cod_acta(driver):
    """Selecciona el radio button Cod. Acta."""
    print('Esperando el radio button Cod. Acta')
    try:
        cod_acta_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[2]/div[1]/app-principal[1]/div[3]/div[1]/p-tabview[1]/div[1]/div[1]/p-tabpanel[2]/div[1]/app-acta[1]/div[1]/div[1]/form[1]/mat-radio-group[1]/div[1]/div[3]/mat-radio-button[1]/label[1]/div[1]/div[1]"))
        )
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cod_acta_button)).click()
    except Exception as e:
        print(f"Error al hacer clic en el radio button Cod. Acta: {e}")

def ingresar_codigo_acta(driver, codigo):
    """Ingresa el código del acta en el campo correspondiente."""
    input_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='______-_']")
    input_field.send_keys(codigo)

def hacer_click_boton_enviar(driver):
    """Hace clic en el botón de envío."""
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mat-raised-button.mat-button-base.mat-accent span.mat-button-wrapper"))
        )
        button.click()
        print("Botón clicado con éxito.")
    except Exception as e:
        print(f"Error al hacer clic en el botón: {e}")

def guardar_imagen(driver, codigo):
    """Guarda la imagen del acta en formato JPEG y retorna la ruta de la imagen."""
    time.sleep(2)
    try:
        img_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Acta']"))
        )
        img_src = img_element.get_attribute('src')
        
        if img_src.startswith('data:image/jpg;base64,'):
            base64_str = img_src.split(',')[1]
            image_data = base64.b64decode(base64_str)
            image_path = f'imagenes/acta_imagen_{codigo}.jpg'
            with open(image_path, 'wb') as f:
                f.write(image_data)
            print(f"Imagen guardada como '{image_path}'")
            return image_path  # Retornar la ruta de la imagen
        else:
            print("El formato de la imagen no es JPEG.")
            return None
    except Exception as e:
        print(f"Error al obtener la imagen: {e}")
        return None

def obtener_codigos_mesa():
    """Obtiene los códigos de mesa de la base de datos."""
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT CODIGO_MESA FROM votaciones")
    codigos = cursor.fetchall()
    conn.close()
    return [codigo[0] for codigo in codigos]  # Extraer los códigos de la lista de tuplas

def ruta_imagen_existente(codigo):
    """Verifica si la ruta de la imagen ya está guardada en la base de datos."""
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ruta_imagen FROM votaciones WHERE CODIGO_MESA = ?", (codigo,))
    ruta = cursor.fetchone()
    conn.close()
    
    # Retorna True si la ruta de la imagen no está vacía
    return ruta[0] is not None and ruta[0] != ""

def actualizar_ruta_imagen(codigo, ruta_imagen):
    """Actualiza la ruta de la imagen en la base de datos usando la consulta específica."""
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE votaciones SET ruta_imagen = ? WHERE CODIGO_MESA = ?", (ruta_imagen, codigo))
    conn.commit()
    conn.close()
    print(f"Ruta de imagen actualizada para el código {codigo}: {ruta_imagen}")

def mostrar_datos_mesa(codigo):
    """Muestra todos los datos de la mesa en la consola."""
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM votaciones WHERE CODIGO_MESA = ?", (codigo,))
    datos = cursor.fetchone()
    conn.close()

    if datos:
        # Obtener nombres de las columnas
        column_names = [description[0] for description in cursor.description]
        
        # Imprimir los datos con los nombres de las columnas
        for name, value in zip(column_names, datos):
            print(f"{name}: {value}")
        print("-" * 40)  # Separador para mejor legibilidad
    else:
        print(f"No se encontraron datos para el código de mesa: {codigo}")

def main():
    """Función principal que orquesta las operaciones."""
    driver = configurar_controlador()
    abrir_sitio_web(driver, 'https://computoalcaldes-int.oep.org.bo')
    hacer_click_boton_actas(driver)
    seleccionar_cod_acta(driver)
    
    # Obtener los códigos de mesa de la base de datos
    codigos_mesa = obtener_codigos_mesa()
    
    for codigo in codigos_mesa:
        if ruta_imagen_existente(codigo):  # Verificar si la ruta de imagen ya existe
            print(f"Saltando el código mesa {codigo}, ya tiene imagen.")
            continue  # Saltar al siguiente código

        mostrar_datos_mesa(codigo)  # Mostrar todos los datos de la mesa
        ingresar_codigo_acta(driver, str(codigo))
        hacer_click_boton_enviar(driver)
        ruta_imagen = guardar_imagen(driver, str(codigo))
        
        if ruta_imagen:
            actualizar_ruta_imagen(codigo, ruta_imagen)  
    
    print('Esperar unos segundos')
    time.sleep(10)
    
    print('Cerrar')
    driver.quit()

if __name__ == "__main__":
    main()
