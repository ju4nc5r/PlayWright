# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stRescate import stRescate
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, CUENTA_COMITENTE


@allure.feature(u'Fondos Comun de inversion')
@allure.story(u'Rescate de Fondos Comunes de Inversion.')
@allure.testcase(u'HB-T180-0280: Rescate de fondos comunes de inversion con cuenta (validacion)')
@allure.title(u'HB-T180-0280: Rescate de fondos comunes de inversion con cuenta (validacion)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Validacion de elementos de la pantalla de rescate de fondos comunes de inversion seleccionando cuenta
    comitente. Se valida la grilla con las siguientes columnas: "Fondo", "Moneda","Fecha valor de cuotaparte", 
    "Cantidad de cuotaparte", "Saldo valorizado" y  "Valor Cuotaparte".</br>
    
    1.Desde posicion consolidada acceder a <b>Productos</b>.</br>
    2.Click en <b>Rescate de fondos comunes de inversion</b>.</br>
    4.Seleccionar cuenta comitente.</br>
    5.Validar visualizacion de fondos contratados.</b>.</br>
    </br>"""
)

class HB_T180(unittest.TestCase, stLogin, stInicio, stRescate):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T455(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarRescatar()
            self.seleccionarCuenta(self.cuenta)
            self.verificarTablaFondos()
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


if __name__ == "__main__":
    unittest.main()
