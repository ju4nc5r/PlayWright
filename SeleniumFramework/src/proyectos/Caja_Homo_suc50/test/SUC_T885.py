# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,MENSAJE_IMPRESION,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA
from asyncio.tasks import sleep
             

@allure.feature(u'Cobros')
@allure.story(u'Cobro de Servicios - CML')
@allure.testcase(u"SUC-T885 - Cobro de Servicios - CML")
@allure.title(u'SUC-T885 - Cobro de Servicios - CML')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja:</br>
https://fe-icaja-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la transaccion Servicio de Cobros CML</br>
6.-Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?</br>
7.-Hacer clic en el boton SI</br>
8.-Ingresar los datos del cliente</br>
9.-Seleccionar Tipo de Documento "DNI"</br>
10.-Ingresar Numero de Documento "20203570"</br>
11.-Hacer clic en el Botón "IDENTIFICAR"</br>
12.-Hacer clic en el Botón "SIN CLAVE"</br>
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
14.-Hacer hecklist en "Mismo Documento que Cliente Identificado"</br>
15.-Hacer clic en el boton "SIGUIENTE"</br>
16.-Hacer clic en Convenios Habilitados y Seleccionar "ACINDAR COBRANZAS IMPUTADAS"</br>
17.-Hacer clic en el boton "SIGUIENTE"</br>
18.-Hacer clic en NUEVO DOCUMENTO</br>
19.-Seleccionar tipo "Factura"</br>
20.-Ingresar numero "20241010"</br>
21.-Ingresar Cuota "1"</br>
22.-Ingresar Monto "10.000,00"</br>
23.-Hacer clic "AGREGAR"</br>
24.-Hacer clic en la flecha, el monto debera cambiar a color verde</br>
25.-Hacer clic el boton "FIN CARGA"</br>
26.-¿Se utilizarán CHEQUES para realizar el pago de esta transacción? Hacer clic en "NO"</br>
27.-Visualizar el resumen en pantalla</br>
28.-Formas de pago "Efectivo" agregar "10.000,00"</br>
29.-Hacer clic en el Botón "CONFIRMAR"</br>
30.-Visualizar el Mensaje - "Impresión finalizada con éxito "</br>
31.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
32.-Hacer clic en Botón "FINALIZAR"</br>
33.-Visualizar la impresión del ticket</br>
34.-Hacer clic en el recuadro Hola, UIC10021</br>
35.-Hacer clic en CERRAR SESIÓN</br>
</br>   
"""
)
class SUC_T885(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T885(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_cobros_CML()
            self.visualizarCuadroNecesitaIdentificarAlCliente()
            self.identificarCliente()
            self.selecionar_boton_costumers()
            self.seleccionar_check_box()            
            self.seleccionar_siguiente_5()
            self.seleccionar_reacuadro_C_H()
            self.seleccionar_opcion_("ACINDAR COBRANZAS IMPUTADAS")
            self.seleccionar_siguitente_6()
            self.seleccionar_nuevo_doc()
            self.seleccionar_recuadro_tipo()
            self.seleccionar_factura()
            self.ingresar_numero("20241010")
            self.ingresar_cuota("1")
            self.ingresar_monto_servicio_2("10.000,00")
            self.seleccionar_agregar()
            self.seleccionar_flecha_azul()
            self.validar_monto_en_verde("10.000,00")
            self.seleccionar_fin_de_carga()
            self.seleccionar_NO()
            self.visualizar_datos_resumen()
            self.ingresar_monto_3("10.000,00")
            self.seleccionar_Confirmar()
            self.visualizarMensajeExito()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")
            self.visualizarTicket2()
            self.cerrarSesion()
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
        self.nombreCliente = self.usuario.get(NOMBRE)
        self.apellidoCliente = self.usuario.get(APELLIDO)
        self.tipoDoc = self.usuario.get(TIPO_DOC_CLIENTE)
        self.documento =  self.usuario.get(NRO_DOC_CLIENTE)
        self.cuenta = self.usuario.get(CUENTA)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.mensaje_impresion = self.usuario.get(MENSAJE_IMPRESION)
        self.importe = self.usuario.get(IMPORTE)
        self.dias = self.usuario.get(DIAS)
        self.moneda = self.usuario.get(MONEDA)
        

if __name__ == "__main__":
    unittest.main()
