# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebOperaciones import pl_MesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebOperaciones import stMesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

    

             

@allure.feature(u'Operaciones')
@allure.story(u'compra de acciones')
@allure.testcase(u"Mesa_Web - INV-T277 - compra de acciones")
@allure.title(u'Mesa_Web - INV-T277 - compra de acciones')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar
3.-Presionar en la sección perfil sobre el operador asignado 
4.-Elegir perfil "OperadorMesaDeDinero" y luego presionar "Cambiar Perfil"
5.-Dentro del menú "Operaciones" ir a la opción "Acciones" y realizar click en el submenú "Compra"
6.-Realizar búsqueda del cliente por "Nro cliente" = B00019 y presionar Buscar
7.-Presionar siguiente.
8.-Ingresar instrumento AGRO (AGROMETAL ORD. 1 VOTO 0) y seleccionar Especie Pago U$S
9.-Presionar siguiente
10.-Ingresar cantidad 111 y precio debe ser igual al informado en la seccion detalle del instrumento como "ult. Pcio. Oper"
11.-Presionar Compra banco
12.-Presionar Aceptar
13.-Presionar Aceptar
14.-Debe mostrar el número de operación generado y luego Presionar ir a la bandeja
15.-En la bandeja de ordenes debe aparecer el registro con el nro de operación generado en el paso anterior
</br>
    """
)
class INV_T277(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebOperaciones, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T277(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operadorMesaDinero)
            self.wait(1)
            self.seleccionar_operaciones()
            self.seleccionar_acciones()
            self.seleccionar_compra_2()
            self.seleccionarBuscarCliente_por(pl_MesaWebOperaciones.tipo_cliente_Nro)
            self.completarNroCliente("B00019")
            self.seleccionar_btn_buscar_cliente()
            self.validarCliente(MSJ_ESPERADO, pl_MesaWebOperaciones.contains_empresa_alfa_10)
            self.resaltar_advertencia_sin_clasificacion(pl_MesaWebOperaciones.msj_no_posee_clasificacion)
            self.select_btn_siguiente(pl_MesaWebOperaciones.btn_siguiente)
            self.seleccionar_instrumento(self.instrumento)
            self.wait(5)
            self.select_btn_siguiente(pl_MesaWebOperaciones.btn_siguiente)
            self.ingresar_precio()
            self.ingresar_cantidad(self.cantidad)
            self.select_btn_compra_banco(pl_MesaWebOperaciones.btn_compra_banco)
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
