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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO, NRO_CONTROL, SUCURSAL_DEST,SUCURSAL_ORIG,\
              IMPORTE_A_VALIDAR,OPERACION_A_VALIDAR,OPERACION1,OPERACION2,OPERACION3,\
              OPERACION_VALIDAR1,OPERACION_VALIDAR2,IMPORTE1,IMPORTE2,IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,\
              NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,NUMERO_TARJETA,NUMERO_SOCIO,MARCA_TARJETA,MARCA_TARJETA1,CUENTA1


@allure.feature(u'Cobros de Tarjeta de Credito')
@allure.story(u'Cobros de Tarjeta de Credito')
@allure.testcase(u"ICaja - SUC-T857 -Cobro de Tarjeta de Crédito - Numero de Socio ")
@allure.title(u'SUC-T857 - Cobros de Tarjeta de Crédito ')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción - "Cobro de Tarjeta de Crédito"</br>
6.-Visualizar en pantalla el Recuadro identificar cliente</br>
7.-Hacer clic en la opción "NO"</br>
8.-Visualizar la opción Numero de Socio</br>
9.-Ingresar el numero de Socio "0000320017"</br>
10.-Seleccionar Marca "Visa"</br>
11.-Seleccionar Moneda "Pesos"</br>
12.-Hacer clic en el recuadro "Importe" e ingresar "75"</br>
13.-Hacer clic en el Botón "SIGUIENTE"</br>
14.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
15.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el Botón "FINALIZAR"</br>
16.-Visualizar la impresión del ticket</br>
17.-Hacer clic en el recuadro Hola, UIC10021</br>
18.-Hacer clic en CERRAR SESIÓN</br>
"""
)

class SUC_T857(unittest.TestCase, stICajaInicio, stICaja,stAutorizInicio, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
              
    def test_SUC_T857(self):
        try: 
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarCobroDeTarjetaCredito()
            self.visualizarCuadroNecesitaIdentificarAlCliente2()
            self.clickRadioBtn3(self.operacion3)
            self.ingresarNroTarjeta(self.numeroSocio, self.operacion3)
            self.mostrarTiposDeTarjeta(self.marcaDeTarjeta)
            self.mostrarTiposDeMoneda2(self.tipoMoneda) 
            self.ingresarImporte(self.importe2,self.tipoMoneda)
            self.seleccionarSiguiente()
            datos = [self.numeroSocio,self.marcaDeTarjeta,self.nombreYApellido2,self.operacion_validar1,self.tipoMoneda,self.importe_validar2]
            texto = ["Numero de socio: ", "Marca: ","Nombre como figura en la Tarjeta: ","Forma de Pago: ","Moneda: ","Importe a debitar: " ]
            self.frecuencia =[]
            for dato,text in zip(datos,texto):
                self.frecuencia.append(dato)                
                self.validarDatos(dato,text)     
            print(self.frecuencia)  
            self.seleccionarConfirmar()
            self.visualizarMensajeExito()  
            self.verificarMensajeExitoExtracciones(self.mensaje)  
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importe_validar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importe_validar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.operacion1= self.usuario.get(OPERACION1)
        self.operacion2= self.usuario.get(OPERACION2)  
        self.operacion3= self.usuario.get(OPERACION3)
        self.operacion_validar1= self.usuario.get(OPERACION_VALIDAR1)
        self.operacion_validar2= self.usuario.get(OPERACION_VALIDAR2)
        self.nombreYApellido1= self.usuario.get(NOMBRE_APELLIDO1)
        self.nombreYApellido2= self.usuario.get(NOMBRE_APELLIDO2)
        self.numeroTarjeta = self.usuario.get(NUMERO_TARJETA)
        self.numeroSocio = self.usuario.get(NUMERO_SOCIO)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.marcaDeTarjeta = self.usuario.get(MARCA_TARJETA)
        self.marcaDeTarjeta1 = self.usuario.get(MARCA_TARJETA1)
        self.cuentaDebito = self.usuario.get(CUENTA1)
        
if __name__ == "__main__":
    unittest.main()
