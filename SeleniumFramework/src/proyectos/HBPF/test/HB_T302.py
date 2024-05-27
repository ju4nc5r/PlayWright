# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stCompraTitulos import stCompraTitulos
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, CUENTA_COMITENTE, TITULO, IMPORTE, RUEDAS, LETRAS,
    CANTIDAD, CUENTA_DEB
)


@allure.feature(u' Bonos y Titulos')
@allure.story(u'HB_T302 - tst_0287: Compra de Bonos y Titulos (validar advertencia)')
@allure.testcase(u'HB_T302 - tst_0287: Compra de Bonos y Titulos (validar advertencia) ')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Compra de Bonos/Titulos" </br>
    Pasos: </br>
    1-Ingresa a la posicion consolidada </br>
    2-Click en el menu "Productos" </br>
    3-Click en "Compra de titulos y acciones" </br>
    4-Seleccionar cuenta comitente </br>
    5-Seleccionar Bono/Titulos publicos como tipo de inversion </br>
    6-Escribir en el campo especie las 3 primeras letras de un tipo de
    bono/titulo publico existente </br>
    7-validar mensaje de advertencia: La especie ingresada no pudo ser encontrada. Por favor intenta nuevamente 
                                    o comunicate con el Centro de Inversiones Itaú llamando al 0810-345-4900
"""
)
class test_HB_T302(unittest.TestCase, stLogin, stInicio, stCompraTitulos):
    def setUp(self):
        inicio_test(self)

    def test_HB_T302(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarComprarTitulos()
            self.verificarPantallaCargaDatos()
            self.seleccionarCuenta(self.cuenta)
            self.seleccionarTitulos()
            self.ingresarLetras(self.letras)
            self.seleccionar_btn_buscar()
            self.verificar_advertencia()
#             self.seleccionarTituloAComprar(self.titulo)
#             self.ingresarCantidadNominales(self.cantidad)
#             self.seleccionarContinuar()
#             self.ingresarPrecio(self.precio)
#             self.seleccionarCantidadRueda(self.ruedas)
#             self.seleccionarCuentaDebito(self.cuentaDeb)
#             self.seleccionarAceptarCondiciones()
#             self.seleccionarContinuar()
#             self.verificarPantallaConfirmacion()
#             self.seleccionarAceptarCondiciones()
#             self.seleccionarConfirmar()
#             self.verificarPantallaResultado()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        # Usuario con o sin fondos comunes de inversion
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CUENTA_COMITENTE)
        self.titulo = self.usuario.get(TITULO)
        self.letras = self.usuario.get(LETRAS)
        self.titulo = self.usuario.get(TITULO)
        self.cantidad = self.usuario.get(CANTIDAD)
        self.precio = self.usuario.get(IMPORTE)
        self.ruedas = self.usuario.get(RUEDAS)
        self.cuentaDeb = self.usuario.get(CUENTA_DEB)


if __name__ == "__main__":
    unittest.main()
