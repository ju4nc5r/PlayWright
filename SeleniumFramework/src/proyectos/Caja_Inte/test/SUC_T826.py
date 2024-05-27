# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
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
@allure.story(u'Envio de Remesa Interna')
@allure.testcase(u"SUC-T826 - Envió de Remesas Interna CAJA - CAF Antes del Cierre de Caja (UIC10020)")
@allure.title(u'SUC-T826 - Envió de Remesas Interna CAJA - CAF Antes del Cierre de Caja (UIC10020)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(    
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo: UIC10020 / Terminal: IA0500820/ Contraseña:Ingreso20</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10020 y visualizar los datos del operador UIC10020</br>
5.-Hacer clic en el recuadro Hola, UIC10020 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - Consulta de Saldos.</br>
7.-Verificar Los Saldos</br>
8.-Verificar los Saldos Caja - Moneda Pesos</br>
9.-Copiar el Saldo de la moneda Pesos y copiarlo en la tx Envió de Remesa Interna.</br>
10.-Hacer clic en el Botón "SALIR"</br>
11.-Hacer clic en la Transacción - Envio de Remesa Interna</br>
12.-Visualizar en pantalla el titulo Remesa Interna - Cajero</br>
13.-Seleccionar en Origen "Caja"</br>
14.-Seleccionar Destino "Caf"</br>
15.-Seleccionar Moneda "Pesos"</br>
16.-Ingresar Importe</br>
17.-Hacer clic en el Botón "CONFIRMAR"</br>
18.-Visualizar el recuadro de los datos de la TX y hacer clic en el boton CONFIMAR "CONFIRMAR"</br>
19.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
20.-Visualizar la impresión del ticket</br>
21.-Hacer clic en la Transacción - Consulta de Saldos.</br>
22.-Verificar los Saldos Caja - Moneda Dolares</br>
23.-Copiar el Saldo de la moneda Dolares y copiarlo en la tx Envio de Remesa Interna.</br>
24.-Hacer clic en el Botón "SALIR"</br>
25.-Hacer clic en la Transacción - Envió de Remesa Interna</br>
26.-Seleccionar en Origen "Caja"</br>
27.-Seleccionar Destino "Caf"</br>
28.-Seleccionar Moneda "Dolares"</br>
29.-Ingresar Importe</br>
30.-Hacer clic en el Botón "CONFIRMAR" "CONFIRMAR"</br>
31.-Visualizar el recuadro de los datos de la TX y hacer clic en el Botón "CONFIRMAR"</br>
32.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
33.-Visualizar la impresión del ticket</br>
34.-Hacer clic en la Transacción - Consulta de Saldos.</br>
35.-Verificar los Saldos Caja - Moneda Dolares</br>
36.-Copiar el Saldo de la moneda Euros y copiarlo en la tx Envió de Remesa Interna.</br>
37.-Hacer clic en el Botón "SALIR"</br>
38.-Hacer clic en la Transacción - Envió de Remesa Interna</br>
39.-Seleccionar en Origen "Caja"</br>
40.-Seleccionar Destino "Caf"</br>
41.-Seleccionar Moneda "Euros"</br>
42.-Ingresar Importe</br>
43.-Hacer clic en el Botón "CONFIRMAR"</br>
44.-Visualizar el recuadro de los datos de la TX y hacer clic en el boton "CONFIRMAR"</br>
45.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el botón "FINALIZAR"</br>
46.-Visualizar la impresión del ticket</br>
47.-Hacer clic en el recuadro Hola, UIC10007</br>
48.-Hacer clic en CERRAR SESIÓN</br>
"""
)
class SUC_T826(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T826(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()      
            self.monedas = ["Pesos","Dolares","Euros"]
            self.posiciones = ["1","2","3"]
            self.posiciones1 = ["1","2","3"]
            self.seleccionarConsultaDeSaldo()
            for posicion in self.posiciones:       
                self.verificarSaldosDeCaja(posicion)       
                if self.monedaSaldo == "0,00" and posicion =='1':
                    self.monedas.remove("Pesos")
                    self.posiciones1.remove('1')
                    print("se elimina Moneda Pesos de la lista")           
                elif self.monedaSaldo == "0,00" and posicion =='2':
                    self.monedas.remove("Dolares")
                    self.posiciones1.remove('2')
                    print("se elimina Moneda dolares de la lista")
                    
                elif self.monedaSaldo == "0,00" and posicion =='3':
                    self.monedas.remove("Euros")
                    self.posiciones1.remove('3')
                    print("se elimina Moneda Euros de la lista")          
                    print(self.monedas) 
                    
            if self.monedas == []:
                self.skip_msg(u"Los saldos de las monedas en Caja Estan En ceros,No se puede hacer el pase sin saldos{}".format(self.monedas))
               
            self.seleccionarSalir()            
            for moneda,posicion in zip(self.monedas,self.posiciones1):  
                self.obtenerSaldosDeCaja(posicion)           
                self.seleccionarEnvioDeRemesaInterna()
                self.clickRadioBtn("Caja")
                self.mostrarDestino("Caf")
                self.mostrarMoneda(moneda)
                self.ingresarImporte(self.monedaSaldo,moneda)
                self.seleccionarConfirmar()
                texto = ["Origen","Destino","Moneda","importe"]
                datos = ["Caj","Caf",moneda,self.monedaSaldo]
                self.frecuencia = []
                for dato,text in zip(datos,texto):
                    self.frecuencia.append(dato)                
                    self.validarDatos(dato,text)
                print(self.frecuencia)
                self.seleccionarConfirmar3() 
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
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
       # self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
