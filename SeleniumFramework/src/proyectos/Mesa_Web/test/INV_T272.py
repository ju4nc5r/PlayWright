# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebOperaciones import pl_MesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebBandeja import pl_MesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebOperaciones import stMesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

@allure.feature(u'Operaciones')
@allure.story(u'Venta de acciones')
@allure.testcase(u"Mesa_Web - INV-272 - Venta de acciones")
#@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/21300')                
@allure.title(u'Mesa_Web - INV-272 - Venta de acciones')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml </br>
2-Poner Usuario y Contraseña de Red y luego presionar ingresar </br>
3-Presionar en la sección perfil sobre el operador asignado </br>
4-Elegir perfil OperadorMesaDeDinero y luego presionar "Cambiar Perfil" </br>
5-Dentro del menú "Operaciones" ir a la opción Acciones y realizar click en el submenú "venta" </br>
6-Realizar búsqueda del cliente por "Nro cliente" = 000026" y presionar Buscar </br>
7-Seleccionar Nombre/Razón Social= "Automatización Mesa Web". </br>
8-Presionar siguiente. </br>
9-Seleccionar Cuenta custodia 00000000098. </br>
10-Ingresar instrumento AGRO y seleccionarlo del desplegable. </br>
11-Presionar siguiente </br>
12-Ingresar cantidad 111 y precio debe ser igual al informado en la seccion detalle del instrumento como "ult. Pcio. Oper" </br>
13-Presionar Venta banco </br>
14-Presionar Aceptar </br>
15-Presionar Aceptar </br>
16-Presionar ir a la bandeja </br>
17-En la bandeja de ordenes debe aparecer la operación y debe quedar en estado "Aceptado o Ejecutado" (puede demorse unos segundos en pasar de estado Pend a aceptado)
 </br>
    """
)
class INV_272(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebOperaciones, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T272(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operadorMesaDinero)
            self.wait(4)
            self.seleccionar_operaciones()
            self.seleccionar_acciones()
            self.seleccionar_venta()
            self.seleccionarBuscarCliente_por(pl_MesaWebOperaciones.tipo_cliente_Nro)
            self.completarNroCliente(self.nrocliente)
            self.seleccionar_btn_buscar_cliente()
            self.validarCliente(MSJ_ESPERADO, pl_MesaWebOperaciones.contains_automatizacion)
            self.select_nom_razon_social(pl_MesaWebOperaciones.select_Nom_Razon_social)
            self.resaltar_advertencia_sin_clasificacion(pl_MesaWebOperaciones.msj_no_posee_clasificacion)
            self.select_btn_siguiente(pl_MesaWebOperaciones.btn_siguiente)
            self.seleccionar_instrumento(self.instrumento)
            self.wait(5)
            self.select_btn_siguiente(pl_MesaWebOperaciones.btn_siguiente)
            self.ingresar_precio()
            self.ingresar_cantidad(self.cantidad)
            self.select_btn_venta_banco(pl_MesaWebOperaciones.btn_venta_banco)
            self.select_btn_aceptar_ord_venta(pl_MesaWebOperaciones.btn_aceptar_ord_venta)
            self.wait(1)
            self.select_btn_aceptar(pl_MesaWebOperaciones.btn_aceptar)
            self.wait(2)
            self.orden = self.obtener_Nro_orden()
            self.seleccionar_bandeja() 
            self.wait(5)
            self.validar_orden(self.orden)
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
