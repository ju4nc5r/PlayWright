# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaFondoInversion import (
    plConsutalFondoInversion as CFI
)
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaFondoInversion(menu):
    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta comitente'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(CFI.select_cuentaComitente, cuenta)
            self.capture_image(msgOk)

    # Verificar Pantallas
    def verificacionConsultaFondos(self):
        self.verificarCuenta()
        # self.verificarTablaFondos()
        self.verificarBotonVolver()
        self.verificarBotonCuotaparte()
        self.verificarBotonCaracteristica()

    # Verificar elementos
    def verificarCuenta(self):
        accion = u'Verificar select cuentas'
        with self.step(accion):
            self.checkElement(CFI.select_cuentaComitente, accion)

    def verificarBotonVolver(self):
        accion = u'Verificar botón volver'
        with self.step(accion):
            self.checkElement(CFI.button_volver, accion)

    def verificarBotonCaracteristica(self):
        accion = u'Verificar botón característica'
        with self.step(accion):
            self.checkElement(CFI.button_caracteristica, accion)

    def verificarBotonCuotaparte(self):
        accion = u'Verificar botón de valor cuotaparte'
        with self.step(accion):
            self.checkElement(CFI.button_valorCuotaparte, accion)

    def verificarTablaFondos(self):
        accion = u'Verificar tabla de fondos'
        to = 10
        with self.step(accion):
            xpath1 = CFI.tabla_fondos
            xpath2 = CFI.span_sinFondos
            if self.double_visibility_element(xpath1, xpath2, to):
                self.checkElement(xpath1, accion)
                return True
            self.checkElement(xpath2, 'La cuenta no posee fondos')
            return False
