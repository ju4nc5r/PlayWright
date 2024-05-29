# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,MONEDA1,MONEDA2,MONEDA3          
import pytest

@allure.feature(u'Operaciones de Caja')
@allure.story(u'Consulta de Posición del Líquido de la Sucursal')
@allure.testcase(u"ICaja - SUC-T837 - Consulta de Posición del Líquido de la Sucursal - (Perfil Operador)")
@allure.title(u'SUC-T837 - Consulta de Posición del Líquido de la Sucursal - (Perfil Operador)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821/ Contraseña:Testicaja09</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en la Transacción - "Consulta de Posición del Líquido de la Sucursal"</br>
5.-Validar el mensaje "Transacción no autorizada" "Solo un operador con perfil Centralizador puede ingresar a esta transacción."</br>
6.-Hacer clic en el botón "ACEPTAR"</br>
7.-Hacer clic en el recuadro Hola, UIC10021 </br>
.8-Hacer clic en CERRAR SESIÓN </br>
"""
)
class SUC_T837(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T837(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarConsultaDePoicionDelLiquidoDeLaSucursal()
            self.validarMsgTransaccionNoAutorizada("Solo un operador con perfil Centralizador puede ingresar a esta transacción")
            self.seleccionarAceptar3()
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
