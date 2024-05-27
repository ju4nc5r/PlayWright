# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from proyectos.Caja_Homo.st.stAdminInicio import stAdminInicio
from proyectos.Caja_Homo.st.stAdminTerminales import stAdminTerminales
from proyectos.Caja_Homo.st import inicioAdminCaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE, TIT_ESPERADO

@allure.feature(u'Administracion de cajas')
@allure.story(u'Terminales')
@allure.testcase(
    u"Adm.Caja - Caso de Prueba 0021", u''
)
@allure.title(u'test_0021 - Terminales')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina Administracion de cajas 
    2-Colocar  el usuario y password y hacer clik en Aceptar.
    3-Visualizar los datos del usuario: 
    Legajo.
    Usuario.
    Terminal
    Sucursal.
    4-Verificar que no tenga acceso a la pestaña Sucursales, dicha pestaña debera estar inhabilitada 
    """
)
class tstAdmCaja_0021(unittest.TestCase, stAdminTerminales, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0021(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.validarBtnMnuTerminalesDisabled()
            self.wait(5)
            self.seleccionarSalirApp()
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def tearDown(self):
        fin(self)

    def getDatos(self):
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.legajo = self.usuario.get(LEGAJO)
        self.terminal = self.usuario.get(TERMINAL)
        self.sucursal = self.usuario.get(SUCURSAL)
        self.tituloEsperado = self.usuario.get(TIT_ESPERADO)

if __name__ == "__main__":
    unittest.main()
