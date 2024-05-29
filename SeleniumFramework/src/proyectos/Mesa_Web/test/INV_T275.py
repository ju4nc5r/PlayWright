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
from SeleniumFramework.constants.excel_constants import NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

    

             

@allure.feature(u'Operaciones')
@allure.story(u'Venta de Titulos')
@allure.testcase(u"Mesa_Web - INV-T275 - Venta de Titulos")
@allure.title(u'Mesa_Web - INV-T275 - Venta de Titulos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-    Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>
2.-   Pone.r Usuario y Contraseña de Red y luego presionar ingresar</br>
3.-  Presionar en la sección perfil sobre el operador asignado </br>
4.-  Elegir perfil "OperadorSucursal" y luego presionar "Cambiar Perfil"</br>
5.-  Dentro del menú "Operaciones" ir a la opción "Títulos" y realizar click en el submenú "venta"</br>
6.-  Realizar búsqueda del cliente por "Nro cliente" = 533412 y presionar Buscar</br>
7.-  Seleccionar Nombre/Razón Social= "Automatización Mesa Web".</br>
8.-  Presionar siguiente.</br>
9.-  Seleccionar Cuenta custodia 00500010375 y cuenta monetaria 04449233016.</br>
10.-   Ingresar instrumento AO20 y seleccionarlo del desplegable.</br>
11.-  Presionar siguiente</br>
12.-  Ingresar cantidad 111 y precio debe ser igual al informado en la seccion detalle del instrumento como "ult. Pcio. Oper"</br>
13.-  Presionar Venta banco</br>
14.-  Realizar check en la opción "Confirmar aceptación de cativo de valores"</br>
15.-  Presionar Aceptar</br>
16.-  Presionar Aceptar</br>
17    Debe mostrar el número de operación generado y luego Presionar ir a la bandeja</br>
18    En la bandeja de ordenes debe aparecer el registro con el nro de operación generado en el paso anterior</br>

 </br>
    """
)
class INV_T275(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebOperaciones, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T275(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operador_sucursal)
            self.seleccionar_operaciones()
            self.seleccionar_titulos()
            self.seleccionar_venta_2()
            self.abrir_tipoCliente()
            self.seleccionar_item_nro_cliente()
            self.completarNroCliente("533412")
            self.seleccionar_btn_buscar_cliente()
            self.select_btn_siguiente(pl_MesaWebOperaciones.btn_siguiente)
            self.seleccionar_btn_seleccionar(pl_MesaWebOperaciones.btn_seleccionar)
            self.seleccionar_recuadro_instrumentos(pl_MesaWebOperaciones.lista_instrumentos)
            self.ingresar_instrumento("AO20")
#             self.seleccionar_recuadro_seleccionar(pl_MesaWebOperaciones.recuadro_seleccionar)
#             self.seleccionar_item(pl_MesaWebOperaciones.item_moneda)
            self.select_btn_siguiente(pl_MesaWebOperaciones.btn_siguiente)
            self.ingresar_cantidad("111")
            self.ingresar_precio_2()   
            self.seleccionar_btn_venta_del_banco()
            self.seleccionar_check_box()
            self.selecionar_aceptar()
            self.selecionar_aceptar_alta_de_orden()
            self.visualizar_msj_alta_exito()
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
