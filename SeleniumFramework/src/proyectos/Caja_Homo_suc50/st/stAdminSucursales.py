# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.pageLoc.plAdminSucursales import plAdminSucursales
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.pasos import abrirNavegador
from selenium.webdriver.common.by import By


from SeleniumFramework.common_functions import get_msg

class stAdminSucursales(abrirNavegador):
    
    def validarBtnMnuSucursalesDisabled(self):
        to = 10
        accion = "Validar boton menu Sucursales deshabilitado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminSucursales.mnuBtnSucursales
            if self.visibility_element(xpath, to):                 
                if self.get_attribute(xpath,'disabled') == 'true':
                    self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def validarTituloApertura(self,leyendaTitulo):
        to = 10
        accion = "Validar titulo de apertura :".format(leyendaTitulo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminSucursales.txt_titulo.format(leyendaTitulo)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    
    def visualizarRecuadroOperador(self):
        to = 10
        accion = "Visualizar recuadro operador centralizador "
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminSucursales.recuadro_operador
            if self.visibility_element(xpath, to): 
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def seleccionarOperador(self, user):
        to = 10
        accion = "Seleccionar operador"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminSucursales.btn_operador.format(user)
            self.resaltar_msj_cierre_forzado()

            if self.visibility_element(xpath, to):
                # self.jsClick(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                print(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarAceptar(self):
        to = 10
        accion = "Seleccionar aceptar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminSucursales.btn_aceptar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_aceptar(self):
        to = 10
        accion = "Seleccionar aceptar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminSucursales.btn_aceptar_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                pass
    
    def verificarApertura(self):
        to = 10
        accion = "verificar mensaje apertura exitosa"             
        with self.step(accion):
            xpath = plAdminSucursales.msjAperturaExitosa
            btnCerrar = plAdminSucursales.btnCerrar   
            msgOk, msgFail = get_msg(accion) 
            if self.visibility_element(xpath, to):               
                self.highlight(xpath, accion)
                               
                accionBtn="hacer click en boton cerrar"
                msgOk, msgFail = get_msg(accionBtn)                
                if self.visibility_element(btnCerrar, to):
                    self.selectElement(btnCerrar, msgOk, msgFail, to)
                    self.wait(1)
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)
            else:            
                self.fail_msg(msgFail)

    def resaltar_msj_cierre_forzado(self):
        to = 30
        accion = u'validar que se encuentre el msj Se procederá a la apertura forzada de la sucursal'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plAdminSucursales.txt_titulo_apertura_forzada
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.seleccionar_aceptar()
            else:
                pass              
    