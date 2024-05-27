# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
import pyautogui
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO
             

@allure.feature(u'Extracciones')
@allure.story(u'Extracción Efectivo')
@allure.testcase(u"ICaja - SUC-T841 - Extracción de Efectivo - Moneda Cruzada - Pesos Dolar.")
@allure.title(u'SUC-T841 -  Extracción de Efectivo - Moneda Cruzada - Pesos Dolar.')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Extracciones en efectivo</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "22999439"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón SIN CLAVE</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Cliente"</br>
14.-Seleccionar cuenta "CA $ 1000108-301/3"</br>
15.-Hacer clic en seleccionar Moneda a extraer "Dolares"</br>
16.-Ingresar importe "1,00"</br>
17.-Hacer clic en "SIGUIENTE"</br>
18.-Visualizar los datos de la Transacción</br>
19.-hacer clic en el Botón "SIGUIENTE"</br>
20.-Marcar el check si coincide la firma</br>
21.-Hacer clic en el Botón "SIGUIENTE"</br>
22.-Visualizar los datos de la Transacción</br>
23.-Hacer clic en el Botón "CONFIRMAR"</br>
24.-Visualizar la DDJJ en PDF</br>
25.-Visualizar el mensaje "Operación realizada con éxito"</br>
26.-Hacer clic en el botón "FINALIZAR"</br>
27.-Visualizar la impresión del ticket</br>
28.-Hacer clic en el recuadro Hola, UIC10021</br>
29.-Hacer clic en CERRAR SESIÓN</br> 
"""
)
class SUC_T888(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T888(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarExtracciones()
            self.identificarCliente() 
            self.seleccionarCuentaExtraccion(self.cuenta)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarImporte(self.importe,self.tipoMoneda)
            self.seleccionarSiguiente()
            self.visualizar_datos_moneda_cambio()
            self.seleccionarSiguiente2()        
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente2()
            self.visualizarDatosOperacion2(self.importe,self.cuenta,self.tipoMoneda)
            self.seleccionarConfirmar()
            self.wait(5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            pyautogui.press('enter')
            pyautogui.PAUSE = 2.5
            pyautogui.press('enter')
            self.wait(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.visualizar_msj_no_hay_suficiente_saldo_depositos
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
