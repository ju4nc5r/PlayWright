# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminConsulta import stAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
            MONEDA1,MONEDA2,MONEDA3



@allure.feature(u'Operaciones de Caja')
@allure.story(u'Cierre de Caja')
@allure.testcase(u"ICaja - SUC-T782 - Cierre de Caja - Operador UIC10020")
@allure.title(u'SUC-T782 - Cierre de Caja - Operador UIC10020')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10020 / Terminal:IA0500820 / Contraseña:Ingreso20</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10020 y visualizar los datos del operador UIC10020</br>
5.-Hacer clic en el recuadro Hola, UIC10020 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Cierre de Caja"</br>
7.-Visualizar los Saldos y Estado "Pendiente"</br>
8.-Hacer clic en Botón "SIGUIENTE"</br>
9.-Visualizar el recuadro con el mensaje "Si inicia el proceso de cierre no podrá realizar más operaciones"</br>
10.-Hacer clic en ¿Desea continuar la operación?" "SI"</br>
11.-Visualizar Moneda "Reales"</br>
12.-Hacer checklist en la opción "No existen diferencias"</br>
13.-Hacer clic en Botón "CERRAR MONEDA"</br>
14.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
15.-Hacer clic en Botón "FINALIZAR"</br>
16.-Visualizar la impresión del ticket</br>
17.-Visualizar Moneda "Euros"</br>
18.-Hacer checklist en la opción "No existen diferencias"</br>
19.-Hacer clic en Botón "CERRAR MONEDA"</br>
20.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
21.-Hacer clic en Botón "FINALIZAR"</br>
22.-Visualizar la impresión del ticket</br>
23.-Visualizar Moneda "Dolares"</br>
24.-Hacer checklist en la opción "No existen diferencias"</br>
25.-Hacer clic en Botón "CERRAR MONEDA"</br>
26.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
27.-Hacer clic en Botón "FINALIZAR"</br>
28.-Visualizar la impresión del ticket</br>
29.-Visualizar Moneda "Pesos"</br>
30.-Hacer checklist en la opción "No existen diferencias"</br>
31.-Hacer clic en Botón "CERRAR MONEDA"</br>
32.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
33.-Hacer clic en Botón "FINALIZAR"</br>
34.-Visualizar la impresión del ticket</br>
35.-Visualizar el mensaje "Cierre de caja realizado con éxito " "Se procederá a desloguearlo"</br>
36.-Hacer clic en Botón "FINALIZAR""</br>
 </br>    
 "  . 
    """
)

class SUC_T782(unittest.TestCase, stICajaInicio, stICaja,stAdminInicio,stAdminConsulta,stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T782(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarCierreDeCaja()
            self.visualizar_msj_existen_monedas_con_saldos()
            self.monedas=["reales","euros","dolares","pesos"]
            self.posiciones = ["1","2","3","4"]
            columnas = ["2","3","4","5"]
            for colum in columnas:
                self.verificar_estado_monedas(colum)            
            self.seleccionarSiguiente() 
            if self.visualizar_advertencia_de_cierre():     
                self.wait(2)
            for moneda,posicion in zip (self.monedas,self.posiciones):
                self.seleccionarCheckNoExistenDiferencias(posicion)
                self.seleccionarCierreMonedaCaja(posicion) 
                self.validarMsgMonedaCerrada(moneda)
                self.visualizarTicket2()
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
        self.moneda = self.usuario.get(MONEDA)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.sucudestino = self.usuario.get(SUCURSAL_ORIG)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL) 
        
           
        

if __name__ == "__main__":
    unittest.main()
