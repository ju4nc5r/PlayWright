# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
    LEGAJO_AUTORIZ, TERMINAL_AUTORIZ, PASWORD_AUTORIZ,MONEDA1,MONEDA2,MONEDA3         
import pytest

@allure.feature(u'Operaciones de Caja')
@allure.story(u'Consulta de Posición del Líquido de la Sucursal')
@allure.testcase(u"ICaja - SUC-T796 - Consulta de Posición del Líquido de la Sucursal - (Perfil Centralizador)")
@allure.title(u'SUC-T796 - Consulta de Posición del Líquido de la Sucursal - (Perfil Centralizador)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822  / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en la Transacción - "Consulta de Posición del Líquido de la Sucursal"</br>
5.-Hacer clic en "Moneda"</br>
6.-Seleccionar "Pesos"</br>
7.-Hacer clic en el Botón "Consultar"</br>
8.-Visualizar la información de los Saldos</br>
9.-Hacer clic en "Moneda"</br>
10.Seleccionar "Dolares"</br>
11.-Hacer clic en el Botón "Consultar"</br>
12.-Visualizar la información de los Saldos</br>
13.-Hacer clic en "Moneda"</br>
14.-Seleccionar "Euros"</br>
15.-Hacer clic en el Botón "Consultar"</br>
16.-Visualizar la información de los Saldos</br>
17.-Hacer clic en "Moneda"</br>
18.-Seleccionar "Reales"</br>
19.-Hacer clic en el Botón "Consultar"</br>
20.-Visualizar la información de los Saldos</br>
21.-Hacer clic en el recuadro Hola, UIC10022</br>
22.-Hacer clic en CERRAR SESIÓN </br>
"""
)
class SUC_T796(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T796(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarConsultaDePoicionDelLiquidoDeLaSucursal()
            monedas = ["Pesos","Dolares","Euros","Reales"]
            for moneda in monedas:
                self.wait(1) 
                self.mostrarTiposDeMoneda()
                self.seleccionarTipoDeMoneda(moneda)
                self.seleccionarConsultar()
                saldos = ["Saldo Total Cajas (Cajon)","Saldo Total CAF",
                          "Saldo Total Tesoro Intermedio","Saldo Total Tesoro Sucursal",
                          "Saldo Total ATM","Saldo Total General","Encaje Sucursal"]
                for saldo in saldos:
                    self.wait(1) 
                    self.visualizarDatosDeSaldo(moneda, saldo)
                    html = self.driver.find_element_by_tag_name('html')
                    html.send_keys(Keys.PAGE_UP)
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
        self.sucuorigen = self.usuario.get(SUCURSAL)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        #self.mensaje = "La operacion finalizo correctamente"   
        

if __name__ == "__main__":
    unittest.main()
