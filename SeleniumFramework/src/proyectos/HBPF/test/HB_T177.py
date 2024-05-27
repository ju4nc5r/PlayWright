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
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, CUENTA_COMITENTE


@allure.feature(u'Fondos Comun de inversion')
@allure.story(u'Suscripcion de Fondos Comunes de Inversion')
@allure.testcase(u'HB-T177-0277: Suscripcion de Fondos Comunes de Inversion seleccionando cuenta (validacion)')
@allure.title(u'HB-T177-0277: Suscripcion de Fondos Comunes de Inversion seleccionando cuenta (validacion)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Verificacion de elementos presentes en Suscripcion de fondos
    comunes de inversion.</br>
    
    1. Desde posicion consolidada acceder a <b>Productos</b></br>
    2. Click en <b>Fondos Comunes de inversion</b>-><b>Suscripcion</b>. </br>
    3. Seleccionar la cuenta comitente. </br>
    4. Validar los fondos visibles para el perfil del usuario</br>
    5. Validar el boton <b>Caracteristicas de nuestros fondos</b>. </br>
    
    </br></br>"""
)

class HB_T177(unittest.TestCase, stLogin, stInicio,
               stSuscripcionFondoInversion):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T453(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudFondosInversion()
            self.seleccionarCuentaComitente(self.cuenta)
            self.verificarPantallaFondosOpciones()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CUENTA_COMITENTE)


if __name__ == "__main__":
    unittest.main()
