# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebOperaciones import pl_MesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebBandeja import pl_MesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPrecios import stMesaWebPrecios
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

             

@allure.feature(u'Operaciones')
@allure.story(u'Carga de precios conocidos')
@allure.testcase(u"Mesa_Web - INV-T274 - Carga de precios conocidos")
@allure.title(u'Mesa_Web - INV-T274 - Carga de precios conocidos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar</br>
3.-Presionar en la sección perfil sobre el operador asignado</br>
4.-Elegir perfil BAckOfficeConf y luego presionar "Cambiar Perfil"(de ser perfil default, presionar Cancelar)</br>
5.-Dentro del menú de "Precios" ir a la opción "Precios FCI"</br>
6.-Editar el Fondo con nombre "GPESOS A"</br>
7.-Presionar Aceptar</br>
8.-Debe aparecer un cartel con la leyenda "Precios FCI El precio del Fondo se ha actualizado correctamente."</br>
9.-Repeter pasos 6 y 7 para el Fondo con nombre "GPESOS B"</br>
10.-Debe aparecer un cartel con la leyenda "Precios FCI El precio del Fondo se ha actualizado correctamente."</br>
 </br>
    """
)
class INV_T274(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebPrecios, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T274(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operador_backOffice)
            self.seleccionar_precios()
            self.seleccionar_precios_FCI()
            self.selecionar_editar_celda("3")
            self.editar_monto("48.0")
            self.selecionar_aceptar()
            self.visualizar_msj_fondo_actualizado()
            self.selecionar_editar_celda("2")
            self.editar_monto("48.0")
            self.selecionar_aceptar()
            self.visualizar_msj_fondo_actualizado()
            self.cerrarSesion()
            self.finalizo = True
        except Exception:
            self.cerrarSesion()
            self.error = traceback.format_exc()

    def tearDown(self):
        fin(self)

    def getDatos(self):
        
        self.nrocliente = self.usuario.get(NROCLIENTE)
        self.mensaje_esperado = self.usuario.get(MSJ_ESPERADO)
        self.cuenta = self.usuario.get(CUENTA)
        self.instrumento = self.usuario.get(INSTRUMENTO) 
        self.cantidad = self.usuario.get(CANTIDAD)
        self.orden = ""
        

if __name__ == "__main__":
    unittest.main()
