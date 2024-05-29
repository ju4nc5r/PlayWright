# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from proyectos.Caja_Homo.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte, get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST            
import pytest

@allure.feature(u'ICaja')
@allure.story(u'Ingreso Interno del Numerario')
@allure.testcase(
    u"test_0094 - Ingreso Interno del Numerario - pesos", u''
)
@allure.title(u'test_0094 - Ingreso Interno del Numerario - Pesos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Hacer clic en la transacción: Ingreso/Egreso Interno  
    2-Visualizar en pantalla el cuadro: Egreso Interno del Numerario  
    3-Hacer clic en el recuadro: Monedas 
    4-Seleccionar Moneda: pesos
    5-Ingresar Valor 1000
    6-Hacer click en el Boton: ACEPTAR
    7-Visualizar el mensaje: La operacion finalizo correctamente 
    8-Hacer click en el Boton:ACEPTAR
    """
)
class tstICaja_0094(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def testICaja_0094(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarMnuIngresoEgreso()
            self.seleccionarEgresoInternoNumerario()
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarValor(self.valor)
            self.seleccionarAceptarNun()
            # self.verificarMsjeExitoImpreOK("Impresion OK")
            self.verificarMensajeExitoEgresoIngresoInterno(self.mensaje)  
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucuorigen = self.usuario.get(SUCURSAL)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        #self.mensaje = "La operacion finalizo correctamente"       


if __name__ == "__main__":
    unittest.main()
