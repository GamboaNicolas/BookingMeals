from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import getpass as getpass
import pyautogui as gui


import time as time


user = gui.prompt("ingrese su DNI")
password = gui.password("Ingrese su contraseña:")

options = Options()
options.set_preference("detach", True)
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(GeckoDriverManager().install()), 
                          options = options)

driver.get("https://comedores.unr.edu.ar/comedor-reserva/reservar")

driver.maximize_window()

# links = driver.find_elements("xpath", "//a[@href]")
enter_username = driver.find_element("name", "form-login[dni]")
enter_password = driver.find_element("name", "form-login[clave]")
submit_keys = driver.find_element("name", "botones[botonEnviar]")
# for link in links:
#     print(link)



enter_username.send_keys(user)
enter_password.send_keys(password)
submit_keys.click()


# comedor = "Comedor Universitario Área Salud"

# driver.find_element("xpath",
#                     "//div[contains(@class, 'card card-block reservar-comedor card-filtros grow animated fadeIn faster')][.//h2[text()[contains(., 'Comedor Universitario Área Salud')]]]")

# reservar-comedor-nombre

# Comedor Universitario Área Salud

# salud = driver.find_element("xpath",
#                               "//*[@id='reservar']/div[2]/div[3]/div/div[2]/button")

# time.sleep(1)
# salud = driver.find_element("xpath",
#                               "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área Salud')]")


# salud.click()

# time.sleep(1)

# horario_noche = driver.find_elements("xpath",
#                                     "//*[@class='reservar-servicio-horario-desde']")
                                    
# horario_noche = driver.find_element("xpath",
#                                     "//*[@class='reservar-servicio-horario-desde' and contains(text(),'20:00')]")
# horario_noche.click()
# time.sleep(2)



# for i in horario_noche:
#     print(i)

# print(horario_noche)
# lala = driver.find_elements("xpath", 
#                            "//div[@class = 'calendario-dia calendario-dia-clickeable']/span[contains(text(), 'lunes')]")



# lista = driver.find_element("xpath",
#                             "//div[@class='calendario-dia calendario-dia-clickeable' and ./div[@class='calendario-dia-cabecera' and ./span[contains(text(),'lunes')]]]/div[@class='calendario-dia-turno']")

# horario_noche = driver.find_elements("xpath",
#                                     "//div[@class='calendario-dia calendario-dia-clickeable' and contains(.,'martes')]/div[@class='calendario-dia-turno']")

# for i in horario_noche:
#     print(i)

# horario_noche[0].click()

# for i in lista:
#     print(i)

# print(lista)

# lista.click()
# for i in lala:
#     print(i)

# print(lala)
# driver.get("https://comedores.unr.edu.ar/comedor-reserva/reservar")


# for i in comedor:
#     print(i)


def reservar_noche():

    time.sleep(1)
    salud = driver.find_element("xpath",
                                "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área Centro')]")
    salud.click()

    horario_noche = []
    for dia in ["martes"]:
        salir = []
        while horario_noche == []:
            horario_noche = driver.find_elements("xpath",
                                                 "//*[@class='reservar-servicio-horario-desde' and contains(text(),'"+"14:00"+"')]")
            time.sleep(0.25)
        horario_noche[-1].click()
        time.sleep(6)
        comida = []
        while comida == []:
            comida = driver.find_elements("xpath",
                                          "//div[@class='calendario-dia calendario-dia-clickeable' and contains(.,'"+dia+"')]/div[@class='calendario-dia-turno']")
            time.sleep(0.1)
        time.sleep(0.15)
        driver.execute_script("arguments[0].click()", comida[-1])
        print("Encontró el botón de comida")
        time.sleep(0.15)
        aceptar = driver.find_elements("xpath",
                                          "//button[@class='swal2-confirm swal2-styled']")
        driver.execute_script("arguments[0].click()", aceptar[-1])

        print("arrancó el while")
        while True:
            time.sleep(1)
            salir = driver.find_elements("xpath",
                                         "//button[@class='ticket-iframe-cerrar reservar-ticket-iframe-cerrar']")
            if salir != []:
                driver.execute_script("arguments[0].click()", salir[-1])
                break
            driver.execute_script("arguments[0].click()", comida[-1])
            time.sleep(0.1)
            aceptar = []
            while aceptar == []:
                aceptar = driver.find_elements("xpath",
                                               "//button[@class='swal2-confirm swal2-styled']")
            
            driver.execute_script("arguments[0].click()", aceptar[-1])
        print("Terminó con "+dia)


    return None


"@class='ticket-iframe-cerrar reservar-ticket-iframe-cerrar'"
reservar_noche()