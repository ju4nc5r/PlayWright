'''
Created on 27 may. 2022

@author: GON13535
'''
# -*- coding: utf-8 -*-
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPrecios import pl_MesaWebPrecios


class stMesaWebPrecios():

    
    def seleccionar_precios(self):
        to = 10
        accion = u'Seleccionar precios'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.slp_precios
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)        
                
                
    def seleccionar_precios_cierre(self):
        to = 10
        accion = u'Seleccionar precios cierre'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.slp_precios_cierre
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_precios_FCI(self):
        to = 10
        accion = u'Seleccionar precios FCI'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.slp_precios_fci
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_admin_precios_cierre(self):
        to = 10
        accion = u'Seleccionar admnistracion de precios cierre'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.slp_admin_precios_cierre
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_btn_exportar(self):
        to = 10
        accion = u'Seleccionar boton exportar txt'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.btn_exportar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    
    def seleccionar_btn_slc_archivo(self):
        import getpass
        user = getpass.getuser()
        to = 10
        accion = u'Seleccionar boton seleccionar archivo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.btn_seleccionar_archivo
            if self.visibility_element(xpath, to):
                archivo_input = self.driver.find_element_by_xpath(xpath)
                archivo_input.send_keys(r'C:\Users\{}\Downloads\Precios.txt'.format(user.lower()))
                self.click(xpath)
                self.capture_image(msgOk)
                
            else:
                self.fail_msg(msgFail)    
                
                
    def seleccionar_importar_archivo(self):
        to = 10
        accion = u'Seleccionar boton importar archivo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.btn_importar       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def eliminar_archivo_txt(self,ruta):
        accion = u'Seleccionar boton actualizar_precios '
        msgOk, msgFail = get_msg(accion)      
        import os 
        ruta_archivo = ruta
        os.remove(ruta_archivo)
        print("Archivo elimindo")
        
        
    def seleccionar_btn_actualizar_precios(self):
        to = 10
        accion = u'Seleccionar boton actualizar_precios '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.btn_actualizar_precios
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
        
    
    def seleccionar_btn_aceptar(self):
        to = 10
        accion = u'Seleccionar boton aceptar '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.btn_aceptar_1
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_visualizar_msj_actualizados_satisfactoriamente(self):
        to = 10
        accion = u'Visualizar msj: Precios actualizados satisfactoriamente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.msj_actualizados_satisfactoriamente
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
 
    def visualizar_msj_fondo_actualizado(self):
        to = 10
        accion = u'Visualizar msj: fondo actualizado'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.msj_fondo_actualizado
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                               

    def selecionar_editar_celda(self,celda):
        to = 10
        accion = u'Seleccionar editar celda'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.cell_editar.format(celda)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def editar_monto(self,monto):
        to = 10
        accion = u'Editar monto'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.input_valor_cuotaparte
            if self.visibility_element(xpath,to):
                self.write(xpath,monto,to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def selecionar_aceptar(self):
        to = 10
        accion = u'Seleccionar editar celda'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPrecios.btn_aceptar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)