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
@allure.story(u'Tus cosas - Hogar')
@allure.testcase(u'HB-T167 -0270- Solicitud de seguro Hogar')
@allure.title(u'HB-T167 -0270- Solicitud de seguro Hogar')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T167")
@allure.description(
    u"""
1-Desde las posición consolidada ir al menú Productos </br>
2-Selecionar Seguros Solicitud </br>  
3-Dirigirse a la seccion Tus cosas </br>
4-Seleccionar boton contratar Hogar </br>
5-Seleccionar un Plan A </br>
6-Seleccionar boton continuar </br> 
7-Seleccionar en el combo medio de pago Caja de ahorro" </br> 
8-Seleccionar en el combo cuenta CA$ </br>
9-Seleccionar Domicilio igual al titular </br>
10-Seleccionar Acepto los Terminos y condiciones. </br>
11-Seleccionar continar </br> 
12-Pantalla confirmacion </br>
13-Validar los campos Nombre, Linea de producto,Producto, </br>
   Plan,Suma Asegurada Maxima,costo medio de Pago.</br>
14-Seleccionar Boton continuar </br>
15-Pantalla resultado.</br>
16-Validar ticket </br>
17-Seleccionar boton descarga </br> 
18-Validar que se descargue el comprobante </br>
19-Seleccionar boton continuar </br>
20-Validar que luego de seleccionar el boton continar redirecione a la consolidada </br>
21-Fin """
)

class HB_T167(unittest.TestCase, stLogin, stInicio, stSolicitudSeguro):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T206(self):
        try:
            self.usuario = get_user_hb(self._testMethodName)
            self.get_datos()
            self.login()
            self.seleccionarSolicitudSeguro()
            self.seleccionar_btn_seccion_seguro(self.seccion_seguro)
            self.seleccionar_btn_contratar_tipo(self.seguro)
            self.seleccionarPlan(self.plan)
            self.seleccionarContinuar()
            self.seleccionarMedioDePago(self.medioPago)
            self.seleccionarCuenta(self.cuenta)
            self.seleccionarIgualTitualar()
            self.seleccionarTerminosYCondiciones() 
            self.seleccionarContinuar()
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
