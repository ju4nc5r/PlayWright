# -*- coding: utf-8 -*-
from SeleniumFramework.sub import sub
from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.proyectos.Mesa_Web.settings import url_MesaWeb

class abrirNavegador(sub):
    def openMesaWeb(self):
        accion = u'Abrir Mesa Web'
        msgOk, msgFail = get_msg(accion)
        self.paso = 0
        with self.step(accion):
            self.openBrowser("CHROME",url_MesaWeb)
            self.capture_image(accion)
    
