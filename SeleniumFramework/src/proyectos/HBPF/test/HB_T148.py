# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stComprobantes import stComprobantes
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Transferencias- Consulta de comprobantes')
@allure.story(u"Verificar el  resultado de la transferencia desde el centro de recibos")
@allure.testcase(u"HB-T148 -0060- Transferencias consulta de comprobantes")
@allure.title(u"HB-T148 -0060- Transferencias consulta de comprobantes")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T148")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario accede al Centro de Recibos para verificar la transferencia. </br>
    1. Acceder al menú <b>Servicios</b> </br>
    2. Clickear <b>Consulta de comprobantes</b> </br>
    3. Cerrar session</b>
    """
)
class tst_HB_T148(unittest.TestCase, stComprobantes):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T188(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMasSoluciones()
            self.seleccionarMenuConsultaComprobante()
            self.verificarCampos()
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
