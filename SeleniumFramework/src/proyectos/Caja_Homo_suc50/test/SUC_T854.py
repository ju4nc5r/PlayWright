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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
              IMPORTE_A_VALIDAR,OPERACION_A_VALIDAR,OPERACION1,OPERACION2,OPERACION3,\
              OPERACION_VALIDAR1,OPERACION_VALIDAR2,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,\
              NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,NUMERO_TARJETA,NUMERO_SOCIO,MARCA_TARJETA,MARCA_TARJETA1,CUENTA1
import pytest


@allure.feature(u'Cobros de Tarjeta de Credito')
@allure.story(u'Cobros de Tarjeta de Credito')
@allure.testcase(u"ICaja - SUC-T854 -Cobros de Tarjeta de Credito - Pago Efectivo ")
@allure.title(u'SUC-T854 - Cobros de Tarjeta de Crédito')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - "Cobro de Tarjeta de Crédito"</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Hacer clic en la opción "SI"</br>
8.-Ingresar los datos del cliente</br>
9.-Seleccionar Tipo de Documento "DNI"</br>
10.-Ingresar Numero de Documento "27011435"</br>
11.-Hacer clic en el Botón "IDENTIFICAR"</br>
12.-Hacer clic en el Botón SIN CLAVE</br>
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
14.-Visualizar Tarjeta "Máster"</br>
15.-Forma de Pago "Efectivo"</br>
16.-Seleccionar Moneda "Pesos"</br>
17.-Hacer clic en el recuadro "Importe" e ingresar "100"</br>
18.-Hacer clic en el Botón "SIGUIENTE"</br>
19.-Hacer clic en el Botón "SIGUIENTE"</br>
20.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
21.-Visualizar la impresión del ticket</br>
22.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el Botón "FINALIZAR"</br>
23.-Visualizar la impresión del ticket</br>
24.-Hacer clic en Botón "FINALIZAR"</br>
25.-Hacer clic en el recuadro Hola, UIC10021</br>
26.-Hacer clic en CERRAR SESIÓN </br>
"""
)

class SUC_T854(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
              
    def test_SUC_T854(self):
        try: 
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarCobroDeTarjetaCredito()
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente()
            self.visualizarDatosTarjeta()
            self.wait(2)
            self.seleccionarComboBoxCobros(self.operacion1)  
            self.wait(1)
            self.mostrarTiposDeMonedaAtm()  
            self.wait(1)      
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.wait(1)
            self.ingresarImporte2(self.importe1)
            self.seleccionarSiguiente()
            self.seleccionarSiguiente() 
            self.validar_nro_tarjeta(self.numeroTarjeta) 
            self.validar_marca_tarjeta(self.marcaDeTarjeta1)
            self.validar_nombre(self.nombreYApellido1) 
            self.validar_operacion(self.operacion_validar1)
            self.validar_moneda(self.tipoMoneda)
            self.validar_importe(self.importe_validar1)                                       
            self.seleccionarConfirmar()  
            self.visualizarMensajeExito()        
            self.verificarMensajeExitoExtracciones(self.mensaje)  
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
        self.cuenta = self.usuario.get(CUENTA)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importe_validar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importe_validar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.operacion1= self.usuario.get(OPERACION1)
        self.operacion2= self.usuario.get(OPERACION2)  
        self.operacion3= self.usuario.get(OPERACION3)
        self.operacion_validar1= self.usuario.get(OPERACION_VALIDAR1)
        self.operacion_validar2= self.usuario.get(OPERACION_VALIDAR2)
        self.nombreYApellido1= self.usuario.get(NOMBRE_APELLIDO1)
        self.nombreYApellido2= self.usuario.get(NOMBRE_APELLIDO2)
        self.numeroTarjeta = self.usuario.get(NUMERO_TARJETA)
        self.numeroSocio = self.usuario.get(NUMERO_SOCIO)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.marcaDeTarjeta = self.usuario.get(MARCA_TARJETA)
        self.marcaDeTarjeta1 = self.usuario.get(MARCA_TARJETA1)
        self.cuentaDebito = self.usuario.get(CUENTA1)
        
if __name__ == "__main__":
    unittest.main()
