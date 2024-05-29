# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from proyectos.CRM.st.stBusquedaClientes import  stBusquedaClientes
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE,\
              MONEDA, IMPORTE, MSJ_ESPERADO, SUCURSAL_DEST,SUCURSAL_ORIG,\
              CUENTA_ACRED,CUENTA1,CUENTA2,CUENTA_VALIDAR1,CUENTA_VALIDAR2,\
              NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,IMPORTE_VALIDAR_1,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
import pytest



@allure.feature(u'Depósitos')
@allure.story(u'Deposito Cheques Propios')
@allure.testcase(u"ICaja - SUC-T791 - Deposito Cheques Propios")
@allure.title(u'SUC-T791 - Deposito Cheques Propios')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br> 
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br> 
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br> 
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br> 
6.-Hacer clic en la Transacción - "Depósito Cheques Propios"</br> 
7.-Visualizar el recuadro identificar al cliente, hacer clic en "SI"</br> 
8.-Ingresar los datos del cliente</br> 
9.-Seleccionar Tipo de Documento "DNI"</br> 
10.-Ingresar Numero de Documento "25227274"</br> 
11.-Hacer clic en el Botón "IDENTIFICAR"</br> 
12.-Hacer clic en el Botón SIN CLAVE</br> 
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br> 
14.-Hacer clic en el recuadro "Cuentas Cliente"</br> 
15.-Seleccionar cuenta "CC$ 0444583-100/3"</br> 
16.-Hacer clic en "SIGUIENTE"</br> 
17.-Ingresar los datos del cheque desde la aplicación "CRM"</br> 
18.-Hacer clic en cualquier espacio de la pantalla</br> 
19.-Visualizar en la parte inferior de la pantalla los datos del cheque depositado</br> 
20.-Hacer clic en el Botón "FIN DE CARGA"</br> 
21.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br> 
22.-Visualizar la impresión del ticket</br> 
23.-Visualizar el mensaje "Operación realizada con éxito"</br> 
24.-Hacer clic en Botón "VALIDAR CHEQUE"</br> 
25.-Visualizar el mensaje "Cheque timbrado con éxito" y hacer clic en el Botón "FINALIZAR"</br> 
26.-Visualizar la impresión del ticket</br> 
27.-Hacer clic en Botón "FINALIZAR"</br> 
28.-Hacer clic en la Transacción - "Depósito Cheques Propios"</br> 
29.-Visualizar el recuadro identificar al cliente, hacer clic en "NO"</br> 
30.-Ingresar la cuenta de Terceros: "03200151003"</br> 
31.-Ingresar los datos del cheque desde la aplicación "CRM"</br> 
32.-Hacer clic en cualquier espacio de la pantalla</br> 
33.-Visualizar en la parte inferior de la pantalla los datos del cheque depositado</br> 
34.-Hacer clic en el Botón "FIN DE CARGA"</br> 
35.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br> 
36.-Visualizar la impresión del ticket</br> 
37.-Visualizar el mensaje "Operación realizada con éxito"</br> 
38.-Hacer clic en Botón "VALIDAR CHEQUE"</br> 
39.-Visualizar el mensaje "Cheque timbrado con éxito" y hacer clic en el Botón "FINALIZAR"</br> 
40.-Visualizar la impresión del ticket</br> 
41.-Hacer clic en Botón "FINALIZAR"</br> 
42.-Hacer clic en el recuadro Hola, UIC10021</br> 
43.-Hacer clic en CERRAR SESIÓN</br>     
"""
)

class SUC_T791(unittest.TestCase, stICajaInicio,stICaja,stBusquedaClientes,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
    
    def test_SUC_T791(self):
        try:      
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarDepositoDeChequesPropios()
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente()
            self.seleccionarRecuadroCuentasCliente()
            self.seleccionarCuentaDeposito(self.cuenta)
            self.seleccionarSiguiente()
            self.ingresarImporte3(self.valor,self.tipoMoneda)
            self.ingresarDatosDeChequera()
            self.seleccionarFindeCarga()  
            self.validarDatosOperacionDepositos()
            self.seleccionarConfirmar()  
            self.seleccionar_validar_cheques_dps()
            self.visualizarMensajeExito()       
            self.verificarMensajeExitoExtracciones(self.mensaje)      
            self.verificar_numero_de_transaccion_cheques()
            self.wait(1) 
            self.seleccionarRevesoDeTrasaccion()
            self.ingresarNroTranssaccion(self.NumeroTrans)
            self.mostrarTiposDeMotivos()
            self.seleccionarMotivo("Error Carga Cajero")
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizarOperacionPg()
            self.seleccionarAceptarAutoriz()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")
            self.seleccionarDepositoDeChequesPropios()
            self.visualizarCuadroNecesitaIdentificarAlCliente2()
            self.ingresarCuenta(self.cuenta2)
            self.seleccionarSiguiente()
            self.ingresarImporte3(self.valor,self.tipoMoneda)
            self.ingresarDatosDeChequera()
            self.seleccionarFindeCarga()  
            self.validarDatosOperacionDepositos2()
            self.seleccionarConfirmar()  
            self.seleccionar_validar_cheques_dps()
            self.visualizarMensajeExito()       
            self.verificarMensajeExitoExtracciones(self.mensaje)  
            self.verificar_numero_de_transaccion_cheques()
            self.wait(1) 
            self.seleccionarRevesoDeTrasaccion()
            self.ingresarNroTranssaccion(self.NumeroTrans)
            self.mostrarTiposDeMotivos()
            self.seleccionarMotivo("Error Carga Cajero")
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizarOperacionPg()
            self.seleccionarAceptarAutoriz()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")       
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
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
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
