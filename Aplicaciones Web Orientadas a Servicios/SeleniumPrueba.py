from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

#Inicializar el navegador
def inicializarDriver():
    driver = webdriver.Edge()
    return driver

def login(driver):
    #1- Aqui busco el elemento html que deseo ubicar
    inputUsername=driver.find_element(By.ID, "user-name")
    #2- Encontrar la credencial para acceder en el input de username 
    contentUsername = driver.find_element(By.ID, "login_credentials")
    #3- Se separo el div para obtener la primer credencial (username)
    splitContentUsername = contentUsername.text.split("\n")
    #4- Tengo el valor que se pondra en el input de username
    valueUsername = splitContentUsername[1]
    #5- Pegar el username en el input
    inputUsername.send_keys(valueUsername)

    #1- Aqui busco el elemento html que deseo ubicar
    inputPassword=driver.find_element(By.ID, "password")
    #2- Encontrar la credencial para acceder en el input de password 
    contentPassword = driver.find_element(By.CLASS_NAME, "login_password")
    #3- Se separo el div para obtener la primer credencial (password)
    splitContentPassword = contentPassword.text.split("\n")
    #4- Tengo el valor que se pondra en el input de password
    valuePassword = splitContentPassword[1]
    #5- Pegar el username en el input
    inputPassword.send_keys(valuePassword)

    btnLogin = driver.find_element(By.ID, "login-button")
    btnLogin.click()


    time.sleep(10)
    return driver

def main():
    driver = inicializarDriver()
    driver.get("https://www.saucedemo.com/")
    driver = login(driver)

    #comprobacion
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print('Si pude entrar:)')
    else: print('Nel')
        
if __name__ == '__main__':
    main()