# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Inte.st.stLogin import stLogin
import subprocess
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
              OPERACION1,OPERACION2,\
              MONEDA1,MONEDA2,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,\
              IMPORTE_VALIDAR_2,OPERACION_VALIDAR1,OPERACION_VALIDAR2,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
import pytest



@allure.feature(u'Pagos')
@allure.story(u'Pagos Varios')
@allure.testcase(u"ICaja - SUC-T853 Pagos Varios - Moneda Dolares") 
@allure.title(u'SUC-T853 - Pagos Varios')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - "Pagos Varios"</br>
6.-Hacer clic en el "Tipo de Operación"</br>
7.-Seleccionar el ítem "99 Otros Débitos"</br>
8.-Hacer clic en seleccionar Moneda a extraer "Dolares"</br>
9.-Ingresar importe "20"</br>
10.-Hacer clic en "SIGUIENTE"</br>
11.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
12.-Visualizar el recuadro de autorizaciones</br>
13.-Realizar la autorización de la Tx mediante el modulo de autorizaciones</br>
14.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
15.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
16.-Hacer clic en el botón ACEPTAR</br>
17.-Hacer clic en el botón ACTUALIZAR</br>
18.-Visualizar la autorización en estado pendiente</br>
19.-Hacer clic en el checklist verde</br>
20.-Visualizar en pantalla el recuadro para confirmar la autorización y hacer clic en Autorizar</br>
21.-Volver al aplicación ICaja</br>
22.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
23.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
24.-Hacer clic en el Botón Validar</br>
25.-Visualizar el mensaje "Timbrado de cobro con éxito"</br>
26.-Hacer clic en Botón "FINALIZAR"</br>
27.-Visualizar la impresión del ticket</br>
28.-Hacer clic en el recuadro Hola, UIC10021</br>
29.-Hacer clic en CERRAR SESIÓN</br>    
 "  . 
    """
)

class SUC_T853(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T853(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarPagosVarios()
            self.wait(3)
            self.seleccionarRecuadroTpdeOperacion()
            self.seleccionarTipoDeOperacion(self.Operacion2)
            self.seleccionarComboBox()          
            self.seleccionarMoneda(self.moneda2)        
            self.ingresarImporte2(self.importe2)
            self.seleccionarBtnSiguiente() 
            self.validarTipoDeOperacion(self.operacionAValidar2)
            self.validarMonedaOpn(self.moneda2)
            self.validarImporteOpn(self.importeValidar2) 
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.autorizarOperacionPg()
            self.seleccionarAceptarAutoriz()
            self.seleccionarValidar()
            self.visualizarMensajeExito()
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
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucudestino = self.usuario.get(SUCURSAL_ORIG)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_DEST)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
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
