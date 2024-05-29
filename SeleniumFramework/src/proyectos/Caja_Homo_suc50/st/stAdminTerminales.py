# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.pageLoc.plAdminTerminales import plAdminTerminales
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.pasos import abrirNavegador
# from proyectos.Caja_Homo_suc50.constants.constants import (
#     USUARIO_INVALIDO, USUARIO_BLOQUEADO, USUARIO_YA_LOGUEADO, CLAVE_VENCIDA,
#     INTENTAR, REVISAR, LOGUEADO
from selenium.webdriver.common.by import By

# )
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