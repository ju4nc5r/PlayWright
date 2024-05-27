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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, \
              IMPORTE, MSJ_ESPERADO,CUENTA1,MONEDA1,\
              IMPORTE1,CUENTA_VALIDAR1,\
              IMPORTE_VALIDAR_1,NOMBRE_APELLIDO1,\
              DOCUMENTO1,INDENTIFICADOR1,\
              OPERACION1,CBU_DESTINATARIO1,CUIT_CUIL1,OPERACION3
             

@allure.feature(u'Transferencias')
@allure.story(u'Transferencias a Otro Bancos')
@allure.testcase(u"ICaja - SUC-T848 - Transferencias a Otro Bancos - Por CBU")
@allure.title(u'SUC-T848 - Transferencias a Otro Bancos')
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
15.-Tildar la opción "CBU"</br>
16.-Agregar la cuenta crédito "CBU - 1500000800000110388878"</br>
17.-Hacer clic en el recuadro "Concepto" y seleccionar "Varios"</br>
18.-Hacer clic en el recuadro "Referencia" y agregar "Pagos"</br>
19.-Hacer clic en el recuadro "Importe" e ingresar "1000"</br>
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
class SUC_T848(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
        
    def test_SUC_T848(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()    
            self.seleccionarTrasferenciaAOtrosBancos()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente2(self.cuenta1)
            self.clickRadioBtn3(self.idenificandor1)
            self.ingresarCuenta2(self.documento1, "Credito")
            self.mostrarTiposDeOperecion(self.operacion1)
            self.ingresarReferencia(self.operacion1)
            self.ingresarImporte(self.importe1,self.moneda1)
            self.wait(1)
            self.seleccionarSiguiente4()
            self.wait(1)
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente()
            self.validar_cuenta_debito(self.cuenta1)
            self.validar_cbu_destinatario(self.cbuDestinatario1)
            self.validar_cuit_cuil(self.cuit_cuil1)
            self.validar_concepto(self.operacion1)
            self.validar_referencia(self.operacion1)
            self.validar_nombre(self.nombreYApellido1)
            self.validar_importe_total_a_liberar(self.importeValidar1)
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
        self.idenificandor1 = self.usuario.get(INDENTIFICADOR1)
        self.documento1 = self.usuario.get(DOCUMENTO1)
        self.operacion1 = self.usuario.get(OPERACION1)
        self.operacion3 = self.usuario.get(OPERACION3)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.nombreYApellido1 = self.usuario.get(NOMBRE_APELLIDO1)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.cuentaValidar1 = self.usuario.get(CUENTA_VALIDAR1)
        self.cbuDestinatario1 = self.usuario.get(CBU_DESTINATARIO1)                                           
        self.cuit_cuil1 = self.usuario.get(CUIT_CUIL1)                                     

# self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
