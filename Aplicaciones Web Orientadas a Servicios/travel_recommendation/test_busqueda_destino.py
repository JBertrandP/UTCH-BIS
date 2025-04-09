from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Edge()


driver.get("file:///C:/xampp/htdocs/travel_recommendation/index.html")


time.sleep(1)

# Seleccionar destino: París
Select(driver.find_element("id", "destino")).select_by_value("paris")

# Seleccionar interés: Arte
Select(driver.find_element("id", "interes")).select_by_value("arte")

# Seleccionar presupuesto: Medio
Select(driver.find_element("id", "presupuesto")).select_by_value("medio")

# Seleccionar clima: Frío
Select(driver.find_element("id", "clima")).select_by_value("frio")

# Seleccionar época: Invierno
Select(driver.find_element("id", "epoca")).select_by_value("invierno")

# Clic en el botón de buscar
driver.find_element("id", "buscar-btn").click()


time.sleep(2)


scroll_pause = 0.3  
scroll_height = 100  
total_scroll_time = 10  
steps = int(total_scroll_time / scroll_pause)

for _ in range(steps):
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_height)
    time.sleep(scroll_pause)


time.sleep(2)


driver.quit()
