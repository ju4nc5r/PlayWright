# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stConsultaCBUyAlias import stConsultaCBUyAlias
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, ALIAS, CBU, CUENTA


@allure.feature(u'Consulta de CBU/Alias')
@allure.story(u'Consulta de CBU /Alias CG')
@allure.testcase(u"HB-T162 Consulta de CBU /Alias CG")
@allure.title(u"HB-T162 Consulta de CBU /Alias CG")
@allure.link(u"https://itau-arg.atlassian.net/projects/CDPF?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.kanoah.test-manager__main-project-page#!/testCase/CDPF-T201")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u""" 
    1- En posición consolidada, hacer click en la opcion Productos/cuentas
    2- Seleccionar la opcion Consulta de CBU/Alias
    3- Seleccionar cuentas
    4- Selecionar la cuenta CA$
    5- Validar en pantalla que se visualicen el campo CBU (clave bancaria uniforme) y Alias   
    6- Seleccionar volver 
    7- Seleccionar salir
    

""")

class HB_T162(unittest.TestCase, stLogin, stInicio, stConsultaCBUyAlias):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T201(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.wait(5)
            self.seleccionarConsultaCBUyAlias()
            self.seleccionarCuentaCBU(self.cuenta)
            self.validarCBU()
            #self.validarAlias()                 
            
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.CBU   = self.usuario.get(CBU)
        self.Alias = self.usuario.get(ALIAS)
        self.cuenta = self.usuario.get(CUENTA)
       
if __name__ == "__main__":
    unittest.main()