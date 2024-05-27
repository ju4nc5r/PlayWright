# -*- coding: utf-8 -*-
import allure
from SeleniumFramework.sub import sub

from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.settings import url_iCaja, url_adminCaja, url_autorizCaja

class abrirNavegador(sub):
    def openICaja(self):
        accion = 'Abrir ICaja'
        msgOk, msgFail = get_msg(accion)
        self.paso = 0
        with self.step(accion):
            self.openChrome(url_iCaja)
            self.capture_image(accion)
    
    def openAdminCaja(self):
        accion = 'Abrir Admin caja'
        msgOk, msgFail = get_msg(accion)
        self.paso = 0
        with self.step(accion):
            self.openBrowser("CHROME",url_adminCaja)
            self.capture_image(accion)

    def openAutorizCaja(self):
        accion = 'Abrir autoriz Caja'
        msgOk, msgFail = get_msg(accion)
        self.paso = 0
        with self.step(accion):
            self.openBrowser("CHROME",url_autorizCaja)
            self.capture_image(accion)
    
