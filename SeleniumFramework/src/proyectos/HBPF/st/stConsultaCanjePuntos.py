# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.ConsultaCanjePuntos import ConsultaCanjePuntos
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaCanjePuntos(menu):
    def verificarPuntos(self):
        accion = u'verificar puntos en pantalla'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = ConsultaCanjePuntos.span_puntos
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def verificarPuntosOtherPage(self):
        accion = u'verificar puntos en pantalla en Tu mundo Puntos'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = ConsultaCanjePuntos.span_puntos_other
        with self.step(accion):
            self.driver.switch_to.window(self.driver.window_handles[1])
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.wait(5)
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                self.fail_msg(msgFail)

    def seleccionarIngresar(self):
        accion = u'seleccionar ingresar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = ConsultaCanjePuntos.btn_ingresar
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuar(self):
        accion = u'seleccionar continuar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = ConsultaCanjePuntos.btn_continuar
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)

    def seleccionarVolver(self):
        accion = u'seleccionar volver'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = ConsultaCanjePuntos.btn_volver
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.selectElement(xpath,msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)