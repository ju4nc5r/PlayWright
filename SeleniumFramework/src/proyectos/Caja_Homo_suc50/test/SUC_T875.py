# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stAutorizInicio import stAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st import fin
from SeleniumFramework.common_functions import get_user_caja_homo_suc_50
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,MENSAJE_IMPRESION,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA
             

@allure.feature(u'Plazo Fijo')
@allure.story(u'Pago Plazo Fijo Efectivo')
@allure.testcase(u"SUC-T875 - Pago Plazo Fijo Efectivo")
@allure.title(u'SUC-T875 - Pago Plazo Fijo Efectivo')
@allure.link(u'')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21
3.-Hacer clic en el botón "INGRESAR"
4.-Validar nombre del Operador "Hola, UIC10021
5.-Hacer clic en la trassacicion Pago Plazo Fijo Efectivo
6.-Visualizar en pantalla el Recuadro Numero de Certificado
7.-Ingresar Numero de Certificado "23540"
8.-Hacer clic en el Botón "SIGUIENTE"
9.-Visualizar en pantalla los datos del Plazo Fijo Efectivo
10.-Hacer clic en el Botón "SIGUIENTE"
11.-Visualizar firmantes
12.-Hacer clic en el check de firma
13.-Hacer clic en el Botón "SIGUIENTE"
14.-Visualizar el Mensaje - "Impresión finalizada con éxito "
15.-Hacer el botón "FINALIZAR"
16.-Visualizar la impresión del ticket
17.-Hacer clic en la Transacción - "Reverso de Transacción"
18.-En el ticket visualizar el numero de Tx copiarla e ingresarla en el campo Numero de secuencia
19.-Visualizar los datos de la Transacción
20.-Hacer clic en el recuadro y seleccionar "Otros motivos"
21.-Marcar el check "El cliente presente ticket"
22.-Hacer clic en el Botón "CONFIRMAR"
23.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/
24.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10023 / Terminal: IA0500823 / Contraseña:Ingreso23
25.-Visualizar la autorización en estado pendiente
26.-Hacer clic en el botón ACEPTAR
27.-Hacer clic en el botón AUTORIZAR
28.-Hacer clic en el botón Salir
29.-Volver al aplicación ICaja
30.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR
31.-Visualizar el Mensaje - "Operación realizada con éxito"
32.-Hacer clic en Botón "FINALIZAR"
33.-Visualizar la impresión del ticket
34.-Hacer clic en el recuadro Hola, UIC10021
35.-Hacer clic en CERRAR SESIÓN
</br>   
"""
)
class SUC_T875(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T875(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_pago_de_plazo_fijo() 
            self.ingresar_nro_certificado("23562")
            self.seleccionarSiguiente()
            self.visualizar_msj_no_hay_deposito_disponible()  
            self.visualizar_datos_plazo_fijo()
            self.seleccionarSiguiente2()
            self.visualizar_firmante()
            self.seleccionar_chek_firmante()
            self.seleccionarSiguiente3ros()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizar_pago_plazo_fijo()
            self.seleccionarAceptarAutoriz()    
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")  
            self.verificar_autorizante("TX.  AUTORIZADA  POR    UIC10023")
            self.obtener_nro_transaccion_pf()
            self.seleccionarRevesoDeTrasaccion()
            self.ingresarNroTranssaccion(self.nro)
            self.mostrarTiposDeMotivos()
            self.seleccionarMotivo("Otros motivos")
            self.seleccionarConfirmar()
            self.obtenerNroDeAutorizacion()
            self.validarBotonAutorizacionesSolicitadas()
            self.autorizarOperacionSucursal50()
            self.seleccionarAceptarAutoriz()
            self.verificarMensajeExitoExtracciones("Operación realizada con éxito")
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
