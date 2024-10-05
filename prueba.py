import base64
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el controlador de Firefox (geckodriver debe estar en el PATH)
options = webdriver.FirefoxOptions()
options.set_preference("devtools.console.stdout.content", True)  # Para ver la salida de la consola en la consola del script
driver = webdriver.Firefox(options=options)

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
    cod_acta_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[2]/div[1]/app-principal[1]/div[3]/div[1]/p-tabview[1]/div[1]/div[1]/p-tabpanel[2]/div[1]/app-acta[1]/div[1]/div[1]/form[1]/mat-radio-group[1]/div[1]/div[3]/mat-radio-button[1]/label[1]/div[1]/div[1]"))
    )
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/div[2]/div[1]/app-principal[1]/div[3]/div[1]/p-tabview[1]/div[1]/div[1]/p-tabpanel[2]/div[1]/app-acta[1]/div[1]/div[1]/form[1]/mat-radio-group[1]/div[1]/div[3]/mat-radio-button[1]/label[1]/div[1]/div[1]"))).click()
except Exception as e:
    print(f"Error al hacer clic en el radio button Cod. Acta: {e}")

# Encontrar el campo de entrada por el placeholder
input_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='______-_']")
input_field.send_keys("7000561")    

# Intentar hacer clic en el botón
try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mat-raised-button.mat-button-base.mat-accent span.mat-button-wrapper"))
    )
    button.click()
    print("Botón clicado con éxito.")
except Exception as e:
    print(f"Error al hacer clic en el botón: {e}")

# Esperar hasta que la imagen esté presente
time.sleep(2)
try:
    img_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Acta']"))
    )
    
    img_src = img_element.get_attribute('src')
    if img_src.startswith('data:image/jpg;base64,'):
        base64_str = img_src.split(',')[1]
        image_data = base64.b64decode(base64_str)
        with open('acta_image.jpg', 'wb') as f:
            f.write(image_data)
        print("Imagen guardada como 'acta_image.jpg'")
    else:
        print("El formato de la imagen no es JPEG.")
except Exception as e:
    print(f"Error al obtener la imagen: {e}")

# Capturar los JSON impresos en la consola
print('Capturando JSON de la consola...')
logs = driver.get_log('browser')
for log in logs:
    try:
        message = json.loads(log['message'])  # Intenta cargar el mensaje como JSON
        print("JSON capturado:", message)
    except json.JSONDecodeError:
        continue  # Ignora mensajes que no sean JSON

print('Esperar unos segundos')
time.sleep(10)

print('Cerrar')
driver.quit()
