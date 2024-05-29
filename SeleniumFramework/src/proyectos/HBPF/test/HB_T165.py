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
@allure.story(u'Tus cosas - Auto')
@allure.testcase(u'HB-T164 -0271- Solicitud de seguro auto')
@allure.title(u'HB-T164 -0271- Solicitud de seguro auto')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T165")
@allure.description(
    u"""
1-Desde las posición consolidada ir al menú Productos </br>
2-Selecionar Seguros Solicitud </br>  
3-Dirigirse a la seccion Tus cosas </br>
4-Selecionar boton contratar Auto </br> 
5-Verificar que se realice el salto de sito a https://www.itau.com.ar/seguros/Paginas/seguros-para-tu-patrimonio.aspx </br>
6-Fin """
)

class HB_T165(unittest.TestCase, stLogin, stInicio, stSolicitudSeguro):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T204(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudSeguro()
            self.seleccionar_btn_seccion_seguro(self.seccion_seguro)
            self.seleccionar_btn_contratar_tipo(self.seguro)
            self.verificar_salto_a_itau_seguros()
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
