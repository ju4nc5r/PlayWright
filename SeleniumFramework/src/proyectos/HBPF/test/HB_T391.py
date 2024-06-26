# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CV
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, IMPORTE, CUENTA_DEB, CUENTA_ACRED, MONEDA



@allure.feature(u'Transferencias Compra/Venta de moneda extranjera (CG)')
@allure.story(u"Realizar una transferencia de venta de dolares desde 'Moneda Extranjera'")
@allure.testcase(u"HB-T116 -0064- Transferencias Venta de moneda extranjera")
@allure.title(u"HB-T116 -0064- Transferencias Venta de moneda extranjera")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T116")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario completa campos para realizar transferencia, cuenta de origen
    y destino en distinta moneda </br>
    1-Ir al men� Transferencias </br>
    2-Clickear <b>Entre cuentas propias Ita� - compra/venta de moneda
    extranjera</b> </br>
    3-Seleccionar cuenta de d�bito en U$S </br>
    4-Seleccionar cuenta de acreditaci�n en $ </br>
    5-Ingresar importe </br>
    6-Presionar <b>continuar</b></br>  
    7-Validadar ticket</br>
    8-Cerrar Session</br>
    """
)
class tst_HB_T391(unittest.TestCase, CV):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T451(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMonedaExtranjera()
            self.seleccionarCtaDebito()
            self.seleccionarCtaAcreditacion()
            self.completarImporte(self.importe)
            # self.seleccionarMoneda(self.moneda)
            self.mostrarTipoMonedas()
            self.seleccionarTipoMoneda(self.moneda)
            # self.aceptarDeclaracionJurada()
            self.seleccionarContinuar_compra_venta()
            self.verificarPantallaConfirmacion()
            self.seleccionarConfirmar()
            self.verificarResultado()
            self.seleccionarContinuar()
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
        self.moneda = self.usuario.get(MONEDA)


if __name__ == "__main__":
    unittest.main()
