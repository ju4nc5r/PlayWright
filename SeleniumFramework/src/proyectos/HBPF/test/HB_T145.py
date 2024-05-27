# -*- coding: utf-8 -*-
import unittest,pytest
import allure
import traceback
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.src.utils.excel_file import excel_file, usuarios
from SeleniumFramework.src.proyectos.HBPF.st.stTransferenciasTerceros import (
    stTransferenciaTerceros as stTT
)
from SeleniumFramework.constants.excel_constants import (USUARIO, CLAVE, CUENTA_DEB, CUENTA_ACRED, CBU, IMPORTE, CONCEPTO, CARACTERISTICA, TERCER_CUARTO)


@allure.feature(u'Transterencias a terceros con ALIAS')
@allure.story( u"Transferencia a Terceros con ALIAS con diversos conceptos")
@allure.testcase(u"HB-T145 -0340- Transferencia a Terceros ALIAS con concepto Seguros")
@allure.title(u"HB-T145 -0340- Transferencia a Terceros ALIAS con concepto Seguros")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T145")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario selecciona cuenta origen e ingresa un Alias de otro banco" </br>
    1-Ir al menú Transferencias </br>
    2-Clickear A terceros con cuenta Itaú </br>
    3-Seleccionar Cuenta de débito </br>
    4-Ingresar ALIAS de otro banco</br>
    5-ingresar las coordenas + pin
    6-Seleccionar concepto Seguros</br>
    6-Ingresar importe </br>
    7-Presionar continuar </br>
    9-Validar ticket </br>
    10-cerrar session </br>
    """
)

class tst_HB_T145(unittest.TestCase, stTT, stLogin):
    def setUp(self):
        inicio_test(self)

    def test_HB_T145(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            # self.TransferenciaTercerosOtrosBancos()
            self.seleccionar_a_terceros()
            self.seleccionarCuentaCorriente()
            #self.verAgenda()
            #self.seleccionarDestinatario(self.CBU)
            self.ingresarCuentaDestinoCases(self.CBU)
            self.seleccionarConcepto()
            self.seleccionarDeclaracionJurada()
            self.seleccionarImporte()
            self.continuar()
            self.completarCoordenadas()
            self.finalizarTransferencia()
            self.comprobar_tabla_cuenta()
            self.wait(10)
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuentaDeb = self.usuario.get(CUENTA_DEB)
        self.cuentaAcred = self.usuario.get(CUENTA_ACRED)
        self.CBU = self.usuario.get(CBU)
        self.importe = self.usuario.get(IMPORTE)
        self.concepto = self.usuario.get(CONCEPTO)
        self.caracteristica = self.usuario.get(CARACTERISTICA)
        self.tercerCuarto = self.usuario.get(TERCER_CUARTO)


if __name__ == "__main__":
    unittest.main()