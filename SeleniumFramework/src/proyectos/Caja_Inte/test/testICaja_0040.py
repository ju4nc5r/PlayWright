# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from proyectos.Caja_Homo.st.stLogin import stLogin
from proyectos.Caja_Homo.st.stICajaInicio import stICajaInicio
from proyectos.Caja_Homo.st.stICaja import stICaja
from proyectos.Caja_Homo.st import inicioICaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,\
             CLAVE, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, TIPO_DOC_IDENTIF, NOMBRE, \
             APELLIDO, MONEDA, IMPORTE, MSJ_ESPERADO, OPERACION
from proyectos.Caja_Homo.st.stICajaTickets import stICajaTickets
                
               
@allure.feature(u'ICaja')
@allure.story(u'Compraventa de Moneda Extranjera')
@allure.testcase(
    u"ICaja - Caso 0040 - Compra Moneda Extranjera - Dolares", u''
)
@allure.title(u'test_0040 - Compra Moneda Extranjera - Dolares')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina ICaja
    2-Ingresar usuario, terminal y password 
    3-Hacer clik en Aceptar   
    4-Hacer click  en el Boton "Identificar Cliente" 
    5-Visualizar en pantalla el cuadro identificar cliente 
    6-Seleccionar Tipo de Documento "DNI" 
    7-Ingresar numero de Documento 
    8-Hacer click  en el Boton "Identificar" 
    9-Visualizar en pantalla los datos del cliente y firma asociada  
    10-Hacer click  en el Boton "Cerrar" 
    11-Hacer click en la flecha de despliegue de TX 
    12-Hacer click en la opcion Moneda Extranjera 
    13-Hacer click en la opcion Compra/Venta Moneda Extranjera 
    14-Visualizar en pantalla el cuadro Tx Compra de Moneda Extranjera 
    15-Seleccionar el campo Monedas (Dolares)
    16-Seleccionar importe a comprar 
    17-Ingresar Importe 5 USD 
    18-Seleccionar Tipo de Documento (CUIL) 
    19-Ingresasr numero de Documento 
    20-Seleccionar botón Siguiente 
    21-Visualizar el detalle  de los datos de la operacións y datos del cliente: 
       Importe a comprar - Cotizacion Comprador - Importe en Pesos de la compra 
       CUIL Numero CUIL 
    22-Hacer click en botón Finalizar 
    23-Visuaizar el mensaje "La operación finalizó correctamente"  

    """
)
class tstICaja_0040(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0040(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
#             self.validarUsuario(self.user)
#             self.validarTerminal(self.terminal)
#             self.validarSucursal(self.sucursal)
            self.identificarCliente()
            self.minimizarFirma()
            self.desplazarSideBar()
            self.compraventaME(self.tipoOpME, self.tipoMoneda, pagTkt=self.paginasTicket)          
#             self.seleccionarSalirApp()
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
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.tipoDocMoneda = self.usuario.get(TIPO_DOC_IDENTIF)
        self.cuil = "20100767725"  # self.usuario.get(CUIL)
        self.nombreUser = self.usuario.get(NOMBRE)
        self.apellidoUser = self.usuario.get(APELLIDO)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.tipoOpME = self.usuario.get(OPERACION)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.paginasTicket = 1

if __name__ == "__main__":
    unittest.main()
