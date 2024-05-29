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
              MONEDA, IMPORTE, MSJ_ESPERADO, CUENTA_ACRED, IMPORTE_DEPOSITAR,\
              IMPORTE_INGRESADO
             

@allure.feature(u'ICaja')
@allure.story(u'Deposito Efectivo')
@allure.testcase(
    u"Test_081 - Deposito Efectivo", u''
)
@allure.title(u'Test_081 - Deposito Efectivo - Dolares en cuenta en pesos')
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
    12-Hacer clic en la opcion Deposito
    13-Hacer clic en la opcion Deposito  en Efectivo
    14-Hacer clic en la opcion Cuentas Cliente
    15-Seleccionar  cuenta CC
    16-Hacer clic en seleccionar Moneda operacion
    17-Seleccionar Moneda dolares
    18-Ingresar importe 15
    19-Hacer clic en  Continuar
    20- Verificar los datos del Depósito efectivo cliente
    21-Hacer clic en  Confirmar
    22-Visualiza Operacion Realizada Con Exito     
    """
)
class tstICaja_0081(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0081(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.validarUsuario(self.user)
            self.wait(5)
            self.identificarCliente()
            self.wait(5)
            self.minimizarFirma()
            self.desplazarSideBar()
            self.seleccionarDepositoEfectivo()
            self.wait(20)
            self.seleccionarCuentaDeposito(self.cuenta)
            self.mostrarTiposDeMonedaDeposito()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarImporteDeposito(self.valor)
            self.seleccionarContinuar()
            self.wait(5)
            self.validarCuentaDeposito(self.cuentaAcred)
            self.validarImporteADepositar(self.importeDepositar)
            self.validarImporteIngresado(self.importeIngresado)
            self.wait(5)
            self.seleccionarConfirmar()           
            # self.verificarMsjeExitoImpreOK("Impresion OK")
#             self.wait(20)
            self.CerrarDialogoImpresion()           
            self.verificarMensajeExitoDepositos(self.mensaje)
            self.visualizarTicket()
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
        self.nombreUser = self.usuario.get(NOMBRE)
        self.apellidoUser = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.valor = self.usuario.get(IMPORTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.SucuOrig = self.usuario.get(SUCURSAL)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.cuentaAcred = self.usuario.get(CUENTA_ACRED)
        self.importeDepositar = self.usuario.get(IMPORTE_DEPOSITAR)
        self.importeIngresado = self.usuario.get(IMPORTE_INGRESADO)
        
        

if __name__ == "__main__":
    unittest.main()
