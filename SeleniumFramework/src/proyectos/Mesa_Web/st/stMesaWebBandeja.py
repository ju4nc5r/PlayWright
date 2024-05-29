'''
Created on 1 jun. 2022

@author: GON13535
'''
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebBandeja import pl_MesaWebBandeja
import SeleniumFramework.mouse

class stMesaWebBandeja():
    
    def seleccionar_bandeja(self):
        to = 10
        accion = u'Seleccionar Bandeja'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebBandeja.menu_bandeja
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def validar_orden(self, orden):
        to = 10
        accion = u'validar numero de orden'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebBandeja.registro_de_orden.format(orden)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                #self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)           
                