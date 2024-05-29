# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from datetime import date
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
    u"Adm.Caja - Caso de Prueba 0110", u''
)
@allure.title(u'test_0110 - Consultas - Tickets')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina del modulo de Administracion.
    2-Colocar  el usuario y password y hacer clik en Aceptar.
    3-Visualizar los datos del usuario: 
    Legajo:  UIC10009
    Usuario: UIC10009
    Terminal: IBA0009
    Sucursal: 0046
    4-Visualizar y hacer clic en la opcion Consultas.
    5-Visualizar y hacer clic en el Item Listado de Tickets.
    6-Escribir en el Item operador (UIC10009)
    7-Validar y confirmar la fecha del dia
    8-Hacer clic en Sucursal y seleccionar (0046 - Puerto Madero)
    9-Hacer clic en Buscar 
    10-Visualizar en pantalla la informacion  los Movimientos y/o TX realizadas 
    """
)
class tstAdmCaja_0110(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0110(self):
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
            self.seleccionarListadosTickets()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            self.validarFechaDia(self.hoyFecha)
            self.wait(5)
            self.seleccionarBuscarTotales()
            self.wait(5)
            self.visualizarInformacion()
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
        hoy = date.today()
        self.dia = hoy.strftime("%d")
        self.mes = hoy.strftime("%m")
        self.year = hoy.strftime("%Y")
        self.hoyFecha = self.dia+"/"+self.mes+"/"+self.year
        

if __name__ == "__main__":
    unittest.main()
