# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from proyectos.Caja_Homo.st.stAdminInicio import stAdminInicio
from proyectos.Caja_Homo.st.stAdminConsulta import stAdminConsulta
from proyectos.Caja_Homo.st import inicioAdminCaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE,\
              TIT_ESPERADO, MONEDA, USUARIO_CONTROL

@allure.feature(u'Administracion de cajas')
@allure.story(u'Consultas - Administracion de cajas')
@allure.testcase(
    u"test_0092 - Consultas - Totales ingresos, egresos y líquido de caja - Euros", u''
)
@allure.title(u'test_0092 - Consultas - Euros')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina del modulo de Administracion.
    2-Colocar  el usuario y password y hacer clik en Aceptar.
    3-Visualizar los datos del usuario: 
    Legajo.
    Usuario.
    Terminal.
    Sucursal.         
    4-Ingresar Moneda
    5-Hacer click en buscar
    6-Visualizar en pantalla las  Consultas - Totales ingresos, egresos y líquido de caja   en este caso visualizar:  Ingresos de caja /  Egresos de caja / Liquido de caja
    7-Hacer click  en el Boton  Imprimir
    8-Hacer click  en el Boton Salir "Salir de la aplicacion"
    """
)

class tstAdmCaja_0092(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0092(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarTotalesIngresEgresos()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            # self.ingresarUserControl(self.userControl)
            self.seleccionarMoneda()
            self.seleccionarTipoMoneda(self.moneda)
            self.wait(5)
            self.seleccionarBuscarTotales()
            self.wait(5)
            self.visualizarIngresos()
            self.visualizarEgresos()
            self.visualizarLiquido()
            self.wait(5)
            self.seleccionarImprimirTotales()
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
        self.userControl = self.usuario.get(USUARIO_CONTROL)
        self.moneda = self.usuario.get(MONEDA)

if __name__ == "__main__":
    unittest.main()
