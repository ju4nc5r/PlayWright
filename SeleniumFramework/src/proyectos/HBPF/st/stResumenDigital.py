# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locResumenDigital import locResumenDigital
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg



class stResumenDigital(menu):
                    
    def seleccionarCuenta(self, cuenta):
        accion = 'Seleccionar Cuenta'
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locResumenDigital.cboCuenta
            try:
                self.selectListByPartialText(xpath, cuenta)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)   
                
    def seleccionarAnio(self, anio):
        accion = u'Seleccionar Año'
        to = 10
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locResumenDigital.cboAnio
            print ('año ' + anio)
            try:
                self.selectListByPartialText(xpath, anio)
                self.capture_image(accion) 
            except Exception:
                self.fail_test(msgFail)          
                         
            
    def seleccionarLupa1(self):
        accion = u'seleccionar Lupa de primera fecha cierre'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locResumenDigital.imgLupaFecha1
        with self.step(accion):
            if self.visibility_element(xpath, to):               
                self.selectElement(xpath,msgOk, msgFail, to)
#               Se valida si abrió ventana visualización pdf, si no se hace click de nuevo en la lupa (la aplicación funciona así)
                xpath2 = locResumenDigital.pdfResumen  
                for x in range(4):
                    if self.visibility_element(xpath2, to):
                        break
                    else:
                        self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)        
                
    def validarVisualizacionResumenCta(self):
        accion = u'Validar visualización resumen de cuenta'
        msgOk, msgFail = get_msg(accion)
        to = 20
        with self.step(accion):
            xpath = locResumenDigital.pdfResumen  
            if self.visibility_element(xpath, to):
                self.wait(5)
                self.highlight(xpath, msgOk)                       
            else:
                self.fail_msg(msgFail)
            
    def seleccionarCerrar(self):
        accion = u'Seleccionar Cerrar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locResumenDigital.btnCerrar
        with self.step(accion):
            if self.visibility_element(xpath, to):               
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)        


    def seleccionarLinkResumenDigital(self):
        accion = u'Seleccionar link resumen digital en posicion consolidada'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = locResumenDigital.lnkResumenDigital
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.highlight(xpath, u"link resumen digital en posicion consolidada") 
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)        

    
 
        
 