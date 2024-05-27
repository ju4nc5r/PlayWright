# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plVencimiento import plVencimiento
from SeleniumFramework.common_functions import get_msg
from sub import sub


class stVencimiento(sub):
    def seleccionarTarjetas(self):
        accion = "Seleccionar boton Itau - Tarjetas"
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plVencimiento.btn_ItauTarjetas
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = plVencimiento.table_tarjetas
            if self.visibility_element(xpath1, to):
                self.capture_image(u'Se muestra la tabla de tarjetas')
            else:
                self.capture_image(u'El usuario no posee tarjetas')
    
    # def seleccionarFirstCard(self):
    #     accion = "Seleccionar primer tarjeta"
    #     msgOk, msgFail = get_msg(accion)
    #     to = 10
    #     with self.step(accion):
    #         xpath = plVencimiento.first_card
    #         if self.visibility_element(xpath):
    #             self.selectElement(xpath, msgOk, msgFail, to)
    #             self.capture_image(msgOk)
    #         else:
    #             self.fail_msg(msgFail)

    def seleccionarPrestamos(self):
        accion = "Seleccionar boton Itau - Prestamos"
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plVencimiento.btn_ItauPrestamos
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = plVencimiento.table_prestamos
            xpath2 = plVencimiento.span_sinPrestamos
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(u'Se muestra la tabla de préstamos')
            else:
                self.capture_image(u'El usuario no posee préstamos')

    def seleccionarDebitoAutomatico(self):
        accion = "Seleccionar boton Itau - Debito automatico"
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plVencimiento.btn_ItauDebitoAutomatico
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = ''  # Falta agregar el xpath de la tabla de debito auto
            xpath2 = plVencimiento.span_sinDebitoAutomatico
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(u'Se muestra la tabla de débito automático')
            else:
                self.capture_image(u'El usuario no tiene débito automático')

    def seleccionarPagoMisCuentas(self):
        accion = "Seleccionar boton PagoMisCuentas"
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plVencimiento.btn_PagoMisCuentas
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = ''  # Falta obtener el xpath de pago mis cuenta
            xpath2 = plVencimiento.span_sinPagoMisCuentas
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(u'Se muestra la tabla de PagoMisCuentas')
            else:
                self.capture_image(u'No hay vencimientos de PagoMisCuentas')

    def seleccionarServiciosVisa(self):
        accion = "Seleccionar boton ServiciosVisa"
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plVencimiento.btn_ServiciosVisa
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = ''  # Falta xpath si tiene vencimientos
            xpath2 = plVencimiento.span_sinServicioVisa
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(u'Se muestra vencimiento del servicio Visa')
            else:
                self.capture_image(u'No hay vencimiento del servicio Visa')
