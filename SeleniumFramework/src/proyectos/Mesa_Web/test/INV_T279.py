# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebFCI import pl_MesaWebFCI
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebBandeja import pl_MesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebFCI import stMesaWebFCI
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

    

             

@allure.feature(u'FCI')
@allure.story(u'Rescate FCI')
@allure.testcase(u"Mesa_Web - INV-T279 - Rescate FCI")
#@allure.link(u'https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/21300')                
@allure.title(u'Mesa_Web - INV-T279 - Rescate FCI')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml </br>
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar </br>
3.-Presionar en la sección perfil sobre el operador asignado </br>
4.-Elegir perfil "OperadorBancaPrivada" y luego presionar "Cambiar Perfil" </br>
5.-Presoinar FCI en la Barra de menús </br>
6.-Realizar búsqueda del cliente por "Nro cliente" = 538011 y presionar Buscar </br>
7.-Seleccionar Nombre/Razón Social= "DAVID FOOD 2661".</br>
8.-En la sección Cuentas seleccionar la cuenta monetaria 00026611005 </br>
9.-En la sección Operaciones presionar "Fondos Comunes" </br>
10.-Seleccionar el Fondo GOAL PESOS B y luego Presionar el botón "Rescate por cuota-parte" </br>
11.-Ingresar 50 en el campo "Cantidad Cuotas Parte" y presionar aceptar </br>
12.-Presionar Confirmar </br>
13.-Debe mostrar el número de operación generado </br>
</br>
    """
)
class INV_T279(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebFCI, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T279(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operador_banca_privada)
            self.wait(4)
            self.seleccionar_fci()
            self.seleccionarBuscarCliente_por(pl_MesaWebFCI.tipo_cliente_Nro)
            self.completarNroCliente(self.nrocliente)
            self.seleccionar_btn_buscar_cliente()
            self.validarCliente(MSJ_ESPERADO, pl_MesaWebFCI.contains_david_food_2661)
            self.seleccionar_btn_seleccionar(pl_MesaWebFCI.btn_seleccionar_2)
            self.select_btn_fondos_comunes(pl_MesaWebFCI.btn_fondos_comunes) 
            self.select_item_fondo(pl_MesaWebFCI.item_fondos_pesosB)
            self.select_btn_rescate_por_cuota_parte(pl_MesaWebFCI.btn_rescate_cuota_parte)
            self.ingresar_cuotas("50")
            self.selecionar_aceptar()
            self.selecionar_confirmar()
            self.orden = self.obtener_Nro_orden()
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
