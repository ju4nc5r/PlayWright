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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,MENSAJE_IMPRESION,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA
             

@allure.feature(u'Plazo Fijo')
@allure.story(u'Consulta de Plazo Fijo')
@allure.testcase(u"SUC-T871 - Consulta de Plazo Fijo")
@allure.title(u'SUC-T871 - Consulta de Plazo Fijo')
@allure.link(u'')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br> 
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br> 
3.-Hacer clic en el botón "INGRESAR"</br> 
4.-Validar nombre del Operador "Hola, UIC10021</br> 
5.-Hacer clic en la consulta: Consulta de Plazo Fijo</br> 
6.-Visualizar en pantalla el Recuadro identificar cliente</br> 
7.-Ingresar los datos del cliente</br> 
8.-Seleccionar Tipo de Documento "DNI"</br> 
9.-Ingresar Numero de Documento "17112015"</br> 
10.-Hacer clic en el Botón "IDENTIFICAR"</br> 
11.-Hacer clic en el Botón "SIN CLAVE"</br> 
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br> 
13.-Visualizar en pantalla los datos del cliente.</br> 
14.-Hacer clic en el Botón "IMPRIMIR"</br> 
15.-Visualizar la impresión del ticket</br> 
16.-Hacer clic en el Botón "FINALIZAR"</br> 
17.-Hacer clic en el recuadro Hola, UIC10021</br> 
18.-Hacer clic en CERRAR SESIÓN</br> 
</br>   
"""
)
class SUC_T871(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T871(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_consulta_de_plazo_fijo() 
            self.identificarCliente()
            self.validar_cliente("JUAN VISADE") 
            self.validar_dni("17112015")
            self.seleccionar_imprimir()
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
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.mensaje_impresion = self.usuario.get(MENSAJE_IMPRESION)
        self.importe = self.usuario.get(IMPORTE)
        self.dias = self.usuario.get(DIAS)
        self.moneda = self.usuario.get(MONEDA)
        

if __name__ == "__main__":
    unittest.main()
