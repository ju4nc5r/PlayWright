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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,NUMERO_ATM,\
              MONEDA, MSJ_ESPERADO,OPERACION1,OPERACION2,OPERACION3,OPERACION4,SUCURSAL,SUC_JOB,\
              IMPORTE,IMPORTE1,IMPORTE2,IMPORTE3,IMPORTE_A_VALIDAR,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,IMPORTE_VALIDAR_3
             

@allure.feature(u'ATM')
@allure.story(u'ATM Banelco')
@allure.testcase(u"ICaja - SUC-T783  - ATM Banelco")
@allure.title(u'SUC-T783 - ATM Banelco')
@allure.severity(allure.severity_level.NORMAL)
@allure.description( 
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br> 
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br> 
3.-Hacer clic en el botón "INGRESAR"</br> 
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br> 
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br> 
6.-Hacer clic en la Transacción - "ATM Banelco"</br> 
7.-Validar Número de Sucursal "0050"</br> 
8.-Hacer clic en el "Tipo de Operación"</br> 
9.-Seleccionar el ítem "Carga Atm"</br> 
10.-Hacer clic en "Numero de ATM"</br> 
11.-Seleccionar el ítem "S1GIB078"</br> 
12.-Hacer clic en seleccionar Moneda "Pesos"</br> 
13.-Ingresar importe "5000"</br> 
14.-Hacer clic en "SIGUIENTE"</br> 
15.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br> 
16.-Visualizar el Mensaje - "Operación realizada con éxito"</br> 
17.-Hacer clic en Botón "FINALIZAR"</br> 
18.-Visualizar la impresión del ticket</br> 
19.-Hacer clic en la Transacción - "ATM Banelco"</br> 
20.-Validar Número de Sucursal "0050"</br> 
21.-Hacer clic en el "Tipo de Operación"</br> 
22.-Seleccionar el ítem "Descarga Atm"</br> 
23.-Hacer clic en "Numero de ATM"</br> 
24.-Seleccionar el ítem "S1GIB078"</br> 
25.-Hacer clic en seleccionar Moneda "Pesos"</br> 
26.-Ingresar importe "5000"</br> 
27.-Hacer clic en "SIGUIENTE"</br> 
28.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br> 
29.-Visualizar el Mensaje - "Operación realizada con éxito"</br> 
30.-Hacer clic en Botón "FINALIZAR"</br> 
31.-Visualizar la impresión del ticket</br> 
32.-Hacer clic en la Transacción - "ATM Banelco"</br> 
33.-Validar Número de Sucursal "0050"</br> 
34.-Hacer clic en el "Tipo de Operación"</br> 
35.-Seleccionar el ítem "Incremento Atm"</br> 
36.-Hacer clic en "Numero de ATM"</br> 
37.-Seleccionar el ítem "S1GIB078"</br> 
38.-Hacer clic en seleccionar Moneda "Pesos"</br> 
39.-Ingresar importe "2.500"</br> 
40.-Hacer clic en "SIGUIENTE"</br> 
41.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br> 
42.-Visualizar el Mensaje - "Operación realizada con éxito"</br> 
43.-Hacer clic en Botón "FINALIZAR"</br> 
44.-Visualizar la impresión del ticketV</br> 
45.-Hacer clic en la Transacción - "ATM Banelco"</br> 
46.-Validar Número de Sucursal "0050"</br> 
47.-Hacer clic en el "Tipo de Operación"</br> 
48.-Seleccionar el ítem "Decremento Atm"</br> 
49.-Hacer clic en "Numero de ATM"</br> 
50.-Seleccionar el ítem "S1GIB078"</br> 
51.-Hacer clic en seleccionar Moneda "Pesos"</br> 
52.-Ingresar importe "2.500"</br> 
53.-Hacer clic en "SIGUIENTE"</br> 
54.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br> 
55.-Visualizar el Mensaje - "Operación realizada con éxito"</br> 
56.-Hacer clic en Botón "FINALIZAR"</br> 
57.-Visualizar la impresión del ticket</br> 
58.-Hacer clic en el recuadro Hola, UIC10021</br> 
59.-Hacer clic en CERRAR SESIÓN </br>  
""")

class SUC_T783(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
               
    def test_SUC_T783(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            operaciones=[self.operacion1,self.operacion2,self.operacion3,self.operacion4]
            importes = [self.importe,self.importe1,self.importe2,self.importe3]
            importesValidar = [self.importeValidar,self.importeValidar1,self.importeValidar2,self.importeValidar3]
            for operacion,importe,importeValidar in zip(operaciones,importes,importesValidar):     
                self.wait(2)
                self.seleccionarATMBanelco()
                self.wait(2)
                self.mostrarYSeleccionarTipoDeTransaccion(operacion)
                self.wait(1)
                self.mostrarYSeleccionarNroAtm("S1GIB081")
                self.wait(4)
                self.mostrarTiposDeMonedaAtm()
                self.seleccionarTipoDeMoneda(self.tipoMoneda)
                self.ingresarImporte(importe,self.tipoMoneda)
                self.seleccionarSiguiente()
                self.validar_sucursal(self.sucursal)
                self.validar_operacion(operacion)
                self.validar_moneda(self.tipoMoneda)
                self.validar_numero_atm("S1GIB081")
                self.validar_importe(importeValidar)
                self.seleccionarConfirmar()
                self.verificarMensajeExitoExtracciones(self.mensaje)  
            self.cerrarSesion()
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()

    def tearDown(self):
        fin(self)

    def getDatos(self):
        self.sucursal = self.usuario.get(SUC_JOB)
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.legajo = self.usuario.get(LEGAJO)
        self.terminal = self.usuario.get(TERMINAL)
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento = self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.numeroAtm = self.usuario.get(NUMERO_ATM)
        self.operacion1 = self.usuario.get(OPERACION1)
        self.operacion2 = self.usuario.get(OPERACION2)
        self.operacion3 = self.usuario.get(OPERACION3)
        self.operacion4 = self.usuario.get(OPERACION4)
        self.importe = self.usuario.get(IMPORTE)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importe3 = self.usuario.get(IMPORTE3)
        self.importeValidar =self.usuario.get(IMPORTE_A_VALIDAR)
        self.importeValidar1 =self.usuario.get(IMPORTE_VALIDAR_1)
        self.importeValidar2 =self.usuario.get(IMPORTE_VALIDAR_2)
        self.importeValidar3 =self.usuario.get(IMPORTE_VALIDAR_3)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        
if __name__ == "__main__":
    unittest.main()