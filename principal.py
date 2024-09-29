from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Configurar el controlador de Firefox (geckodriver debe estar en el PATH)
driver = webdriver.Firefox()

#abrir google.com
driver.get('https://computoalcaldes-int.oep.org.bo')

#esperar unos segundos para ver los resultados
time.sleep(10)

#imprimir el contenido
html = driver.page_source
print(html)
# Cerrar el navegador
driver.quit()
