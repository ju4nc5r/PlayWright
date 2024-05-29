# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CVM
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, IMPORTE, MSJ_ESPERADO



@allure.feature(u'Transferencias entre cuentas propias')
@allure.story(u'Validacion de campos oblgatorios mensaje cuenta debito')
@allure.testcase(u"HB-T111 -0054- Transferencias entre cuentas propias(Campos obligatorios)")
@allure.title(u'HB-T111 -0054- Transferencias entre cuentas propias(Campos obligatorios)')
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T111")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario deja vacío el campo cuenta origen.</br>
    1-Ir al menú Transferencias </br>
    2-Clickear <b>Entre cuentas propias Itaú - compra/venta de moneda
    extranjera</b> </br>
    3-Completar campo importe pero no seleccionar cuenta de débito </br>
    4-Presionar <b>continuar</b></br>
    5-Cerrar sesión </b></br>
    """
)
class tst_HB_T111(unittest.TestCase, CVM):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T151(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMenuProductos()
            self.seleccionarCompraVenta()
            self.completarImporte(self.importe)
            self.seleccionarContinuar_compra_venta(True)
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje_esperado = self.usuario.get(MSJ_ESPERADO)


if __name__ == "__main__":
    unittest.main()
