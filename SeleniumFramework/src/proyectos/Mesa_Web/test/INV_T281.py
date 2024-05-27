# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebFCI import pl_MesaWebFCI
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebOperaciones import pl_MesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebOperaciones import stMesaWebOperaciones
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebFCI import stMesaWebFCI
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import USUARIO, CLAVE, NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

    

             

@allure.feature(u'Operaciones')
@allure.story(u'Alta Generica MAE')
@allure.testcase(u"Mesa_Web - INV-T281 - Alta Generica MAE")
@allure.title(u'Mesa_Web - INV-T281 - Alta Generica MAE')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar</br>
3.-Presionar en la sección perfil sobre el operador asignado </br>
4.-Elegir perfil "OperadorMesaDeDinero" y luego presionar "Cambiar Perfil"</br>
5.-Dentro del menú "Operaciones" hacer click en "Operaciones Genéricas"</br>
6.-Realizar búsqueda del cliente por "Nro. cliente" = 000026 y presionar Buscar</br>
7.-Seleccionar "Nombre/Razón Social" AUTOMATIZACIÓN MESA WEB</br>
8.-Completar los siguientes campos Mercado = "MAE" , instrumento="TY27P", Especie Pago='$', Tipo='Vnta', Cantidad=50000, Precio='0.93', Cartera Propia='No', Realizar "Check en Nro. Referencia y Nro. Orden Mae, plazo="Inmediato"</br>
9.-resionar Aceptar y luego aceptar</br>
10.-Debe mostrar el número de operación generado y luego Presionar ir a la bandeja</br>
11.-En la bandeja de operaciones debe aparecer el registro con el nro. de operación generado en el paso anterior</br>
    """
)
class INV_T281(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebFCI, stMesaWebBandeja,stMesaWebOperaciones):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T281(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operadorMesaDinero)
            self.wait(3)
            self.seleccionar_operaciones()
            self.seleccionar_operaciones_genericas()
            self.wait(4)
            self.seleccionar_recuadro_buscar_por()
            self.seleccionar_Nro_de_cliente()
            self.completarNroCliente(self.nrocliente)
            self.seleccionar_btn_buscar_cliente()
            self.validarCliente(MSJ_ESPERADO, pl_MesaWebFCI.contains_automatizacion)   
            self.seleccionar_btn_seleccionar(pl_MesaWebOperaciones.btn_seleccionar_3)
            self.seleccionar_recuadro_mercado()
            self.seleccionar_item_Mae()
            self.ingresar_instrumento_2("TY27P - BONTE TF mayo 2027") 
            self.seleccionar_recuadro_especie()
            self.seleccionar_item_moneda("$")
            self.seleccionar_recuadro_tipo()
            self.seleccionar_item_Vnta()
            self.seleccionar_recuadro_carpeta_propia()
            self.seleccionar_item_no("No")
            self.seleccionar_check_Nro_referencia_mae()
            self.wait(1)
            self.seleccionar_check_Nro_orden_mae()
            self.wait(1)
            self.ingresar_cantidad_2("50000")
            self.wait(1)
            self.ingresar_precio_3("0.93")   
            self.wait(1)
            self.selecionar_aceptar_3()
            self.selecionar_aceptar2()
            self.orden = self.obtener_Nro_orden()
            self.selecionar_ir_a_bandeja()  
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
