from selenium import webdriver
import urllib
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By


def extraer_dato_trayectoria_partidaria(seccion_):
    lista_trayectoria_partidaria = list()
    seccion_trayectoria_partidaria = seccion_
    seccion_col = seccion_trayectoria_partidaria.find_elements_by_class_name("col-md-12.col-sm-12.m-b-30.cleaner.ng-scope")[0]
    articles = seccion_col.find_elements_by_tag_name('article')
    lista = []
    print("len(articles)")
    print(len(articles))
    for article in articles:
        datos = article.find_elements_by_class_name("main__radios.displayBlock.ng-scope")
        for labe in datos:
            if labe.find_elements_by_tag_name('input')[0].get_attribute('checked'):
                print(labe.text)
        datos1 = [date.text for date in article.find_elements_by_class_name("element__label ")]
        for e in datos1:
            print(e)
    return lista_trayectoria_partidaria

def extraer_info_adicional(seccion):
    lista_info_adicional = list()
    for  div in seccion.find_elements_by_tag_name("article"):
        datos= [element.text for element in div.find_elements_by_class_name("element__label ")]
        lista_info_adicional.append({
            'info_adicional': datos[0]
            })
    for e in lista_info_adicional:
        print()
        for k, v in e.items():
            print(k, ":", v)
    print("\n")
    return lista_info_adicional

def extraer_datos_academicos(seccion):
    datos = [element.text for element in seccion.find_elements_by_class_name("element__label ")]
    diccionario_academico = {
        'tiene_estu_primarios': datos[2],
        'concluido_estu_primarios': datos[4],
        'tiene_estu_secundarios': datos[6],
        'concluido_estu_secundarios': datos[8],
        'tiene_estu_tecnicos': datos[11],
        'centro_estu_tecnicos': datos[13],
        'carrera_tecnica': datos[15],
        'concluido_estu_tecnicos': datos[17],
        'comentario_estu_tecnicos': datos[19],
        'tiene_estu_no_universitarios': datos[21],
        'centro_estu_no_universitarios': datos[23],
        'carrera_no_universitaria': datos[25],
        'concluido_estu_no_universitarios': datos[27],
        'tiene_estu_universitarios': datos[30],
        'registros_universitarios' : [],
        'tiene_estu_postgrado': datos[44],
        'centro_estu_postgrado': datos[46],
        'grado_estu_postgrado': datos[48],
        'concluido_estu_postgrado': datos[50],
        'es_egresado_postgrado': datos[52],
        'grado_maestro': datos[54],
        'grado_doctor': datos[56],
        'anhio_obtencion_estu_postgrado': datos[58],
        'comentario_estu_postgrado': datos[60]
    }
    lista_estudios_universitarios = []

    for item in seccion.find_elements_by_class_name("ContenedorRegistro"):
        datos2 = [element.text for element in item.find_elements_by_class_name("element__label ")]
        lista_estudios_universitarios.append({
            'centro_estu_universitarios': datos2[1],
            'concluido_estu_universitarios': datos2[3],
            'grado_estu_universitarios': datos2[5],
            'es_egresado_universitario': datos2[7],
            'anhio_obtencion_est_universitarios': datos2[9],
            'comentario_estu_universitarios': datos2[11]
        })
    diccionario_academico['registros_universitarios'] = lista_estudios_universitarios

    for e in lista_estudios_universitarios:
        print()
        for k, v in e.items():
            print(k, ":", v)
    print("\n")
    return lista_estudios_universitarios

def extraer_datos_personales(seccion, contador):

    lista_datos_personales = list()
    a =  seccion.find_element_by_class_name("FotoPerfil")
    foto = a.get_attribute("src")

    if contador == 0:
        cargo = "PRESIDENTE DE LA REPÚBLICA"
    elif contador == 1: 
        cargo = "PRIMER VICEPRESIDENTE DE LA REPÚBLICA"
    elif contador ==2:
        cargo = "SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA"

        
    #datos = [element.text for element in articulo.find_elements_by_class_name("element__label ")]
    datos = seccion.find_elements_by_class_name("element__label ")
    print(len(datos))
    lista_datos_personales.append({
        'link_foto': foto,
        'dni': datos[1].text,
        'sexo': datos[3].text,
        'apellido_paterno': datos[5].text,
        'apellido_materno':datos[7].text,
        'nombres': datos[9].text,
        'fecha_nacimiento': datos[11].text,
        'carnet_extranjeria': datos[13].text,
        'l_n_pais': datos[15].text,
        'l_n_departamento': datos[17].text,
        'l_n_provincia': datos[19].text,
        'l_n_distrito': datos[21].text,
        'l_d_departamento': datos[23].text,
        'l_d_provincia': datos[25].text,
        'l_d_distrito': datos[27].text,
        'l_d_direccion': datos[29].text,
        'org_politica_postula': datos[31].text,
        'cargo_postula': cargo,
    })
    for e in lista_datos_personales:
        print()
        for k, v in e.items():
            print(k, ":", v)
    print("\n")
    return lista_datos_personales

def extraer_relacion_sentencias(seccion):
    lista_relacion_sentencias= list()
    for articulo in seccion.find_elements_by_tag_name("article"):
        datos = [element.text for element in articulo.find_elements_by_class_name("element__label ")]
        if datos[1] == "":
            continue
        lista_relacion_sentencias.append({
            'numero_expediente': datos[1],
            'fecha_sentencia': datos[3],
            'orga_judicial': datos[5],
            'delito': datos[7],
            'fallo': datos[9],
            'modalidad': datos[11],
            'cumplimiento_fallo': datos[13]
        })
    for e in lista_relacion_sentencias:
        print()
    for k, v in e.items():
        print(k, ":", v)
    print("\n")
    return lista_relacion_sentencias


def extraer_dato_relacion_sentencias_fundadas(seccion_):
    datos_sentencias_fundados = list()
    datos = seccion_.find_elements_by_class_name("content__radios")
    if datos[1].get_attribute('checked') == False:
        return datos_sentencias_fundados

    datos_sentencias = seccion_.find_elements_by_tag_name("article")
    for sentencia in datos_sentencias:
        datos = sentencia.find_elements_by_class_name("element__label")
        datos_sentencias_fundados.append({
            'material_demanda' : datos[1].text,
            'n_expediente' : datos[3].text,
            'organo_judi' : datos[5].text,
            'fallo' : datos[7].text,
        })
    for e in datos_sentencias_fundados:
        print()
    for k, v in e.items():
        print(k, ":", v)
    print("\n")
    return datos_sentencias_fundados

def extraer_datos_laborales(seccion):
    lista_registro_laboral = list()
    for articulo in seccion.find_elements_by_tag_name("article"):
        datos = [element.text for element in articulo.find_elements_by_class_name("element__label ")]
        lista_registro_laboral.append({
            'nombre': datos[1],
            'ocupacion': datos[3],
            'ruc': datos[5],
            'direccion': datos[7],
            'inicio': datos[9],
            'fin': datos[11],
            'pais': datos[13],
            'departamento': datos[15],
            'provincia': datos[17],
        })
    return lista_registro_laboral


def extraer_la_data(driver_, contador_):
    print("Entro a la funcion")
    driver_.refresh()
    time.sleep(3)
    seccion1_datos_personales = driver_.find_element_by_id("datos_personales")

    secciones_experiencia_laboral = driver_.find_elements_by_class_name("experiencia_laboral")
   
    seccion_exp_laboral = secciones_experiencia_laboral[0]

    expe_laboral = extraer_datos_laborales(seccion_exp_laboral)
    

    seccion_formacion_academica = secciones_experiencia_laboral[1]
    datos_academicos = extraer_datos_academicos(seccion_formacion_academica)

    seccion_trayectoria_partidaria = secciones_experiencia_laboral[2]
    datos_trayectoria = extraer_dato_trayectoria_partidaria(seccion_trayectoria_partidaria)

    seccion_renuncias_otros_partidos = secciones_experiencia_laboral[3]
    seccion_relacion_sentencias = secciones_experiencia_laboral[4]
    datos_relacion_sentencias = extraer_relacion_sentencias(seccion_relacion_sentencias)
    
    seccion_relacion_sentencias_fundadas = secciones_experiencia_laboral[5] 
    datos_relacion_sentencias_fundadas = extraer_dato_relacion_sentencias_fundadas(seccion_relacion_sentencias_fundadas)

    seccion_declaracion_jurada = secciones_experiencia_laboral[6] 
    seccion_info_adicional = secciones_experiencia_laboral[7]
    

    datos_adicionales = extraer_info_adicional(seccion_info_adicional)


        
    return {
        'informacion_personal' : {
            
        },
        'ademico' : {
            
        },
        'laboral' : {
            
        }
    }


driver = webdriver.Firefox()
driver.get("https://plataformaelectoral.jne.gob.pe/ListaDeCandidatos/Index")

driver.refresh()
driver.refresh()

# tags_select es una lista de todos los tag selects de la pagina
tags_select = driver.find_elements_by_css_selector('.element__select--normal')
# select1 es el select con las opciones de tipos de elecciones
select1 = tags_select[1]
tipo_de_eleccion = [x for x in select1.find_elements_by_tag_name("option")]

# all_options = select1.find_elements_by_tag_name(".option")
# imprimir = all_options[1].get_attribute("label")
# print(imprimir)

parlamento_andino = tipo_de_eleccion[1]
presidencial = tipo_de_eleccion[2]
congresal = tipo_de_eleccion[3]

presidencial.click()

button_buscar = driver.find_elements_by_class_name("button")
buscar_normal = button_buscar[0].click()
# busqueda_avanzada = button_buscar[1].click()

button_vermas = driver.find_elements_by_class_name("VotonesVerMas")
len_vermas = len(button_vermas)

window_parent = driver.window_handles[0]
for button in button_vermas:
    button.click()
    button_HDV = driver.find_elements_by_xpath('//*[@title="Ver Hoja de vida del candidato"]')
    contador = 0
    for HDV in button_HDV:
        HDV.click()
        contador = contador + 1
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        extraer_la_data(driver,contador)
        # time.sleep(5)
        driver.close()
        driver.switch_to_window(window_parent)
    button.click()
