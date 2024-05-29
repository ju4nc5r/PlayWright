# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CVM
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, CUENTA_DEB, CUENTA_ACRED, MSJ_ESPERADO
)


@allure.feature(u'Transferencias entre cuentas propias')
@allure.story(u'Validacion de campos oblgatorios')
@allure.testcase(u"HB-T113 -0056-Transferencias entre cuentas propias sin ingresar el importe")
@allure.title(u'HB-T113 -0056-Transferencias entre cuentas propias sin ingresar el importe')
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T113")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario deja vacío el campo importe.</br>
    1-Ir al menú Transferencias </br>
    2-Clickear <b>Entre cuentas propias Itaú - compra/venta de moneda
    extranjera</b> </br>
    3-Seleccionar cuenta de débito </br>
    4-Seleccionar cuenta de acreditación </br>
    5-No Ingresar importe </br>
    6-Presionar <b>continuar</b></br>
    6-Presionar continuar.</br>
    7-Presionar confirmar.</br>
    8-Validar mensaje de error</br>
    9-Cerrar sesion </br>
    """
)
class tst_HB_T113(unittest.TestCase, CVM):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T152(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMenuProductos()
            self.seleccionarCompraVenta()
            self.seleccionarCtaDebito()
            self.seleccionarCtaAcreditacion()
            self.seleccionarContinuar_compra_venta(True)
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.tipoCuentaDebito = self.usuario.get(CUENTA_DEB)
        self.tipoCuentaAcredita = self.usuario.get(CUENTA_ACRED)
        self.mensaje_esperado = self.usuario.get(MSJ_ESPERADO)


if __name__ == "__main__":
    unittest.main()
