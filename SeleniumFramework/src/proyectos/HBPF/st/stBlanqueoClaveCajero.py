# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plBlanqueoClaveCajero import plBlanqueoClaveCajero
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stBlanqueoClaveCajero(menu):
    def seleccionarCuenta(self, cuenta):
        to = 10
        accion = 'Seleccionar cuenta'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plBlanqueoClaveCajero.ipt_nroCuenta
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = plBlanqueoClaveCajero.opt_nroCuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
    
    def seleccionarTarjeta(self, numTarj):
        to = 10
        accion = 'Seleccionar tarjeta'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plBlanqueoClaveCajero.ipt_nroTarjeta
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = plBlanqueoClaveCajero.opt_nroTarjeta.format(numTarj)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
    
    def seleccionarContinuar(self):
        to = 10
        accion = 'Seleccionar Continuar'
        msgOk = accion
        msgFail = 'No se pudo'+ msgOk.lower()
        with self.step(accion):
            xpath = plBlanqueoClaveCajero.btn_continuar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else: 
                self.fail_msg(msgFail)
    
    def verificarTicket(self):
        to = 10
        accion = 'Verificar Ticket'
        msgOk = accion
        msgFail = 'No se pudo'+ msgOk.lower()
        with self.step(accion):
            xpath = plBlanqueoClaveCajero.ticket
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)