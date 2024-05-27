# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,MENSAJE_IMPRESION,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA,\
              USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
from asyncio.tasks import sleep
             

@allure.feature(u'Cobros')
@allure.story(u'Cobro de Servicios - SIRE')
@allure.testcase(u"SUC-T884 - Cobro servicios - SIRE - Debito en Cuenta")
@allure.title(u'SUC-T884 - Cobro servicios - SIRE - Debito en Cuenta')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""

1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la trassacicion Cobro servicios - SIRE</br>
6.-Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?</br>
7.-Hacer clic en el boton SI</br>
8.-Ingresar los datos del cliente</br>
9.-Seleccionar Tipo de Documento "DNI"</br>
10.-Ingresar Numero de Documento "16555772"</br>
11.-Hacer clic en el Botón "IDENTIFICAR"</br>
12.-Hacer clic en el Botón "SIN CLAVE"</br>
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
14.-Seleccionar forma de pago "Debito en Cuenta"</br>
15.-Seleccionar Forma de Pago Cuenta "CC $ - 0000178-100/4"</br>
16.-Hacer clic en el boton "SIGUIENTE"</br>
17.-Tipo de Servicio a Abonar "BARRA"</br>
18.-Seleccionar Servicio "EDESUR"</br>
19.-Ingresar Codigo de Barras "3041100630108324020200055422124003530102"</br>
20.-Hacer Enter</br>
21.-Visualizar pantalla con datos de del Servicio.</br>
22.-Hacer clic en el boton "CONFIRMAR"</br>
23.-Verificar firma (Marca Si)</br>
24.-Hacer clic en el boton "CONFIRMAR"</br>
25.-Visualizar el Mensaje - "Impresión finalizada con éxito "</br>
26.-Hacer el boton "FINALIZAR"</br>
27.-Visualizar la impresión del ticket</br>
28.-Hacer clic en la Transacción - "Reverso de Transacción"</br>
29.-En el ticket visualizar el numero de Tx e ingresarla en el campo Numero de secuencia</br>
30.-Visualizar los datos de la Transacción</br>
31.-Hacer clic en el recuadro "Motivo" y seleccionar "Error Carga Cajero"</br>
32.-Marcar el check "El cliente presente ticket"</br>
33.-Hacer clic en el Botón "CONFIRMAR</br>
34.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
35.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822 / Contraseña: Ingreso22</br>
36.-Visualizar la autorización en estado pendiente</br>
37.-Hacer clic en el botón ACEPTAR</br>
38.-Hacer clic en el botón AUTORIZAR</br>
39.-Hacer clic en el botón Salir</br>
40.-Volver al aplicación ICaja</br>
41.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
42.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
43.-Hacer clic en Botón "FINALIZAR"</br>
44.-Visualizar la impresión del ticket</br>
45.-Hacer clic en el recuadro Hola, UIC10021</br>   
46.-Hacer clic en CERRAR SESIÓN</br>   
</br>   
"""
)
class SUC_T884(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T884(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_cobros_sires()
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente()
            self.seleccionar_debito_en_cuenta()
            self.seleccionar_formas_de_pago()
            self.seleccionar_pago("CC $ - 0000178-100/4")
            self.seleccionarSiguiente4()
            self.seleccionar_barra()
            self.seleccionar_recuadro_servicios()
            self.seleccionar_servicio("AYSA S.A")
            self.ingresar_codigo_de_barra("3041100630108324020200055422124003530102")
            self.visualizar_datos_servicio()      
            self.seleccionar_Confirmar()
            self.seleccionar_check_marca_si_coincide()
            self.seleccionarConfirmar3()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")
            self.visualizarMensajeExito()
            self.verificar_Nro_servicios_2()
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.mensaje_impresion = self.usuario.get(MENSAJE_IMPRESION)
        self.importe = self.usuario.get(IMPORTE)
        self.dias = self.usuario.get(DIAS)
        self.moneda = self.usuario.get(MONEDA)
        

if __name__ == "__main__":
    unittest.main()
