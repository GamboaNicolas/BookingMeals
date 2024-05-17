



def reservar(comedor, dias, hora):

    time.sleep(1)
    salud = driver.find_elements("xpath",
                                "//h2[@class='reservar-comedor-nombre' and contains(text(),'Comedor Universitario Área "+comedor+"')]")
    driver.execute_script("arguments[0].click()", salud[-1])

    horario_noche = []
    for dia in dias:
        salir = []
        while horario_noche == []:
            horario_noche = driver.find_elements("xpath",
                                                 "//*[@class='reservar-servicio-horario-desde' and contains(text(),'"+ hora +"')]")
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
        print("Terminó con "+dia)


    return None


