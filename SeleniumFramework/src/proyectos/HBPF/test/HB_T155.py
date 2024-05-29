# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.src.proyectos.HBPF.st.stAgendaDeCuentas import stAgendaDeCuentas
from SeleniumFramework.constants.excel_constants import (USUARIO, CLAVE, CUENTA_ACRED, CONCEPTO, CARACTERISTICA)


@allure.feature(u'Transferencias - Agenda de cuentas')
@allure.story(u"Transferencias - Agenda de cuentas - Elimina de agenda cliente itau")
@allure.testcase( u"HB-T155 -0352- Agenda de cuentas - Elimina de agenda cliente itau")
@allure.title(u"HB-T155 -0352- Agenda de cuentas - Agenda de cuentas elimina de agenda cliente itau")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T155")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u""""Usuario selecciona la funcion agenda de cuentas </br>
    1-Ir al menu Transferencias </br>
    2-Clickear la opcion Agenda de cuentas </br>
    3-Seleccionar el cbu agendado </br>
    4-Selecionar el boton eliminar/br>
    5-Clikear continuar </br>
    6-Clikear Confirmar </br>
    7-Verificar Ticket </br>
    8-cerrar sesion </br>
    """
)


class HB_T155(unittest.TestCase, stAgendaDeCuentas, stLogin):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T194(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.wait(10)
            self.seleccionarAgendaCuentas()
            self.wait(5)
            self.seleccionarClienteNuevo(self.desc)
            self.wait(5)
            self.seleccionarEliminar()
            self.wait(5)
            self.seleccionarConfirmar()
            self.wait(5)
            self.validarTicket()
            self.wait(10)
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CUENTA_ACRED)
        self.concepto = self.usuario.get(CONCEPTO)
        self.desc = self.usuario.get(CARACTERISTICA)


if __name__ == "__main__":
    unittest.main()
