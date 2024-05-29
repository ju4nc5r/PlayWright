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
              TIT_ESPERADO, MONEDA, USUARIO_CONTROL, SUCURSAL_DEST, CONDICION,\
              IMPORTE
@allure.feature(u'Administracion de cajas')
@allure.story(u'Consultas')
@allure.testcase(
    u"Adm.Caja - Caso de Prueba 0102", u''
)
@allure.title(u'test_0102 - Consultas - Listados Multiples - Euros')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina del modulo de Administracion.
    2-Colocar  el usuario y password y hacer clik en Aceptar.
    3-Visualizar los datos del usuario: 
    Legajo:  UIC10005
    Usuario:  UIC10005
    Terminal: IBA0005
    Sucursal: 0998
    4-Hacer clic en el menu Consultas.
    5-Hacer clic en el tem Listados Multiples.
    6-Seleccionar Sucursal - (0046 - Puerto Madero)
    7-Seleccionar Condicion - Menor que
    8-Seleccionar Operador - (UIC10009)
    9-Seleccionar Moneda - Euros
    10-Agregar valor 1000
    11-Hacer checklist en seleccionar Todo
    12-Hacer Clic en Imprimir (Guardar en PDF)
    12-Hacer Clic en descargar
    13-Hacer click  en el Boton Salir "Salir de la aplicacion"
    """
)
class tstAdmCaja_0102(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0102(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarListadosMultiples()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            self.seleccionarSucursal()
            self.seleccionarNumSucursal(self.sucursalDestino)
            self.wait(5)
            self.seleccionarCondicion()
            self.seleccionarTipoCondicion(self.condicion)
            self.wait(5)
            self.ingresarOperador(self.userControl)
            self.wait(5)
            self.seleccionarMoneda()
            self.seleccionarTipoMoneda(self.moneda)
            self.wait(5)
            self.ingresarImporte(self.importe)
            self.wait(5)
            self.seleccionarTodasLasOpc()
            self.wait(5)
            self.seleccionarDescargarMovimientos()
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
        self.sucursalDestino = self.usuario.get(SUCURSAL_DEST)
        self.condicion = self.usuario.get(CONDICION)
        self.userControl = self.usuario.get(USUARIO_CONTROL)
        self.moneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE)
if __name__ == "__main__":
    unittest.main()
