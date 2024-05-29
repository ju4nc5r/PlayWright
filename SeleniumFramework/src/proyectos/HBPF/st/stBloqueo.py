# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plBloqueo import plBloqueo as plB
from sub import sub
from SeleniumFramework.common_functions import get_msg


class stBloqueo(sub):
    def seleccionarMotivo(self, motivo):
        accion = 'Seleccionar motivo'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(plB.select_motivo, motivo)
            self.capture_image(msgOk)

    def seleccionarTipoTarjeta(self, tarjeta):
        accion = 'Seleccionar el tipo de la tarjeta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(plB.select_tipoTarjeta, tarjeta)
            self.capture_image(msgOk)

    def seleccionarCuenta(self, cuenta):
        accion = 'Seleccionar la cuenta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(plB.select_cuenta, cuenta)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        accion = 'Seleccionar continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(plB.button_continuar, '', '', to)
            if self.visibility_element(plB.span_cuenta, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificar pantallas
    def verificarPantallaBloqueo(self):
        pass

    def verificarPantallaBloqueoConf(self):
        self.verificarCuenta()
        self.verificarTitular()
        self.verificarOperacion()
        self.verificarDomicilio()

    # Verificacion de los elementos
    def verificarCuenta(self):
        accion = 'Verificar cuenta'
        with self.step(accion):
            self.checkElement(plB.span_cuenta, accion)

    def verificarTitular(self):
        accion = u'Verificar titular'
        with self.step(accion):
            self.checkElement(plB.span_titular, accion)

    def verificarOperacion(self):
        accion = u'Verificar operación'
        with self.step(accion):
            self.checkElement(plB.span_operacion, accion)

    def verificarDomicilio(self):
        accion = u'Verificar domicilio'
        with self.step(accion):
            self.checkElement(plB.span_domicilio, accion)