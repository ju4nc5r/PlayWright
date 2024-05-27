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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO

@allure.feature(u'ICaja')
@allure.story(u'Certificacion Firma')
@allure.testcase(
    u"test_0050 - Certificacion de firma", u''
)
@allure.title(u'test_0050 - Certificacion de firma')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina  Icaja.
    2-Realizar login
    3-Igresar  usuario y password y hacer clic en Aceptar.
    4-Hacer clic  en el Boton "Identificar Cliente"
    5-Visualizar en pantalla el cuadro identificar cliente. 
    6-Seleccionar Tipo de Documento "DNI"
    7-Ingresar numero de Documento
    8-Hacer clic  en el Boton "Identificar"  
    9-Visualizar en pantalla los datos del cliente y firma asociada.
    10-Hacer clic  en el Boton "Cerrar"
    11-Hacer clic en la flecha de despliegue de las TX
    12-Hacer clic en la opcion Clientes
    13-Hacer clic en la opcion Certificacion Firma
    14-Hacer clic en la opcion Seleccione una cuenta
    15-Seleccionar una cuenta
    16-Hacer clic en el boton siguiente
    17-Hacer clic en el boton aceptar e utilizar la opcion guardar
    18-Hacer clic en el chek confirmar firma
    19--Hacer clic en confirmar 
    """
)
class tstICaja_0050(unittest.TestCase, stICajaInicio, stICaja):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0050(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.identificarCliente()
            self.minimizarFirma()
            self.desplazarSideBar()
            self.seleccionarCertificacionFirma()
            self.wait(5)
            self.ingresarCuenta(self.cuenta)
            self.wait(5)
            self.seleccionarSiguiente()
            self.seleccionarConfirmarFirma()
            self.wait(5)
            self.seleccionarConfirmar()
            self.wait(5)
            self.verificarMensajeExitoEgresoIngreso(self.mensaje)
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
        self.nombreUser = self.usuario.get(NOMBRE)
        self.apellidoUser = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        

if __name__ == "__main__":
    unittest.main()
