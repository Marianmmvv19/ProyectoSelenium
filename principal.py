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

print('Esperar unos segundos')
# Esperar unos segundos
time.sleep(10)

print('Cerrar')
# Cerrar el navegador
driver.quit()
