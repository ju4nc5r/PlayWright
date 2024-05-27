# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaCBUyAlias import locConsultaCBUyAlias
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaCBUyAlias(menu):
        
#     def seleccionarCuentaCBU(self,cuenta):
#         to = 10
#         accion = 'Seleccionar cuenta CBU'
#         msgOk = accion
#         msgFail = 'No se pudo %s'%msgOk
#         with self.step(accion):
#             xpath = locConsultaCBUyAlias.cboCuentaCBU
#             xpath_cuenta = locConsultaCBUyAlias.cboCuentaCBU.format(cuenta)
#             self.selectElement(xpath, msgOk, msgFail, to)
#             self.selectElement(xpath_cuenta, msgOk, msgFail, to)
#             self.capture_image(accion)
            
    def seleccionarCuentaCBU(self, cuenta):
        accion = 'Seleccionar Cuenta CBU'
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locConsultaCBUyAlias.cboCuentaCBU
            try:
                self.selectListByPartialText(xpath, cuenta)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)           
    
#     def seleccionarCuenta(self, cuenta):
#         accion = u'Seleccionar cuenta'
#         msgOk, _ = get_msg(accion)
#         with self.step(accion):
#             self.selectListByPartialText(SS.select_cuenta, cuenta)
#             self.capture_image(msgOk)

    
#     
    def validarCBU(self):
        accion = 'Validar CBU'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locConsultaCBUyAlias.CBU
            if self.visibility_element(xpath, to):
                numeroCBU = self.get_element_text(xpath)
                if self.CBU == numeroCBU:
                    self.highlight(xpath, accion)                    
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
    def validarAlias(self):
        accion = 'Validar Alias'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locConsultaCBUyAlias.alias
            if self.visibility_element(xpath, to):
                textoAlias = self.get_element_text(xpath)
                if self.Alias == textoAlias:
                    self.highlight(xpath, accion)                    
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                       
    
# 

# 
#     def verDetalle(self):
#         accion = 'Ver detalle ECheq'
#         msgOk, msgFail = get_msg(accion)
#         to = 10
#         with self.step(accion):
#             xpath = plConsultaEcheq.tbl_detalles
#             if self.visibility_element(xpath, to):
#                 self.highlight(xpath, accion)
#             else:
#                 self.fail_msg(accion)
