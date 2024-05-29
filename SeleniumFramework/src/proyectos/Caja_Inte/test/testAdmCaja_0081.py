# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from proyectos.Caja_Homo.st.stAdminInicio import stAdminInicio
from proyectos.Caja_Homo.st.stAdminConsulta import stAdminConsulta
from proyectos.Caja_Homo.st import inicioAdminCaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE, TIT_ESPERADO

@allure.feature(u'Administracion de cajas')
@allure.story(u'Consultas - Administracion de cajas')
@allure.testcase(
    u"test_0081 - Consultas de Movimientos de caja - Imprimir", u''
)
@allure.title(u'test_0081 - consulta de Movimientos de caja - Imprimir')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina del modulo de Administracion.
    2-Colocar  el usuario y password y hacer clik en Aceptar.
    3-Visualizar los datos del usuario: 
    Legajo.Usuario.Terminal.Sucursal.          
    4-Hacer click en buscar
    5-Visualizar en pantalla los movimientos
    6-Hacer click en imprimir
    7-Hacer click  en el Boton Salir "Salir de la aplicacion"    
    """
)
class tstAdmCaja_0081(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0081(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarMovimientosdecaja()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            self.seleccionarBuscarMovimientos()
            self.wait(5)
            self.validarTablaMovimientosdecaja()
            self.wait(5)
            self.seleccionarImprimirMovimientos()
            # self.wait(5)
            # self.seleccionarSalirApp()
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
