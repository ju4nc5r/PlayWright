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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO 

@allure.feature(u'Clientes')
@allure.story(u'Consulta de Posición de Cuenta')
@allure.testcase(u"SUC-T780 - Consulta de Posición de Cuenta")
@allure.title(u'SUC-T780 - Consulta de Posición de Cuenta')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br> 
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br> 
3.-Hacer clic en el botón "INGRESAR"</br> 
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br> 
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br> 
6.-Hacer clic en la Transacción - "Consulta de Posición de Cuenta"</br> 
7.-Visualizar en pantalla el Recuadro identificar cliente</br> 
8.-Ingresar los datos del cliente</br> 
9.-Seleccionar Tipo de Documento "DNI"</br> 
10.-Ingresar Numero de Documento "25227274"</br> 
11.-Hacer clic en el Botón "IDENTIFICAR"</br> 
12.-Hacer clic en el Botón "SIN CLAVE"</br> 
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br> 
14.-Hacer clic en el recuadro "Raíces"</br> 
15.-Seleccionar cuenta "0444583 DIEGO SIGNA QA"</br> 
16.-Hacer clic en "CONSULTAR"</br> 
17.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br> 
18.-Visualizar la impresión del ticket</br> 
19.-Hacer clic en el Botón"FINALIZAR"</br> 
20.-Hacer clic en el recuadro Hola, UIC10021</br> 
21.-Hacer clic en CERRAR SESIÓN </br> 
"""
)
class SUC_T780(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T780(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarConsultaPocisionCuenta() 
            self.identificarCliente()
            self.validarBtnDeshabilitado() 
            self.seleccionarRaices()
            self.seleccionarCuentasRaices(self.cuenta)
            self.seleccionarConsultar()
            self.visualizarMensajeExito()  
            self.visualizarTicket()
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
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        

if __name__ == "__main__":
    unittest.main()
