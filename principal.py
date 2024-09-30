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
    cod_acta_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='mat-radio-label-content' and contains(., 'Cod. Acta')]"))
    )
    # Asegurar que el botón esté clicable antes de hacer clic
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-radio-label-content' and contains(., 'Cod. Acta')]"))).click()
except Exception as e:
    print(f"Error al hacer clic en el radio button Cod. Acta: {e}")
    driver.quit()
    exit()

print('Esperar unos segundos')
# Esperar unos segundos
time.sleep(10)

print('Cerrar')
# Cerrar el navegador
driver.quit()
