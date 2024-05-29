# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stRescate import stRescate
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, CUENTA_COMITENTE, CUENTA_ACRED, FONDO, IMPORTE
)


@allure.feature(u'Fondos Comun de inversion')
@allure.story(u'Rescate de fondos comunes de inversion')
@allure.testcase(u'HB-T181-0281: Rescate de fondos comunes de inversion ingresando monto a rescatar')
@allure.title(u'HB-T181-0281: Rescate de fondos comunes de inversion ingresando monto a rescatar')
@allure.severity(allure.severity_level.NORMAL)

@allure.description(
    u"""Rescate de fondos ingresando monto a rescatar</b> </br>
    </br>
    
    1. Desde posicion consolidada acceder a <b>Productos</b> </br>
    2. Click en <b>Fondos Comunes de inversion -> Rescate</b> </br>
    3. En la pantalla de <b>Rescate</b> seleccionar la cuenta comitente. </br>
    4. Seleccionar el fondo a rescatar. </br>
    5. Seleccionar la cuenta de acreditacion. </br>
    7. Ingresar el monto a rescatar. </br>
    8. Seleccionar continuar. </br>
    9. Validar elementos de la pantalla de confirmacion. </br>
    10. Seleccionar confirmar. </br>
    11. Verificar pantalla de resultado. </br>
     </br>""" 
)

class HB_T181(unittest.TestCase, stLogin, stInicio, stRescate):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T456(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarRescatar()
            self.seleccionarCuenta(self.cuentaDeb)
            self.verificarTablaFondos()
            self.seleccionarFondo(self.fondo)
            self.seleccionarCuentaAcred(self.cuentaAcred)
            self.seleccionarMontoARescatar(self.monto)
            self.seleccionarContinuar()
            self.verificarPantallaConfirmacion()
            self.seleccionarConfirmar()
            self.verificarPantallaResultado()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        # Usuario con o sin fondos comunes de inversion
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuentaDeb = self.usuario.get(CUENTA_COMITENTE)
        self.cuentaAcred = self.usuario.get(CUENTA_ACRED)
        self.fondo = self.usuario.get(FONDO)
        self.monto = self.usuario.get(IMPORTE)


if __name__ == "__main__":
    unittest.main()