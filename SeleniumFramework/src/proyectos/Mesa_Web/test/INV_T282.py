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
@allure.testcase(u"Mesa_Web - INV-T282 - Alta Generica MAE - Editar Op Gene. Sin impt")
@allure.title(u'Mesa_Web - INV-T282 - Alta Generica MAE - Editar Op Gene. Sin impt')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar</br>
3.-Presionar en la sección perfil sobre el operador asignado </br>
4.-Elegir perfil "OperadorMesaDeDinero" y luego presionar "Cambiar Perfil"</br>
5.-Dar de alta una operación Genérica de acuerdo al Caso "Alta genérica Mae"</br>
6.-Desde la bandeja de operaciones buscar la operación dada de alta en el punto anterior y presionar el botón "Editar" (es el botón con el dibujito de un lápiz ubicado en la sección acciones en la grilla de operaciones)</br>
7.-Modificar el campo Book por Banking y estrategia por Banca Patrimonial</br>
9.-Presionar Aceptar</br>
10.-Debe mostrar cartel verde confirmando actualización de la operación</br>
11.-En el detalle de la operación  (es la lupita en la sección Acciones) debe aparece el nuevo Book y Estrategia</br>
    """
)
class INV_T282(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebFCI, stMesaWebBandeja,stMesaWebOperaciones):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T282(self):
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
            self.wait(5)
            self.selecionar_OPERACIONES()
            self.validar_numero_de_OPERACION(self.orden)
            self.selecionar_boton_editar()
            self.wait(5)
            self.selecionar_recuadro_book()
            self.selecionar_Item_banking()
            self.wait(1)
            self.selecionar_recuadro_estrategia()
            self.selecionar_Item_Banca_Patrimonial()
            self.wait(1)
            self.selecionar_aceptar_4()
            self.wait(5)
            self.selecionar_detalles_de_la_operacion()
            self.validar_cambio("book", "BANKING")
            self.validar_cambio("Estrategia", "BANCA PATRIMONIAL")
            self.selecionar_cerrar_detalles()
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
