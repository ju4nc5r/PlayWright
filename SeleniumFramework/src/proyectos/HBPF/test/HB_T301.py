# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stConsultaTItulos import stConsultaTitulo
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, CUENTA, TITULO


@allure.feature(u'Bonos y Titulos')
@allure.story(u'Detalle de un titulo u accion desde la consulta')
@allure.testcase(u"HB_T301 - tst_0286: Detalle de un titulo u accion desde la consulta",)
@allure.title(u'Detalle de un titulo u accion desde la consulta')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""Ingreso al Detalle de un titulo u accion desde la consulta" </br>
    Pasos: </br>
    1-Ingresa a la posicion consolidada </br>
    2-Click en el menu "Productos" </br>
    3-Click en "Consulta de Titulos y Acciones" </br>
    4-Se muestra el label de la cuenta comitente con titulos y acciones </br>
    5-Se muestra la grilla de titulos y acciones con los siguientes campos:
    </br>
        *Titulos y Valores </br>
        *Moneda </br>
        *Nominales </br>
        *Cotizacion(*) </br>
        *Saldo </br>
    6-Click en un bono o accion de la lista </br>
    7-Verificacion de elementos </br></br>"""
)
class HB_T301(unittest.TestCase, stLogin, stInicio, stConsultaTitulo):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T460(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarConsultaTitulosYAcciones()
            self.seleccionarTitulo(self.cuenta, self.titulo)
            self.verificarPantallaDetalle()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        # Usuario con o sin fondos comunes de inversion
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.cuenta = self.usuario.get(CUENTA)
        self.titulo = self.usuario.get(TITULO)


if __name__ == "__main__":
    unittest.main()
