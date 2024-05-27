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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE,\
              IMPORTE, MSJ_ESPERADO,CUENTA2,MONEDA2,\
              IMPORTE2,CUENTA_VALIDAR2,\
              IMPORTE_VALIDAR_2,NOMBRE_APELLIDO2,\
              DOCUMENTO2,INDENTIFICADOR2,\
              OPERACION2
             

@allure.feature(u'Transferencias')
@allure.story(u'Transferencias entre Cuentas Itaú')
@allure.testcase(u"ICaja - SUC-T846  -Transferencia a Otro Cliente Itaú - Por CBU")
@allure.title(u'SUC-T846 - Transferencia a otro cliente Itaú')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Transferencias a Otro Clientes</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "25227274"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Boton SIN CLAVE</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Débito"</br>
14.-Seleccionar cuenta "CA $ 0444583-301/7"</br>
15.-Tildar la opcion "CBU"</br>
16.-Agregar la cuenta credito "CBU - 2590002820000007230158"</br>
17.-Hacer clic en el recuadro "Concepto" y seleccionar "Expensas"</br>
18.-Hacer clic en el recuadro "Importe" e ingresar "5000"</br>
19.-Hacer clic en "SIGUIENTE"</br>
20.-Marcar el check si coincide la firma y hacer clic en el boton "SIGUIENTE"</br>
21.-Visualizar los datos de la Transaccion</br>
22.-Hacerer clic en el boton "CONFIRMAR"</br>
23.-Visualizar la impresion del ticket</br>
24.-Visualizar el mensaje "Operación realizada con éxito"</br>
25.-Hacer clic en boton "FINALIZAR"</br>
26.-Hacer clic en el recuadro Hola, UIC10021</br>
27.-Hacer clic en CERRAR SESIÓN</br>
"""
)
class SUC_T846 (unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
        
    def test_SUC_T846(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()             
            self.seleccionarTrasferenciaAOtroCliente()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente2(self.cuenta2)
            self.clickRadioBtn3(self.idenificandor2)
            self.ingresarCuenta2(self.documento2, "Credito")
            self.mostrarTiposDeOperecion(self.operacion2)
            self.ingresarImporte(self.importe2,self.moneda2)
            self.wait(1)
            self.seleccionarSiguiente4()
            self.wait(2)
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente()
            self.validar_cuenta_debito(self.cuenta2)
            self.validar_cuenta_credito(self.cuentaValidar2)
            self.validar_nombre(self.nombreYApellido2)
            self.validar_concepto(self.operacion2)
            self.validar_moneda(self.moneda2)
            self.validar_importe_total_a_liberar(self.importeValidar2)
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
        self.cuenta2 = self.usuario.get(CUENTA2)
        self.idenificandor2 = self.usuario.get(INDENTIFICADOR2)
        self.documento2 = self.usuario.get(DOCUMENTO2)
        self.operacion2 = self.usuario.get(OPERACION2)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.nombreYApellido2 = self.usuario.get(NOMBRE_APELLIDO2)
        self.importeValidar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.cuentaValidar2 = self.usuario.get(CUENTA_VALIDAR2)
     

# self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
