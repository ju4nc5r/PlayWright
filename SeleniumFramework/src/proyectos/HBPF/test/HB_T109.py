# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CVM
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Transferencias entre cuentas propias')
@allure.story(u'Transferecias entre cuentas propias - Botón limites diarios')
@allure.testcase(u"HB-T109 -0051- Transferencias entre cuentas propias - Botón limites diarios")
@allure.title(u"HB-T109 -0051- Transferencias entre cuentas propias - BotónLimites Diarios")
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T109")
@allure.description(
    u"""Usuario clickea en el botón Límites diarios.</br>
    1-Ir al menú Transferencias </br>
    2-Clickear <b>Entre cuentas propias Itaú - compra/venta de moneda
    extranjera</b> </br>
    3-Presionar el botòn <b>límites diarios</b>
    4-Presionar continuar </b>
    5-Cerrar sesion </b>
    """
)
class HB_T109(unittest.TestCase, CVM):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T148(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMenuTransferencias()
            self.seleccionarCompraVenta()
            self.seleccionarLimiteDiario()
            self.seleccionarCerrar()
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
