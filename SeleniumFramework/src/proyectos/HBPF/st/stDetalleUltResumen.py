# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plDetalleUltResumen import plDetalleUltResumen as DUR
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stDetalleUltResumen(menu):
    def seleccionarTarjeta(self, tarjeta):
        accion = u'Seleccionar tarjeta'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = DUR.select_tarjeta
            if self.selectListByPartialText(xpath, tarjeta):
                self.capture_image(msgOk)
            #else:
            #    self.fail_msg(msgFail)
            #xpath1 = DUR.img_resumen
            #xpath2 = DUR.span_sinResumen
            #xpath3 = DUR.div_error
            #elem_list = [xpath1, xpath2, xpath3]
            #numero = self.array_visibility(elem_list, to)
            #if numero == 0:
            #    pass
            #elif numero == 1:
            #    self.fail_msg('El usuario no tiene resumenes')
            #else:
            #    self.fail_msg('Se muestra mensaje de error')

    def seleccionarVerResumen(self):
        accion = u'Seleccionar el botón ver resumen'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.go_to_xpath(DUR.button_verResumen)
            self.selectElement(DUR.button_verResumen, '', '', to)
            self.capture_image(msgOk)

    def seleccionarVolver(self):
        accion = u'Seleccionar el botón volver'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(DUR.button_volver, '', '', to)
            self.capture_image(msgOk)

    def seleccionarPagar(self):
        accion = u'Seleccionar el botón pagar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(DUR.button_pagar, '', '', to)
            self.capture_image(msgOk)

    def seleccionarDescargar(self):
        accion = u'Seleccionar el botón descargar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(DUR.button_descargar, '', '', to)
            self.capture_image(msgOk)

    def seleccionarEnviarMail(self):
        accion = u'Seleccionar checkbox para enviar mail'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(DUR.checkbox_enviarMail, '', '',to)
            self.capture_image(msgOk)
