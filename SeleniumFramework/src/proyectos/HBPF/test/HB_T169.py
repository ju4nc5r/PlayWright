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
@allure.story(u'Tus cosas - Bolso protegido')
@allure.testcase(u'HB-T169 -0266- Solicitud de seguro bolso protegido')
@allure.title(u'HB-T169 -0266- Solicitud de seguro bolso protegido')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T169")
@allure.description(
    u"""
1-Desde las posición consolidada ir al menú Productos </br>
2-Seleccionar Seguros Solicitud </br>
3-Dirigirse a la seccion Tus cosas </br>
4-Seleccionar boton Contratar Bolso protegido.</br>
5-Seleccionar un Plan A.</br>
6-Seleccionar boton continuar </br>
7-Seleccionar en el combo medio de pago Caja de ahorro" </br>
8-Seleccionar en el combo cuenta CA$ </br>
9-Seleccionar Acepto los Terminos y condiciones. </br>
10-Seleccionar continar </br>
11-Pantalla confirmacion </br>
12-Validar los campos Nombre, Linea de producto,Producto,</br> 
   Plan,Suma Asegurada Maxima,costo medio de Pago.</br>
13-Seleccionar Boton continuar </br>
14-Pantalla resultado.</br>
15-Validar ticket </br>
16-Seleccionar boton descarga </br> 
17-Validar que se descargue el comprobante </br> 
18-Seleccionar boton continuar </br>
19-Validar que luego de seleccionar el boton continar redirecione a la consolidada </br>
20-Fin  """
)

class HB_T169(unittest.TestCase, stLogin, stInicio, stSolicitudSeguro):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T208(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudSeguro()
            self.seleccionar_btn_seccion_seguro(self.seccion_seguro)
            self.seleccionar_btn_contratar_tipo(self.seguro)
            self.solicitarSeguro(self.seguro, self.plan, self.medioPago, self.cuenta)        
            self.verificarPantallaConfirmacion()
#             self.seleccionarConfirmar()
#             self.validar_ticket()
#             self.seleccionar_boton_descargar()
#             self.validar_descarga_comprobante()
#             self.seleccionar_btn_continuar()
#             self.validar_pagina_posicion_consolidada()
            
            
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
