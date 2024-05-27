# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stCompraVentaMoneda import stCompraVentaMoneda as CV
from SeleniumFramework.common_functions import plazo_fecha, get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, IMPORTE, CUENTA_ACRED, CUENTA_DEB, PERIODO, FECHA_DESDE,
    REPETICION
)


@allure.feature(u'Transferencias entre cuentas propias')
@allure.story( u'Transferecias entre cuentas propias - Programada semanalmente')
@allure.testcase(u"HB-T117 -0067- Transferencias programadas entre cuentas propias (semanalmente)")
@allure.title(u"HB-T117 -0067- Transferencias programadas entre cuentas propias (semanalmente)")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T117")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario completa campos para realizar transferencia programada:
    semanal" </br>
    1-Ir al menú Transferencias </br>
    2-Clickear "Entre cuentas propias Itaú - compra/venta de moneda
    extranjera" </br>
    3-Seleccionar para cuenta de débito CA $ </br>
    4-Seleccionar para cuenta de acreditación CA $ </br>
    5-Ingresar importe </br>
    6-Clickear el check box de Programar transferencia </br>
    7-En el combo de selección de "Realizar esta transferencia" seleccionar
    <b>Semanalmente</b> </br>
    8-Seleccionar Fecha o escribirla en el text box de calendario ubicado
    al lado del label "El día" </br>
    9-Seleccionar repeticiones </br>
    10-Presionar <b>continuar</b>"""
)

class tst_HB_T117(unittest.TestCase, CV):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T156(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarCompraVenta()
            self.seleccionarCtaDebito()
            self.seleccionarCtaAcreditacion()
            self.completarImporte()
            self.transferenciaSemanalMensual(
                self.periodo, self.fechaProgramada, self.repe
            )
            self.seleccionarContinuar_compra_venta()
            self.verificarPantallaConfirmacion(self.periodo)
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
        self.periodo = self.usuario.get(PERIODO)
        self.fechaProgramada = plazo_fecha(self.usuario.get(FECHA_DESDE))
        self.repe = self.usuario.get(REPETICION)


if __name__ == "__main__":
    unittest.main()
