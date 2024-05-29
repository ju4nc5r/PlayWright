# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CVM
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, CUENTA_DEB, CUENTA_ACRED, IMPORTE
)


@allure.feature(u'Transferencias entre cuentas propias')
@allure.story(    u"Transferecias entre sus cuentas propias CA a CC")
@allure.testcase(u"HB-T114 -0058- Transferencias entre cuentas propias de CA a CC")
@allure.title(u"HB-T114 -0058- Transferencias entre cuentas propias de CA a CC")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T114")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario completa campos para realizar transferencia. Primera
    pantalla </br>
    1-Ir al menú Transferencias </br>
    2-Clickear <b>Entre cuentas propias Itaú - compra/venta de moneda
    extranjera</b> </br>
    3-Seleccionar cuenta de débito en $  </br>
    4-Seleccionar cuenta de acreditación $ </br>
    5-Ingresar importe</br>
    6-Presionar <b>continuar</b></br>
    7-Presionar <b>confirmar</b></br>  
    8-Validar Ticket</br>
    9-Cerrar sesion</br>
    """
)
class tst_HB_T114(unittest.TestCase, CVM):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T149(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMenuTransferencias()
            self.seleccionarCompraVenta()
            self.seleccionarCtaDebito()
            self.seleccionarCtaAcreditacion()
            self.completarImporte(self.importe)
            self.seleccionarContinuar_compra_venta()
            self.seleccionarConfirmar()
            self.verificarResultado()
            self.verificarBtnDescargar()
            self.verificarNuevaTransferencia()
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
        self.importe = self.usuario.get(IMPORTE)


if __name__ == "__main__":
    unittest.main()
