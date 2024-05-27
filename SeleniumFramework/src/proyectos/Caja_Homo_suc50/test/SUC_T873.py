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
             

@allure.feature(u'Plazo Fijo')
@allure.story(u'Deposito a Plazo Fijo en Cuenta')
@allure.testcase(u"SUC-T873 - Depósito Plazo Fijo Débito en Cuenta - Fecha de Vencimiento")
@allure.title(u'SUC-T873 - Depósito Plazo Fijo Débito en Cuenta - Fecha de Vencimiento')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br>         
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la trassacicion Deposito a Plazo Fijo en Cuenta</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Ingresar los datos del cliente</br>
8.-Seleccionar Tipo de Documento "DNI"</br>
 9.-Ingresar Numero de Documento "29005251"</br>
10.-Hacer clic en el Botón "IDENTIFICAR"</br>
11.-Hacer clic en el Botón "SIN CLAVE"</br>
12.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
13.-Hacer clic en el recuadro "Cuenta debito"</br>
14.-Seleccionar cuenta "CA $ / 0000673-301/9 "</br>
15.-Hacer clic en el recuadro "Tipo de plazo fijo"</br>
16.-Seleccionar item "CLASICO "</br>
17.-Hacer clic en el check del recuadro Fecha de Vencimiento</br>
18.-Seleccionar la cantidad de dias "35"</br>
19.-Hacer clic en el recuadro "Monto" e Ingresar: "20.000,00"</br>
20.-Hacer clic en el botón "Simular"</br>
21.-Visualizar pantalla con datos de simulación.</br>
22.-Hacer clic en el botón "IMPRIMIR"</br>
23.-Visualizar la impresión del ticket</br>
24.-Hacer clic en el boton "CONFIRMAR"</br>
25.-Visualizar la impresión del ticket</br>
26.-Hacer clic en el check "Marcar si coincide"</br>
27.-Hacer clic en el boton "CONFIRMAR"</br>
28.-Visualizar el Mensaje - "Impresión finalizada con éxito "</br>
29.-Hacer el boton "FINALIZAR"</br>
30.-Visualizar la impresión del ticket</br>
31.-Hacer clic en el recuadro Hola, UIC10021</br>
32.-Hacer clic en CERRAR SESIÓN</br>
</br>   
"""
)
class SUC_T873(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T872(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_deposito_de_plazo_fijo_en_cuenta() 
            self.identificarCliente() 
            self.seleccionar_recuadro_cuenta_debito_PL()
            self.wait(1)
            self.seleccionar_recuadro_tp_plazo_fj()
            self.seleccionar_item_plazo_fj("PF MAX")
            self.seleccionar_fecha_Vecimiento()
            self.seleccionar_calendario()
#             self.ingresar_dias("35")
#             self.ingresarImporte("2000000", self.moneda)
#             self.seleccionar_bto_simular()
#             self.visualizar_datos_de_simulacion()
#             self.seleccionar_confirmar()
#             self.seleccionar_check_marca_si_coincide()
#             self.seleccionarConfirmar()
#             self.verificarMensajeExitoExtracciones(self.mensaje) 
#             self.visualizarTicket2()
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
