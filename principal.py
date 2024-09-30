from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Configurar el controlador de Firefox (geckodriver debe estar en el PATH)
driver = webdriver.Firefox()

#abrir google.com
driver.get('https://computoalcaldes-int.oep.org.bo')

#esperar unos segundos para ver los resultados
time.sleep(10)
print('Click en el boton')

#click en el boton actas
actas_button = driver.find_element(By.XPATH, "//span[contains(text(), 'ACTAS')]")
actas_button.click()

#click en el radio buttun buscar por codigo actas,espera explícita para asegurarse de que el radio button esté visible
wait = WebDriverWait(driver, 3)
radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-radio-inner-circle']")))

# Hacer clic en el radio button
radio_button.click()

print('Esperar unos segundos')
#esperar unos segundos
time.sleep(10)

print('Cerrar')
# Cerrar el navegador
driver.quit()
