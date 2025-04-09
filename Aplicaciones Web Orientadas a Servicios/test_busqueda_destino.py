from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Crea el navegador (asegúrate de tener el WebDriver adecuado, como ChromeDriver)
driver = webdriver.Edge()

# Abre tu página local (ajusta el path si es diferente)
driver.get("file:///C:/Users/tu_usuario/ruta_a_tu_proyecto/index.html")

# Espera a que cargue
time.sleep(1)

# Selecciona "París" en el select de destino
Select(driver.find_element("id", "destino")).select_by_value("paris")

# Selecciona "Arte"
Select(driver.find_element("id", "interes")).select_by_value("arte")

# Selecciona "Medio" en presupuesto
Select(driver.find_element("id", "presupuesto")).select_by_value("medio")

# Selecciona "Invierno"
Select(driver.find_element("id", "epoca")).select_by_value("invierno")

# Presiona el botón de buscar
driver.find_element("id", "buscar-btn").click()

# Espera para ver el resultado (puedes ajustar o remover si haces assertions)
time.sleep(3)

# Cierra el navegador
driver.quit()
