# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
import pytest
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL,CLAVE,\
              MONEDA, MSJ_ESPERADO , SUCURSAL_DEST,SUCURSAL_ORIG,\
              OPERACION1,OPERACION2,\
              MONEDA1,MONEDA2,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,\
              IMPORTE_VALIDAR_2,OPERACION_VALIDAR1,OPERACION_VALIDAR2,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO



@allure.feature(u'Pagos')
@allure.story(u'Pago de Jubilaciones Italianas')
@allure.testcase(u"ICaja - SUC-T868 Pago de Jubilaciones Italianas - Numero de Pensión") 
@allure.title(u'SUC-T868 - Pago de Jubilaciones Italianas')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción"Pago de Jubilaciones Italianas"</br>
6.-Validar que este seleccionado el Item "Numero de Pension"</br>
7.-Ingesar Numero de Pension "47001236-9300-006"</br>
8.-Hacer clic en "SIGUIENTE"</br>
9.-Visualizar los datos de la pension.</br>
10.-Visualizar el campo "PAGOS PENDIENTES"</br>
11.-Hacer checklist y seleccionar un pago pendiente.</br>
12.-Hacer clic en "SIGUIENTE"</br>
13.-Visualizar los datos de la Pensión</br>
14.-Hacer checklist y seleccionar "Beneficiario"</br>
15.-Visualizar los datos que aparece en pantalla.</br>
16.-Seleccionar el item "Debe presentar CUIT/CUIL/CDI del Beneficiario"</br>
17.-Seleccionar el campo Tipo de documento y seleccionar "CUIL"</br>
18.- Ingresar Numero de documento "27933471220"</br>
19.-Hacer clic en "SIGUIENTE"</br>
20.-Visualizar los datos de la Transaccion</br>
21.-Hacer clic en el botón "SIGUIENTE"</br>
22.-Visualizar el ticket DDJJ</br>
23.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
24.-Hacer clic en Botón "FINALIZAR"</br>
25.-Visualizar la impresión del ticket</br>
26.-Hacer clic en la Transacción - "Reverso de Transacción"</br>
27.-En el ticket visualizar el numero de Tx e ingresarla en el campo Numero de secuencia</br>
28.-Visualizar los datos de la Transacción</br>
29.-Hacer clic en el recuadro "Motivo" y seleccionar "Error Carga Cajero"</br>
30.-Marcar el check "El cliente presente ticket"</br>
31.-Hacer clic en el Botón "CONFIRMAR"</br>
32.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
33.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
34.-Visualizar la autorización en estado pendiente</br>
35.-Hacer clic en el botón ACEPTAR</br>
36.-Hacer clic en el botón AUTORIZAR</br>
37.-Hacer clic en el botón Salir</br>
38.-Volver al aplicación ICaja</br>
39.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
40.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
41.-Hacer clic en Botón "FINALIZAR"</br>
42.-Visualizar la impresión del ticket</br>
43.-Hacer clic en el recuadro Hola, UIC10021</br>
44.-Hacer clic en CERRAR SESIÓN</br>    
 "  . 
    """
)



class SUC_T868(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T868(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_pago_de_jubilaciones_italianas()
            self.seleccionar_item_nro_de_pension()
            self.ingresar_nro_pension("450068628800004")
            self.seleccionarSiguiente()
            self.visualizar_datos_pension()
            self.visualizar_campo_pagos_pendientes()
            self.seleccionar_pago_pendiete_2()
            self.seleccionarSiguiente2()
            self.visualizar_datos_pension2()
            self.seleccionar_item_beneficiario()
            self.visualizar_datos_de_la_pantalla()
            self.mostrar_tipos_documento()
            self.seleccionarTipoDoc("CUIL")  
            self.ingresar_nro_doc("27262823623")
            self.seleccionarSiguiente3ros()
            self.visualizar_datos_de_comfirmacion()  
            self.seleccionar_siguiente_4() 
            self.wait(10)
            self.verificar_numero_de_transaccion()
            self.verificarMensajeExitoExtracciones(self.mensaje)  
            self.seleccionarRevesoDeTrasaccion()
            self.ingresarNroTranssaccion(self.NumeroTrans)
            self.mostrarTiposDeMotivos()
            self.seleccionarMotivo("Error Carga Cajero")
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizarOperacionPg()
            self.seleccionarAceptarAutoriz()
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
