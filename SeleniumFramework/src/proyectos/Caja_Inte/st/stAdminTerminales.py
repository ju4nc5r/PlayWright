# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Inte.pageLoc.plAdminTerminales import plAdminTerminales
from SeleniumFramework.src.proyectos.Caja_Inte.st.pasos import abrirNavegador
from SeleniumFramework.common_functions import get_msg

class stAdminTerminales(abrirNavegador):

    def validarBtnMnuTerminalesDisabled(self):
        to = 10
        accion = "Validar boton menu Terminales deshabilitado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminTerminales.mnuBtnTerminales
            if self.visibility_element(xpath, to):                 
                if self.get_attribute(xpath,'disabled') == 'true':
                    self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def validarTituloTerminales(self,leyendaTitulo):
        to = 10
        accion = "Validar titulo de terminales :".format(leyendaTitulo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminTerminales.txt_titulo.format(leyendaTitulo)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def validarTerminalesActivas(self):
        to = 10
        accion = "Validar terminales activas"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminTerminales.tbl_terminales
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)