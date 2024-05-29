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
@allure.story(u'Envio de Remesa')
@allure.testcase(u"ICaja - SUC-T864 - Envió de Remesa - Tesoro Intermedio - Cajero UIC10021")
@allure.title(u'SUC-T864 -  Envió de Remesa - Tesoro Intermedio - Cajero UIC10021')
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/36164')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar el nombre de usuario "Hola, UIC10022</br>
5.-Hacer clic en la Transacción - Envio de Remesa</br>
8.-Tildar la opción "Tesoro Intermediol"</br>
9.-Visualizar en pantalla el recuadro Destino y Seleccionar "UIC10021"</br>
10.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Pesos"</br>
11.-Visualizar en pantalla el recuadro Importe y agregar "200.000,00"</br>
12.-Hacer clic en boton "CONFIRMAR"</br>
13.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
14.-Visualizar el mensaje "Operación realizada con éxito"</br>
15.-Hacer clic en boton "FINALIZAR"</br>
16.-Visualizar la impresion del tickett</br>
    """
)
class SUC_T864(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T864(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()       
            self.seleccionarEnvioDeRemesa()
            self.clickRadioBtn("Tesoro Intermedio")
            self.mostrarDestino("Uic10021")
            self.mostrarMoneda("Pesos")
            self.ingresarImporte("200.000,00","Pesos")
            self.seleccionarConfirmar()
            self.visualizar_msj_no_hay_suficiente_saldo()     
            self.validar_origen("Tesoro Intermedio")
            self.validar_destino("Uic10021")
            self.validar_moneda("Pesos")
            self.validar_importe("200.000,00")
            self.seleccionarConfirmar3() 
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
