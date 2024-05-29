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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO
             

@allure.feature(u'Clientes')
@allure.story(u'Certificación de Firma')
@allure.testcase(u"SUC-T775 - Certificacion de firma")
@allure.title(u'SUC-T775 - Certificacion de firma')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 � / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10009</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador </br>
6.-Hacer clic en la Transacción - "Certificación de Firma"</br>
7.-Visualizar el recuadro identificar al cliente, hacer clic en "SI"</br>
8.-Ingresar los datos del cliente</br>
9.-Seleccionar Tipo de Documento "DNI"</br>
10.-Ingresar Numero de Documento "25227274"</br>
11.-Hacer clic en el Botón "IDENTIFICAR"</br>
12.-Hacer clic en el Botón SIN CLAVE</br>
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
14.-Hacer clic en el recuadro Cuenta</br>
15.-Seleccionar cuenta CC $ - 0444583-100/3</br>
16.-Hacer clic en el Botón "SIGUIENTE"</br>
17.-Hacer check en Confirmar firma.</br>
18.-Hacer clic en el Botón "CONFIRMAR"</br>
19.-16-Visualizar el Mensaje - Operación Realizada Con Éxito.</br>
20.-Hacer clic en Botón "ACEPTAR"</br>
21.-Visualizar la impresión del ticket</br>
22.-Hacer clic en el recuadro Hola, UIC10021</br>
23.-Hacer clic en CERRAR SESIÓN</br>
 </br>   
"""
)
class SUC_T775(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T775(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarCertificacionFirma() 
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasFirmas()
            self.seleccionarCuentaFirmas(self.cuenta)
            self.seleccionarSiguiente()
            self.wait(2)
            self.seleccionarConfirmarFirma()  
            self.seleccionar_imprimir_template()
            self.seleccionarFinalizar2()
            self.verificarMensajeExitoDeposito2("La operacion se realizo con exito.")
            self.seleccionarAceptarComun() 
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
