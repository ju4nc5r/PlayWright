# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from proyectos.Caja_Homo.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE


@allure.feature(u'ICaja')
@allure.story(u'Seguridad')
@allure.testcase(
    u"ICaja - Caso de Prueba 0010", u''
)
@allure.title(u'test_0010 - Login  ')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1-Ingresar a la pagina Icaja </br>
2-Realizar login </br>
3-Ingresar los datos: Legajo - Terminal - Contraseña </br>
5-Hacer clic en el recuadro Hola, UIC10009 </br>
6-Visualizar los datos del operador UIC10009 : </br>
     Legajo: UIC10009 - Terminal: IBA0009 - Sucursal: 0046 </br>
7-Hacer clic en el recuadro Hola, UIC10009 para que desaparezca los datos del operador </br>
    """
)
class tstICaja_0010(unittest.TestCase, stICajaInicio):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0010(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarIconoVcard()                     
            self.validarUsuario(self.user)
            self.validarLegajo(self.legajo)            
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.CerrarDatosOperador() 
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
        self.sucursal = self.usuario.get(SUCURSAL)

if __name__ == "__main__":
    unittest.main()

