import re
import time
import allure
import unittest
from traceback import format_exc
from PlaywrightFramework.projects.HBPF.st import inicio_test, finalizar_test
from playwright.sync_api import Playwright, sync_playwright, expect
from PlaywrightFramework.projects.HBPF.st.stBrowser import stBrowser


@allure.epic('Consulta datos personales')
@allure.feature('Cliente Selecta')
@allure.story('Flujo exitoso de consulta de datos personales por cliente selecta')
@allure.issue('https://linkaticketabierto.com')
@allure.testcase('https://linkatestdezephyr.com')
class HB_T03(unittest.TestCase, stBrowser):

    def setUp(self):
        inicio_test(self)
        name = str(self._testMethodName)
        page = stBrowser(rec=f'../HBPF/files/{name}')
        self.HB = page

    def test_HB03(self):

        try:
            self.HB.openHB()
            self.HB.login()
            self.HB.seleccionarMenuProductos()
            self.HB.consultarCBUyAlias()

            with allure.step("Validar campos y textos"):
                expect(self.HB.page.locator("#label_selectField0")).to_contain_text("Cuenta")
                expect(self.HB.page.locator("#label_textField0")).to_contain_text("CBU (clave bancaria uniforme)")
                expect(self.HB.page.locator("#label_textField3")).to_contain_text("Nro. de cuenta")
                expect(self.HB.page.locator("#constantLabel1")).to_contain_text("Documento primer Titular")
                expect(self.HB.page.locator("#label_textField6")).to_contain_text("Alias")
                expect(self.HB.page.locator("#label_textField2")).to_contain_text("Nombre primer Titular")
                expect(self.HB.page.get_by_label("Cuenta")).to_be_visible()
                expect(self.HB.page.get_by_text("2590046220000464230191")).to_be_visible()
                expect(self.HB.page.get_by_text("0004642-301/9", exact=True)).to_be_visible()
                expect(self.HB.page.get_by_text("DNI")).to_be_visible()
                expect(self.HB.page.get_by_role("cell", name="DNI 20.190.729", exact=True).locator("div").first).to_be_visible()
                expect(self.HB.page.get_by_text("No disponible")).to_be_visible()
                expect(self.HB.page.locator("#textField2")).to_be_visible()
                expect(self.HB.page.get_by_role("checkbox", name="Enviar vía mail a")).to_be_visible()
                expect(self.HB.page.get_by_text("Enviar vía e-mail a")).to_be_visible()
                expect(self.HB.page.locator("#richText0")).to_contain_text("Recordá que podrás incorporar un alias a cada una de tus claves bancarias uniformes (CBUs), de manera tal que en oportunidad de informar tus datos a un emisor de transferencia o generador de pago, sólo deberás indicar el alias previamente asignado a la cuenta en la que desees recibir la transacción. Por su parte, el emisor de la transferencia o el generador del pago, a través de los respectivos aplicativos para llevar a cabo su gestión, deberá ingresar el alias de la cuenta receptora para su realización, sin necesidad de indicar la CBU correspondiente.")

            self.finalizo = True

        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()
