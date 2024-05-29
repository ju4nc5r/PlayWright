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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE


@allure.feature(u'ICaja')
@allure.story(u'Extracciones en Efectivo')
@allure.testcase(
    u"test_0062 - test_0062 - Extracción en pesos de cuenta en dólares", u''
)
@allure.title(u'test_0062 - Extracción en pesos de cuenta en dólares')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina Icaja.
    2-Realizar login
    3-Ingresar usuario y password y hacer clic en Aceptar.
    4-Hacer clic  en el Boton "Identificar Cliente"
    5-Visualizar en pantalla el cuadro identificar cliente. 
    6-Seleccionar Tipo de Documento "DNI"
    7-Ingresar numero de Documento
    8-Hacer clic  en el Boton "Identificar"
    9-Visualizar en pantalla los datos del cliente y firma asociada.
    10-Hacer clic  en el Boton "Cerrar"
    11-Hacer clic en la flecha de despliegue de las TX
    12-Hacer clic en la opcion Extracciones
    13-Hacer clic en la opcion Extracciones  en Efectivo
    14-Hacer clic en la opcion Cuenta Cliente
    15-Seleccionar  cuenta  Dolares
    16-Hacer clic en seleccionar Moneda a extraer
    17-Seleccionar Moneda Pesos
    18-Ingresar importe 40  pesos
    19--Hacer clic en Siguiente
    20- Verificar los datos de la compra-venta de moneda extranjera
    21-Marcar el check si coincide la firma
    22- Visualizar y validar los datos del cliente e importe a Extraer
    23-Confirmar
    24-Visualizar impresion
    """
)
class tstICaja_0062(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0062(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.identificarCliente()
            self.minimizarFirma()
            self.desplazarSideBar()
            self.seleccionarExtracciones()
            self.wait(10)
            self.seleccionarCuentaExtraccion(self.cuenta)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarImporte(self.importe)
            self.seleccionarSiguiente()
            self.seleccionarSiguiente2()
            self.seleccionarConfirmarFirma()
            self.wait(5)
            self.seleccionarSiguiente3()
            self.seleccionarConfirmar()
            self.wait(10)
            # self.verificarMsjeExitoImpreOK("Impresion OK")
            self.verificarMensajeExitoExtracciones(self.mensaje)
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
        self.cuenta = self.usuario.get(CUENTA)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE)
        # self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
