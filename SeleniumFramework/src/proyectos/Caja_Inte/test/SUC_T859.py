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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE1, MSJ_ESPERADO,CUENTA1,CUENTA2,CUENTA3,CUENTA4,CUENTA5,\
              DOCUMENTO1,DOCUMENTO2,DOCUMENTO3,DOCUMENTO4,DOCUMENTO5,\
              INDENTIFICADOR1,INDENTIFICADOR2,INDENTIFICADOR3,INDENTIFICADOR4,INDENTIFICADOR5
              



@allure.feature(u'Depósitos')
@allure.story(u'Depósito a Terceros')
@allure.testcase(u'SUC-T859 Depósito en efectivo de 3° inferior a $ 280,000')
@allure.title(u'SUC-T859 - Depósito a Terceros - Inferior a $ 280,000 - Por Documento')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Depósito a Terceros</br>
6.-Seleccionar "CBU"</br>
7.-Ingresar CBU: CC$ 2590002810000007210012</br>
8-Hacer clic en el Boton SIGUIENTE</br>
9-Hacer clic en el recuadro Importe a depositar e Ingresar importe: 10.000,00</br>
10-Hacer clic en el Boton SIGUIENTE</br>
11-Validar los datos de la Cuenta</br>
12.-Hacer clic en el Botón "CONFIRMAR"</br>
13.-Visualizar el Mensaje - "La finalizo correctamente"</br>
14.-Visualizar el Mensaje - "Impresión finalizada con exito"</br>
15.-Visualizar la impresión del ticket</br>
16.-Realizar una Extracción</br>
17.-Hacer clic en el recuadro Hola, UIC10021</br>
18.-Hacer clic en CERRAR SESIÓN </br>          
 </br> 
    """
)
class SUC_T859(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T859(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()   
            self.seleccionarDepositoTerceros()
            self.seleccionarTiposDeDocumentos(self.tipoDoc2)
            self.mostrarTiposDoc()
            self.seleccionarTipoDoc("DNI") 
            self.ingresarDatosDeCuentas("numeroDocumento",self.DNI)
            self.seleccionarSiguiente()            
            self.mostrarCuentas2()
            self.seleccionarCuentaCliente("CA")
            self.ingresarImporteDepo3ros(self.importe)
            self.seleccionarSiguiente2()
            self.visualizarDatosDeposito3ros2(self.importe,self.cuenta2,"pesos")
            self.seleccionarConfirmar()
            self.verificarMensajeExitoDeposito2("La operacion se realizo con exito.")
            self.seleccionarAceptarComun()                  
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE1)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL) 
        

                
                
               
  
if __name__ == "__main__":
    unittest.main()
