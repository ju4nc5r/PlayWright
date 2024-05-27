import time
import allure
import unittest
from traceback import format_exc
from PlaywrightFramework.projects.HBPF.st import inicio_test, finalizar_test
from PlaywrightFramework.projects.HBPF.st.stBrowser import stBrowser
from PlaywrightFramework.config.utils import config as utils

@allure.epic('Consulta datos personales')
@allure.feature('Cliente Selecta')
@allure.story('Flujo exitoso de consulta de datos personales por cliente selecta')
@allure.issue('https://linkaticketabierto.com')
@allure.testcase('https://linkatestdezephyr.com')
class HB_T02(unittest.TestCase, stBrowser):

    def setUp(self):
        inicio_test(self, clean=True)
        name = str(self._testMethodName)
        page = stBrowser(rec=f'../HBPF/files/{name}')
        self.HB = page

    def test_HB02(self):

        try:
            self.HB.openHB()
            self.HB.login()
            self.HB.selecccionarPerfil()
            self.HB.seleccionarDatosPersonales()
            self.HB.validarCamposDatosPersonales()

            self.finalizo = True

        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()


