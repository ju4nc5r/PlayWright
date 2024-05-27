# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from datetime import date
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminInicio import stAdminInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAdminConsulta import stAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioAdminCaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE,\
              TIT_ESPERADO


@allure.feature(u'Consultas')
@allure.story(u'Tickets')
@allure.testcase( u"Adm.Caja - SUC-T349")
@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/BOX-T400')
@allure.title(u'SUC-T349- Consultas - Tickets')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1-Ingresar a la pagina Administración de Cajas (https://fe-admincaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/)</br>
2-Colocar los datos del Supervisor (Legajo - Terminal - Password).</br>
Legajo: UIC10022</br>
Terminal:IA0500822   </br>
Password:</br>
Hacer clic en Aceptar. </br>
3-Visualizar los datos del Cajero: "Hola UIC10022 !" </br>
4-Visualizar en el recuadro los datos del cajero: </br>
Legajo: "UIC10022" </br>
Terminal: "IA0500822  " </br>
Sucursal: "0050" Terminal: "IA0500822  " Sucursal: "0050" </br>
5-Hacer clic en el Botón Consultas. </br>
6-Hacer clic en el Botón Listado de Tickets </br>
7-Visualizar el Titulo Consultas - Tickets </br>
8-Visualizar los Item:</br>
Operador: (Todos)</br>
Fecha: (Del día)</br>
Sucursal: "0050 - Puerto Madero" </br>
9-Hacer clic en el Botón Buscar. </br>
10-Visualizar en pantalla los Totales los ticket´s </br>
11-Hacer clic en el Botón Salir. </br>
    """)
class SUC_T349(unittest.TestCase, stAdminConsulta, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def test_SUC_T349(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.validarUsuario(self.user)
            self.validarTerminal(self.terminal)
            self.validarSucursal(self.sucursal)
            self.wait(5)
            self.seleccionarConsultas()
            self.wait(5)
            self.seleccionarListadosTickets()
            self.validarTituloConsulta(self.tituloEsperado)
            self.wait(5)
            self.validarFechaDia(self.hoyFecha)
            self.wait(5)
            self.seleccionarBuscarTotales()
            self.wait(5)
            self.visualizarInformacion()
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
        hoy = date.today()
        self.dia = hoy.strftime("%d")
        self.mes = hoy.strftime("%m")
        self.year = hoy.strftime("%Y")
        self.hoyFecha = self.dia+"/"+self.mes+"/"+self.year
        

if __name__ == "__main__":
    unittest.main()
