# -*- coding: utf-8 -*-
import unittest
import allure
from traceback import format_exc
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stSolicitudSeguro import stSolicitudSeguro
from SeleniumFramework.common_functions import get_user_hb
from SeleniumFramework.constants.excel_constants import (
    USUARIO, CLAVE, M_PAGO, CUENTA, SEGURO, PLAN, SECCION_SEGURO
)


@allure.feature(u'Seguros')
@allure.story(u'Consorcio')
@allure.testcase(u'HB-T174 - Solicitud de seguro Consorcio')
@allure.title(u'HB-T174 - Solicitud de seguro Consorcio')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T174")
@allure.description(
    u"""
1-Desde las posición consolidada ir al menú Productos </br>
2-Selecionar Seguros solicitud </br>   
3-Dirigirse a la seccion Consorcio </br>
4-Selecionar boton contratar Integral de consorcios </br>
5-Verificar que se realice el salto de sito a https://www.itau.com.ar/consorcios/Paginas/default.aspx </br>
6-Fin  
"""
)

class HB_T174(unittest.TestCase, stLogin, stInicio, stSolicitudSeguro):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T213(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudSeguro()
            self.seleccionar_btn_seccion_seguro(self.seccion_seguro)
            self.seleccionar_btn_contratar_tipo(self.seguro)
            self.verificar_salto_a_itau_seguros_consorcios()
            self.finalizo = True
        except Exception:
            self.error = format_exc()

    def tearDown(self):
        finalizar_test(self)

    def get_datos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.seccion_seguro = self.usuario.get(SECCION_SEGURO)
        self.seguro = self.usuario.get(SEGURO)
        self.plan = self.usuario.get(PLAN)
        self.medioPago = self.usuario.get(M_PAGO)
        self.cuenta = self.usuario.get(CUENTA)


if __name__ == "__main__":
    unittest.main()
