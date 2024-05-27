# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Inte.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO
             

@allure.feature(u'Remesas')
@allure.story(u'Envio de Remesa Interna')
@allure.testcase(u"ICaja - SUC-T820 - Envió de Remesas Interna CAF - CAJA (UIC10021)")
@allure.title(u'SUC-T820 - Envió de Remesas Interna CAF - CAJA (UIC10021)')
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/34300')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login </br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021/Terminal:IA0500821/ Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - Envió de Remesa Interna</br>
7.-Visualizar en pantalla el titulo Remesa Interna - Cajero</br>
8.-Seleccionar en Origen "Caf"</br>
9.-Seleccionar Destino "Caja"</br>
10.-Seleccionar Moneda "Pesos"</br>
11.-Ingresar Importe "10.000,00"</br>
12.-Hacer clic en el Botón "CONFIRMAR"</br>
13.-Visualizar el recuadro de los datos de la TX y hacer clic en el boton CONFIMAR "CONFIRMAR"</br>
14.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
15.-Visualizar la impresión del ticket</br>
16.-Hacer clic en la Transacción - Envió de Remesa Interna</br>
17.-Seleccionar en Origen "Caf"</br>
18.-Seleccionar Destino "Caja"</br>
19.-Seleccionar Moneda "Dolares"</br>
20.-Ingresar Importe "1.000"</br>
21.-Hacer clic en el Botón "CONFIRMAR" "CONFIRMAR"</br>
22.-Visualizar el recuadro de los datos de la TX y hacer clic en el Botón "CONFIRMAR"</br>
23.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
24.-Visualizar la impresión del ticket</br>
25.-Hacer clic en la Transacción - Envió de Remesa Interna</br>
26.-Seleccionar en Origen "Caf"</br>
27.-Seleccionar Destino "Caja"</br>
28.-Seleccionar Moneda "Euros"</br>
29.-Ingresar Importe "500"</br>
30.-Hacer clic en el Botón "CONFIRMAR"</br>
31.-Visualizar el recuadro de los datos de la TX y hacer clic en el boton "CONFIRMAR"</br>
32.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
33.-Visualizar la impresión del ticket</br>
34.-Hacer clic en el recuadro Hola, UIC10021</br>
35.-Hacer clic en CERRAR SESIÓN</br>
    """
)
class SUC_T820(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T820(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            monedas = ["Pesos","Dolares","Euros"]
            posiciones = ["1","2","3"]
            importes = ["10.000,00","1.000,00","500,00"]
            for moneda,posicion,importe,in zip(monedas,posiciones,importes):        
                self.obtenerSaldosDeCaf(posicion)           
                self.seleccionarEnvioDeRemesaInterna()
                self.clickRadioBtn("Caf")
                self.mostrarDestino("Caja")
                self.mostrarMoneda(moneda)
                self.ingresarImporte(importe,moneda)
                self.seleccionarConfirmar()   
                self.validar_origen("Caf")
                self.validar_destino("Caja")
                self.validar_moneda(moneda)
                self.validarImporteOpn(importe)
                self.seleccionarConfirmar3() 
                self.visualizar_msj_no_hay_suficiente_saldo()
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
