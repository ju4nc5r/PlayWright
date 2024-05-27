# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,MENSAJE_IMPRESION,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA
             

@allure.feature(u'Operaciones de Caja')
@allure.story(u'Cierre Forzado de Caja')
@allure.testcase(u"SUC-T877 - Cierre Forzado de Caja")
@allure.title(u'SUC-T877 - Cierre Forzado de Caja')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822 / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10022</br>
5.-Hacer clic en Cierre Forzado de Caja</br>
6.-Visualizar en pantalla el Recuadro de los Operadores activos</br>
7.-Hacer clic y seleccionar el Operador UIC10022</br>
8.-Hacer clic en el Botón "SIGUIENTE"</br>
9.-Seleccionar sin diferencia en celda de moneda Pesos
10.-Seleccionar sin diferencia en celda de moneda Dolares
11.-Seleccionar sin diferencia en celda de moneda Euros
12.-Seleccionar sin diferencia en celda de moneda Reales
13.-Hacer clic en el Botón "CERRAR CAJA"
15.-Visualizar mensaje Operacion Finalizada con Exito
</br>   
"""
)
class SUC_T877(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T877(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.verificar_operadores_activos()
            for operador in range(1,self.vueltas):
                self.wait(1)
                operador = 1
                self.seleccionar_cierre_forzado() 
                self.seleccionar_recuadro_operadores()
                self.seleccionar_item_operador(str(operador))
                self.seleccionar_siguiente()
                posiciones = ["1","2","3","4"]
                for posicion in posiciones:
                    self.wait(1)
                    self.seleccionar_sin_diferencia(posicion)
                self.seleccionar_cerrar_caja()
                self.verificarMensajeExitoExtracciones(self.mensaje)
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
