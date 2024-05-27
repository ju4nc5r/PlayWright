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
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Fondos Comun de inversion')
@allure.story(u'Suscripcion de fondos comunes de inversion')
@allure.testcase(u'HB-T176-0276: Suscripcion de Fondos Comunes de Inversion sin seleccionar cuenta (validacion)')
@allure.title(u'HB-T176-0276: Suscripcion de Fondos Comunes de Inversion sin seleccionar cuenta (validacion)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Verificacion de elementos presentes en Suscripcion de fondos
    comunes de inversion.
    </br>
    1. Desde posicion consolidada acceder a <b>Productos</b> </br>
    2. Click en <b>Fondos Comunes de inversion</b>-><b>Suscripcion</b>. </br>
    3. En la pantalla de Suscripcion validar los elementos: </br>
        - Cuenta comitente. </br>
        - Boton Cancelar. </br>
        - Boton Continuar </br>
        </br>
    </br></br>"""
)

class HB_T176(unittest.TestCase, stLogin, stInicio,
               stSuscripcionFondoInversion):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T462(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudFondosInversion()
            self.verificarPantallaSolicitud()
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
