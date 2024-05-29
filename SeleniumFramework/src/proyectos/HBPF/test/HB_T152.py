# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.src.proyectos.HBPF.st.stAgendaDeCuentas import stAgendaDeCuentas
from SeleniumFramework.constants.excel_constants import (USUARIO, CLAVE, CBU, CONCEPTO, CARACTERISTICA)


@allure.feature(u'Transferencias - Agenda de cuentas')
@allure.story(u"Transferencias - Agenda de cuentas - Alta cliente de otro banco")
@allure.testcase(u"HB-T152 -0351- Agenda de cuentas - Alta cliente de otro banco")
@allure.title(u"HB-T152 -0351- Agenda de cuentas alta otro cliente de otro banco")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T152")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario selecciona la funcion agenda de cuentas </br>
    1-Ir al menu Transferencias </br>
    2-Clickear la opcion Agenda de cuentas </br>
    3-Seleccionar boton alta </br>
    4-Selecionar la opcion "Agendar cliente de otro banco/br>
    5-Completar los campos requeridos cuenta-Descripcion </br>
    6-Clikear continuar </br>
    7-Clikear Confirmar </br>
    8-Verificar Ticket </br>
    9-cerrar sesion </br>
    """
)

class HB_T152(unittest.TestCase, stAgendaDeCuentas, stLogin):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T191(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.wait(10)
            self.seleccionarAgendaCuentas()
            self.wait(5)
            self.seleccionarAlta()
            self.seleccionarOtroBanco()
            self.wait(5)
            self.seleccionarContinuar()
            self.wait(5)
            self.ingresarCuenta(self.cuenta)
            self.ingresarDescripcion(self.desc)
            self.seleccionarContinuar()
            self.wait(5)
            self.seleccionarConfirmar()
            self.wait(5)
            # self.seleccionarConfirmar()
            self.wait(5)
            self.validarTicket()
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CBU)
        self.concepto = self.usuario.get(CONCEPTO)
        self.desc = self.usuario.get(CARACTERISTICA)


if __name__ == "__main__":
    unittest.main()