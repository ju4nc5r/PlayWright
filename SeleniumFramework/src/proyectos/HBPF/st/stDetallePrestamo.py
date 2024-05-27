# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plDetallePrestamo import plDetallePrestamo
from SeleniumFramework.common_functions import get_msg
from sub import sub

class stDetallePrestamo(sub):
    def seleccionarDetalleCuotas(self):
        accion = u'Seleccionar botón detalle de cuotas'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.cmdButton_detalleCuotas
            self.selectElement(xpath, msgOk, msgFail, to)
            self.verificarPantallaDetalleCuotas()
                
    def seleccionarVolverADetallePrestamo(self):
        accion = u'Seleccionar botón volver al detalle de préstamo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.cmdButton_volver_aPrestamo
            self.selectElement(xpath, msgOk, msgFail, to)
                
    def seleccionarVolverAInicio(self):
        accion = u'Seleccionaer bot�n volver al Inicio'
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.cmdButton_volver_aInicio
            self.selectElement(xpath, "", "", to)
            self.capture_image(accion)
            
    def seleccionarCuota(self, nroCuota):
        accion = u'Seleccionar cuota ' + nroCuota
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.td_numeroCuota.format(nroCuota)
            self.selectElement(xpath,"","",to)
            self.capture_image(accion)
    
    def verificarPantallaDetallePrestamo(self):
        accion = u'Verificar pantalla de detalle préstamos'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.label_tituloDetallePrestamo
            if (self.visibility_element(xpath, to)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def verificarPantallaDetalleCuotas(self):
        accion = u'Verificar pantalla de detalle cuotas'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.label_tituloDetalleCuotas
            if (self.visibility_element(xpath, to)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)