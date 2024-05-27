# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaCotizacion import plConsultaCotizacion
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaCotizacion(menu):
    def verficarCotizacionDolar(self):
        accion = u'Consulta Cotizacion Dolar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath1 = plConsultaCotizacion.dolar_compra
        xpath2 = plConsultaCotizacion.dolar_venta
        with self.step(accion):
            if self.double_visibility_element(xpath1, xpath2, to):
                self.highlight(xpath1, accion)
                self.highlight(xpath2, accion)
            else:
                self.fail_msg(msgFail)
    
    def verficarCotizacionEuro(self):
        accion = u'Consulta Cotizacion Euro'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath1 = plConsultaCotizacion.euro_compra
        xpath2 = plConsultaCotizacion.euro_venta
        with self.step(accion):
            if self.double_visibility_element(xpath1, xpath2, to):
                self.highlight(xpath1, accion)
                self.highlight(xpath2, accion)
            else:
                self.fail_msg(msgFail)

    def verficarCotizacionReal(self):
        accion = u'Consulta Cotizacion Real'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath1 = plConsultaCotizacion.real_compra
        xpath2 = plConsultaCotizacion.real_venta
        with self.step(accion):
            if self.double_visibility_element(xpath1, xpath2, to):
                self.highlight(xpath1, accion)
                self.highlight(xpath2, accion)
            else:
                self.fail_msg(msgFail)

    