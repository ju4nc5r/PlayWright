# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE,\
              MSJ_ESPERADO,CUENTA1,MONEDA1,IMPORTE1,CUENTA_VALIDAR1,IMPORTE_VALIDAR_1
             

@allure.feature(u'Depósitos')
@allure.story(u'Depósito de Cliente')
@allure.testcase(u"ICaja - SUC-T842 - Deposito de Cliente - Moneda Pesos")
@allure.title(u'SUC-T842 - Deposito en Efectivo - Moneda Pesos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Deposito en Efectivo</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
9.-Ingresar Numero de Documento "25227274"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón "SIN CLAVE"</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta Cliente"</br>
14.-Seleccionar cuenta "CA $"</br>
15.-Hacer clic en seleccionar Moneda a extraer "Pesos"</br>
16.-Ingresar importe "50.000"</br>
17.-Hacer clic en "SIGUIENTE"</br>
18.-Visualizar los datos de la tx</br>
19.-Hacer clic en el botón "CONFIRMAR"</br>
20.-Visualizar el Mensaje - "La operación se realizo con éxito. "</br>
21.-Hacer el boton "ACEPTAR"</br>
22.-Visualizar la impresión del ticket</br>
23.-Hacer clic en el recuadro Hola, UIC10021</br>
24.-Hacer clic en CERRAR SESIÓN</br>
</br>
    """
)
class SUC_T842(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T842(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarDepositoCliente()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente()
            self.seleccionarCuentaDeposito(self.cuenta1)
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.moneda1)
            self.ingresarImporte(self.importe1,self.moneda1)
            self.seleccionarSiguiente()
            parts = ["cuenta","importeADepositar"]
            datos = [self.cuentaValidar1,self.importeValidar1]
            for part,dato in zip (parts,datos):
                self.validarDatosDepositos(part,dato)
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
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta1 = self.usuario.get(CUENTA1)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.cuentaValidar1 = self.usuario.get(CUENTA_VALIDAR1)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
     

       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
