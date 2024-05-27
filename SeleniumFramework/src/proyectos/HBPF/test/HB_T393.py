# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CV
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, CUENTA_DEB, CUENTA_ACRED, MONEDA



@allure.feature(u'Solicitud de venta Dolar MEP(CG)')
@allure.story(u"'Solicitud de venta Dolar MEP(CG)'")
@allure.testcase(u"HB-T392 - Solicitud de venta Dolar MEP(CG)")
@allure.title(u"HB-T392 - Solicitud de venta Dolar MEP(CG)")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario completa campos para realizar transferencia, cuenta de origen
    y destino en distinta moneda </br>
    1- Ir al menu Moneda Extranjera </br>
    2- Seleccionar Dolar MEP </br> //a[@id='dolarMepV2']
    3- Seleccionar Venta </br> //tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]
    4- Seleccionar cuenta comitente </br>
    5-Ingresar monto </br>
    6-Presionar <b>Confirmar</b></br>  
    7-Validadar ticket</br>
    8-Cerrar Session</br>
    """
)

class tst_HB_T393(unittest.TestCase, CV):
    def setUp(self):
        inicio_test(self)

    def test_HB_T393(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarMonedaExtranjera()
            self.seleccionarDolarMep()
            self.seleccionarVenderMep()
            self.seleccionarCtaComitente()
            self.completarMonto()
            self.verificarBtnDescargar()
            self.seleccionarDescargar()
            self.seleccionarContinuar()
            #self.verificarPantallaConfirmacion()
            #self.seleccionarConfirmar()
            #self.verificarResultado()
            #self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.tipoCuentaDebito = self.usuario.get(CUENTA_DEB)
        self.tipoCuentaAcredita = self.usuario.get(CUENTA_ACRED)
        self.monto = self.usuario.get(MONTO)
        self.moneda = self.usuario.get(MONEDA)
        