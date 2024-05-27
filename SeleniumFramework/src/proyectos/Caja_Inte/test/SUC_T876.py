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
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA, MSJ_ESPERADO,IMPORTE,DIAS,MONEDA,\
              USER_AUTO,PASSWORD_AUTO,TERMINAL_AUTO
             

@allure.feature(u'Plazo Fijo')
@allure.story(u'Pago Plazo Fijo Efectivo')
@allure.testcase(u"SUC-T876 - Pago Plazo Fijo Efectivo - Nivel Autorizante")
@allure.title(u'SUC-T876 - Pago Plazo Fijo Efectivo - Nivel Autorizante')
@allure.link(u'')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-inte.ocprch.sis.ad.bia.itau/#/login</br> 
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br> 
3.-Hacer clic en el botón "INGRESAR"</br> 
4.-Validar nombre del Operador "Hola, UIC10021</br> 
5.-Hacer clic en la transaccion Pago Plazo Fijo Efectivo</br> 
6.-Visualizar en pantalla el Recuadro Numero de Certificado</br> 
7.-Ingresar Numero de Certificado "23540"</br> 
8.-Hacer clic en el Botón "SIGUIENTE"</br> 
9.-Visualizar en pantalla los datos del Plazo Fijo Efectivo</br> 
10.-Hacer clic en el Botón "SIGUIENTE</br> "
11.-Visualizar firmantes</br> 
12.-Hacer clic en el check de firma</br> 
13.-Hacer clic en el Botón "SIGUIENTE"</br> 
14.-Visualizar el recuadro de autorizacion por Validación por falta de firma (Gerente)</br> 
15.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br> 
16.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10023 / Terminal: IA0500823 / Contraseña:Ingreso23</br> 
17.-Visualizar la autorización en estado pendiente</br> 
18.-Hacer clic en el botón ACEPTAR</br> 
19.-Hacer clic en el botón AUTORIZAR</br> 
20.-Hacer clic en el botón Salir</br> 
21.-Volver al aplicación ICaja</br> 
22.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br> 
23.-Visualizar el Mensaje - "Operación realizada con éxito"</br> 
24.-Hacer el botón "FINALIZAR"</br> 
25.-Visualizar la impresión del ticket</br> 
26.-Validar que en el ticket se muestre el Nivel Autorizante " TX. AUTORIZADA POR UIC10023"</br> 
27.-Hacer clic en la Transacción - "Reverso de Transacción"</br> 
28.-En el ticket visualizar el numero de Tx copiarla e ingresarla en el campo Numero de secuencia</br> 
29.-Visualizar los datos de la Transacción</br> 
30.-Hacer clic en el recuadro y seleccionar "Otros motivos"</br> 
31.-Marcar el check "El cliente presente ticket"</br> 
32.-Hacer clic en el Botón "CONFIRMAR"</br> 
33.-Realizar el Login en el modulo de administración de Autorizaciones: https://fe-autorizacion-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/</br> 
34.-Realizar login e ingresar los datos del operador centralizador: Legajo: UIC10023 / Terminal: IA0500823 / Contraseña:Ingreso23</br> 
35.-Visualizar la autorización en estado pendiente</br> 
36.-Hacer clic en el botón ACEPTAR</br> 
37.-Hacer clic en el botón AUTORIZAR</br> 
38.-Hacer clic en el botón Salir</br> 
39.-Volver al aplicación ICaja</br> 
40.-Visualizar el recuadro de la autorización y hacer clic en el botón ACEPTAR</br> 
41.-Visualizar el Mensaje - "Operación realizada con éxito"</br> 
42.-Hacer clic en Botón "FINALIZAR"</br> 
43.-Visualizar la impresión del ticket</br> 
44.-Hacer clic en el recuadro Hola, UIC10021</br> 
45.-Hacer clic en CERRAR SESIÓN</br> 
</br>   
"""
)
class SUC_T876(unittest.TestCase, stICajaInicio, stICaja , stICajaTickets,stAutorizInicio):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T876(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionar_pago_de_plazo_fijo() 
            self.ingresar_nro_certificado("23540")
            self.seleccionarSiguiente()
#             self.visualizar_msj_no_hay_deposito_disponible()  
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
        self.user_auto = self.usuario.get(USER_AUTO)
        self.clave_auto = self.usuario.get(PASSWORD_AUTO)
        self.terminal_auto = self.usuario.get(TERMINAL_AUTO)
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
