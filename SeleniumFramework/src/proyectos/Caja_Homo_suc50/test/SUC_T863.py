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
              MONEDA, IMPORTE, MSJ_ESPERADO
             

@allure.feature(u'Remesas')
@allure.story(u'Envio de Remesa')
@allure.testcase(u"ICaja - SUC-T863 - Envió de Remesa - Tesoro Sucursal- Tesoro Intermedio(UIC10022)")
@allure.title(u'SUC-T863 - Envió de Remesa - Tesoro Sucursal- Tesoro Intermedio (UIC10022)')
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/36163')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22
3.-Hacer clic en el botón "INGRESAR"
4.-Validar el nombre de usuario "Hola, UIC10022
5.-Hacer clic en la Transacción - Envio de Remesa
8.-Tildar la opción "Tesoro Sucursal"
9.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"
10.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Pesos"
11.-Visualizar en pantalla el recuadro Importe y agregar "200.000,00"
12.-Hacer clic en boton "CONFIRMAR"
13.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
14.-Visualizar el mensaje "Operación realizada con éxito"
15.-Hacer clic en boton "FINALIZAR"
16.-Visualizar la impresion del ticket</br>
    """
)
class SUC_T863(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T863(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()       
            self.seleccionarEnvioDeRemesa()
            self.clickRadioBtn("Tesoro Sucursal")
            self.mostrarDestino("Tesoro Intermedio")
            self.mostrarMoneda("Pesos")
            self.ingresarImporte("200.000,00","Pesos")
            self.seleccionarConfirmar() 
            self.validar_origen("Tesoro Sucursal")
            self.validar_destino("Tesoro Intermedio")
            self.validar_moneda("Pesos")
            self.validar_importe("200.000,00")
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
