# -*- coding: utf-8 -*-
import pytest

def get_msg(msg):
    """Metodo para generar los mensajes de ok y fail a partir de la accion"""
    msgOk = u'Se pudo {}'.format(msg.lower())
    msgFail = u'No se pudo {}'.format(msg.lower())
#     msgFail = u'No {}'.format(msgOk.lower())
    return msgOk, msgFail


def get_fecha_hora(hora=0, minutos=0, segundos=0):
    """ Metodo para generar una fecha y hora
    :param hora: Integer. Cantidad de horas que se quiere desplazar.
    :param minutos: Integer. Cantidad de minutos que se quiere desplazar.
    :param segundos: Integer. Cantidad de segundos que se quiere desplazar.
    :return: String. Devuelve el horario que se quiso generar
    """
    from datetime import datetime, timedelta
    now = datetime.now()
    s = (now.strftime("%H:%M:%S"))
    horario = datetime.strptime(s, "%H:%M:%S")
    modified_hours = horario + timedelta(
        hours=hora, minutes=minutos, seconds=segundos)
    horario = datetime.strftime(modified_hours, "%H:%M")
    return horario


def plazo_fecha(plazo):
    """
    Metodo para generar una fecha
    :param plazo: Integer. Cantidad de dias a desplazar. Si se ingresa en
    negativo, se genera una fecha previa al dia de hoy
    """
    import time
    from datetime import datetime, timedelta
    s = (time.strftime("%d/%m/%Y"))
    date = datetime.strptime(s, "%d/%m/%Y")
    modified_date = date + timedelta(days=plazo)
    fecha = datetime.strftime(modified_date, "%d/%m/%Y")
    return fecha


def obtener_fecha_laboral(plazo):
    """
    Metodo para obtener una fecha que  sea laboral, en caso que la fecha
    caiga un dia de fin semana, se retorna la proxima fecha laboral
    :param plazo: Integer. Cantidad de dias a desplazar. Si se ingresa en
    negativo, se genera una fecha previa al dia de hoy
    """
    from datetime import datetime, timedelta
    formato = "%d/%m/%Y"
    fecha = plazo_fecha(plazo)
    day = datetime.strptime(fecha, formato).date()
    weekday = day.weekday()
    if weekday == 5:
        delta = 2
    elif weekday == 6:
        delta = 1
    else:
        return fecha
    day += timedelta(delta)
    return day.strftime(formato)



def obtener_fecha_no_laboral(plazo):
    """
    Metodo para obtener una fecha que no sea laboral, en caso que la fecha
    caiga un dia de semana, se retorna la proxima fecha no laboral
    :param plazo: Integer. Cantidad de dias a desplazar. Si se ingresa en
    negativo, se genera una fecha previa al dia de hoy
    """
    from datetime import datetime, timedelta
    formato = "%d/%m/%Y"
    fecha = plazo_fecha(plazo)
    day = datetime.strptime(fecha, formato).date()
    weekday = day.weekday()
    if weekday == 0:
        delta = 5
    elif weekday == 1:
        delta = 4
    elif weekday == 2:
        delta = 3
    elif weekday == 3:
        delta = 2
    elif weekday == 4:
        delta = 1
    else:
        return fecha
    day += timedelta(delta)
    return day.strftime(formato)


def desbloqueoUsuarios(numDoc):
    """
    Metodo para desbloquear el login a un usuario
    :param numDoc: String. Numero de documento del usuario que se quiere
    desbloquear
    """
    from SeleniumFramework.src.utils.settings import path_xml
    from os.path import join

    def CopiarArchConRemplazoString(origen, destino, doc):
        """
        Metodo para generar los archivos xml temporales
        :param origen: String. Path de la ubicacion del archivo template
        :param destino: String. Path de la ubicacion del archivo temporal
        :param doc: Strign. numero de documento que se quiere modificar
        """
        f = open(origen, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("DNIparaRemplazar", doc)
        f = open(destino, 'w')
        f.write(newdata)
        f.close()

    def ejecutar_bat():
        """
        Metodo para ejecutar el bat
        """
        import subprocess
        Archivo = join(path_xml, 'DesbloqueoUsuarios.bat')
        subprocess.call([Archivo])
    numDoc = str(numDoc)  # el numero tiene que ser string
    ArchivoOrigen = join(path_xml,
                         'DesbloqueoUsuariosCanal1-soapui-project.xml')
    canales = [1, 111, 120, 121]  # Canales a desbloquear
    for canal in canales:
        ArchivoDestino = join(
            path_xml,
            'TempDesbloqueoUsuariosCanal{}-soapui-project.xml'.format(canal)
        )
        CopiarArchConRemplazoString(ArchivoOrigen, ArchivoDestino, numDoc)
    ejecutar_bat()


def get_user_hb(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import hb_user_excel, hb_user_sheet

    excel = usuarios(hb_user_excel, hb_user_sheet)
    return excel.obtener_datos_usuarios(nombre_caso, 'hb')

def get_user(nombre_usuario):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import hb_user_excel, hb_user_login
    
    excel = usuarios(hb_user_excel, hb_user_login)
    user = excel.usuarios_activos(nombre_usuario, 'hb')
    return user

def get_user_mb(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import hb_user_excel, mb_test_sheet

    excel = usuarios(hb_user_excel, mb_test_sheet)
    return excel.obtener_datos_usuarios(nombre_caso, 'hb')

    
def get_user_caja_inte(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import caja_user_excel, caja_user_sheet

    excel = usuarios(caja_user_excel, caja_user_sheet)
    return excel.obtener_datos_usuarios(nombre_caso, 'Caja')

def get_user_IBE_homo(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import IBE_user_excel, IBE_user_sheet_homo

    excel = usuarios(IBE_user_excel, IBE_user_sheet_homo)
    return excel.obtener_datos_usuarios(nombre_caso, 'IBE')

def get_user_caja_homo(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import caja_user_excel, caja_user_sheet_homo

    excel = usuarios(caja_user_excel, caja_user_sheet_homo)
    return excel.obtener_datos_usuarios(nombre_caso, 'Caja')

def get_user_caja_homo_suc_50(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import caja_user_excel, caja_user_sheet_homo_suc_50

    excel = usuarios(caja_user_excel, caja_user_sheet_homo_suc_50)
    return excel.obtener_datos_usuarios(nombre_caso, 'Caja')


def get_user_caja_desa(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import caja_user_excel, caja_user_sheet_desa

    excel = usuarios(caja_user_excel, caja_user_sheet_desa)
    return excel.obtener_datos_usuarios(nombre_caso, 'Caja')


def get_user_NHBE_homo(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import NHBE_user_excel, NHBE_user_sheet_homo

    excel = usuarios(NHBE_user_excel, NHBE_user_sheet_homo)
    return excel.obtener_datos_usuarios(nombre_caso, 'IBE')


def test_Modificar_XML_Enviroments(allure_path='../allure-results/'):
    """ Metodo para detallar el entorno en la ejecucion de allure """
    import os
    import shutil
    from os.path import join
    from SeleniumFramework.src.utils.settings import allure_xml, browser

    print ("Entro a Modificar_XML_Environmemts -------------------------------------------")
    def reemplazarString(template, archivo):
        # Metodo para reemplazar los valores del xml
        texto = template.read()
        texto = texto.replace("JOB_NAME", JOB_NAME)
        texto = texto.replace("NODE_NAME", NODE_NAME)
        texto = texto.replace("NAVEGADOR", NAVEGADOR)
        texto = texto.replace("ENVIRONMENT", ENVIRONMENT)
        archivo.write(texto)
        template.close()
        archivo.close()

    def obtener_xml():
        # Lectura y escritura de los xml para guardar los datos
        enviroment = open(join(allure_xml, 'environment.xml'), 'w')
        template = open(join(allure_xml, 'environment_Template.xml'), 'r')
        return template, enviroment

    def generar_carpeta_allure():
        # Copia del xml en la carpeta de resultados de allure
        from SeleniumFramework.src.utils.settings import path
        # Este path esta pensado para que se le pase un path parcial y se
        # la complete con el path de donde se encuentra el archivo del test
        allure_results = join(path, allure_path)
        print(allure_results)
        try:
            # Se intenta borrar la carpeta
            shutil.rmtree(allure_results)
            print('Se borra carpeta en {}'.format(allure_results))
        except WindowsError:
            pass
        try:
            # Se intenta crear la carpeta
            os.makedirs(allure_results)
            print('Se crea carpeta en {}'.format(allure_results))
        except OSError:
            pass
        # Se realiza la copia del xml modificado en la carpeta de resultados
        shutil.copy(join(allure_xml, "environment.xml"), allure_results)

    # Varaibles que se obtienen cuando se ejecuta desde jenkins
    JOB_NAME = os.environ['JOB_NAME']  # Nombre del proyecto en jenkins
    NODE_NAME = os.environ['NODE_NAME']  # Nombre del nodo donde se ejecuta
    NAVEGADOR = browser
    
    # SE ESTABLECE AMBIENTE DONDE SE ESTÁ EJECUTANDO EN FUNCION DEL NOMBRE DEL PROYECTO JENKINS
    
    if "Caja" in JOB_NAME:
    
        if "HOMOLOGACION" in JOB_NAME:
            ENVIRONMENT = "Homologacion"
        elif "INTEGRACION" in JOB_NAME:
            ENVIRONMENT = "Integracion"
        elif "DESARROLLO" in JOB_NAME:
            ENVIRONMENT = "Desarrollo"                  
        else:
            pytest.fail("EL NOMBRE DE PROYECTO EN JENKINS NO TIENE EL AMBIENTE")
            
    else:
    
        ENVIRONMENT = "Homologacion"
        
        
    template, modificado = obtener_xml()
    reemplazarString(template, modificado)
    generar_carpeta_allure()
