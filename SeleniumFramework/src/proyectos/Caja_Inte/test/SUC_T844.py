# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE,\
              MSJ_ESPERADO,CUENTA1,CUENTA2,CUENTA3,MONEDA1,MONEDA2,MONEDA3,\
              IMPORTE1,IMPORTE2,IMPORTE3,CUENTA_VALIDAR1,CUENTA_VALIDAR2,CUENTA_VALIDAR3,\
              IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,IMPORTE_VALIDAR_3
             

@allure.feature(u'Depósitos')
@allure.story(u'Depósito de Cliente')
@allure.testcase(u"ICaja - SUC-T844 - Deposito de Cliente - Moneda Euros")
@allure.title(u'SUC-T844 - Deposito en Efectivo - Moneda Euros')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Deposito en Efectivo</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "25227274"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón "SIN CLAVE"</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Cliente"</br>
14.-Seleccionar cuenta "CA EUR"</br>
15.-Hacer clic en seleccionar Moneda a extraer "Euros"</br>
16.-Ingresar importe "50"</br>
17.-Hacer clic en "SIGUIENTE"</br>
18.-Visualizar los datos de la tx</br>
19.-Hacer clic en el botón "CONFIRMAR"</br>
20.-Visualizar el Mensaje - "La operación se realizo con éxito.</br> "
21.-Hacer el boton "ACEPTAR"</br>
22.-Visualizar la impresión del ticket</br>
23.-Hacer clic en el recuadro Hola, UIC10021</br>
24.-Hacer clic en CERRAR SESIÓN </br>
    """
)
class SUC_T844(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T844(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()     
            self.seleccionarDepositoCliente()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente()
            self.seleccionarCuentaDeposito(self.cuenta3)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.moneda3)
            self.ingresarImporte(self.importe3,self.moneda3)
            self.seleccionarSiguiente()
            parts = ["cuenta","importeADepositar"]
            datos = [self.cuentaValidar3,self.importeValidar3]
            for part,dato in zip (parts,datos):
                self.validarDatosDepositos(part,dato)
            self.seleccionarConfirmar() 
            self.verificarMensajeExitoDeposito2("La operacion se realizo con exito.")
            self.seleccionarAceptarComun()
            self.visualizarTicket2()
            self.cerrarSesion()
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta3 = self.usuario.get(CUENTA3)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.importe3 = self.usuario.get(IMPORTE3)
        self.importeValidar3 = self.usuario.get(IMPORTE_VALIDAR_3)
        self.cuentaValidar3 = self.usuario.get(CUENTA_VALIDAR3)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
     

       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
