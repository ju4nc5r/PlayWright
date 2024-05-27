# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebFCI import pl_MesaWebFCI
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebFCI import stMesaWebFCI
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

    

             

@allure.feature(u'FCI')
@allure.story(u'Suscripcion FCI')
@allure.testcase(u"Mesa_Web - INV-T283 - Baja Suscripcion FCI sin importe")
@allure.title(u'Mesa_Web - INV-T283 - Baja Suscripcion FCI sin importe')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar</br>
3.-Presionar en la sección perfil sobre el operador asignado </br>
4.-Elegir perfil "OperadorMesaDeDinero" y luego presionar "Cambiar Perfil"</br>
5.-Dar de alta una suscripción de FCI de acuerdo al Caso "Suscripción FCI"</br>
6.-Desde la bandeja de FCI buscar la suscripción dada de alta en el punto anterior y presionar el botón "Anular" (es el botón con el dibujito de un X en rojo ubicado en la sección acciones en la grilla de FCI)</br>
9.-Presionar Aceptar</br>
10.-Debe mostrar cartel verde confirmando anulación del FCI</br>
11.-Debe "desaparecer" de la bandeja de Fci y "aparecer" en la Bandeja de Bajas.</br>
 </br>
    """
)
class INV_T283(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebFCI, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T283(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operadorMesaDinero)
            self.wait(4)
            self.seleccionar_fci()
            self.seleccionarBuscarCliente_por(pl_MesaWebFCI.tipo_cliente_Nro)
            self.completarNroCliente(self.nrocliente)
            self.seleccionar_btn_buscar_cliente()
            self.validarCliente(MSJ_ESPERADO, pl_MesaWebFCI.contains_automatizacion)
            self.seleccionar_btn_seleccionar(pl_MesaWebFCI.btn_seleccionar_2)
            self.select_btn_fondos_comunes(pl_MesaWebFCI.btn_fondos_comunes) 
            self.select_item_fondo(pl_MesaWebFCI.item_fondos)
            self.select_btn_suscripcion(pl_MesaWebFCI.btn_suscripcion)
            self.ingresar_monto("50")
            self.selecionar_aceptar()
            self.selecionar_confirmar()
            self.orden = self.obtener_Nro_orden()
            self.selecionar_bandeja()
            self.wait(3)
            self.selecionar_FCI()
            self.wait(3)
            self.validar_numero_de_FCI(self.orden)
            self.selecionar_X()
            self.selecionar_aceptar_alta_de_orden()
            self.wait(5)
            self.validar_msj_exito()
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
