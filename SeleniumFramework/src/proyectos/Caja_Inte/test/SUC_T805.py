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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,IMPORTE1,IMPORTE2,\
              IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,OPERACION1,TITULO_ESPERADO,NUMERO_TAS,OPERACION_A_VALIDAR         
import pytest

@allure.feature(u'TAS')
@allure.story(u'TAS Liberaciones')
@allure.testcase(u"ICaja - SUC-T805 - TAS Liberaciones - Deposito de Efectivo Inteligente")
@allure.title(u'SUC-T805 - TAS Liberaciones - Deposito de Efectivo Inteligente')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción "TAS Liberaciones"</br>
7.-Validar Número de Sucursal "0050"</br>
8.-Hacer clic en Transacción</br>
9.-Seleccionar el ítem "Deposito Efectivo Inteligente"</br>
10.-Hacer clic en "Numero de TAS"</br>
11.-Ingresar numero de TAS "00052" y hacer enter</br>
12.-Validar moneda "Pesos"</br>
13.-Hacer clic en el Botón "REDEPOSITAR"</br>
14.-Ingresar importe Total A Liberar "1.500"</br>
15.-Ingresar importe Total A Liberar Reject "500"</br>
16.-Hacer clic en "SIGUIENTE"</br>
17.-Visualizar los datos de la Transaccion y hacer clic en el botón "CONFIRMAR"</br>
18.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
19.-Hacer clic en Botón "FINALIZAR"</br>
20.-Visualizar la impresión del ticket</br>
21.-Visualizar el Mensaje - Operación Realizada Con Éxito.</br>
22.-Hacer clic en el recuadro Hola, UIC10021</br>
23.-Hacer clic en CERRAR SESIÓN </br>   
"""
)
class SUC_T805(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T805(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarTasLiberaciones()
            self.mostrarTiposDeOperacion()
            self.seleccionarTipoOperacion(self.operacion)
            self.mostrarTiposDeMonedaAtm()
            self.seleccionarTipoDeMoneda("Pesos")
            self.wait(2)
            self.mostrar_seleccionar_nro_tas(self.numeroTas) 
            self.ingresarImporte5(self.importe2)
            self.ingresarNroTas(self.importe1)
            self.seleccionarSiguiente()
            self.validar_sucursal(self.sucursal)
            self.validar_transaccion(self.operacionValidar)
            self.validar_moneda(self.tipoMoneda)
            self.validar_importe_total(self.importeValidar2)
            self.validar_nro_tas(self.numeroTas)
            self.validar_importe_total_a_liberar(self.importeValidar1)        
            self.seleccionarConfirmar()
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
        self.sucursal = self.usuario.get(SUCURSAL)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.operacion = self.usuario.get(OPERACION1)
        self.operacionValidar = self.usuario.get(OPERACION_A_VALIDAR)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importeValidar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.msg_imprecion = self.usuario.get(TITULO_ESPERADO)
        self.numeroTas = self.usuario.get(NUMERO_TAS)

        #self.mensaje = "La operacion finalizo correctamente"   
        

if __name__ == "__main__":
    unittest.main()
