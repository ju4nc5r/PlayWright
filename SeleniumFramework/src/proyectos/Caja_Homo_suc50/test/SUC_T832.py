# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
            MONEDA1,MONEDA2,MONEDA3,IMPORTE1,IMPORTE2,IMPORTE3,NUMERODECONTROL1,NUMERODECONTROL2,NUMERODECONTROL3,\
            MSJ_ESPERADO, SUCURSAL_DEST,SUCURSAL_ORIG,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO            
import pytest


@allure.feature(u'Operaciones de Caja')
@allure.story(u'Ingreso / Egreso Externo')
@allure.testcase(u"ICaja - SUC-T832  Egreso Externo del Numerario - Pesos - Dolares - Euros - (Nivel Centralizador)") 
@allure.title(u'SUC-T832 - Egreso Externo del Numerario - Pesos - Dolares - Euros - (Nivel Centralizador)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10022</br>
5.-Hacer clic en la Transacción - Ingreso / Egreso Externo</br>
6.-Hacer clic en la pestaña"Egreso Externo del Numerario"</br>
7.-Seleccionar Moneda "Pesos"</br>
8.-Validar los recuadro Origen y Destino</br>
9.Ingresar Numero de control "0001"</br>
10.-Ingresar Valor "600.000,00"</br>
11.-Hacer clic en el Boton "ACEPTAR"</br>
12.-Visualizar el Mensaje - "La operación finalizo correctamente"</br>
13.-Hacer clic en Boton "ACEPTAR"</br>
14.-Visualizar la impresion del ticket</br>
15.-Hacer clic en la Transacción - Ingreso / Egreso Externo</br>
16.-Hacer clic en la pestaña"Egreso Externo del Numerario"</br>
17.-Seleccionar Moneda "Dolares"</br>
18.-Validar los recuadro Origen y Destino</br>
19.Ingresar Numero de control "0002"</br>
20.-Ingresar Valor "1500"</br>
21.-Hacer clic en el Boton "ACEPTAR"</br>
22.-Visualizar el Mensaje - "La operación finalizo correctamente"</br>
23.-Hacer clic en Boton "ACEPTAR"</br>
24.-Visualizar la impresion del ticket</br>
25.-Hacer clic en la Transacción - Ingreso / Egreso Externo</br>
26.-Hacer clic en la pestaña"Egreso Externo del Numerario"</br>
27.-Seleccionar Moneda "Euros"</br>
28.-Validar los recuadro Origen y Destino</br>
29.-Ingresar Numero de control "0003"</br>
30.-Ingresar Valor "1500"</br>
31.-Hacer clic en el Boton "ACEPTAR"</br>
32.-Visualizar el Mensaje - "La operación finalizo correctamente"</br>
33.-Hacer clic en Boton "ACEPTAR"</br>
34.-Visualizar la impresion del ticket</br>
35.-Hacer clic en el recuadro Hola, UIC10022 </br>
36.-Hacer clic en CERRAR SESIÓN </br> "  . 
    """
)
class SUC_T832 (unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio,stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T832(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            monedas = [self.moneda1,self.moneda2,self.moneda3]
            numerosDeControl = [self.nroControl1,self.nroControl2,self.nroControl3]
            importes = [self.valor1,self.valor2,self.valor3]
            for moneda,numeroDeControl,importe in zip(monedas,numerosDeControl, importes):
                self.seleccionarMnuIngresoEgresoExterno()
                self.seleccionarSolapaEgresoExternodelNumerario()
                self.mostrarTiposDeMoneda()
                self.seleccionarTipoDeMoneda(moneda)
                self.validarSucursalOrigenEgr(self.sucudestino)
                self.validarSucursalDestinoEgr(self.Sucursal_orig)          
                self.ingresarNumeroControlEgr(numeroDeControl)        
                self.ingresarValor(importe)
                self.seleccionarAceptarComun() 
                self.obtenerNroDeAutorizacion()
                self.validarBotonAutorizacionesSolicitadas()
                self.autorizarOperacion()
                self.seleccionarAceptarAutoriz()
                self.verificarMensajeExitoDeposito2("La operacion se realizo con exito.")
                self.seleccionarAceptar2()                
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
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl1 = self.usuario.get(NUMERODECONTROL1)
        self.nroControl2 = self.usuario.get(NUMERODECONTROL2)
        self.nroControl3 = self.usuario.get(NUMERODECONTROL3)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_ORIG)
        self.valor1 = self.usuario.get(IMPORTE1)
        self.valor2 = self.usuario.get(IMPORTE2)
        self.valor3 = self.usuario.get(IMPORTE3)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL) 
        
        
           
        

if __name__ == "__main__":
    unittest.main()
