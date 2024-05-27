# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL,CLAVE,\
              MONEDA, MSJ_ESPERADO,SUCURSAL_DEST,SUCURSAL_ORIG,\
              OPERACION1,OPERACION2,\
              MONEDA1,MONEDA2,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,\
              OPERACION_VALIDAR1,OPERACION_VALIDAR2,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
 



@allure.feature(u'Pagos')
@allure.story(u'Pago de Jubilaciones Italianas')
@allure.testcase(u"ICaja - SUC-T869 - Pago de Jubilaciones Italianas - Tipo y Número de Documento") 
@allure.title(u'SUC-T869 - Pago de Jubilaciones Italianas Tipo y Número de Documento')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción"Pago de Jubilaciones Italianas"</br>
6.-Seleccionar el Item "Tipo y Número de Documento"</br>
7.-Hacer clic en Tipo de documento y seleccionar "LC"</br>
8.-Ingesar Numero de Pension "3587736"</br>
9.-Hacer clic en el boton "BUSCAR PENSIÓN"</br>
10.-Seleccionar el item "Nro. de Pensión"</br>
11.-Hacer clic en "SIGUIENTE"</br>
12.-Visualizar los datos de la pension.</br>
13.-Visualizar el campo "PAGOS PENDIENTES"</br>
14.-Seleccionar un pago pendiente.</br>
15.-Hacer clic en "SIGUIENTE"</br>
16.-Visualizar los datos de la Pensión</br>
17.-Seleccionar el item "Beneficiario"</br>
18.-Visualizar los datos que aparece en pantalla.</br>
19.-Seleccionar el item "Debe presentar CUIT/CUIL/CDI del Beneficiario"</br>
20.-Seleccionar el campo Tipo de documento y seleccionar "CUIL"</br>
21.- Ingresar Numero de documento "27933471220"</br>
22.-Hacer clic en "SIGUIENTE"</br>
23.-Visualizar los datos de la Transaccion</br>
24.-Hacer clic en el botón "SIGUIENTE"</br>
25.-Visualizar el ticket DDJJ</br>
26.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
27.-Hacer clic en Botón "FINALIZAR"</br>
28.-Visualizar la impresión del ticket</br>
29.-Hacer clic en la Transacción - "Reverso de Transacción"</br>
30.-En el ticket visualizar el numero de Tx e ingresarla en el campo Numero de secuencia</br>
31.-Visualizar los datos de la Transacción</br>
32.-Hacer clic en el recuadro "Motivo" y seleccionar "Error Carga Cajero"</br>
33.-Marcar el check "El cliente presente ticket"</br>
34.-Hacer clic en el Botón "CONFIRMAR"</br>
35.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
36.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
37.-Visualizar la autorización en estado pendiente</br>
38.-Hacer clic en el botón ACEPTAR</br>
39.-Hacer clic en el botón AUTORIZAR</br>
40.-Hacer clic en el botón Salir</br>
41.-Volver al aplicación ICaja</br>
42.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
43.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
44.-Hacer clic en Botón "FINALIZAR"</br>
45.-Visualizar la impresión del ticket</br>
46.-Hacer clic en el recuadro Hola, UIC10021</br>
47.-Hacer clic en CERRAR SESIÓN</br>    
 "  . 
    """
)

class SUC_T869 (unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T869(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_pago_de_jubilaciones_italianas()
            self.seleccionar_item_tipo_doc()
            self.mostrar_tipos_documento()
            self.seleccionarTipoDoc("DNI")  
            self.ingresar_nro_doc("50000122")
            self.seleccionar_buscar_pension()
            self.seleccionar_nro_pension()
            self.seleccionarSiguiente()
            self.visualizar_datos_pension_2()
            self.visualizar_campo_pagos_pendientes()
            self.seleccionar_pago_pendiete()
            self.seleccionarSiguiente2()
            self.visualizar_datos_pension_3()
            self.seleccionar_item_beneficiario()
            self.visualizar_datos_de_la_pantalla()
            self.mostrar_tipo_doc_2()
            self.seleccionarTipoDoc("CUIL")  
            self.ingresar_nro_doc_2("27262823623")
            self.seleccionarSiguiente3ros()
            self.visualizar_datos_de_comfirmacion_2()
            self.seleccionar_siguiente_4()        
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
