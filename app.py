import customtkinter as ctk 
import tkinter.messagebox as tkmb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import getpass as getpass
import time as time

options = Options()
# options.set_preference("detach", True)
# options.experimental_options("detach", True)
# dia = "viernes"
# hora = "20:00"
# comedor = "Salud"
# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 

# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue")

app = ctk.CTk() 
app.geometry("800x400") 
app.title("BookingMeals by Nicolas Gamboa")
# def reservar_unico():

def reservar_unico(driver, comedor, dia, hora):
    lugar = driver.find_elements("xpath",
                                 "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área "+comedor+"')]")
    driver.execute_script("arguments[0].click()", lugar[-1])

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



def reservar(): 
	
    dni = user_entry.get()
    password = user_pass.get()

  # app.destroy()
    
    if checkbox.get():
        options.add_argument("--headless")
    # print(ocultar)
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), 
                              options = options)
    driver.minimize_window()
    driver.get("https://comedores.unr.edu.ar/comedor-reserva/reservar")
	
    enter_username = driver.find_element("name", "form-login[dni]")
    enter_password = driver.find_element("name", "form-login[clave]")
    submit_keys = driver.find_element("name", "botones[botonEnviar]")
    
    enter_username.send_keys(dni)
    enter_password.send_keys(password)
    
    submit_keys.click()
    time.sleep(5)
    reservar_unico(driver, "Salud", "viernes", "20:00")




# label = ctk.CTkLabel(app,text="") 

# label.pack(pady=20) 


frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label = ctk.CTkLabel(master=frame,text='BookingMeals') 
label.pack(pady=12,padx=10) 


user_entry= ctk.CTkEntry(master=frame,placeholder_text="DNI") 
user_entry.pack(pady=12,padx=10) 

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 


button = ctk.CTkButton(master=frame,text='Login',command=reservar) 
button.pack(pady=12,padx=10) 

checkbox = ctk.CTkCheckBox(master=frame,text='Ocultar navegador') 
checkbox.pack(pady=12,padx=10) 

app.mainloop()
