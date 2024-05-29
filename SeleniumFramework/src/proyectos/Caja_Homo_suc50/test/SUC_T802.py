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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO,MONEDA1,MONEDA2,MONEDA3
             

@allure.feature(u'Remesas')
@allure.story(u'Consulta de Saldos')
@allure.testcase(u"SUC-T802 -  Consulta de Saldos Sucursal - Centralizador")
@allure.title(u'SUC-T802 -  Consulta de Saldos Sucursal - Centralizador')
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/33998')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(    
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10022 y visualizar los datos del operador UIC10022</br>
5.-Hacer clic en el recuadro Hola, UIC10022 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Consulta de Saldos Sucursal"</br>
7.-Visualizar el recuadro de la Consulta de Saldos de Sucursal "Operadores - Tesoro Intermedio - Tesoro Sucursal"</br>
8.-Hacer clic en el ítem Operadores</br>
9.-Hacer clic en el Botón "LISTAR"</br>
10.-Visualizar la información del saldo de los operadores</br>
11.-Hacer clic en la flecha "Búsqueda"</br>
12.-Hacer clic en el ítem Tesoro Intermedio</br>
13.-Hacer clic en el Botón "LISTAR"</br>
14.-Visualizar la información del saldo del Tesoro Intermedio</br>
15.-Hacer clic en la flecha "Búsqueda"</br>
16.-Hacer clic en el ítem Tesoro Sucursal</br>
17.-Hacer clic en el Botón "LISTAR"</br>
18.-Visualizar la información de los saldos del Tesoro Sucursal</br>
19.-Hacer clic en el recuadro Hola, UIC10022</br>
20.-Hacer clic en CERRAR SESIÓN</br>

"""
)
class SUC_T802(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T802(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()             
            self.seleccionarConsultaDeSaldosSucursal()
            self.visualizarRecuadroConsultaSaldosSucursal()
            self.selecionarParametro("Operadores")
            self.seleccionarListar()  
            self.visualizarTablaDeSaldos()            
            self.seleccionarBusqueda() 
            self.selecionarParametro("Tesoro Intermedio")
            self.seleccionarListar()
            self.visualizarTablaDeTesoroIntermedio()                
            self.seleccionarBusqueda()                
            self.selecionarParametro("Tesoro Sucursal")
            self.seleccionarListar()
            self.visualizarTablaDeTesoroSucursal()                
            self.seleccionarBusqueda()
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
        self.moneda = self.usuario.get(MONEDA)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2= self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)

        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
