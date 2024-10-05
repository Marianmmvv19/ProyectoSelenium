import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el controlador de Firefox (geckodriver debe estar en el PATH)
driver = webdriver.Firefox()

# Abrir el sitio web
driver.get('https://computoalcaldes-int.oep.org.bo')

# Esperar unos segundos para ver los resultados
time.sleep(5)
print('Click en el botón ACTAS')

# Esperar hasta que el botón "ACTAS" esté presente y clicable, luego hacer clic
try:
    actas_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'ACTAS')]"))
    )
    actas_button.click()
except Exception as e:
    print(f"Error al hacer clic en el botón ACTAS: {e}")
    driver.quit()
    exit()

# Esperar hasta que el radio button "Cod. Acta" esté presente en el DOM
print('Esperando el radio button Cod. Acta')
try:
    # Esperar la presencia del elemento específico utilizando el XPath proporcionado
    cod_acta_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[2]/div[1]/app-principal[1]/div[3]/div[1]/p-tabview[1]/div[1]/div[1]/p-tabpanel[2]/div[1]/app-acta[1]/div[1]/div[1]/form[1]/mat-radio-group[1]/div[1]/div[3]/mat-radio-button[1]/label[1]/div[1]/div[1]"))
    )

    # Asegurar que el botón esté clicable antes de hacer clic
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[2]/div[1]/app-principal[1]/div[3]/div[1]/p-tabview[1]/div[1]/div[1]/p-tabpanel[2]/div[1]/app-acta[1]/div[1]/div[1]/form[1]/mat-radio-group[1]/div[1]/div[3]/mat-radio-button[1]/label[1]/div[1]/div[1]"))).click()
except Exception as e:
    print(f"Error al hacer clic en el radio button Cod. Acta: {e}")
    
# Encontrar el campo de entrada por el placeholder
input_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='______-_']")

# Ingresar el valor "7000561" en el campo de entrada
input_field.send_keys("7000561")    


# Intentar hacer clic en el botón
try:
    # Esperar hasta que el botón esté presente y clicable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mat-raised-button.mat-button-base.mat-accent span.mat-button-wrapper"))
    )
    button.click()
    print("Botón clicado con éxito.")
except Exception as e:
    print(f"Error al hacer clic en el botón: {e}")

# Guardar la imagen del acta
try:
    # Esperar hasta que la imagen esté presente
    img_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Acta']"))
    )
    
    # Obtener el atributo 'src' de la imagen
    img_src = img_element.get_attribute('src')

    # Asegurarse de que el src sea en formato base64
    if img_src.startswith('data:image/jpg;base64,'):
        # Extraer la parte base64 del string
        base64_str = img_src.split(',')[1]

        # Decodificar la imagen de base64
        image_data = base64.b64decode(base64_str)

        # Guardar la imagen como archivo JPEG
        with open('acta_image.jpg', 'wb') as f:
            f.write(image_data)

        print("Imagen guardada como 'acta_image.jpg'")
    else:
        print("El formato de la imagen no es JPEG.")
except Exception as e:
    print(f"Error al obtener la imagen: {e}")
    
    

print('Esperar unos segundos')
# Esperar unos segundos
time.sleep(10)

print('Cerrar')
# Cerrar el navegador
driver.quit()
