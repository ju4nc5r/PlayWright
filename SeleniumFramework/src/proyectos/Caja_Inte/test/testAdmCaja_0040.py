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
    u"Adm.Caja - Caso de Prueba 0040", u''
)
@allure.title(u'test_0040 - Parametria de límites máximos y mínimos. Editar Sucursales')
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
    5-Hacer click  en el Boton Editar Sucursales 
    6-Visualizar en pantalla el recuadro "Edición de limites máximos y mínimos para todas las sucursales"
    7-Hacer click en el boton "Tipo de Limite"
    8-Poder seleccionar la opcion "Retención de caja"
    9-Ingresar un monto en la seleccion moneda Pesos
    10-Ingresar un monto en la seleccion moneda Dolares.
    11-Ingresar un monto en la seleccion moneda Euros.   
    12-Ingresar un monto en la seleccion moneda Reales.    
    13-Hacer click  en el Boton Guardar.      
    14-Hacer click  en el Boton  Aceptar para confirmar.
    15- Validar el mensaje Se ha actualizado para todas las sucursales el límite          
    16-Validar que los montos se hayan actualziados correctamente  
    17-Hacer click  en el Boton Salir "Salir de la aplicacion"      
    """
)
class tstAdmCaja_0040(unittest.TestCase, stAdminParametria, stAdminInicio):
    def setUp(self):
        inicioAdminCaja(self)
        
    def testAdmCaja_0040(self):
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
            self.seleccionarEditarSucursales()
            self.visualizarTiposDeLimite()
            self.seleccionarTipoDeLimite(self.tipoLimite)
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
