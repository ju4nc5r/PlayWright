# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminConsulta import stAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              MONEDA,MONEDA1,MONEDA2,MONEDA3, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG



@allure.feature(u'Operaciones de Caja')
@allure.story(u'Cierre de Sucursal')
@allure.testcase(u"ICaja - SUC-T811 - Cierre de Caja + Sucursal UIC10022")
@allure.title(u'SUC-T811 - Cierre de Caja + Sucursal UIC10022')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar el nombre del operador "Hola, UIC10022</br>
5.-Hacer clic en la Transacción - "Cierre de Caja"</br>
6.-Visualizar los Saldos y Estado "Pendiente"</br>
7.-Hacer clic en Botón "SIGUIENTE"</br>
8.-Visualizar el recuadro con el mensaje "Si inicia el proceso de cierre no podrá realizar más operaciones"</br>
9.-Hacer clic en ¿Desea continuar la operación?" "SI"</br>
10.-Visualizar Moneda "Reales"</br>
11.-Hacer checklist en la opción "No existen diferencias"</br>
12.-Hacer clic en Botón "CERRAR MONEDA"</br>
13.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
14.-Hacer clic en Botón "FINALIZAR"</br>
15.-Visualizar la impresión del ticket</br>
16.-Visualizar Moneda "Euros"</br>
17.-Hacer checklist en la opción "No existen diferencias"</br>
18.-Hacer clic en Botón "CERRAR MONEDA"</br>
19.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
20.-Hacer clic en Botón "FINALIZAR"</br>
21.-Visualizar la impresión del ticket</br>
22.-Visualizar Moneda "Dolares"</br>
23.-Hacer checklist en la opción "No existen diferencias"</br>
24.-Hacer clic en Botón "CERRAR MONEDA"</br>
25.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
26.-Hacer clic en Botón "FINALIZAR"</br>
27.-Visualizar la impresión del ticket</br>
28.-Visualizar Moneda "Pesos"</br>
29.-Hacer checklist en la opción "No existen diferencias"</br>
30.-Hacer clic en Botón "CERRAR MONEDA"</br>
31.-Visualizar el mensaje "Cierre de moneda reales realizado con éxito"</br>
32.-Hacer clic en Botón "FINALIZAR"</br>
33.-Visualizar la impresión del ticket</br>
34.-Visualizar el mensaje "Cierre de sucursal realizado con éxito" "Se procederá a desloguearlo"</br>
35.-Hacer clic en Botón "FINALIZAR"</br>
 </br>    
 "  . 
    """
)

class SUC_T811(unittest.TestCase, stICajaInicio, stICaja,stAdminInicio,stAdminConsulta,stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T811(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()        
            self.seleccionarCierreDeCaja()
            self.visualizar_msj_existen_cajas_sin_cerrar()
            self.monedas=[self.moneda,self.moneda1,self.moneda2,self.moneda3]
            self.posiciones = ["1","2","3","4"]
            columnas = ["2","3","4","5"]
            for colum in columnas:
                self.verificar_estado_monedas(colum)            
            self.seleccionarSiguiente() 
            if self.visualizar_advertencia_de_cierre():
                self.seleccionarSI()
            self.wait(2)
            for moneda,posicion in zip (self.monedas,self.posiciones):
                self.seleccionarCheckNoExistenDiferencias(posicion)
                self.seleccionarCierreMonedaCaja(posicion)
                self.validarMsgMonedaCerrada_SUC(moneda)
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucudestino = self.usuario.get(SUCURSAL_ORIG)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL) 
        self.moneda = self.usuario.get(MONEDA)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
           
        

if __name__ == "__main__":
    unittest.main()
