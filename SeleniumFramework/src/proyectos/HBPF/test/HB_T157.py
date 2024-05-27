# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stPlazoFijo import stPlazoFijo
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Constitución de Plazo Fijo')
@allure.story(u'Constituir Plazo fijo')
@allure.testcase(u"HB-T157 Constituir Plazo Fijo (Simulacion)")
@allure.title(u"HB-T157 Constituir Plazo Fijo (Simulacion)")
@allure.link(u"https://itau-arg.atlassian.net/projects/CDPF?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.kanoah.test-manager__main-project-page#!/testCase/CDPF-T196")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1. Desde las posicion consolidada ir al menu Productos -> Inversiones y
    hacer click en "Constitucion de plazo fijo"
    2. Seleccionar cuenta con saldo 
    3. Seleccionar "Tipo de plazo fijo clasico" 
    4. Ingresar "Plazo" o "Fecha de vencimiento"
    5. Ingresar Monto inicial
    6. Presionar boton "Simular"
    }"""
)

class tst_HB_T157(unittest.TestCase, stPlazoFijo):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T196(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMenuInversiones()
            self.seleccionarConstitucionDePlazoFijo()
            self.seleccionarCuenta('2')
            self.seleccionarTipoPlazoFijo(tipo='CLASICO')
            self.completarCampoPlazo(90)
            self.completarMontoinicial('500,00')
            self.seleccionarSimular()
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
