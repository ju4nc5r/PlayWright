# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from proyectos.Caja_Homo.st.stLogin import stLogin
from proyectos.Caja_Homo.st.stICajaInicio import stICajaInicio
from proyectos.Caja_Homo.st.stICaja import stICaja
from proyectos.Caja_Homo.st.stICajaTickets import stICajaTickets
from proyectos.Caja_Homo.st import inicioICaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST
             

@allure.feature(u'ICaja')
@allure.story(u'Egreso  Externo del Numerario')
@allure.testcase(
    u"Test_077 - Egreso Externo del Numerario", u''
)
@allure.title(u'Test_077 - Egreso Externo del Numerario - Reales')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina Icaja
    2-Realizar login
    3-Ingresar  usuario y password y hacer clik en Aceptar.
    4-Hacer clic en la flecha de despliegue de las TX
    5-Hacer click en la opcion Operaciones de Caja  
    6-Hacer click  en el Boton "Ingreso/Egreso"
    7-Visualizar en la pantalla la opcion Ingreso Externo del Numerario
    8-Selecionar Moneda
    9-Hacer clic y seleccionar  monedas Reales
    10-Validar que la sucursal de origen sea la sucursal 046
    11-Validar que la sucursal de destino sea la sucursal 997
    12-Ingresar en numero control (1234)
    13-Ingresar valor (100)
    14-Hacer click  en el Boton siguiente
    15-Impresion ok  
    """
)
class tstICaja_0077(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0077(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.desplazarSideBar()
            self.seleccionarIngresoEgreso()
            self.seleccionarSolapaEgreso()
            self.mostrarTiposDeMonedaEgreso()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.validarSucursalOrigenE(self.SucuOrig)
            self.validarSucursalDestinoE(self.SucuDest)
            self.ingresarNroControlE(self.nroControl)
            self.ingresarValorE(self.valor)
            self.seleccionarAceptar()
#             self.verificarMsjeExitoImpreOK("Impresion OK")
            self.verificarMensajeExitoEgresoIngreso(self.mensaje)
            self.visualizarTicket()
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
        self.nombreUser = self.usuario.get(NOMBRE)
        self.apellidoUser = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.valor = self.usuario.get(IMPORTE)
        self.SucuDest = self.usuario.get(SUCURSAL_DEST)
        self.SucuOrig = self.usuario.get(SUCURSAL)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        
        

if __name__ == "__main__":
    unittest.main()
