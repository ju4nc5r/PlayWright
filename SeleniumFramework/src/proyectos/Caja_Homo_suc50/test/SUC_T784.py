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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO,OPERACION1,NUMERO_ATM,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,SUCURSAL_DEST
             

@allure.feature(u'ATM')
@allure.story(u'ATM Liberaciones')
@allure.testcase(u"ICaja - SUC-T784 - ATM Liberaciones")
@allure.title(u'SUC-T784 - ATM Liberaciones')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja "https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login"</br>
2.-Realizar login e ingresar los datos del operador:</br>
Legajo: UIC10021 / Terminal: IA0500821 / Contraseña: Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021"</br>
5.-Visualizar los datos del operador UIC10021:</br>
Legajo: UIC10021 / Terminal: IA0500821 / Sucursal: 0050</br>
6.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
7.-Hacer clic en la Transaccion - "ATM Liberaciones"</br>
8.-Validar Número de Sucursal "46"</br>
9.-Hacer clic en Transaccion</br>
10.-Seleccionar el item "Deposito Efectivo"</br>
11.-Hacer clic en "Numero de ATM"</br>
12.-Seleccionar el item "S1GIB078"</br>
13.-Validar moneda "Pesos"</br>
14.-Ingresar importe Total a Liberar "1.500"</br>
15.-Hacer clic en "SIGUIENTE"</br>
16.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
17.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
18.-Hacer clic en boton "FINALIZAR"</br>
19.-Visualizar la impresion del ticket</br> 
""")

class SUC_T784(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
                   
    def test_SUC_T784(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarATMLiveraciones()
            self.mostrarYSeleccionarTipoDeTransaccion(self.operacion)
            self.wait(4)
            self.mostrarYSeleccionarNroAtm(self.numeroATM)
            self.ingresarImporte(self.importe,self.tipoMoneda)
            self.ingresarImporte3(self.importe,self.tipoMoneda)
            self.seleccionarSiguiente()         
            self.validar_importe(self.importe_Validar1)
            self.validar_importe_total(self.importe_Validar2)
            self.validar_moneda(self.tipoMoneda)
            self.validar_numero_atm(self.numeroATM)
            self.validar_operacion(self.operacion)
            self.validar_sucursal(self.sucursal)
            self.seleccionarConfirmar() 
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.operacion = self.usuario.get(OPERACION1)
        self.numeroATM = self.usuario.get(NUMERO_ATM)
        self.sucursal = self.usuario.get(SUCURSAL_DEST)
        self.importe_Validar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importe_Validar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
    # self.mensaje = "La operacion finalizo correctamente"
        
        
    
        

if __name__ == "__main__":
    unittest.main()