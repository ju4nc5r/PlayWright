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
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,MONEDA1,MONEDA2,MONEDA3           

@allure.feature(u'Operaciones de Caja')
@allure.story(u'Consulta de Totales')
@allure.testcase(u"ICaja - SUC-T798 - Consulta de Totales")
@allure.title(u'SUC-T798 - Consulta de Totales')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Consulta de Totales"</br>
7.-Visualizar el numero de Sucursal "0050"</br>
8.-Hacer clic en "Moneda"</br>
9.-Seleccionar "Pesos"</br>
10.-Hacer clic en el Botón "Consultar"</br>
11.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
12.-Visualizar la impresión del ticket</br>
13.-Hacer clic en "Moneda"</br>
14.-Seleccionar "Dolares"</br>
15.-Hacer clic en el Botón "Consultar"</br>
16.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
17.-Visualizar la impresión del ticket</br>
18.-Hacer clic en "Moneda"</br>
19.-Seleccionar "Euros"</br>
20.-Hacer clic en el Botón "Consultar"</br>
21.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
22.-Visualizar la impresión del ticket</br>
23.-Hacer clic en "Moneda"</br>
24.-Seleccionar "Reales"</br>
25.-Hacer clic en el Botón "Consultar"</br>
26.-Visualizar el Mensaje - "Se ha impreso un comprobante de su consulta"</br>
27.-Visualizar la impresión del ticket</br>
28.-Hacer clic en el recuadro Hola, UIC10021</br>
29.-Hacer clic en CERRAR SESIÓN </br>
"""
)
class SUC_T798(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T798(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarConsultaDeTotales()
            monedas = [self.moneda,self.moneda1,self.moneda2,self.moneda3]
            for moneda in monedas: 
                self.mostrarTiposDeMoneda()
                self.seleccionarTipoDeMoneda(moneda)
                self.seleccionarConsultar()
                self.visualizarMensajeExito()  
#                 self.visualizarMensajeExito(self.mensaje)       
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
        self.moneda = self.usuario.get(MONEDA)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.sucuorigen = self.usuario.get(SUCURSAL)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        #self.mensaje = "La operacion finalizo correctamente"   
        

if __name__ == "__main__":
    unittest.main()
