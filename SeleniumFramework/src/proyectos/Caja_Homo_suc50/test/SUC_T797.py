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
              OPERACION1,OPERACION2,\
              MONEDA1,MONEDA2,MONEDA3,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,OPERACION_VALIDAR1,OPERACION_VALIDAR2,\
              USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
import pytest



@allure.feature(u'Operaciones de Caja')
@allure.story(u'Consulta del Liquido en Caja')
@allure.testcase(u"ICaja - SUC-T797 - Consulta del Líquido en Caja ") 
@allure.title(u'SUC-T797 - Consulta del Líquido en Caja')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Consulta del Líquido en Caja"</br>
7.-Hacer clic en "Moneda"</br>
8.-Seleccionar "Pesos"</br>
9.-Hacer clic en el Botón "Consultar"</br>
10.-Visualizar el recuadro de la autorización</br>
11.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
12.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
13.-Visualizar la autorización en estado pendiente</br>
14.-Hacer clic en el botón ACEPTAR</br>
15.-Hacer clic en el botón AUTORIZAR</br>
16.-Hacer clic en el botón Salir</br>
17.-Volver al aplicación ICaja</br>
18.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
19.-Visualizar el Mensaje - "El ticket se imprimió correctamente"</br>
20.-Visualizar la impresión del ticket</br>
21.-Hacer clic en "Moneda"</br>
22.-Seleccionar "Dolares"</br>
23.-Hacer clic en el Botón "Consultar"</br>
24.-Visualizar el recuadro de la autorización</br>
25.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
26.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
27.-Visualizar la autorización en estado pendiente</br>
28.-Hacer clic en el botón ACEPTAR</br>
29.-Hacer clic en el botón AUTORIZAR</br>
30.-Hacer clic en el botón Salir</br>
31.-Volver al aplicación ICaja</br>
32.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
33.-Visualizar el Mensaje - "El ticket se imprimió correctamente"</br>
34.-Visualizar la impresión del ticket</br>
35.-Hacer clic en "Moneda"</br>
36.-Seleccionar "Euros"</br>
37.-Hacer clic en el Botón "Consultar"</br>
38.-Visualizar el recuadro de la autorización</br>
39.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
40.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
41.-Visualizar la autorización en estado pendiente</br>
42.-Hacer clic en el botón ACEPTAR</br>
43.-Hacer clic en el botón AUTORIZAR</br>
44.-Hacer clic en el botón Salir</br>
45.-Volver al aplicación ICaja</br>
46.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
47.-Visualizar el Mensaje - "El ticket se imprimió correctamente"</br>
48.-Visualizar la impresión del ticket</br>
49.-Hacer clic en "Moneda"</br>
50.-Seleccionar "Reales"</br>
51.-Hacer clic en el Botón "Consultar"</br>
52.-Visualizar el recuadro de la autorización</br>
53.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
54.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
55.-Visualizar la autorización en estado pendiente</br>
56.-Hacer clic en el botón ACEPTAR</br>
57.-Hacer clic en el botón AUTORIZAR</br>
58.-Hacer clic en el botón Salir</br>
59.-Volver al aplicación ICaja</br>
60.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
61.-Visualizar el Mensaje - "El ticket se imprimió correctamente"</br>
62.-Visualizar la impresión del ticket</br>
63.-Hacer clic en el recuadro Hola, UIC10021</br>
64.-Hacer clic en CERRAR SESIÓN </br>    
 "  . 
    """
)

class SUC_T797(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T797(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            monedas = [self.moneda,self.moneda1,self.moneda2,self.moneda3]
            for moneda in monedas:
                self.seleccionarConsultaDeLiquidoDeCuenta()
                self.mostrarTiposDeMoneda()
                self.seleccionarTipoDeMoneda(moneda)
                self.seleccionarConsultar()
                self.obtenerNroDeAutorizacion()
                self.autorizarOperacionPg()
                self.seleccionarAceptarAutoriz()
                self.visualizarMensajeExito()  
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
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
        self.terminal = self.usuario.get(TERMINAL)
        self.sucudestino = self.usuario.get(SUCURSAL_ORIG)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_DEST)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.moneda = self.usuario.get(MONEDA) 
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
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
