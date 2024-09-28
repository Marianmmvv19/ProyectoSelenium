from selenium import webdriver
from selenium.webdriver.common.by import By

# Configurar el controlador de Firefox (geckodriver debe estar en el PATH)
driver = webdriver.Firefox()

#abrir google.com
driver.get('https://computoalcaldes-int.oep.org.bo')


# Esperar unos segundos para ver los resultados
#driver.implicitly_wait(60)

# Cerrar el navegador
#driver.quit()
