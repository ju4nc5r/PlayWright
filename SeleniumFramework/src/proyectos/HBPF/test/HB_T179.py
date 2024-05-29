# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stRescate import stRescate
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Fondos Comunes de inversion')
@allure.story(u'Rescate de fondos comunes de inversion')
@allure.testcase(u'HB-T179-0279: Rescate de fondos comunes de inversion sin seleccionar cuenta (validacion)')
@allure.title(u'HB-T179-0279: Rescate de fondos comunes de inversion sin seleccionar cuenta (validacion)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Validacion de elementos de la pantalla de rescate de fondos sin seleccionar cuenta.
    </br>
    1.Desde posicion consolidada acceder a <b>Productos</b> </br>
    2.Click en <b>Rescate de fondos comunes de inversion</b>.</br>
    4.Se valida el label de <b>Cuenta Comitente</b>.</br>
    5.Se muestra habilitado el dropdown de <b>Cuenta Comitente</b>.</br>
    6.Se valida la visualizan de los mensajes.</br>
    """)

class HB_T179(unittest.TestCase, stLogin, stInicio, stRescate):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T463(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarRescatar()
            self.verificarPantallaRescate()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        # Usuario con o sin fondos comunes de inversion
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)


if __name__ == "__main__":
    unittest.main()
