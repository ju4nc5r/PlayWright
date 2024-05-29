# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locRecargaCelulares import locRecargaCelulares
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg



class stRecargaCelulares(menu):
                    
    def seleccionarCuenta_a_debitar(self, cuenta):
        accion = 'Seleccionar Cuenta a debitar'
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.cboCuenta_a_debitar
            try:
                self.selectListByPartialText(xpath, cuenta)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)           
                         
            
    def seleccionarOperadora(self, operadora):
        accion = 'Seleccionar la operadora'
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.cboOperadora
            try:
                self.selectListByPartialText(xpath, operadora)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)           
    
    def seleccionarNumero(self, numero):
        accion = 'Seleccionar número ' + numero
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.cboNumero
            try:
                self.selectListByPartialText(xpath, numero)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)     

    def ingresarCodArea(self, codArea):
        
        to = 10
        accion = 'Ingresar código de area'
        msgOk, _ = get_msg(accion)
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.txtCodArea
            try:
                self.write(xpath, codArea, to)
                self.capture_image(msgOk)
            except Exception:
                self.fail_test(msgFail)

    def ingresarNumero(self, numero):
        
        to = 10
        accion = 'Ingresar número de celular'
        msgOk, _ = get_msg(accion)
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.txtNumero
            try:
                self.write(xpath, numero, to)
                self.capture_image(msgOk)
            except Exception:
                self.fail_test(msgFail)
                
    def ingresarDescripcion(self, descripcion):
        
        to = 10
        accion = 'Ingresar descripcion'
        msgOk, _ = get_msg(accion)
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.txtDescripcion
            try:
                self.write(xpath, descripcion, to)
                self.capture_image(msgOk)
            except Exception:
                self.fail_test(msgFail)
        
    def seleccionarImporte(self, importe):
        accion = 'Seleccionar importe ' + importe
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locRecargaCelulares.cboImporte
            try:
                self.selectListByPartialText(xpath, importe)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)     
        
    def seleccionarContinuar(self):
        accion = u'seleccionar Continuar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locRecargaCelulares.btnContinuar
        with self.step(accion):
            if self.visibility_element(xpath, to):               
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarContinuarTkt(self):
        accion = u'seleccionar Continuar despues de generar ticket'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locRecargaCelulares.btnContinuaTkt      
        with self.step(accion):
            if self.visibility_element(xpath, to):               
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)                

                
    def seleccionarConfirmar(self):
        accion = u'seleccionar Confirmar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locRecargaCelulares.btnConfirmar
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)


    def VerificarGeneracionTicket(self):
        accion = u'Verificar generación del ticket o mensaje de exito sin ticket'
        msgOk, msgFail = get_msg(accion)
        to = 20
        with self.step(accion):
            xpath1 = locRecargaCelulares.pdfTicket
            xpath2 = locRecargaCelulares.msgExitoSinTicket
#             resultado_busqueda = self.double_visibility_element(xpath1, xpath2, to)
#             if resultado_busqueda == True:
#                 self.highlight(xpath1, msgOk)  # hb muestra ticket
#             elif resultado_busqueda == False:
#                 self.highlight(xpath2, msgOk)  #hb muestar mensaje de exito sin ticket
#             else:
#                 self.fail_msg(msgFail)  
            if self.visibility_element(xpath1, to):
                self.highlight(xpath1, msgOk)
            elif self.visibility_element(xpath2, to):
                self.highlight(xpath2, msgOk)                
            else:
                self.fail_msg(msgFail)

