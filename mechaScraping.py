from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys


def extraer_la_data(driver_):
    print("Entro a la funcion")
    print(driver_)
    datos = driver_.find_elements_by_class_name("element__label") 
    print(len(datos))
    for dato in datos:
        print(dato.text)




driver = webdriver.Firefox()
driver.get("https://plataformaelectoral.jne.gob.pe/ListaDeCandidatos/Index")

driver.refresh()
driver.refresh()

#tags_select es una lista de todos los tag selects de la pagina 
tags_select = driver.find_elements_by_css_selector('.element__select--normal')
#select1 es el select con las opciones de tipos de elecciones 
select1 = tags_select[1]
tipo_de_eleccion = [x for x in select1.find_elements_by_tag_name("option")]

#all_options = select1.find_elements_by_tag_name(".option")
#imprimir = all_options[1].get_attribute("label")
#print(imprimir)

parlamento_andino = tipo_de_eleccion[1]
presidencial = tipo_de_eleccion[2]
congresal = tipo_de_eleccion[3]

presidencial.click()

button_buscar = driver.find_elements_by_class_name("button")
buscar_normal = button_buscar[0].click() 
#busqueda_avanzada = button_buscar[1].click() 

button_vermas = driver.find_elements_by_class_name("VotonesVerMas")
len_vermas = len(button_vermas)


for button in button_vermas:
    button.click()
    button_HDV = driver.find_elements_by_xpath('//*[@title="Ver Hoja de vida del candidato"]')
    for HDV in button_HDV:
        HDV.click()
        p = driver.current_window_handle
        chwd = driver.window_handles
        for w in chwd:
            if(w!=p):
                driver.switch_to.window(w)
                #extraer_la_data(driver)

        break

        
        """div = driver.find_element_by_class_name("buttons__content")
        button_close = div.find_elements_by_tag_name("button")
        button_close[0].click()"""
        print("Data extraida de candidato")


#driver.close()
