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
@allure.story(u'Transferencias - Agenda de cuentas - Modificacion cliente de otro banco ')
@allure.testcase( u"HB-T154 -0355- Agenda de cuentas- Modificacion cliente de otro banco")
@allure.title(u"HB-T154 -0355- Agenda de cuentas- Modificacion cliente de otro banco")
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T154")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Usuario selecciona la funcion agenda de cuentas </br>
    1-Ir al menu Transferencias </br>
    2-Clickear la opcion Agenda de cuentas </br>
    3-Selecionar de la agenda cliente de otro banco a Modificar </br>
    4-Modificar el campo requerido Descripcion </br>
    5-Clikear continuar </br>
    6-Clikear Confirmar </br>
    7-Verificar Ticket </br>
    8-cerrar sesion </br>
    """  
)

class HB_T154(unittest.TestCase, stAgendaDeCuentas, stLogin):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T193(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarAgendaCuentas()
            self.seleccionarClienteNuevo(self.desc)
            self.seleccionarModificar()
            self.ingresarDescripcion(self.concepto)
            self.seleccionarContinuar()
            self.seleccionarConfirmar()
            self.validarTicket()
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