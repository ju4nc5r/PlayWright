# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stPlazoFijo import stPlazoFijo
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, CUENTA_DEB, IMPORTE, FECHA_DESDE, TIPO_PFIJO
)


@allure.feature(u'Constitución de Plazo Fijo')
@allure.story(u'Constituir Nuevo Plazo fijo')
@allure.testcase(u"HB-T160 Constituir Nuevo Plazo Fijo")
@allure.title(u"HB-T160 Constituir Plazo Fijo Ticket")
@allure.link(u"https://itau-arg.atlassian.net/projects/CDPF?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.kanoah.test-manager__main-project-page#!/testCase/CDPF-T199")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario clickea botón Nuevo plazo fijo </br>
    1-Desde las posición consolidada ir al menú Productos -> Inversiones y
    hacer click en "Constitucion de plazo fijo" </br>
    2-Seleccionar cuenta con saldo </br>
    3-Seleccionar "Tipo de plazo fijo" clásico </br>
    4-Ingresar "Plazo" o "Fecha de vencimiento" </br>
    5-Ingresar Monto inicial </br>
    6-Presionar botón "simular" </br>
    7-Presionar el botón "constituir plazo fijo" </br>
    8-Presionar el botón "confirmar" </br>
    9-Presionar botón "nuevo plazo fijo" </br></br>"""
)

class tst_HB_T160(unittest.TestCase, stPlazoFijo):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T199(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.constituirPlazoFijo(
                self.cuenta, self.monto, self.plazo, self.tipoCuenta
            )
            self.seleccionarNuevoPlazoFijo()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.plazo = self.usuario.get(FECHA_DESDE)
        self.monto = self.usuario.get(IMPORTE)
        self.cuenta = self.usuario.get(CUENTA_DEB)
        self.tipoCuenta = self.usuario.get(TIPO_PFIJO)

    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()
