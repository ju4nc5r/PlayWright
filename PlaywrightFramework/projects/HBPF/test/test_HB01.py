import os
import unittest
import allure
import time
from PlaywrightFramework.projects.HBPF.st import inicio_test, finalizar_test
from PlaywrightFramework.projects.HBPF.st.stBrowser import stBrowser
from traceback import format_exc


@allure.epic('Login')
@allure.feature('Login Selecta')
@allure.story('Camino exitoso de login con validación de textos y objetos')
@allure.issue('https://linkaticketabierto.com')
@allure.testcase('https://linkatestdezephyr.com')
class HB_T01(unittest.TestCase, stBrowser):

    def setUp(self):
        inicio_test(self)
        name = str(self._testMethodName)
        page = stBrowser(rec=f'files/{name}')
        self.HB = page

    def test_HB01(self):
        try:
            self.HB.openHB()
            self.HB.completarUsuario()
            self.HB.completarPassword()
            self.HB.seleccionarIngresar()
            self.finalizo = True

        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()

    # titulo = page.title()
    # self.assertEqual(titulo, 'Google')
    # self.error = traceback.format_exc()

'''
    def getDatos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.claveRandom = "Aa" + str(random.randint(1111111111, 9999999999))
        self.claveNueva = self.claveRandom
'''
