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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO,MONEDA1,MONEDA2,MONEDA3
             

@allure.feature(u'Operaciones de Caja')
@allure.story(u'Ingreso / Egreso Externo')
@allure.testcase(u"SUC-T835 -Ingreso / Egreso Externo (Nivel Cajero)")
@allure.title(u'SUC-T835 - Ingreso / Egreso Externo (Nivel Cajero)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(    
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - Ingreso / Egreso Externo</br>
6.-Visualizar el mensaje "Transacción no autorizada / Solo puede ingresar a esta transacción un operador Centralizador "</br>
7.-Hacer clic en el Botón "ACEPTAR"</br>
8.-Hacer clic en el recuadro Hola, UIC10021</br>
9.-Hacer clic en CERRAR SESIÓN</br>
"""
)
class SUC_T835(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T835(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()      
            self.seleccionarMnuIngresoEgresoExterno()
            self.validarMensajeTransaccionAutorizada3("Transaccion no autorizadaSolo puede ingresar a esta transacción un operador Centralizador")
            self.seleccionarAceptar2()
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
        self.moneda = self.usuario.get(MONEDA)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2= self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
