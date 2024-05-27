# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE,\
              IMPORTE, MSJ_ESPERADO,CUENTA3,MONEDA3,\
              IMPORTE3,CUENTA_VALIDAR3,\
              IMPORTE_VALIDAR_3,NOMBRE_APELLIDO3,\
              DOCUMENTO3,INDENTIFICADOR3,\
              OPERACION3
             

@allure.feature(u'Transferencias')
@allure.story(u'Transferencias entre Cuentas Itaú')
@allure.testcase(u"ICaja - SUC-T847 - Transferencia a Otro Cliente Itaú - Por Alias")
@allure.title(u'SUC-T847 - Transferencia a otro cliente Itaú')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
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
15.-Tildar la opcion "Alias"</br>
16.-Agregar la cuenta credito "Alias - BABY.TESTING.CC</br>
17.-Hacer clic en el recuadro "Concepto" y seleccionar "Expensas"</br>
18.-Hacer clic en el recuadro "Importe" e ingresar "7000"</br>
19.-Hacer clic en "SIGUIENTE"</br>
20.-Marcar el check si coincide la firma y hacer clic en el boton "SIGUIENTE"</br>
21.-Visualizar los datos de la Transaccion</br>
22.-Hacer clic en el boton "CONFIRMAR"</br>
23.-Visualizar la impresion del ticket</br>
24.-Visualizar el mensaje "Operación realizada con éxito"</br>
25.-Hacer clic en boton "FINALIZAR"</br>
26.-Hacer clic en el recuadro Hola, UIC10021</br>
27.-Hacer clic en CERRAR SESIÓN </br>
"""
)
class SUC_T847(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
        
    def test_SUC_T847(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()     
            self.seleccionarTrasferenciaAOtroCliente()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente2(self.cuenta3)
            self.clickRadioBtn3(self.idenificandor3)
            self.ingresarCuenta2(self.documento3, "Credito")
            self.mostrarTiposDeOperecion(self.operacion3)
            self.ingresarImporte(self.importe3,self.moneda3)
            self.wait(1)
            self.seleccionarSiguiente4()
            self.wait(2)
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente()           
            self.validar_cuenta_debito(self.cuenta3)
            self.validar_cuenta_credito(self.cuentaValidar3)
            self.validar_nombre(self.nombreYApellido3)
            self.validar_concepto(self.operacion3)
            self.validar_moneda(self.moneda3)
            self.validar_importe_total_a_liberar(self.importeValidar3)
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
        self.cuenta3 = self.usuario.get(CUENTA3)
        self.idenificandor3 = self.usuario.get(INDENTIFICADOR3)
        self.documento3 = self.usuario.get(DOCUMENTO3)
        self.operacion3 = self.usuario.get(OPERACION3)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.importe3 = self.usuario.get(IMPORTE3)
        self.nombreYApellido3 = self.usuario.get(NOMBRE_APELLIDO3)
        self.importeValidar3 = self.usuario.get(IMPORTE_VALIDAR_3)
        self.cuentaValidar3 = self.usuario.get(CUENTA_VALIDAR3)
     

# self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
