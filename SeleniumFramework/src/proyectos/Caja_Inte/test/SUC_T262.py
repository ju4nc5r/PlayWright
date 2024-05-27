# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminTerminales import stAdminTerminales
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioAdminCaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE, TIT_ESPERADO

@allure.feature(u'Terminales')
@allure.story(u'Baja')
@allure.testcase( u"Adm.Caja - SUC-T262", u'Terminales - Baja')
@allure.title(u'SUC-T262 - Terminales - Baja')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1-Ingresar a la pagina Administración de Cajas. (https://fe-admincaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/)</br> 
2-Ingresar los datos del Tesorero:</br>
Legajo: UIC10022</br>
Terminal: IA0500822  </br>
Password: Ingreso22</br>
3-Hacer clic en Aceptar.</br>
4-Visualizar los recuadros de los datos del Tesorero:</br>
"Hola UIC10022 !"</br>
Legajo: UIC10022 </br>
Terminal: IA0500822   </br>
Sucursal:0050 </br> 
5-Hacer clic en el Botón "Terminales" </br>
6-Hacer clic en el Botón "Baja" </br>
7-Validar el titulo "Terminales - Baja" </br>
8-Visualizar en el recuerdo todas la terminales activas e inactivas. </br>
9-Hacer click en el Boton Salir. </br>
    """
)
class SUC_T262(unittest.TestCase, stAdminTerminales, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def test_SUC_T262(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.wait(5)
            self.seleccionarTerminales()
            self.seleccionarBajaTerminales()
            self.validarTituloTerminales(self.tituloEsperado)
            self.wait(5)
            self.validarTerminalesActivas()
            self.wait(5)
            self.seleccionarSalirApp()
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
        self.tituloEsperado = self.usuario.get(TIT_ESPERADO)

if __name__ == "__main__":
    unittest.main()
