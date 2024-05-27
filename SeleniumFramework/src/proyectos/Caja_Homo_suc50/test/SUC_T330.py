# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminConsulta import stAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioAdminCaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE,\
                TIT_ESPERADO, SUCURSAL_DEST

@allure.feature(u'Consultas')
@allure.story(u'Operadores registrados')
@allure.testcase( u"Adm.Caja - Caso de Prueba SUC-T330")
@allure.title(u'SUC-T330 - Consultas - Operadores registrados')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1-Ingresar a la pagina Administración de Cajas (https://fe-admincaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/)</br>
2-Colocar los datos del Supervisor (Legajo - Terminal - Password).</br>
Legajo: UIC10022</br>
Terminal:IA0500822  </br>
Password:</br>
Hacer clic en Aceptar.</br>
3-Visualizar los datos del Cajero: "Hola UIC10022 !" </br>
4-Visualizar en el recuadro los datos del cajero: </br>
Legajo: "UIC10022" </br>
Terminal: "IA0500822  "</br>
Sucursal: "0050" Terminal: "IA0500822  " Sucursal: "0050"</br>
5-Hacer clic en el Botón Consultas.</br>
6-Hacer clic en el Botón Operadores Regitrados.</br>
7-Visualizar el titulo Consultas - Operadores registrados.</br>
8-Validar que el Item Operador este "Todos" </br>
9-Validar Sucursal "0050 - Puerto Madero" </br>
10-Visualizar en pantalla los Operadores registrados. </br>
11-Hacer clic en el Botón Salir.</br>
    """
)
class SUC_T330(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def test_SUC_T330(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarOperadoresRegis()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            self.seleccionarSucursal()
#             self.seleccionarNumSucursal(self.sucursalDest)
            self.validarTablaOperadores()
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
        self.sucursalDest = self.usuario.get(SUCURSAL_DEST)
        
if __name__ == "__main__":
    unittest.main()
