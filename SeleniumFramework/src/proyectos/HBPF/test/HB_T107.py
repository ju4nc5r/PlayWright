# -*- coding: utf-8 -*-
import unittest
import allure
import random
import traceback
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stCambioClave import stCambioClave
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.utils.excel_file import usuarios
from SeleniumFramework.src.utils.settings import (
    hb_user_excel, hb_user_sheet, hb_user_sheet_2, hb_old_excel, hb_old_sheet
)
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE


@allure.feature(u'Cambio de clave')
@allure.story(u'Realizar cambio de clave')
@allure.testcase(u"HB-T107 -0033- Cambio de clave actual")
@allure.title(u"HB-T107 -0033- Cambio de clave clave actual")
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T107")
@allure.description(
    u"""Realizar cambio de clave </br>
    Condición de prueba: Usuario ingresa clave actual correcta y
    clave nueva y repetición correctas </br>
    pasos: </br>
    1-Hacer click en la rueda de configuración </br>
    2-Hacer click en el cambio de clave </br>
    3-Ingresar clave actual correcta y clave nueva y repetición correctas</br>
    4-Validar ticket</br>
    5-Presionar botón <b>confirmar</b></br>
    5-Validar el ticket</br>
    6-Cerrar sesion</br>
    """
)
class HB_T107 (unittest.TestCase, stLogin, stCambioClave):
    def setUp(self):
        inicio_test(self)
        self.exc_usuarios = usuarios(hb_user_excel, hb_user_sheet)

    def test_CDPF_T146(self):
        try:
            self.usuario = self.exc_usuarios.obtener_datos_usuarios(
                self._testMethodName
            )
            self.getDatos()
            self.infoClave = "La nueva clave es: " + self.claveRandom
            self.log.info(self.infoClave)
            self.capture_image(self.infoClave)
            self.login()
            if self.cambiarClave():
                self.guardarClave()
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def getDatos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.claveRandom = "Aa" + str(random.randint(1111111111, 9999999999))
        self.claveNueva = self.claveRandom

    def guardarClave(self):
        self.usuario.update({CLAVE: self.claveNueva})
#         self.exc_usuarios.actualizar_usuario(self.user, self.usuario)
        excel_nuevo =  usuarios(hb_user_excel, hb_user_sheet_2) 
        excel_nuevo.write_cell_by_cell('B23', self.claveNueva)
        excel_viejo = usuarios(hb_old_excel, hb_old_sheet)
        excel_viejo.write_cell_by_cell('C29', self.claveNueva)

    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()
