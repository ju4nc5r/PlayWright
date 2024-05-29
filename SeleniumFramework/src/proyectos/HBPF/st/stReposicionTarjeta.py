# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.stConsultaTC import stConsultaTC
from SeleniumFramework.src.proyectos.HBPF.loc.locReposicionTarjeta import locReposicionTarjeta
from SeleniumFramework.common_functions import get_msg

class stReposicionTarjeta(stConsultaTC):
    def seleccionarMotivo(self, motivo):
        accion = u'Seleccionar el motivo {}'.format(motivo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locReposicionTarjeta.selectMotivo
            if self.selectListByPartialText(xpath, motivo):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarTipoTarjeta(self, tipo):
        accion = 'Seleccionar tarjeta {}'.format(tipo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locReposicionTarjeta.selectTipoTarjeta
            if self.selectListByPartialText(xpath, tipo):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarCuentaTarjeta(self, cuenta):
        accion = 'Seleccionar la cuenta {}'.format(cuenta)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locReposicionTarjeta.selectCtaTarjeta
            if self.selectListByPartialText(xpath, cuenta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarContinuarReposicion(self):
        accion = u'Seleccionar botón coninuar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locReposicionTarjeta.btnContinuar
            if self.selectElement(xpath, msgOk, msgFail):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarConfirmar(self):
        accion = u'Seleccionar botón confirmar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locReposicionTarjeta.btnConfirmar
            if self.selectElement(xpath, msgOk, msgFail):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarModificar(self):
        accion = u'Seleccionar botón modificar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locReposicionTarjeta.btnModificar
            if self.selectElement(xpath, msgOk, msgFail):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)