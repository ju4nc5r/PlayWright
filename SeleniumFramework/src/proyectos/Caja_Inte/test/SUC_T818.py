# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE


@allure.feature(u'ICaja')
@allure.story(u'Seguridad')
@allure.testcase( u"ICaja SUC-T818 -  Login de ICaja Cajero (UIC10020)")
@allure.title(u'SUC-T818 - Login de ICaja Cajero (UIC10020)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1 Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2 Realizar login e ingresar los datos del operador Legajo:UIC10020 / Terminal:IA0500820 / Contraseña:Ingreso20</br>
3 Hacer clic en el botón "INGRESAR"</br>
4 Hacer clic en el recuadro "Hola, UIC10020 y visualizar los datos del operador UIC10020</br>
5 Hacer clic en el recuadro Hola, UIC10020 para que desaparezca los datos del operador</br>
6 Hacer clic en "CERRAR SESIÓN"</br>
</br>
    """
)
class SUC_T818(unittest.TestCase, stICajaInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T818(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarIconoVcard()                     
            self.validar_usuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.seleccionarCerrarSesion()
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
