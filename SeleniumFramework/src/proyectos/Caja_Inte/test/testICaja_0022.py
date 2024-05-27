# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from proyectos.Caja_Homo.st.stLogin import stLogin
from proyectos.Caja_Homo.st.stICajaInicio import stICajaInicio
from proyectos.Caja_Homo.st.stICaja import stICaja
from proyectos.Caja_Homo.st import inicioICaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,\
             CLAVE, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, APELLIDO


@allure.feature(u'ICaja')
@allure.story(u'Identificar Cliente')
@allure.testcase(
    u"ICaja - Caso de Prueba 0022", u''
)
@allure.title(u'Test_0022 - Identificar Cliente con LC')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""1-Ingresar a la pagina Icaja. </br>
    2-Realizar login </br>
    3-Ingresar  usuario y password y hacer clik en Aceptar.</br>
    4-Hacer click  en el Boton "Identificar Cliente" </br>
    5-Visualizar en pantalla el cuadro identificar cliente.</br> 
    6- Seleccionar Tipo de Documento "LC"</br>
    7-Ingresar numero de Documento. </br>
    8-Hacer click  en el Boton "Identificar"</br> 
    9-Visualizar en pantalla los datos del cliente y firma asociada.</br>
    10-Hacer click  en el Boton "Cerrar"</br>
    11-Hacer click  en el Boton Salir "Salir de la aplicacion"</br>   
    """
)
class tstICaja_0022(unittest.TestCase, stICajaInicio, stICaja):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0022(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.identificarCliente()
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
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.nombreUser = self.usuario.get(NOMBRE)
        self.apellidoUser = self.usuario.get(APELLIDO)


if __name__ == "__main__":
    unittest.main()
