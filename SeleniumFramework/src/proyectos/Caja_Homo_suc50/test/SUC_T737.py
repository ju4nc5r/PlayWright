# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminSucursales import stAdminSucursales
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioAdminCaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE, TIT_ESPERADO


@allure.feature(u'Sucursales') 
@allure.story(u'Apertura')
@allure.testcase(u"ICaja - SUC-T737 - Apertura de Sucursal")
@allure.title(u'SUC-T737 - Apertura de Sucursal')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1-Ingresar a la pagina Administración de Cajas (https://fe-admincaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/) </br> 
2-Colocar los datos del Supervisor (Legajo - Terminal - Password). </br>
    Legajo: UIC10022 </br>
    Terminal:IA0500822   </br>
    Password: </br>
3-Hacer clik en Aceptar. </br>
4-Visualizar los datos del Cajero: "Hola UIC10022 !" </br>
5-Visualizar en el recuadro los datos del cajero: </br>
    Legajo: "UIC10022" </br>
    Terminal: "IA0500822  " </br>
    Sucursal: "0050" Terminal: "IA0500822  " Sucursal: "0050" </br>
6-Hacer clic en el Boton Sucursales </br>
7-Hacer clic en el Boton Apertura </br>
8-Seleccionar el operador UIC10022 y hacer click en Aceptar.</br>
9-Visualizar el mensaje de apertura de la sucursal "Se ha asignado correctamente el operador centralizador: UIC10022. Apertura de sucursal realizada!" </br>
10-Hacer clic en el boton Cerrar </br>
11-Hacer clic en el Boton Salir. </br>
    """ 
)
class SUC_T737(unittest.TestCase, stAdminSucursales, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def test_SUC_T737(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.validarUsuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.seleccionarSucursales()
            self.seleccionarApertura()            
            self.validarTituloApertura(self.tituloEsperado)            
            self.seleccionarOperador(self.user)
            self.seleccionarAceptar()        
            self.verificarApertura()
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
