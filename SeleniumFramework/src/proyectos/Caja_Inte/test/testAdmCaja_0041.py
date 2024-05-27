# -*- coding: utf-8 -*-
import unittest
import allure
import traceback

from proyectos.Caja_Homo.st.stAdminInicio import stAdminInicio
from proyectos.Caja_Homo.st.stAdminParametria import stAdminParametria
from proyectos.Caja_Homo.st import inicioAdminCaja
from proyectos.Caja_Homo.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL, CLAVE, \
     TIT_ESPERADO, TIPO_LIMITE, LIMITE_MAX_DOLARES,LIMITE_MAX_EUROS, \
     LIMITE_MAX_PESOS, LIMITE_MAX_REALES, MSJ_ESPERADO                                                                   

@allure.feature(u'Administracion de cajas')
@allure.story(u'Parametria')
@allure.testcase(
    u"Adm.Caja - Caso de Prueba 0041", u''
)
@allure.title(u'test_0041 - Parametria de límites máximos y mínimos. Editar Sucursal')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    1-Ingresar a la pagina del modulo de Administracion.
    2-Colocar  el usuario y password y hacer clik en Aceptar.
    3-Visualizar los datos del usuario: 
    Legajo.
    Usuario.
    Terminal.
    Sucursal.
    4-Visualizar en pantalla  la parametria de los limites maximos y minimos.     
    5-Hacer click  en el Boton Editar Sucursal 
    6-Visualizar en pantalla el recuadro "Edición de limites máximos y mínimos para una sucursal"
    7-Poder seleccionar la opcion "Límite máximo para CAF"
    8-Ingresar un monto en la seleccion moneda Pesos
    9-Ingresar un monto en la seleccion moneda Dolares.
    10-Ingresar un monto en la seleccion moneda Euros.   
    11-Ingresar un monto en la seleccion moneda Reales.    
    12-Hacer click  en el Boton Guardar.      
    13-Hacer click  en el Boton  Aceptar para confirmar.
    14- Validar el mensaje Se ha actualizado para todas las sucursales el límite          
    15-Validar que los montos se hayan actualziados correctamente  
    16-Hacer click  en el Boton Salir "Salir de la aplicacion"      
    """
)
class tstAdmCaja_0041(unittest.TestCase, stAdminParametria, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0041(self):
        try:
            self.usuario = get_user_caja_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.wait(5)
            self.seleccionarParametria()
            self.wait(5)
            self.seleccionarLimitesMaxMin()
            self.validarTituloParametria(self.tituloEsperado)
            self.validarLimitesMaxMin()
            self.mostrarItemsPorPagina()
            self.seleccionarDiezItems()
            self.seleccionarEditarSucursal(self.tipoLimite)
            # self.visualizarTiposDeLimite()
            # self.seleccionarTipoDeLimite(self.tipoLimite)
            self.ingresarLimitePesos(self.limMaxPesos)
            self.ingresarLimiteDolares(self.limMaxDolares)
            self.ingresarLimiteEuros(self.limMaxEuros)
            self.ingresarLimiteReales(self.limMaxReales)
            self.seleccionarGuardarLimites()
            self.seleccionarAceptarCambios()
            self.validarMensajeDeActualizacion(self.msjEsperado)
            self.mostrarItemsPorPagina()
            self.seleccionarDiezItems()
            self.validarCambiosDeLimites(self.tipoLimite,self.limMaxPesos,
                    self.limMaxDolares,self.limMaxEuros,self.limMaxReales)
            self.wait(5)
            self.seleccionarSalirApp()
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
        self.sucursal = self.usuario.get(SUCURSAL)
        self.tituloEsperado = self.usuario.get(TIT_ESPERADO)
        self.tipoLimite = self.usuario.get(TIPO_LIMITE)
        self.limMaxPesos = self.usuario.get(LIMITE_MAX_PESOS)
        self.limMaxDolares = self.usuario.get(LIMITE_MAX_DOLARES)
        self.limMaxEuros = self.usuario.get(LIMITE_MAX_EUROS)   
        self.limMaxReales = self.usuario.get(LIMITE_MAX_REALES)     
        self.msjEsperado = self.usuario.get(MSJ_ESPERADO)   


if __name__ == "__main__":
    unittest.main()
