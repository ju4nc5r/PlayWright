# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Mesa_Web.st.pasos import abrirNavegador
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil



class stMesaWebPerfil():

    
    def perfil(self, xpath):
        self.modificarPerfil()
        self.seleccionarPerfil(xpath)
        self.boton_cambiarPerfil()
        
        
        
    
    def modificarPerfil(self):
        to = 10
        accion = "Cambiar perfil"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPerfil.btn_otro_perfil
            if self.visibility_element(xpath, to):
                # self.jsClick(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                print(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
                            
    def boton_cambiarPerfil(self):
        to = 10
        accion = "Cambiar perfil"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebPerfil.btn_cambiar_perfil_2
            if self.visibility_element(xpath, to):
                # self.jsClick(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                print(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
#    def validarPerfil(self, msjEsperado):
#        to = 20
#        accion = u'Validar Perfil,'+ msjEsperado
#        msgOk, msgFail = get_msg(accion)
#        with self.step(accion):
#            xpath = pl_MesaWebPerfil.btn_otro_perfil           
#            if self.visibility_element(xpath,to):
#                print(msjEsperado)
#                self.compareText(xpath, msjEsperado)
#                self.highlight(xpath, msgOk)
#                
#            else:
#                self.fail_msg(msgFail)            


    def seleccionarPerfil(self, xpath):
        #self.modificarPerfil()
        to = 10
        accion = "Seleccionar perfil"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            #xpath = pl_MesaWebPerfil.operadorMesaDinero
            if self.visibility_element(xpath, to):
                #self.jsClick(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                print(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)     
                
