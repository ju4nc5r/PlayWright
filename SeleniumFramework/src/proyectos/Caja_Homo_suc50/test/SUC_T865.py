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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,MONEDA1,MONEDA2,MONEDA3          


@allure.feature(u'Remesas')
@allure.story(u'Recepción de Remesas')
@allure.testcase(u"ICaja - SUC-T865 Recepción de Remesas Moneda Pesos")
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/33994')
@allure.title(u'SUC-T865 - Recepción de Remesas Moneda Pesos - UIC10021')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login </br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21 </br>
3.-Hacer clic en el botón "INGRESAR" </br>
4.-Validar el nombre de usuario "Hola, UIC10021 </br>
5.-Hacer clic en la Transacción - Recepción de Remesas </br>
8.-Visualizar en pantalla el recuadro de la recepción de remesas </br>
9.-Hacer clic en el chelisk verde y aceptar la remesa </br>
10.-Visualizar el mensaje "Operación realizada con éxito" </br>
15.-Hacer clic en boton "FINALIZAR" </br>
16.-Visualizar la impresion del ticket </br>
"""
)
class SUC_T865(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T865(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_recepcion_de_Remesas()
            self.movimiento_de_el_mouse_ala_celda()
            self.wait(2)
            self.visualizarMensajeExito()
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucuorigen = self.usuario.get(SUCURSAL)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        #self.mensaje = "La operacion finalizo correctamente"   
        
        

if __name__ == "__main__":
    unittest.main()
