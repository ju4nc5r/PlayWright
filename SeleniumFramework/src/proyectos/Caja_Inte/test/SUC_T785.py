# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
# from SeleniumFramework.src.proyectos.Caja_Inte.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO
             

@allure.feature(u'Remesas')
@allure.story(u'Envío de Remesas de Cheques')
@allure.testcase(u'ICaja - SUC-T785 - Envio Remesas de cheques')
@allure.title(u'SUC-T785 - Envio Remesas de cheques')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(  
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción "Consulta de Totales"</br>
7.-Validar Número de Sucursal "0050"</br>
8.-Validar moneda "Pesos"</br>
9.-Hacer clic en el botón "CONSULTAR"</br>
10.-Visualizar el Mensaje "Se ha impreso un comprobante de su consulta"</br>
11.-Visualizar el ticket de la impresión</br>
12.-Buscar el ítem Total de Imgresos "Cheque.." y copiar el monto de los cheques depositados</br>
13.-Hacer clic en Botón "CANCELAR"</br>
14.-Hacer clic en la Transacción "Envío de Remesas de Cheques"</br>
15.-Validar moneda "Pesos"</br>
16.-Pegar el monto de los cheques depositados en el campo "Importe"</br>
17.-Hacer clic en Botón "CONFIRMAR"</br>
18.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
19.-Visualizar el Mensaje - Operación Realizada Con Éxito.</br>
20.-Hacer clic en Botón "FINALIZAR"</br>
21.-Visualizar la impresión del ticket</br>
22.-Hacer clic en el recuadro Hola, UIC10021</br>
23.-Hacer clic en CERRAR SESIÓN</br>
"""
)
class SUC_T785(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T785(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login() 
            self.seleccionarConsultaDeTotales()
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.seleccionarConsultar()
            self.verificarSaldoDeCheques()
            self.seleccionarCancelar()       
            self.seleccionarEnvioDeRemesasDeCheques()
            self.visualizar_msj_no_hay_operaciones_con_cheques()
            self.mostrarTiposDeMoneda()
            self.seleccionarTipoDeMoneda(self.tipoMoneda)
            self.ingresarImporte(self.saldoCheques,self.tipoMoneda)
            self.seleccionarConfirmar()
            datos = [self.tipoMoneda,self.saldoCheques.strip()]
            texto = ["Moneda", "Importe"]                                       
            self.frecuencia = []
            for dato,text in zip(datos,texto):
                self.frecuencia.append(dato)                
                self.validarDatos(dato,text)
            print(self.frecuencia)      
            self.seleccionarConfirmar3() 
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
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
    # self.mensaje = "La operacion finalizo correctamente"
        
        
    
        

if __name__ == "__main__":
    unittest.main()