# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,CUENTA1
             

@allure.feature(u'Clientes')
@allure.story(u'Consulta de saldos de cuentas')
@allure.testcase(u"SUC-T781 - Consulta de Saldos de Cuentas")
@allure.title(u'SUC-T781 - Consulta de Saldos de Cuentas')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Consulta de Saldos de Cuentas"</br>
7.-Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?</br>
8.-Hacer clic en "SI"</br>
9.-Ingresar los datos del cliente</br>
10.-Seleccionar Tipo de Documento "DNI"</br>
11.-Ingresar Numero de Documento "25227274"</br>
12.-Hacer clic en el Botón "IDENTIFICAR"</br>
13.-Hacer clic en el Botón "SIN CLAVE"</br>
14.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
15.-Hacer clic en el recuadro "Cuentas Cliente"</br>
16.-Seleccionar cuenta "01 CC $ 0444583-100/3 10.583.393,34 DIEGO SIGNA QA"</br>
17.-Hacer clic en "CONSULTAR"</br>
18.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
19.-Visualizar la impresión del ticket</br>
20.-Hacer clic en "FINALIZAR"</br>
21.-Hacer clic en la Transacción - "Consulta de Saldos de Cuentas"</br>
22.-Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?</br>
23.-Hacer clic en "SI"</br>
24.-Ingresar los datos del cliente</br>
25.-Seleccionar Tipo de Documento "DNI"</br>
26.-Ingresar Numero de Documento "25227274"</br>
27.-Hacer clic en el Botón "IDENTIFICAR"</br>
28.-Hacer clic en el Botón "SIN CLAVE"</br>
29.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
30.-Hacer clic en el Botón "TICKET"</br>
31.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
32.-Visualizar la impresión del ticket</br>
33.-Hacer clic en "FINALIZAR"</br>
34.-Hacer clic en la Transacción - "Consulta de Saldos de Cuentas"</br>
35.-Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?</br>
36.-Hacer clic en "NO"</br>
37.-Ingresar en el recuadro el Numero de cuenta cliente "04467751007"</br>
38.-Hacer clic en Botón "CONSULTAR"</br>
39.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
40.-Visualizar la impresión del ticket</br>
41.-Hacer clic en "FINALIZAR"</br>
42.-Hacer clic en el recuadro Hola, UIC10021</br>
43.-Hacer clic en CERRAR SESIÓN </br>
"""
)
class SUC_T781(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T781(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()            
            self.seleccionarConsultaSaldosCuenta() 
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente()
            self.validarBtnDeshabilitado() 
            self.seleccionarRecuadroCuentas()
            self.seleccionarCuentaCliente(self.cuenta)
            self.seleccionarConsultar()
            self.visualizarMensajeExito()  
            self.visualizarTicket2() 
            self.seleccionarFinalizar2()                          
            self.seleccionarConsultaSaldosCuenta() 
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente()
            self.validarBtnDeshabilitado() 
            self.seleccionarticket()
            self.visualizarMensajeExito()  
            self.visualizarTicket2()
            self.seleccionarFinalizar2()                          
            self.seleccionarConsultaSaldosCuenta() 
            self.visualizarCuadroNecesitaIdentificarAlCliente2()
            self.validarBtnDeshabilitado() 
            self.ingresarNroCuenta(self.cuenta1)
            self.seleccionarConsultar()
            self.visualizarMensajeExito()  
            self.visualizarTicket2() 
            self.seleccionarFinalizar2()                         
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
        self.cuenta1 = self.usuario.get(CUENTA1)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        

if __name__ == "__main__":
    unittest.main()
