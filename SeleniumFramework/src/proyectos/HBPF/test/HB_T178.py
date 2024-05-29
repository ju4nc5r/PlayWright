# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stSuscripcionFondoInversion import (
    stSuscripcionFondoInversion)
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, CUENTA_COMITENTE,GOALPESOS_A


@allure.feature(u'Fondos Comun de inversion')
@allure.story(u'Suscripcion de Fondos Comunes de Inversion')
@allure.testcase(u'HB-T178: Suscripcion de Fondos Comunes de Inversion')
@allure.title(u'HB-T178: Suscripcion de Fondos Comunes de Inversion')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Suscripcion a fondo comun de inversion Goal Pesos A.
    </br>
    1. Desde posicion consolidada acceder a <b>Productos</b></br>
    2. Click en <b>Fondos Comunes de inversion</b>-><b>Suscripcion</b>. </br>
    3. En la pantalla de <b>Suscripcion</b> seleccionar la cuenta comitente. </br>
    4. Seleccionar el boton <b>Suscribirme</b> del fondo Goal Pesos A. </br>
    5. Seleccionar la cuenta de debito. </br>
    6. Ingresar el importe a debitar. </br>
    7. Seleccionar el boton continuar. </br>
    8. Seleccionar el boton confirmar. </br>
    
    </br></br>"""
)

class HB_T178(unittest.TestCase, stLogin, stInicio,
               stSuscripcionFondoInversion):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T454(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudFondosInversion()
            self.seleccionarCuentaComitente(self.cuenta)
            self.seleccionarFondo(self.Fondo)
            self.seleccionarCuentaDebito()
            self.seleccionarImporte()
            self.seleccionarCheck()
            self.seleccionarContinuar()
            self.seleccionarConfirmar()
            self.wait(5)
            self.validarTicket()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CUENTA_COMITENTE)
        self.Fondo = self.usuario.get(GOALPESOS_A)

if __name__ == "__main__":
    unittest.main()
