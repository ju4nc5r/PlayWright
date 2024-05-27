# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locResumenesAnteriores import (
    locResumenesAnteriores as RA
)
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stResumenesAnteriores(menu):
    def seleccionarTarjetaRA(self, tarjeta):
        accion = 'Seleccionar Tarjeta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = RA.tarjetasRA
            if self.selectListByPartialText(xpath, tarjeta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
            xpath1 = ''
            xpath2 = RA.span_sinResumen
            xpath3 = RA.div_error
            elem_list = [xpath1, xpath2, xpath3]
            to = 10
            numero = self.array_visibility(elem_list, to)
            if numero == 0:
                pass
            elif numero == 1:
                self.capture_image('La tarjeta no tiene resumenes')
            else:
                self.fail_msg('Se muestra mensaje de error')

    def seleccionarTarjetaUR(self, tarjeta):
        accion = 'Seleccionar Tarjeta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = RA.tarjetasUR
            if self.selectListByPartialText(xpath, tarjeta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
            xpath1 = ''
            xpath2 = RA.span_sinResumen
            xpath3 = RA.div_error
            elem_list = [xpath1, xpath2, xpath3]
            to = 10
            numero = self.array_visibility(elem_list, to)
            if numero == 0:
                pass
            elif numero == 1:
                self.capture_image('La tarjeta no tiene resumenes')
            else:
                self.fail_msg('Se muestra mensaje de error')
