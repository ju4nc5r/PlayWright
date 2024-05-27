# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
              TIPO_DE_OPERACION,IMPORTE_A_VALIDAR,OPERACION_A_VALIDAR,OPERACION1,OPERACION2,\
              MONEDA1,MONEDA2,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,OPERACION_VALIDAR1,OPERACION_VALIDAR2
import pytest



@allure.feature(u'Cobros')
@allure.story(u'Cobros Varios')
@allure.testcase(u"ICaja - SUC-T851-  Cobros Varios")
@allure.title(u'SUC-T851 - Cobros Varios - Moneda Dolares')
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/35775')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""  
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - "Cobros Varios"</br>
6.-Hacer clic en el "Tipo de Operación"</br>
7.-Seleccionar el ítem "48 Deposito Cajeros Banelco"</br>
8.-Hacer clic en seleccionar Moneda "Dolares"</br>
9.-Ingresar importe "10"</br>
10.-Hacer clic en "SIGUIENTE"</br>
11.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
12.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
13.-Hacer clic en el Botón "VALIDAR"</br>
14.-Visualizar el mensaje "Timbrado de cobro con éxito"</br>
15.-Hacer clic en Botón "FINALIZAR"</br>
16.-Visualizar la impresión del ticket</br>
17.-Hacer clic en el recuadro Hola, UIC10021</br>
18.-Hacer clic en CERRAR SESIÓN </br>  
"""
) 
class SUC_T851(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T851(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarCobrosVarios()
            self.seleccionarRecuadroTpdeOperacion()
            self.wait(3)
            self.seleccionarTipoDeOperacion(self.Operacion2)
            self.seleccionarComboBox()          
            self.seleccionarMoneda(self.moneda2)        
            self.ingresarImporte2(self.importe2)
            self.seleccionarBtnSiguiente() 
            self.validarTipoDeOperacion(self.operacionAValidar2)
            self.validarMonedaOpn(self.moneda2)
            self.validarImporteOpn(self.importeValidar2)  
            self.seleccionarConfirmar() 
            self.seleccionarValidar()
            self.visualizarMensajeExitoOpn("Timbrado finalizado con exito")
            self.visualizarTicket2()
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
        self.sucudestino = self.usuario.get(SUCURSAL_ORIG)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.Operacion1 = self.usuario.get(OPERACION1)
        self.Operacion2 = self.usuario.get(OPERACION2)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importeValidar2 = self.usuario.get(IMPORTE_VALIDAR_2)   
        self.operacionAValidar1 = self.usuario.get(OPERACION_VALIDAR1)
        self.operacionAValidar2 = self.usuario.get(OPERACION_VALIDAR2)
        
           
        

if __name__ == "__main__":
    unittest.main()
