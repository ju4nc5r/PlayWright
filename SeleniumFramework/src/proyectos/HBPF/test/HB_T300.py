# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stConsultaTItulos import stConsultaTitulo
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Bonos y Titulos')
@allure.story(u'Consulta de Titulos y Acciones')
@allure.testcase(u'HB_T300: Consulta de Titulos y Acciones (validacion)')
@allure.title(u'Consulta de Titulos y Acciones')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Componentes de la pantalla de "Consulta de Titulos y Acciones" </br>
    Pasos:
    
    1-Ingresa a la posicion consolidada
    2-Click en el menu "Productos"
    3-Click en "Consulta de Titulos y Acciones"
    4-Se muestra el label de la cuenta comitente con titulos y acciones
    5-Se muestra la grilla de titulos y acciones con los siguientes campos:</br>
    *Titulos y Valores
    *Moneda
    *Nominales
    *Cotizacion(*)
    *Saldo
    6-Se muestra el boton de Volver </br>"""
)


class HB_T300(unittest.TestCase, stLogin, stInicio, stConsultaTitulo):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T459(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarConsultaTitulosYAcciones()
            self.verificarPantallaConsulta()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        # Usuario con o sin fondos comunes de inversion
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)


if __name__ == "__main__":
    unittest.main()
