# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE, \
    MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
              TIPO_DE_OPERACION,IMPORTE_A_VALIDAR,OPERACION_A_VALIDAR,CANTIDAD_DE_OFICIOS

@allure.feature(u'Cobros')
@allure.story(u'Arancelamiento de Oficios')
@allure.testcase(u"ICaja SUC-T793 - Realizar la Tx Arancelamiento de Oficios")
@allure.title(u'SUC-T793 - Realizar la Tx Arancelamiento de Oficios')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""  
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - "Arancelamiento de Oficios"</br>
7.-Ingresar la cantidad de Oficios "1"</br>
8.-Visualizar el importe Total $ "25,00"</br>
9.-Hacer clic en "SIGUIENTE"</br>
10.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
11.-Visualizar el Mensaje - "Operación realizada con éxito"</br>
12.-Hacer clic en el Botón "VALIDAR"</br>
13.-Visualizar el mensaje "Timbrado de cobro con éxito"</br>
14.-Hacer clic en Botón "FINALIZAR"</br>
15.-Visualizar la impresión del ticket</br>
16.-Hacer clic en el recuadro Hola, UIC10021</br>
17.-Hacer clic en CERRAR SESIÓN </br>  
"""
) 
class SUC_T793(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
              
    def test_SUC_T793(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarAceleramientoDeOficios()
            self.VisualizarCantidadDeOficios(self.cantidadDeOficios)
            self.visualizarLblDeshabilitado()
            self.seleccionarSiguiente() 
            self.validarOficios(self.cantidadDeOficios)
            self.validarImporteOpn(self.valor_A_validar)  
            self.seleccionarConfirmar() 
            self.seleccionarValidar()
            self.visualizarMensajeExitoOpn("Timbrado realizado con exito")
            self.visualizarTicket()
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucudestino = self.usuario.get(SUCURSAL_ORIG)
        self.Sucursal_orig = self.usuario.get(SUCURSAL_DEST)
        self.nroControl = self.usuario.get(NRO_CONTROL)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.sucursal = self.usuario.get(SUCURSAL) 
        self.tipoDeOperacion = self.usuario.get(TIPO_DE_OPERACION)
        self.valor_A_validar = self.usuario.get(IMPORTE_A_VALIDAR)   
        self.operacionAValidar = self.usuario.get(OPERACION_A_VALIDAR)
        self.cantidadDeOficios = self.usuario.get(CANTIDAD_DE_OFICIOS)

        
           
        

if __name__ == "__main__":
    unittest.main()
