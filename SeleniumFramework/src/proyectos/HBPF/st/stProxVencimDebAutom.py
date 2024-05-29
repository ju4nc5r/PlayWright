# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locProxVencimDebAutom import locProxVtosDebAutom
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg



class stProxVencimDebAutom(menu):    

    def verificarListaProxVtos(self):
        accion = u'Verificar lista de próximos vencimientos'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locProxVtosDebAutom.tblPoximosVencimientos
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                if locProxVtosDebAutom.lblPrimerCeldaProxVtos:
                    self.highlight(locProxVtosDebAutom.lblPrimerCeldaProxVtos, u'Primera Celda lista Proximos vencimientos')
                    
            else:
                self.fail_msg(accion)


# Para tener por si se pueden usar en proximos casos
        
    def seleccionarContinuar(self):
        accion = u'seleccionar Continuar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locProxVtosDebAutom.btnContinuar
        with self.step(accion):
            if self.visibility_element(xpath, to):               
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
 
                
    def seleccionarConfirmar(self):
        accion = u'seleccionar Confirmar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locProxVtosDebAutom.btnConfirmar
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)


 
