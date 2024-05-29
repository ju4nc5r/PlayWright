# -*- coding: utf-8 -*-
import allure
import unittest
from traceback import format_exc
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stPagosTC import stPagosTC
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, TC_MASTER, IMPORTE, CUENTA


@allure.feature(u'Pago de Tarjeta')
@allure.story(u'Pago en pesos sin confirmar')
@allure.testcase(u'HB-T184: Pago en pesos sin confirmar')
@allure.title(u'HB-T184: Pago en pesos sin confirmar')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""En la pantalla de Resultado, Usuario presiona botón "Continuar" </br>
    1- Ingresar con un usuario que posea tarjetas de crédito </br>
    2- Ir al menú Pagos-->Tarjeta de crédito y clickear
    <b>Pago de tarjeta de crédito</b> </br>
    3- Clickear en el combo de tarjetas </br>
    4- Selecciono Cuenta en pesos a debitar </br>
    5- Selecciono Otro Importe </br>
    6- Ingreso importe a pagar </br>
    7- Clickear Continuar </br>
    8- Clikear confirmar </br>
    9- Clikear Continuar </br>"""
)



class HB_T184(unittest.TestCase, stPagosTC):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T458(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.pagoTC(self.tarjeta, self.importe)
            self.seleccionarSaldoPesos()
            self.seleccionarCuentaDebito(self.cuenta)
            self.completarOtroImporte(self.importe)
            self.seleccionarContinuar_PagoTc()
            self.cerrarCartelSaldoMayor()
            self.seleccionarConfirmar()
            #self.seleccionarContinuarAlInicio()
            #self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.tarjeta = self.usuario.get(TC_MASTER)
        self.cuenta = self.usuario.get(CUENTA)
        self.importe = self.usuario.get(IMPORTE)


if __name__ == "__main__":
    unittest.main()
