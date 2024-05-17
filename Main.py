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

driver.minimize_window()


# links = driver.find_elements("xpath", "//a[@href]")
enter_username = driver.find_element("name", "form-login[dni]")
enter_password = driver.find_element("name", "form-login[clave]")
submit_keys = driver.find_element("name", "botones[botonEnviar]")
# for link in links:
#     print(link)



enter_username.send_keys(user)
enter_password.send_keys(password)
submit_keys.click()
time.sleep(5)


# def reservar(comedor, dias, hora):

#     salud = driver.find_elements("xpath",
#                                 "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área "+comedor+"')]")
#     driver.execute_script("arguments[0].click()", salud[-1])

#     horario_noche = []
#     for dia in dias:
#         salir = []
#         while horario_noche == []:
#             horario_noche = driver.find_elements("xpath",
#                                                  "//*[@class='reservar-servicio-horario-desde' and contains(text(),'"+ hora +"')]")
#             time.sleep(0.25)
#         driver.execute_script("arguments[0].click()", horario_noche[-1])
#         time.sleep(6)
#         comida = []
#         while comida == []:
#             comida = driver.find_elements("xpath",
#                                           "//div[@class='calendario-dia calendario-dia-clickeable' and contains(.,'"+dia+"')]/div[@class='calendario-dia-turno']")
#             time.sleep(0.1)
#         time.sleep(0.15)
#         driver.execute_script("arguments[0].click()", comida[-1])
#         print("Encontró el botón de comida")
#         time.sleep(0.15)
#         aceptar = driver.find_elements("xpath",
#                                           "//button[@class='swal2-confirm swal2-styled']")
#         driver.execute_script("arguments[0].click()", aceptar[-1])

#         print("arrancó el while")
#         while True:
#             time.sleep(1.35)
#             salir = driver.find_elements("xpath",
#                                          "//button[@class='ticket-iframe-cerrar reservar-ticket-iframe-cerrar']")
#             if salir != []:
#                 driver.execute_script("arguments[0].click()", salir[-1])
#                 break
#             driver.execute_script("arguments[0].click()", comida[-1])
#             time.sleep(0.25)
#             aceptar = []
#             while aceptar == []:
#                 aceptar = driver.find_elements("xpath",
#                                                "//button[@class='swal2-confirm swal2-styled']")
            
#             driver.execute_script("arguments[0].click()", aceptar[-1])
#         print("Terminó con "+dia)

#     return None

def reservar_unico(comedor, dia, hora):

    salud = driver.find_elements("xpath",
                                 "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área "+comedor+"')]")
    driver.execute_script("arguments[0].click()", salud[-1])

    horario_noche = []
    salir = []
    while horario_noche == []:
        horario_noche = driver.find_elements("xpath",
                                             "//*[@class='reservar-servicio-horario-desde' and contains(text(),'"+ hora +"')]")
        time.sleep(0.25)
    driver.execute_script("arguments[0].click()", horario_noche[-1])
    time.sleep(5)
    comida = []
    while comida == []:
        comida = driver.find_elements("xpath",
                                      "//div[@class='calendario-dia calendario-dia-clickeable' and contains(.,'"+dia+"')]/div[@class='calendario-dia-turno']")
        time.sleep(0.1)
    time.sleep(0.15)
    driver.execute_script("arguments[0].click()", comida[-1])
    print("Reservando...")
    time.sleep(0.15)
    aceptar = driver.find_elements("xpath",
                                      "//button[@class='swal2-confirm swal2-styled']")
    driver.execute_script("arguments[0].click()", aceptar[-1])
    print("No hay cupos. Intentando hasta conseguir")
    while True:
        time.sleep(1.35)
        salir = driver.find_elements("xpath",
                                     "//button[@class='ticket-iframe-cerrar reservar-ticket-iframe-cerrar']")
        if salir != []:
            driver.execute_script("arguments[0].click()", salir[-1])
            break
        driver.execute_script("arguments[0].click()", comida[-1])
        time.sleep(0.25)
        aceptar = []
        while aceptar == []:
            aceptar = driver.find_elements("xpath",
                                           "//button[@class='swal2-confirm swal2-styled']")
          
        driver.execute_script("arguments[0].click()", aceptar[-1])
    print("Comida reservada el día "+ dia + " a las " + hora +"hs.")
    driver.close() # De momento esto funciona bien
    # driver.get("https://comedores.unr.edu.ar/comedor-reserva/reservar") NO BORRAR. Servirá más adelante...
    return None


dia = "viernes"
hora = "13:00"
comedor = "Centro"

reservar_unico(comedor, dia, hora)