from selenium import webdriver
from selenium.webdriver.common.by import By

# Configurar el controlador de Firefox (geckodriver debe estar en el PATH)
driver = webdriver.Firefox()

#abrir google.com
driver.get('https://www.google.com')

#esperar unos segundos para visualizar la página
driver.implicitly_wait(5)

#buscar el campo de búsqueda de Google por su nombre (name="q")
search_box = driver.find_element(By.NAME, 'q')

#escribir "Selenium Python" en el cuadro de búsqueda
search_box.send_keys('Selenium Python')

#enviar la búsqueda (simular presionar Enter)
search_box.submit()

# Esperar unos segundos para ver los resultados
driver.implicitly_wait(5)

# Cerrar el navegador
driver.quit()
