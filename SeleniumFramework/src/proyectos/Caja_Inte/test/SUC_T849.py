# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
import time
# from SeleniumFramework.src.proyectos.Caja_Inte.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, \
              IMPORTE, MSJ_ESPERADO,CUENTA1,CUENTA2,CUENTA3,MONEDA1,MONEDA2,MONEDA3,\
              IMPORTE1,IMPORTE2,IMPORTE3,CUENTA_VALIDAR1,CUENTA_VALIDAR2,CUENTA_VALIDAR3,\
              IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,IMPORTE_VALIDAR_3,NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,NOMBRE_APELLIDO3,\
              DOCUMENTO1,DOCUMENTO2,DOCUMENTO3,INDENTIFICADOR1,INDENTIFICADOR2,INDENTIFICADOR3,\
              OPERACION1,OPERACION2,OPERACION3,CBU_DESTINATARIO1,CBU_DESTINATARIO2,CUIT_CUIL1,CUIT_CUIL2
             

@allure.feature(u'Transferencias')
@allure.story(u'Transferencias a Otro Bancos')
@allure.testcase(u"ICaja - SUC-T849 - Transferencias a Otro Bancos - Por Alias")
@allure.title(u'SUC-T849 - Transferencias a Otro Bancos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Transferencias a Otro Bancos</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "25227274"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón SIN CLAVE</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Débito"</br>
14.-Seleccionar cuenta "CC $ 0444583-100/3</br>
15.-Tildar la opción "Alias"</br>
16.-Agregar la cuenta crédito "Alias - PRUEBAS1"</br>
17.-Hacer clic en el recuadro "Concepto" y seleccionar "Alquiler"</br>
18.-Hacer clic en el recuadro "Referencia" y agregar "Alquiler"</br>
19.-Hacer clic en el recuadro "Importe" e ingresar "10000"</br>
20.-Hacer clic en "SIGUIENTE"</br>
21.-Marcar el check si coincide la firma y hacer clic en el Botón "SIGUIENTE"</br>
22.-Visualizar los datos de la Transacción</br>
23.-Hacer clic en el Botón "CONFIRMAR"</br>
24.-Visualizar el mensaje "Operación realizada con éxito"</br>
25.-Hacer clic en el boton "FINALIZAR"</br>
26.-Visualizar la impresión del ticket</br>
27.-Hacer clic en el recuadro Hola, UIC10021</br>
28.-Hacer clic en CERRAR SESIÓN </br>
"""
)
class SUC_T849(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
        
    def test_SUC_T849(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()    
            self.seleccionarTrasferenciaAOtrosBancos()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente2(self.cuenta2)
            self.clickRadioBtn3(self.idenificandor2)
            self.ingresarCuenta2(self.documento2, "Credito")
            self.mostrarTiposDeOperecion(self.operacion2)
            self.ingresarReferencia(self.operacion2)
            self.ingresarImporte(self.importe2,self.moneda1)
            self.wait(1)
            self.seleccionarSiguiente4()
            self.wait(1) 
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente()
            self.validar_cuenta_debito(self.cuenta2)
            self.validar_cbu_destinatario(self.cbuDestinatario2)
            self.validar_cuit_cuil(self.cuit_cuil2)
            self.validar_concepto(self.operacion2)
            self.validar_referencia(self.operacion2)
            self.validar_nombre(self.nombreYApellido2)
            self.validar_importe_total_a_liberar(self.importeValidar2)
            self.validar_moneda(self.moneda1)                
            self.seleccionarConfirmar()
            self.verificarMensajeExitoExtracciones(self.mensaje)  
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
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.cuenta1 = self.usuario.get(CUENTA1)
        self.cuenta2 = self.usuario.get(CUENTA2)
        self.cuenta3 = self.usuario.get(CUENTA3)
        self.idenificandor1 = self.usuario.get(INDENTIFICADOR1)
        self.idenificandor2 = self.usuario.get(INDENTIFICADOR2)
        self.idenificandor3 = self.usuario.get(INDENTIFICADOR3)
        self.documento1 = self.usuario.get(DOCUMENTO1)
        self.documento2 = self.usuario.get(DOCUMENTO2)
        self.documento3 = self.usuario.get(DOCUMENTO3)
        self.operacion1 = self.usuario.get(OPERACION1)
        self.operacion2 = self.usuario.get(OPERACION2)
        self.operacion3 = self.usuario.get(OPERACION3)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importe3 = self.usuario.get(IMPORTE3)
        self.nombreYApellido1 = self.usuario.get(NOMBRE_APELLIDO1)
        self.nombreYApellido2 = self.usuario.get(NOMBRE_APELLIDO2)
        self.nombreYApellido3 = self.usuario.get(NOMBRE_APELLIDO3)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importeValidar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.importeValidar3 = self.usuario.get(IMPORTE_VALIDAR_3)
        self.cuentaValidar1 = self.usuario.get(CUENTA_VALIDAR1)
        self.cuentaValidar2 = self.usuario.get(CUENTA_VALIDAR2)
        self.cuentaValidar3 = self.usuario.get(CUENTA_VALIDAR3)
        self.cbuDestinatario1 = self.usuario.get(CBU_DESTINATARIO1)                                           
        self.cbuDestinatario2 = self.usuario.get(CBU_DESTINATARIO2) 
        self.cuit_cuil1 = self.usuario.get(CUIT_CUIL1)                                     
        self.cuit_cuil2 = self.usuario.get(CUIT_CUIL2)                                     

# self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
