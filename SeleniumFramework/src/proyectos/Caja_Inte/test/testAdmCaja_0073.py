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
    u"Adm.Caja - Caso de Prueba 0073", u''
)
@allure.title(u'test_0073 - Consulta de totales de saldos de caja por Sucursal - Imprimir')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina Administracion de cajas  
    2-Colocar  el usuario y password y hacer clik en Aceptar.  
    3-Hacer click en consultas - saldos de caja  
    4-Visualizar en pantalla los Totales de saldos por sucursal           
    5-Hacer click en botón Imprimir
    6-Hacer click  en el Boton Salir "Salir de la aplicacion" 
    """
)
class tstAdmCaja_0073(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0073(self): 
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarSaldosCajas()
            self.validarTitulo2Consulta(self.tituloEsperado)
            self.validarTablaSaldosCajasSuc()
            self.ImprimirSaldosPorSucursal()
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
