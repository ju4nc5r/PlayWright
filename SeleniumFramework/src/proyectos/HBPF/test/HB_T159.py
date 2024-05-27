# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stPlazoFijo import stPlazoFijo
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, CUENTA, TIPO_PFIJO, FECHA_DESDE, IMPORTE
)


@allure.feature(u'Constitución de Plazo Fijo')
@allure.story(u'Confirmacion Plazo fijo')
@allure.testcase(u"HB-T159 Constituir Plazo Fijo (validacion de campos)")
@allure.title(u"HB-T159 Constituir Plazo Fijo (validacion de campos)")
@allure.link(u"https://itau-arg.atlassian.net/projects/CDPF?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.kanoah.test-manager__main-project-page#!/testCase/CDPF-T198")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Desde las posición consolidada ir al menú Productos -> Inversiones y
    hacer click en "Constitucion de plazo fijo" 
    2-Seleccionar cuenta con saldo 
    3-Seleccionar "Tipo de plazo fijo" clásico 
    4-Ingresar "Plazo" o "Fecha de vencimiento" 
    5-Ingresar Monto inicial 
    6-Presionar botón "simular" 
    7-Presionar el botón "constituir plazo fijo" 
    8-Presionar el botón "confirmar" 
    """
)

class tst_HB_T159(unittest.TestCase, stPlazoFijo):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T198(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarConstitucionDePlazoFijo()
            self.seleccionarCuenta(self.cuenta)
            self.seleccionarTipoPlazoFijo(tipo='CLASICO')
            self.completarCampoPlazo(self.plazo)
            self.completarMontoinicial(self.monto)
            self.seleccionarSimular()
            self.verificarPantallaSimulacion(self.plazoFijo)
            self.seleccionarConstituirPlazoFijo()
            self.verificarPantallaConfirmacion(self.plazoFijo)
            self.seleccionarConfirmarPlazo()
            self.wait(5)
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        # El usuario debe poseer una cuenta en rosario, y la cuenta utilizada
        # en este test tiene que estar radicada en rosario
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CUENTA)
        self.plazoFijo = self.usuario.get(TIPO_PFIJO)
        self.plazo = self.usuario.get(FECHA_DESDE)
        self.monto = self.usuario.get(IMPORTE)


if __name__ == "__main__":
    unittest.main()
