# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stLogin import stLogin
from proyectos.CRM.st.stBusquedaClientes import  stBusquedaClientes
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, SUCURSAL_DEST,SUCURSAL_ORIG,\
              CUENTA_ACRED, IMPORTE_A_VALIDAR,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
import pytest
@allure.feature(u'Pagos')
@allure.story(u'Pago de Cheque')
@allure.testcase(u"ICaja - SUC-T786 - Pago de Cheque ")
@allure.title(u'SUC-T786 - Pago de Cheque')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""  
1.-Ingresar a la pagina Icaja "https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login"</br>
2.-Realizar login e ingresar los datos del operador:</br>
Legajo: UIC10021 / Terminal: IA0500821 / Contraseña: Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021"</br>
5.-Visualizar los datos del operador UIC10021:</br>
Legajo: UIC10021 / Terminal: IA0500821 / Sucursal: 0050</br>
6.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
7.-Hacer clic en la Transaccion - "Pago Cheque"</br>
8.-Validar el recuadro Moneda "Pesos"</br>
9.-Ingresar importe "1000"</br>
10.-Ingresar los datos del cheque:</br>
11.-Banco: 259 / Suc:046 / CP:1030 / Numero:00824571 / Cuenta:04445831003</br>
12.-Hacer clic en el boton SIGUIENTE</br>
13.-Visualizar el numero de cuenta y tildar la firma</br>
14.-Hacer clic en el boton SIGUIENTE</br>
15.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
16.-Visualizar la impresion del ticket</br>
17.-Visualizar el mensaje "Operación realizada con éxito"</br>
18.-Hacer clic en boton "VALIDAR CHEQUE"</br>
19.-Visualizar el mensaje "Cheque timbrado con exito" y hacer clic en el boton "FINALIZAR"</br>
20.-Visualizar la impresion del ticket</br>
21.-Hacer clic en boton "FINALIZAR"</br>     
"""
    )
class SUC_T786(unittest.TestCase, stICajaInicio, stICaja,stBusquedaClientes,stAutorizInicio,stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T786(self):
        try:      
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarPagoCheques()
            self.ingresarImporte("10000",self.tipoMoneda)
            self.ingresarDatosDeChequera_2()               
            self.seleccionarSiguiente()
            self.wait(2)
            self.seleccionarCheckBoxFirma()
            self.seleccionarSiguiente2()            
            self.validarDatosOperacionPagos()        
            self.seleccionarConfirmar()   
            self.seleccionar_validar_cheques_dps()
            self.visualizarMensajeExito()       
            self.verificarMensajeExitoExtracciones(self.mensaje)  
            self.verificar_numero_de_transaccion_cheques_2()
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
        self.terminal = self.usuario.get(TERMINAL)
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_ORIG)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL)
        self.cuenta  = self.usuario.get(CUENTA)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento = self.usuario.get(NRO_DOC_CLIENTE)
        self.nombreCliente  = self.usuario.get(NOMBRE)
        self.apellidoCliente  = self.usuario.get(APELLIDO)
        self.cuentavalidar = self.usuario.get(CUENTA_ACRED)
        self.importe = self.usuario.get(IMPORTE_A_VALIDAR)

 
if __name__ == "__main__":
    unittest.main()
