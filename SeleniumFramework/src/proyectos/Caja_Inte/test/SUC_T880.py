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


@allure.feature(u'BMACorp')
@allure.story(u'Pago de Vales')
@allure.testcase(u"SUC-T879 - Pago de Vales")
@allure.title(u'SUC-T879 - Pago de Vales')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la transacción 115 Pago de Vales</br>
6.-Seleccionar Cuenta Débito "ARP - 10010218006 RESERVA DEL NORTE TEST 100.000,00"</br>
7.-Seleccionar tipo de documento "DNI" e ingresar Numero de DNI "21015666"</br>
8.-Ingresar Numero de Legajo "00432567"</br>
9.-Ingresar Comprobante "01020304"</br>
10.-Ingresar Importe "10.000"</br>
11.-Hacer clic en el Botón "CONFIRMAR"</br>
12.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
13.-Visualizar la impresión del ticket</br>
14.-Hacer clic en el Botón "Validar"</br>
15.-Visualizar el Mensaje - "Timbrado finalizado con exito"</br>
16.-Visualizar el timbrado en el ticket</br>
17.-Hacer clic en Botón "FINALIZAR"</br>
18.-Hacer clic en el recuadro Hola, UIC10021</br>
19.-Hacer clic en CERRAR SESIÓN</br>
</br>   
"""
)
class SUC_T880(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T880(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_pago_de_vales()
            self.wait(2)
            self.seleccionar_reacuadro_cuenta_debito()
            self.seleccionar_item_cuenta_dbt("ARP - 01031568007 QA ER ARGENTINA S.A.  0,00")
            self.seleccionar_tipo_documento()
            self.seleccionar_item_DNI()
            self.ingresar_numero_de_DNI_2("24123465")
            self.ingresar_numero_de_legajo("00432567")
            self.ingresar_numero_de_comprobante("01020304")
            self.ingresar_monto("1000000")
            self.seleccionar_Confirmar()
            self.visualizarMensajeExito()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")
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
