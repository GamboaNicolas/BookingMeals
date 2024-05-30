import customtkinter as ctk 
from CTkMessagebox import CTkMessagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import getpass as getpass
import time as time
import func

options = Options()

dias = ["lunes", "martes","miércoles", "jueves", "viernes"]
horas = ["11:00(Llevar)", "12:00", "13:00", "14:00", 
         "12:00(Llevar)", "13:00(Llevar)", "14:00(Llevar)", 
         "19:30(Llevar)", "19:30", "20:00"]
comedores = ["Salud", "Centro", "FCEIA", "Siberia", "AGROTECNICA", "Zavalla", "Casilda"]

ctk.set_appearance_mode("dark") 

# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue")

app = ctk.CTk() 


# app.geometry("1300x600") 
# app.wm_attributes('-fullscreen', True)
app.after(0, lambda:app.state('zoomed'))


app.title("BookingMeals by Nicolas Gamboa")
# def reservar_unico():

# def reservar_unico(driver, comedor, dia, hora, llevar):

#     if(llevar):
#         indice_llevar = 0
#     else:
#         indice_llevar = -1

#     lugar = driver.find_elements("xpath",
#                                  "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área "+comedor+"')]")
#     driver.execute_script("arguments[0].click()", lugar[-1])

#     horario_noche = []
#     salir = []
#     while horario_noche == []:
#         horario_noche = driver.find_elements("xpath",
#                                              "//*[@class='reservar-servicio-horario-desde' and contains(text(),'"+ hora +"')]")
#         time.sleep(0.25)
#     driver.execute_script("arguments[0].click()", horario_noche[indice_llevar])
#     time.sleep(5)
#     comida = []
#     while comida == []:
#         comida = driver.find_elements("xpath",
#                                       "//div[@class='calendario-dia calendario-dia-clickeable' and contains(.,'"+dia+"')]/div[@class='calendario-dia-turno']")
#         time.sleep(0.1)
#     time.sleep(0.15)
#     driver.execute_script("arguments[0].click()", comida[-1])
#     print("Reservando...")
#     time.sleep(0.15)
#     aceptar = driver.find_elements("xpath",
#                                       "//button[@class='swal2-confirm swal2-styled']")
#     driver.execute_script("arguments[0].click()", aceptar[-1])
#     print("No hay cupos. Intentando hasta conseguir")
#     while True:
#         time.sleep(1)
#         salir = driver.find_elements("xpath",
#                                      "//button[@class='ticket-iframe-cerrar reservar-ticket-iframe-cerrar']")
#         if salir != []:
#             driver.execute_script("arguments[0].click()", salir[-1])
#             break
#         driver.execute_script("arguments[0].click()", comida[-1])
#         time.sleep(0.25)
#         aceptar = []
#         while aceptar == []:
#             aceptar = driver.find_elements("xpath",
#                                            "//button[@class='swal2-confirm swal2-styled']")
          
#         driver.execute_script("arguments[0].click()", aceptar[-1])

#     # driver.close() # Queda comentado en caso de ser necesario
#     driver.get("https://comedores.unr.edu.ar/comedor-reserva/reservar")
#     time.sleep(3)




def reservar(): 
	
    dni = user_entry.get()
    password = user_pass.get()

    # print(checkbox_vars["lunes"]["12:00"].get()) esto fue épico

    app.destroy()
    
    if checkbox.get():
        options.add_argument("--headless")
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

    # reservar_unico(driver, "Centro", "martes", "14:00", llevar = False)
    mensajes = []
    for dia in dias:
        for hora in horas:
            comedor = checkbox_vars[dia][hora].get()
            
            if hora.endswith("(Llevar)"):
                para_llevar = True
                hora = hora[:5]
            else:
                para_llevar = False
            if (comedor != "No reservar"):
                func.reservar_unico(driver,
                               comedor=comedor,
                               dia=dia,
                               hora=hora, 
                               llevar=para_llevar)
                texto = dia +" en "+comedor+ " a las " + hora +"hs"
                if para_llevar:
                    texto = texto + " para llevar"
                mensajes.append(texto)
                # window = tkinter.Tk()
                # window.after(0, lambda:window.state('zoomed'))

    texto_mostrar = "Comidas Reservadas:"
    for texto in mensajes:
        texto_mostrar = texto_mostrar +"\n\n"+texto
    icono = "check"
    if mensajes == []:
        texto_mostrar = "No se seleccionaron comidas"
        icono = "warning"

    a = CTkMessagebox(message=texto_mostrar, 
                          icon=icono, option_1="Listo")
    a.master.withdraw()
    salida = a.get()
    if salida == "Listo":
        a.destroy()
        a.master.destroy()


                

container = ctk.CTkFrame(master=app)
container.pack(fill="both", expand=True)

frame = ctk.CTkFrame(master=container)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='BookingMeals')
label.grid(row=0, column=0, columnspan=len(horas)+1, pady=12, padx=40)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="DNI")
user_entry.grid(row=1, column=0, columnspan=len(horas)+1, pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.grid(row=2, column=0, columnspan=len(horas)+1, pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=reservar)
button.grid(row=3, column=0, columnspan=len(horas)+1, pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Ocultar navegador')
checkbox.grid(row=4, column=0, columnspan=len(horas)+1, pady=12, padx=10)

for i, horario in enumerate(horas):
    label_dia = ctk.CTkLabel(master=frame, text=horario)
    label_dia.grid(row=5, column=i+1, padx=10, pady=10)

# Crear una grilla de listas para los días y horas
checkbox_vars = {dia: {} for dia in dias}

for i, dia in enumerate(dias):
    label_dia = ctk.CTkLabel(master=frame, text=dia.capitalize())
    label_dia.grid(row=i+6, column=0, padx=10, pady=10)
    for j, hora in enumerate(horas):
        var = ctk.StringVar(value = "No reservar")
        checkbox_vars[dia][hora] = var
        chk = ctk.CTkOptionMenu(master=frame, 
                              values=["No reservar"]+comedores, 
                              variable = var, width= 70)
        chk.grid(row=i+6, column=j+1, padx=5, pady=5)

app.mainloop()