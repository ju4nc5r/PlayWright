# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, CUENTA_ACRED,IMPORTE_VALIDAR_1,USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
             

@allure.feature(u'Operaciones de Caja')
@allure.story(u'Reverso de Transacción')
@allure.testcase(u"SUC-T834 - Reverso de Transacción - Deposito en Efectivo")
@allure.title(u'SUC-T834 - Reverso de Transacción - Deposito en Efectivo')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar el nombre en el recuadro "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Deposito en Efectivo</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "25227274"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón SIN CLAVE</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Cliente"</br>
14.-Seleccionar cuenta "CA $"</br>
15.-Hacer clic en seleccionar Moneda a extraer "Pesos"</br>
16.-Ingresar importe "20.000,00"</br>
17.-Hacer clic en "SIGUIENTE"</br>
18.-Marcar el check si coincide la firma y hacer clic en el Botón "SIGUIENTE"</br>
19.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
20.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
21.-Visualizar la impresión del ticket</br>
22.-Hacer clic en la Transacción - "Reverso de Transacción"</br>
23.-En el ticket visualizar el numero de Tx e ingresarla en el campo Numero de secuencia</br>
24.-Visualizar los datos de la Transacción</br>
25.-Hacer clic en el recuadro y seleccionar "Error Carga Cajero"</br>
26.-Marcar el check "El cliente presente ticket"</br>
27.-Hacer clic en el Botón "CONFIRMAR"</br>
28.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
29.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
30.-Visualizar la autorización en estado pendiente</br>
31.-Hacer clic en el botón ACEPTAR</br>
32.-Hacer clic en el botón AUTORIZAR</br>
33.-Hacer clic en el botón Salir</br>
34.-Volver al aplicación ICaja</br>
35.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
36.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
37.-Hacer clic en Botón "FINALIZAR"</br>
38.-Visualizar la impresión del ticket</br>
39.-Hacer clic en el recuadro Hola, UIC10021</br>
40.-Hacer clic en CERRAR SESIÓN </br>
    """
)
class SUC_T834 (unittest.TestCase, stICajaInicio, stICaja, stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T834(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarDepositoCliente()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente()
            self.seleccionarCuentaDeposito(self.cuenta)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarImporte(self.importe,self.tipoMoneda)
            self.seleccionarSiguiente()
            parts = ["cuenta","importeADepositar"]
            datos = [self.cuentaDeposito,self.importeValidar]
            for part,dato in zip (parts,datos):
                self.validarDatosDepositos(part,dato)
            self.seleccionarConfirmar() 
            self.verificarMensajeExitoDeposito2("La operacion se realizo con exito.")
            self.seleccionarAceptarComun() 
            self.verificarNumeroDeTransaccion_2()
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.cuentaDeposito = self.usuario.get(CUENTA_ACRED)
        self.importeValidar = self.usuario.get(IMPORTE_VALIDAR_1)
     

       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
