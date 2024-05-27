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
@allure.testcase(u"Mesa_Web - INV-T289 - Aprobar Baja FCI con Mov. Fondos imputados")
@allure.title(u'Mesa_Web - INV-T289 - Aprobar Baja FCI con Mov. Fondos imputados')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1 - Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>
2 - Poner Usuario y Contraseña de Red y luego presionar ingresar</br>
3 - Presionar en la sección perfil sobre el operador asignado</br>
4 - Elegir perfil "OperadorSucursal" y luego presionar "Cambiar Perfil"</br>
5 - Dar de alta un rescate de FCI de acuerdo al Caso "Rescate FCI" pero seleccionando el Cliente por DNI: 50000126, fondo GOAL PESOS A y cantidad de cuotaparte 1.</br>
6 - Desde la sección perfil cambiar de "OperadorSucursal" a "OperadorIAM"</br>
7 - Con el nuevo perfil seleccionado, desde la bandeja de FCI buscar el rescate realizado en el punto 5 y presionar el botón "Anular" (es el botón con el dibujito de un X en rojo ubicado en la sección acciones en la grilla de FCI)</br>
8 - Presionar Aceptar</br>
9 - Debe mostrar cartel verde con la Leyenda "La baja de la operación fue enviada para su autorización."</br>
10 - Desloguearse del sistema e ingresar con un usuario diferente..</br>
11 - Presionar en la sección perfil sobre el operador asignado.</br>
12 - Elegir perfil "OperadorBAckOfficeConf" y luego presionar "Cambiar Perfil".</br>
13 -Dentro del Menú Procesos ir a la opción de "Autorizaciones Pendientes"</br>
14 - Buscar el rescate dado de baja en el punto 5 y presionar en la opción "Ver detalle para aprobar/Rechazar" en la sección Acciones de la grilla.</br>
15 - Presionar Aceptar.</br>
16 - Debe mostrar cartel verde con la Leyenda "La eliminación aprobada se realizó satisfactoriamente."</br>
17 - Ir al menú Liquidación\Movimientos\movimientos a imputar.</br>
18 - Buscar por número de operación el rescate dado de baja.</br>
19 - Realizar check en el checkBox, presionar imputar y luego aceptar.</br>
20 - Debe mostrar cartel verde con la leyenda "Se realizaron las imputaciones de movimientos de las operaciones seleccionadas."</br>
21 - En la bandeja de FCI el rescate dado de baja, el campo Tipo debe quedar como ACmp y al posicionarse sobre el nro de operación deben aparecer 4 registros donde deben estar en estado Impt.</br>
22 - También debe "aparecer" en la Bandeja de Bajas con el mismo nro de operación.</br>
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
            self.perfil(pl_MesaWebPerfil.operador_sucursal)
            self.wait(4)
            self.seleccionar_fci()
            self.seleccionarBuscarCliente_por(pl_MesaWebFCI.tipo_cliente_Doc)
            self.completarNroCliente("50000126")
            self.seleccionar_btn_buscar_cliente()
            self.validarCliente(MSJ_ESPERADO, pl_MesaWebFCI.contains_producto_nuevo_vanes)
            self.select_btn_fondos_comunes(pl_MesaWebFCI.btn_fondos_comunes) 
            self.select_item_fondo(pl_MesaWebFCI.item_fondos_pesosA)
            self.select_btn_rescate_por_cuota_parte(pl_MesaWebFCI.btn_rescate_cuota_parte)
            self.ingresar_cuotas("50")
            self.selecionar_aceptar()
            self.selecionar_confirmar()
            self.orden = self.obtener_Nro_orden()
            self.selecionar_bandeja()
            self.perfil(pl_MesaWebPerfil.operador_IAM)
            self.wait(5)
            self.selecionar_X()
            self.selecionar_aceptar_alta_de_orden()  
            self.seleccionarCerrarSesion()
            self.login_2()
            self.perfil(pl_MesaWebPerfil.operador_backOffice)
            self.wait(4)
            self.seleccionar_procesos()
            self.seleccionar_autorizaciones_pendientes()
            self.seleccionar_check_ok()
            self.seleccionar_btn_aprobar()
            self.seleccionar_aceptar_autoriz() 
            self.wait(15)
            self.seleccionar_liquidacion()
            self.seleccionar_movimiento()
            self.seleccionar_movimiento_a_imputar()
            self.ingresar_numero_de_operacion(self.orden)
            self.seleccionar_buscar()
            self.seleccionar_checbox_ok()
            self.seleccionar_imputar()
            self.seleccionar_aceptar_autoriz() 
            self.wait(5)
            self.validar_msj_exito_2()
            self.wait(2)
            self.selecionar_bandeja()
            self.wait(5)       
            self.selecionar_bajas()
            self.wait(10) 
            self.validar_numero_orden_en_bajas(self.orden)
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
