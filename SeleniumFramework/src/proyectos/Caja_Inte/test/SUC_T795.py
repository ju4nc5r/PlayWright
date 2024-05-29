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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,OPERACION1,OPERACION2,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,COMISION,CUENTA1,IMPORTE_VALIDAR_1,\
              MONEDA, IMPORTE, MSJ_ESPERADO,MONEDA1,CANTIDAD_DE_CHEQUES,SUB_TOTAL_DE_MULTAS,SUB_TOTAL_DE_CHEQUES,\
              USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
             

@allure.feature(u'Cobros')
@allure.story(u'Cobros de Multa')
@allure.testcase(u'ICaja - SUC-T795 - Cobro de Multas')
@allure.title(u'SUC-T795 - Cobro de Multas')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(  
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0460809 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Cobro Multas"</br>
7.-Ingresar Cuenta Corriente "01002831004"</br>
8.-Hacer clic en el Botón "SIGUIENTE"</br>
9.-Visualizar la cuenta de cliente y multas pendientes</br>
10.-Marcar el check para seleccionar la Multa</br>
11.-Hacer clic en el Botón "SIGUIENTE"</br>
12.-Visualizar los datos de la Transacción y hacer clic en el boton "CONFIRMAR"</br>
13.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el Botón "FINALIZAR"</br>
14.-Visualizar la impresión del ticket</br>
15.-Hacer clic en la Transacción - "Reverso de Transacción"</br>
16.-En el ticket visualizar el numero de Tx copiarla e ingresarla en el campo Numero de secuencia</br>
17.-Visualizar los datos de la Transacción</br>
18.-Hacer clic en el recuadro y seleccionar "Otros motivos"</br>
19.-Marcar el check "El cliente presente ticket"
20.-Hacer clic en el Botón "CONFIRMAR"</br>
21.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
22.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
23.-Visualizar la autorización en estado pendiente</br>
24.-Hacer clic en el botón ACEPTAR</br>
25.-Hacer clic en el botón AUTORIZAR</br>
26.-Hacer clic en el botón Salir</br>
27.-Volver al aplicación ICaja</br>
28.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
29.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
30.-Hacer clic en Botón "FINALIZAR"</br>
31.-Visualizar la impresión del ticket</br>
32.-Hacer clic en la Transacción - "Cobro Multas"</br>
33.-Ingresar Con Documento: DNI: 18742821</br>
34.-Hacer clic en Buscar Cuentas</br>
35.-Seleccionar la cuenta con multas impagas</br>
36.-Hacer clic en el Botón "SIGUIENTE"</br>
37.-Visualizar la cuenta de cliente y multas pendientes</br>
38.-Marcar el check para seleccionar la Multa</br>
39.-Hacer clic en el Botón "SIGUIENTE"</br>
40.-Visualizar los datos de la Transacción y hacer clic en el boton "CONFIRMAR"</br>
41.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el Botón "FINALIZAR"</br>
42.-Visualizar la impresión del ticket</br>
43.-Hacer clic en la Transacción - "Reverso de Transacción"</br>
44.-En el ticket visualizar el numero de Tx copiarla e ingresarla en el campo Numero de secuencia</br>
45.-Visualizar los datos de la Transacción</br>
46.-Hacer clic en el recuadro y seleccionar "Otros motivos"</br>
47.-Marcar el check "El cliente presente ticket"</br>
48.-Hacer clic en el Botón "CONFIRMAR"</br>
49.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br>
50.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10022 / Terminal: IA0500822   / Contraseña: Ingreso22</br>
51.-Visualizar la autorización en estado pendiente
52.-Hacer clic en el botón ACEPTAR</br>
53.-Hacer clic en el botón AUTORIZAR</br>
54.-Hacer clic en el botón Salir</br>
55.-Volver al aplicación ICaja</br>
56.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br>
57.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
58.-Hacer clic en Botón "FINALIZAR"</br>
59.-Visualizar la impresión del ticket</br>
60.-Hacer clic en el recuadro Hola, UIC10021</br>
61.-Hacer clic en CERRAR SESIÓN</br>
"""
)
class SUC_T795(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T795(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarCobroDeMultas()
            self.clickRadioBtn(self.operacion1)
            self.ingresar_cuenta3("01002831004")
            self.seleccionarSiguiente()
            self.msg_NohayMultasInpagas()
            self.seleccionarCheckMulta()
            datos = [self.cantidadDeCheques,"50,00",self.tipoMoneda,"15,00","1.150,00","65,00"]
            texto = ["Cantidad de Cheques: ","Subtotal de Multas: ","Moneda: ","Comisión: ","Subtotal de Cheques: ","Importe Total a cobrar"]                                       
            self.frecuencia = []
            for dato,text in zip(datos,texto):
                self.frecuencia.append(dato)                
                self.validarDatos(dato,text)
            print(self.frecuencia)
            self.seleccionarSiguiente2()
            self.validarCantidadDeCheques2("1")
            self.validarMoneda2(self.tipoMoneda)
            self.validarImporteTotalACobrar("65,00") 
            self.seleccionarConfirmar() 
            self.verificarMensajeExitoExtracciones(self.mensaje)
            self.verificarNumeroDeTransaccionCobrosDeMulta()
            self.seleccionarRevesoDeTrasaccion()
            self.ingresarNroTranssaccion(self.NumeroTrans)
            self.mostrarTiposDeMotivos()
            self.seleccionarMotivo(self.operacion2)
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizarOperacionPg()
            self.seleccionarAceptarAutoriz()
            self.verificarMensajeExitoExtracciones(self.mensaje)
            self.wait(1)       
            self.seleccionarCobroDeMultas()
            self.clickRadioBtn("Con Documento")
            self.mostrarCuentas()
            self.seleccionarTipoDoc("DNI")
            self.ingresarNroDocTitular("18742821")
            self.seleccionar_buscar_cuentas()
            self.seleccionarCuenta("CC  $  0100283-100/4")
            self.seleccionarSiguiente()
            self.msg_NohayMultasInpagas()
            self.seleccionarCheckMulta()
            datos = [self.cantidadDeCheques,"50,00",self.tipoMoneda,"15,00","1.150,00","65,00"]
            texto = ["Cantidad de Cheques: ","Subtotal de Multas: ","Moneda: ","Comisión: ","Subtotal de Cheques: ","Importe Total a cobrar"]                                       
            self.frecuencia = []
            for dato,text in zip(datos,texto):
                self.frecuencia.append(dato)                
                self.validarDatos(dato,text)
            print(self.frecuencia)
            self.seleccionarSiguiente2()
            self.validarCantidadDeCheques2("1")
            self.validarMoneda2(self.tipoMoneda)
            self.validarImporteTotalACobrar("65,00") 
            self.seleccionarConfirmar() 
            self.verificarMensajeExitoExtracciones(self.mensaje)
            self.verificarNumeroDeTransaccionCobrosDeMulta()
            self.seleccionarRevesoDeTrasaccion()
            self.ingresarNroTranssaccion(self.NumeroTrans)
            self.mostrarTiposDeMotivos()
            self.seleccionarMotivo(self.operacion2)
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizarOperacionPg()
            self.seleccionarAceptarAutoriz()
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA1)
        self.tipoMoneda = self.usuario.get(MONEDA1)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.cantidadDeCheques = self.usuario.get(CANTIDAD_DE_CHEQUES)
        self.subTotalDeMultas = self.usuario.get(SUB_TOTAL_DE_MULTAS)
        self.subTotalDeCheques = self.usuario.get(SUB_TOTAL_DE_CHEQUES)
        self.comision = self.usuario.get(COMISION)
        self.importe_validar = self.usuario.get(IMPORTE_VALIDAR_1)
        self.operacion1 = self.usuario.get(OPERACION1)
        self.operacion2 = self.usuario.get(OPERACION2)
        
    # self.mensaje = "La operacion finalizo correctamente"
        
        
    
        

if __name__ == "__main__":
    unittest.main()