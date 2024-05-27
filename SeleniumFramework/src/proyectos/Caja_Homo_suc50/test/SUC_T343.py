# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAdminConsulta import stAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioAdminCaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE, TIT_ESPERADO

@allure.feature(u'Consultas')
@allure.story(u'Movimientos de caja')
@allure.testcase(u"SUC-T343 - Consultas de Movimientos de caja - Descargar")
@allure.title(u'SUC-T343 - consulta de Movimientos de caja - Descargar')
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
Terminal: "IA0500822  " </br>  
Sucursal: "0050" Terminal: "IA0500822  " Sucursal: "0050" </br>  
5-Hacer clic en el Botón Consultas. </br>  
6-Hacer clic en el Botón Movimientos de Caja </br>  
7-Visualizar el Titulo Movimientos de Caja </br>  
8-Visualizar en pantalla los Totales de saldos por sucursal </br>  
9-Hacer clic item Operador y agregar cajero UIC10021 </br>  
10-Validar item fecha desde </br>  
11-Hacer clic en el Botón Buscar </br>  
12-Hacer click en Descargar. </br>  
13-Hacer clic en el Boton Salir.</br>            
"""
)

class SUC_T343(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def test_SUC_T343(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarMovimientosdecaja()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            self.seleccionarBuscarMovimientos()
            self.wait(5)
            self.validarTablaMovimientosdecaja()
            self.wait(5)
            self.seleccionarDescargarMovimientos()
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
