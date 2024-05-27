# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stConsultaFondoInversion import stConsultaFondoInversion
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Fondos Comun de inversion')
@allure.story(u'Consulta de Fondos Comunes de Inversión')
@allure.testcase(u'HB-T175-0274: Consulta de Fondos Comunes de Inversión(validacion)')
@allure.title(u'HB-T175-0274: Consulta de Fondos Comunes de Inversión(validacion)')
@allure.link(u"https://itau-arg.atlassian.net/projects/CDPF?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.kanoah.test-manager__main-project-page#!/testCase/CDPF-T452")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Validar componentes de la pantalla de Consulta de Fondos Comunes de
    Inversion:</br>
    1. Desde posicion consolidada acceder a <b>Productos</b> </br>
    2. Click en <b>Fondos Comunes de inversion</b> -> <b>Consulta de tenencias</b>.</br>
    3. En la pantalla de Consulta validar los elementos: </br>
        - Cuenta comitente. </br>
        - Fondos. </br> 
        - Fecha valor de cuotaparte. </br>
        - Cantidad de cuotaparte. </br>
        - Saldo valorizado. </br>
        - Botones Volver, Valor Cuotaparte y Características.</br>
""")

class HB_T175(unittest.TestCase, stLogin, stInicio, stConsultaFondoInversion):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T452(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarConsultaFondosInversion()
            if self.verificarTablaFondos():
                self.verificacionConsultaFondos()
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