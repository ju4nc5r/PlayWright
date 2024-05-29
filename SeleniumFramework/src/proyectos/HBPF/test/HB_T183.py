# -*- coding: utf-8 -*-
import allure
import unittest
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stPagosTC import stPagosTC
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Pago de Tarjeta')
@allure.story(u'Intento de pago con usuario que no tiene tarjeta')
@allure.testcase(u'HB-T183-0142: Intento de pago con usuario que no tiene tarjeta')
@allure.title(u'HB-T183-0276: Intento de pago con usuario que no tiene tarjeta')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Intento de pago con usuario que no tiene tajeta.
    </br>
    1. Login con usuario sin tarjeta de credito.</br>
    2. Desde posicion consolidada ingresar a <b>Pagos</b>.</br>
    3. En la solapa <b>Tarjeta de credito</b> ingresar a <b>Pago de tarjeta de credito</b>.</br>
    4. Validacion del mensaje resultante.</br>
""")

class HB_T183(unittest.TestCase, stPagosTC):
    def setUp(self):
        inicio_test(self)

    def test_HB_T183(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarPagoTC()
            self.verificarFaltaTC()
            self.wait(10)
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)


if __name__ == "__main__":
    unittest.main()
