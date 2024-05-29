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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE1, MSJ_ESPERADO,CUENTA1,CUENTA2,CUENTA3,CUENTA4,CUENTA5,\
              DOCUMENTO1,DOCUMENTO2,DOCUMENTO3,DOCUMENTO4,DOCUMENTO5,\
              INDENTIFICADOR1,INDENTIFICADOR2,INDENTIFICADOR3,INDENTIFICADOR4,INDENTIFICADOR5,\
              NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,NOMBRE_APELLIDO3,NOMBRE_APELLIDO4,NOMBRE_APELLIDO5,\
              USER_AUTO,TERMINAL_AUTO,PASSWORD_AUTO



@allure.feature(u'Depósitos')
@allure.story(u'Depósito a Terceros')
@allure.testcase(u"ICaja - SUC-T839 -Depósito en efectivo de 3° Superior a $ 280,000 - Por Raiz")
@allure.title(u'SUC-T839 - Depósito en efectivo de 3° Superior a $ 280,000')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Depósito a Terceros</br>
6.-Seleccionar "Raiz"</br>
7-Ingresar Raiz: AAABSP</br>
8-Hacer clic en el Boton SIGUIENTE</br>
9-Hacer clic en el recuadro Importe a depositar e Ingresar importe: 290.000,00</br>
10-Hacer clic en el Boton SIGUIENTE</br>
11-Validar los datos de la Cuenta</br>
12-Visualizar el recuadro Datos Depositante</br>
13-Hacer clic en Tipo documento y seleccionar DNI</br>
14-Hacer clic en Nro. Documento ingresar numero de documento: 24854132</br>
15-Hacer clic en el Botón SIGUIENTE</br>
16-Validar los datos del depositante</br>
17-Visualizar el recuadro Datos Ordenante</br>
18-Seleccionar la opción Es depositante</br>
19-Validar los datos del Ordenate</br>
20-Hacer clic en el Botón SIGUIENTE</br>
21.-Validar el detalle de la Operación: Cuenta / Moneda / Importe</br>
22.-Hacer clic en el Botón "CONFIRMAR"</br>
23.-Visualizar el Mensaje - "La finalizo correctamente"</br>
23.-Visualizar el Mensaje - "Impresión finalizada con exito"</br>
24.-Visualizar la impresión del ticket</br>
25.-Realizar una Extracción</br>
26.-Hacer clic en el recuadro Hola, UIC10021</br>
27.-Hacer clic en CERRAR SESIÓN</br>          
 </br> 
    """
)
class SUC_T839(unittest.TestCase, stICajaInicio, stICaja,stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T839(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarDepositoTerceros()
            self.seleccionarTiposDeDocumentos(self.tipoDoc4) 
            self.ingresarDatosDeCuentas("raiz",self.Raiz)
            self.seleccionarSiguiente()
            self.mostrarCuentas()
            self.seleccionarCuentaCliente("CA")                         
            self.ingresarImporteDepo3ros(self.importe)
            self.seleccionarSiguiente2()
            self.validarDatosCuenta(self.cuenta4)
            self.validarNombreDelTitular(self.nombreCliente4)
            self.mostrarTiposDoc2()
            self.seleccionarTipoDoc2(self.tipoDoc)
            self.ingresarNroDocDepositante(self.documento)
            self.seleccionarSiguiente3ros()
            self.clickRadioBtn2("Es depositante")
            self.seleccionarSiguiente3ros()
            self.validarDetalleDeOperacion(self.cuenta4,"pesos",self.importe)
            self.seleccionarConfirmar()
            self.verificarMensajeExitoDeposito2("La operacion se realizo con exito.")
            self.seleccionarAceptarComun()
            self.verificar_Numero_de_transaccion_terceros()
            self.ventana_saldo_excedido_en_caja_o_caf() 
            self.reverso(self.NumeroTrans)       
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
        self.documento = self.usuario.get(NRO_DOC_CLIENTE)
        self.tipoDoc1 = self.usuario.get(INDENTIFICADOR1)
        self.tipoDoc2 = self.usuario.get(INDENTIFICADOR2)
        self.tipoDoc3 = self.usuario.get(INDENTIFICADOR3)
        self.tipoDoc4 = self.usuario.get(INDENTIFICADOR4)
        self.tipoDoc5 = self.usuario.get(INDENTIFICADOR5)
        self.Nro_cuenta =  self.usuario.get(DOCUMENTO1)
        self.DNI =  self.usuario.get(DOCUMENTO2)
        self.CBU =  self.usuario.get(DOCUMENTO3)
        self.Raiz =  self.usuario.get(DOCUMENTO4)
        self.Alias =  self.usuario.get(DOCUMENTO5)
        self.cuenta1 = self.usuario.get(CUENTA1)
        self.cuenta2 = self.usuario.get(CUENTA2)
        self.cuenta3 = self.usuario.get(CUENTA3)
        self.cuenta4 = self.usuario.get(CUENTA4)
        self.cuenta5 = self.usuario.get(CUENTA5)
        self.nombreCliente1 = self.usuario.get(NOMBRE_APELLIDO1)
        self.nombreCliente2 = self.usuario.get(NOMBRE_APELLIDO2)
        self.nombreCliente3 = self.usuario.get(NOMBRE_APELLIDO3)
        self.nombreCliente4 = self.usuario.get(NOMBRE_APELLIDO4)
        self.nombreCliente5 = self.usuario.get(NOMBRE_APELLIDO5)

        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE1)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL) 
        
    

                
                
               
  
if __name__ == "__main__":
    unittest.main()
