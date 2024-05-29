# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plAdhesionDebAuto import plAdhesionDebAuto as ADA
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stAdhesionDebAuto(menu, stLogin):
    def seleccionarTarjeta(self, tarjeta):
        accion = u'Seleccionar tarjeta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = ADA.select_tarjeta
            if self.selectListByPartialText(xpath, tarjeta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = ADA.select_cuentaDebito
            if self.selectListByPartialText(xpath, cuenta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarPagoMinimo(self):
        accion = u'Seleccionar pago mínimo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = ADA.radio_pagoMinimo
            if self.selectElement(xpath, '', '', to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarPagoTotal(self):
        accion = u'Seleccionar pago total'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = ADA.radio_pagoTotal
            if self.selectElement(xpath, '', '', to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuar(self):
        accion = u'Seleccionar botón continuar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = ADA.button_continuar
            self.selectElement(xpath, '', '', to)
            xpath1 = ADA.span_tarjeta
            xpath2 = ADA.div_error
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg('Se muestra mensaje de error')

    def seleccioanrCancelar(self):
        accion = u'Seleccionar botón cancelar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = ADA.button_cancelar
            if self.selectElement(xpath, '', '', to):
                if self.visibility_element(locLogin.titulo_esperado, to):
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
