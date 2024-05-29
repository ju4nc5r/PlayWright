# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminConsulta import stAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioAdminCaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE,\
              TIT_ESPERADO, MONEDA, USUARIO_CONTROL, SUCURSAL_DEST

@allure.feature(u'Consultas')
@allure.story(u'Totales ingresos, egresos y líquido de caja')
@allure.testcase(u"SUC-T355 - Consultas - Totales ingresos, egresos y líquido de caja - Reales")
@allure.title(u'SUC-T355 - Consultas - Reales')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1-Ingresar a la pagina Administración de Cajas (https://fe-admincaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/) </br>  
2-Colocar los datos del Supervisor (Legajo - Terminal - Password). </br>  
Legajo: UIC10022 </br>  
Terminal:IA0500822   </br>  
Password:</br>  
Hacer clic en Aceptar. </br>  
3-Visualizar los datos del Cajero: "Hola UIC10022 !" </br>  
4-Visualizar en el recuadro los datos del cajero: </br>  
Legajo: "UIC10022" </br>  
Terminal: "IA0500822  " </br>  
Sucursal: "0050" Terminal: "IA0500822  " Sucursal: "0050" </br>  
5-Hacer clic en el Botón Consultas. </br>  
6-Hacer clic en el Botón Totales ingresos, egresos y líquido de caja. </br>  
7-Visualizar el titulo Consultas - Totales ingresos, egresos y líquido de caja. </br>  
8-Validar el item Moneda y Seleccionar Reales </br>  
9-Validar Sucursal "0050 - Puerto Madero" </br>  
10-Visualizar en pantalla las Terminales registrados. </br>  
11-Hacer clic en el Botón Buscar. </br>  
12-Hacer clic en el Botón Imprimir. </br>  
13-Hacer clic en el Botón Salir. </br>       
""")

class SUC_T355(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def test_SUC_T355(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarTotalesIngresEgresos()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            # self.ingresarUserControl(self.userControl)
            self.seleccionarMoneda()
            self.seleccionarTipoMoneda(self.moneda)
            self.wait(2)
            self.seleccionarSucursal()
#             self.seleccionarNumSucursal(self.sucursalDestino)
            self.wait(5)
            self.seleccionarBuscarTotales()
            self.wait(5)
            self.visualizarIngresos()
            self.visualizarEgresos()
            self.visualizarLiquido()
            self.wait(5)
            self.seleccionarImprimirTotales()
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
        self.userControl = self.usuario.get(USUARIO_CONTROL)
        self.moneda = self.usuario.get(MONEDA)
        self.sucursalDestino = self.usuario.get(SUCURSAL_DEST) 

if __name__ == "__main__":
    unittest.main()
