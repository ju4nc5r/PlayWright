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
@allure.story(u'Ingreso Externo del Numerario')
@allure.testcase(
    u"test_0071 - Ingreso Externo del Numerario - Dolares", u''
)
@allure.title(u'test_0071 - Ingreso Externo del Numerario - Dolares')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina Icaja.
    2-Realizar login.
    3-Ingresar usuario y password y hacer clic en Aceptar. 
    4-Hacer clic en la flecha de despliegue de las TX
    5-Hacer click en la opcion Operaciones de Caja.
    6-Hacer click  en el Boton "Ingreso/Egreso"  
    7-Visualizar en la pantalla la opcion Ingreso Externo del Numerario.
    8-Selecionar Moneda.
    9-Hacer clic y seleccionar  monedas "Dolares"
    10-Validar que la que sea la Sucursal de Origen (997)
    11-Validar que la Sucursal Destino sea (0046)
    12-Ingresar en numero control (0101)    
    13-Ingresar valor (100)  
    14-Hacer click en el Boton Aceptar.   
    15-Impresion ok 
    16-Validar mensaje Operacion Realizada con Exito  
    17-Hacer click  en el Boton Salir "Salir de la aplicacion" 
    """
)
class tstICaja_0071(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0071(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.desplazarSideBar()
            self.seleccionarIngresoEgreso()
            self.seleccionarSolapaIngreso()
            self.wait(5)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.validarSucursalOrigen(self.sucuorigen)
            self.validarSucursalDestino(self.sucudestino)          
            self.ingresarNumeroControl(self.nroControl)        
            self.ingresarValor(self.valor)
            self.seleccionarAceptar()
            # self.verificarMsjeExitoImpreOK("Impresion OK")
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucuorigen = self.usuario.get(SUCURSAL)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        #self.mensaje = "La operacion finalizo correctamente"


if __name__ == "__main__":
    unittest.main()

