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
              MONEDA, IMPORTE, MSJ_ESPERADO
             

@allure.feature(u'Extracciones')
@allure.story(u'Extracción Efectivo')
@allure.testcase(u"ICaja - SUC-T776 - Extracción de Efectivo - Moneda Pesos")
@allure.title(u'SUC-T776 - Extraccion en pesos de cuenta en pesos')
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/23313')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Extracciones en efectivo</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "25227274"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón SIN CLAVE</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Cliente"</br>
14.-Seleccionar cuenta "CA $"</br>
15.-Hacer clic en seleccionar Moneda a extraer "Pesos"</br>
16.-Ingresar importe "100.000"</br>
17.-Hacer clic en "SIGUIENTE"</br>
18.-Marcar el check si coincide la firma y hacer clic en el Botón "SIGUIENTE"</br>
19.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
20.-Visualizar el mensaje "Operación realizada con éxito"</br>
21.-Hacer clic en el botón "FINALIZAR"</br>
22.-Visualizar la impresión del ticket</br>
23.-Hacer clic en el recuadro Hola, UIC10021</br>
24.-Hacer clic en CERRAR SESIÓN</br>
    """
)
class SUC_T776(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T776(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarExtracciones()
            self.identificarCliente() 
            self.seleccionarCuentaExtraccion(self.cuenta)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarImporte(self.importe,self.tipoMoneda)
            self.seleccionarSiguiente()
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente2()
            self.visualizarDatosOperacion2(self.importe,self.cuenta,self.tipoMoneda)
            self.seleccionarConfirmar()
            self.visualizar_msj_no_hay_suficiente_saldo_depositos() 
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
