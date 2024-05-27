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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,MENSAJE_IMPRESION,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA
from asyncio.tasks import sleep
             

@allure.feature(u'Moneda Estranjera')
@allure.story(u'Venta Moneda Extranjera')
@allure.testcase(u"SUC-T879 - Venta Moneda Extranjera")
@allure.title(u'SUC-T879 - Venta Moneda Extranjera')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la transacción 120 Venta Moneda Extranjera</br>
6.-Visualizar en pantalla el Recuadro de los Datos Iniciales</br>
7.-Seleccionar tipo de documento "DNI" e ingresar Numero de DNI "24123465"</br>
8.-Seleccionar Debe Presentar "CUIL" e ingresar Numero de CUIL "20241234658"</br>
9.-Seleccionar Moneda "Dolares"</br>
10.-Hacer clic en el Botón "SIGUIENTE"</br>
11.-Ingresar Importe a comprar "1,00"</br>
12.-Hacer clic en el botón "COTIZAR"</br>
13.-Visualizar en la cotización e importe pesos compra</br>
14.-Hacer clic en el Botón "CONFIRMAR"</br>
15.-Visualizar la impresión del ticket</br>
16.-Visualizar la impresión de la DDJJ y cerrar el navegador</br>
17.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
18.-Hacer clic en Botón "FINALIZAR"</br>
19.-Visualizar la impresión del ticket</br>
20.-Hacer clic en el recuadro Hola, UIC10021</br>
21.-Hacer clic en CERRAR SESIÓN</br>
</br>   
"""
)
class SUC_T879(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T879(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_venta_moneda_extranjera()
            self.seleccionar_tipo_documento()
            self.seleccionar_item_DNI()
            self.ingresar_numero_de_DNI("24123465")
            self.seleccionar_debe_precentar()
            self.seleccionar_item_CUIL()
            self.ingresar_numero_CUIL("20241234658")
            self.seleccionar_moneda()
            self.seleccionar_item_MONEDA()
            self.seleccionarSiguiente()
            self.wait(3)
            self.ingresar_importe_a_comprar("100")
            self.seleccionar_button_cotizar()
            self.visualizar_cotizacion()
            self.seleccionar_Confirmar()
            self.wait(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.visualizar_ticket()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.wait(1)
            self.visualizarMensajeExito()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")
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
