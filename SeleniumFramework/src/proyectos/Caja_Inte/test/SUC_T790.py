# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Inte.st.stLogin import stLogin
from proyectos.CRM.st.stBusquedaClientes import  stBusquedaClientes
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, SUCURSAL_DEST,SUCURSAL_ORIG,\
              CUENTA_ACRED, IMPORTE_A_VALIDAR,CUENTA1,CUENTA2,CUENTA_VALIDAR1,CUENTA_VALIDAR2,NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,IMPORTE_VALIDAR_1
import pytest

@allure.feature(u'Depósitos')
@allure.story(u'Depósito Cheques Otros Bancos')
@allure.testcase(u"ICaja - SUC-T790- Depósito Cheques Otros Bancos")
@allure.title(u'SUC-T790 - Depósito Cheques Otros Bancos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
​1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Depósito Cheques Otros Bancos"</br>
7.-Visualizar el recuadro identidicar al cliente, hacer clic en "SI"</br>
8.-Ingresar los datos del cliente</br>
9.-Seleccionar Tipo de Documento "DNI"</br>
10.-Ingresar Numero de Documento "25227274"</br>
11.-Hacer clic en el Botón "IDENTIFICAR"</br>
12.-Hacer clic en el Boton SIN CLAVE</br>
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
14.-Hacer clic en el recuadro "Cuentas Cliente"</br>
15.-Seleccionar cuenta "CC$ 0444583-100/3"</br>
16.-Hacer clic en "SIGUIENTE"</br>
17.-Ingresar los datos del cheque:</br>
18.-Importe:1000 / Banco:059 / Suc:047 / CP:1030 / Numero:12345678 / Cuenta:98765432101</br>
19.-Hacer clic en cualquier espacio de la pantalla</br>
20.-Visualizar en la parte inferior de la pantalla los datos del cheque depositado</br>
21.-Hacer clic en el Botón "FIN DE CARGA"</br>
22.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
23.-Visualizar la impresión del ticket</br>
24.-Visualizar el mensaje "Operación realizada con éxito"</br>
25.-Hacer clic en Botón "VALIDAR CHEQUE"</br>
26.-Visualizar el mensaje "Cheque timbrado con éxito" y hacer clic en el Botón "FINALIZAR"</br>
27.-Visualizar la impresión del ticket</br>
28.-Hacer clic en Botón "FINALIZAR"</br>
29.-Hacer clic en la Transacción - "Depósito Cheques Otros Bancos"</br>
30.-Visualizar el recuadro identificar al cliente, hacer clic en "NO"</br>
31.-Ingresar la cuenta de Terceros: "03200151003"</br>
32.-Hacer clic en "SIGUIENTE"</br>
33.-Ingresar los datos del cheque:</br>
34.-Importe:1000 / Banco:059 / Suc:047 / CP:1030 / Numero:12345678 / Cuenta:98765432101</br>
35.-Hacer clic en cualquier espacio de la pantalla</br>
36.-Visualizar en la parte inferior de la pantalla los datos del cheque depositado</br>
37.-Hacer clic en el Botón "FIN DE CARGA"</br>
38.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
39.-Visualizar la impresión del ticket</br>
40.-Visualizar el mensaje "Operación realizada con éxito"</br>
41.-Hacer clic en Botón "VALIDAR CHEQUE"</br>
42.-Visualizar el mensaje "Cheque timbrado con éxito" y hacer clic en el Botón "FINALIZAR"</br>
43.-Visualizar la impresión del ticket</br>
44.-Hacer clic en Botón "FINALIZAR"</br>
45.-Hacer clic en el recuadro Hola, UIC10021</br>
46.-Hacer clic en CERRAR SESIÓN </br>
"""
)

class SUC_T790(unittest.TestCase, stICajaInicio,stICaja,stBusquedaClientes,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
    
    def test_SUC_T790(self):
        try:      
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarDepositoDeCheques()
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente()
            self.seleccionarCuentaDeposito(self.cuenta)
            self.seleccionarSiguiente()
            self.ingresarImporte3(self.valor,self.tipoMoneda)
            self.ingresarDatosDeChequeraOtrosBancos()
            self.seleccionarFindeCarga()
            self.validarDatosOperacionDepositos()               
            self.seleccionarConfirmar()  
            self.seleccionar_validar_cheques_dps()
            self.visualizarMensajeExito()       
            self.verificarMensajeExitoExtracciones(self.mensaje)           
            self.seleccionarDepositoDeCheques()
            self.visualizarCuadroNecesitaIdentificarAlCliente2()
            self.ingresarCuenta(self.cuenta2)
            self.seleccionarSiguiente()
            self.ingresarImporte3(self.valor,self.tipoMoneda)
            self.ingresarDatosDeChequeraOtrosBancos()
            self.seleccionarFindeCarga()  
            self.validarDatosOperacionDepositos2()
            self.seleccionarConfirmar()  
            self.seleccionar_validar_cheques_dps()
            self.visualizarMensajeExito()       
            self.verificarMensajeExitoExtracciones(self.mensaje)  
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_ORIG)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL)
        self.cuenta  = self.usuario.get(CUENTA1)
        self.cuenta2  = self.usuario.get(CUENTA2)
        self.cuentaValidar1  = self.usuario.get(CUENTA_VALIDAR1)
        self.cuentaValidar2  = self.usuario.get(CUENTA_VALIDAR2)
        self.nombreApellido = self.usuario.get(NOMBRE_APELLIDO1)
        self.nombreApellido2 = self.usuario.get(NOMBRE_APELLIDO2)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento = self.usuario.get(NRO_DOC_CLIENTE)
        self.nombreCliente  = self.usuario.get(NOMBRE)
        self.apellidoCliente  = self.usuario.get(APELLIDO)
        self.cuentavalidar = self.usuario.get(CUENTA_ACRED)
        self.importe = self.usuario.get(IMPORTE_VALIDAR_1)


 
if __name__ == "__main__":
    unittest.main()
