# -*- coding: utf-8 -*-
import unittest
import allure
import random
import traceback
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stCambioClave import stCambioClave
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Cambio de clave')
@allure.story(u'Realizar cambio de clave')
@allure.testcase( u"HB-T106 -0032- Cambio de clave - clave actual incorrecta")
@allure.title(u'HB-T106 -0032- Cambio de clave - clave actual incorrecta')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T106")
@allure.description(
    u"""Realizar cambio de clave </br>
    Condición de prueba: Usuario ingresa clave actual incorrecta y clave
    nueva y repetición correctas </br>
    pasos: </br>
    1-Hacer click en la rueda de configuración </br>
    2-Hacer click en el cambio de clave </br>
    3-Ingresar clave actual incorrecta y clave nueva y repetición correctas
    </br>
    4-Presionar botón <b>confirmar</b></br>
    5-Verificar el mansaje de error</br>
    6-Cerrar sesion</br>
    """
)
class HB_T105 (unittest.TestCase, stLogin, stCambioClave):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T143(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.getDatos()
            self.login()
            self.cambiarClave(True, True)
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def getDatos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.claveRandom = "Bb" + str(random.randint(1111111111, 9999999999))
        self.claveNueva = self.claveRandom

    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()
