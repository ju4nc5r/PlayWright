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
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO
             

@allure.feature(u'Remesas')
@allure.story(u'Envio de Remesa')
@allure.testcase(u"ICaja - SUC-T808 - Envió de Remesa - Tesorero (Caja - Intermedio - Sucursal) Antes del Cierre de Caja (UIC10022)")
@allure.title(u'SUC-T808 - Envió de Remesa - Tesorero (Caja - Intermedio - Sucursal) Antes del Cierre de Caja (UIC10022)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(

u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22
3.-Hacer clic en el botón "INGRESAR"
4.-Validar el nombre de usuario "Hola, UIC10022
5.-Hacer clic en la Transacción - Consulta de Saldos.
6.-Verificar los Saldos Caja - Moneda Pesos
7.-Copiar el Saldo de la moneda Pesos y copiarlo en la tx Envió de Remesa.
8.-Hacer clic en el Botón "SALIR"
9.-Hacer clic en la Transacción - Envio de Remesa
10.-Tildar la opción "Caja"
11.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"
12.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Pesos"
13.-Visualizar en pantalla el recuadro Importe y pegar el importe.
14.-Hacer clic en botón "CONFIRMAR"
15.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
16.-Visualizar el mensaje "Operación realizada con éxito"
17.-Hacer clic en boton "FINALIZAR"
18.-Visualizar la impresion del ticket
19.-Hacer clic en la Transacción - Consulta de Saldos.
20.-Verificar Los Saldos Tesoro Intermedio
22.-Copiar el Saldo de la moneda Pesos y copiarlo en la tx Envió de Remesa.
23.-Hacer clic en el Botón "SALIR"
24.-Hacer clic en la Transacción - Envio de Remesa
25.-Tildar la opción "Tesoro Intermedio"
26.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Sucursal"
27.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Pesos"
28.-Visualizar en pantalla el recuadro Importe y pegar el importe.
29.-Hacer clic en boton "CONFIRMAR"
30.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
31.-Visualizar el mensaje "Operación realizada con éxito"
32.-Hacer clic en boton "FINALIZAR"
33.-Visualizar la impresion del ticket
34.-Hacer clic en la Transacción - Consulta de Saldos.
36.-Verificar los Saldos Caja - Moneda Dolares
37.-Copiar el Saldo de la moneda Dolares y copiarlo en la tx Envió de Remesa.
38.-Hacer clic en el Botón "SALIR"
39.-Hacer clic en la Transacción - Envio de Remesa
40.-Tildar la opción "Caja"
41.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"
42.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Dolares"
43.-Visualizar en pantalla el recuadro Importe y pegar el importe
44.-Hacer clic en boton "CONFIRMAR"
45.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
46.-Visualizar el mensaje "Operación realizada con éxito"
47.-Hacer clic en boton "FINALIZAR"
48.-Visualizar la impresion del ticket
49.-Hacer clic en la Transacción - Consulta de Saldos.
51.-Verificar los Saldos Tesoro Intermedio - Moneda Dolares
52.-Copiar el Saldo de la moneda Pesos y copiarlo en la tx Envió de Remesa.
53.-Hacer clic en el Botón "SALIR"
54.-Hacer clic en la Transacción - Envio de Remesa
55.-Tildar la opción "Tesoro Intermedio""
56.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Sucursal"
57.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Dolares"
58.-Visualizar en pantalla el recuadro Importe y pegar importe"
59.-Hacer clic en boton "CONFIRMAR"
60.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
62.-Visualizar el mensaje "Operación realizada con éxito"
63.-Hacer clic en boton "FINALIZAR"
64.-Visualizar la impresion del ticket
65.-Hacer clic en la Transacción - Consulta de Saldos.
67.-Verificar los Saldos Caja - Moneda Euros
68.-Copiar el Saldo de la moneda Pesos y copiarlo en la tx Envió de Remesa.
69.-Hacer clic en el Botón "SALIR"
70.-Hacer clic en la Transacción - Envio de Remesa
71.-Tildar la opción "Caja"
72.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"
73.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Euros"
74.-Visualizar en pantalla el recuadro Importe y pegar importe
75.-Hacer clic en boton "CONFIRMAR"
76.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
77.-Visualizar el mensaje "Operación realizada con éxito"
78.-Hacer clic en boton "FINALIZAR"
79.-Visualizar la impresion del ticket
80.-Hacer clic en la Transacción - Consulta de Saldos.
82.-Verificar los Saldos Tesoro Intermedio - Moneda Euros
83.-Copiar el Saldo de la moneda Pesos y copiarlo en la tx Envió de Remesa.
84.-Hacer clic en el Botón "SALIR"
85.-Hacer clic en la Transacción - Envio de Remesa
86.-Tildar la opción "Tesoro Intermedio"
87.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Sucursal"
88.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Euros"
89.-Visualizar en pantalla el recuadro Importe y pegar el importe
90.-Hacer clic en boton "CONFIRMAR"
91.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"
92.-Visualizar el mensaje "Operación realizada con éxito"
93.-Hacer clic en boton "FINALIZAR"
94.-Visualizar la impresion del ticket</br>
    """
)
class SUC_T808(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T808(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.posiciones = ["1","2","3","4"]
            self.posiciones1 = ["1","2","3","4"]
            self.monedas = ["Pesos","Dolares","Euros","Reales"]
            self.seleccionarConsultaDeSaldo()
            for posicion in self.posiciones:    
                self.obeneterSaldoCaja(posicion)              
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
                elif self.monedaSaldo == "0,00" and posicion =='4':
                    self.monedas.remove("Reales")
                    self.posiciones1.remove('4')
                    print("se elimina Moneda Reales de la lista")  
                                                                                
            print(self.monedas)          
            if self.monedas == []:
                self.skip_msg(u"Los saldos de las monedas en Caja Estan En ceros, No se puede hacer el pase sin saldos{}".format(self.monedas))
            self.seleccionarSalir() 
                     
            for posicion,moneda in zip(self.posiciones1,self.monedas):
                self.seleccionarConsultaDeSaldo()
                self.obeneterSaldoCaja(posicion)
                self.seleccionarSalir() 
                self.seleccionarEnvioDeRemesa()
                self.clickRadioBtn("Caja")
                self.mostrarDestino("Tesoro Intermedio")
                self.mostrarMoneda(moneda)
                self.ingresarImporte(self.monedaSaldo,moneda)
                self.seleccionarConfirmar()
                texto = ["Origen","Destino","Moneda","importe"]
                datos = ["Caja","Tesoro Intermedio",moneda,self.monedaSaldo]
                self.frecuencia = []
                for dato,text in zip(datos,texto):
                    self.frecuencia.append(dato)                
                    self.validarDatos(dato,text)
                print(self.frecuencia)  
                self.seleccionarConfirmar3() 
                self.verificarMensajeExitoExtracciones(self.mensaje)      
                self.wait(1)
                self.seleccionarConsultaDeSaldo()
                self.obeneterSaldoCaf2(posicion)
                self.seleccionarSalir()   
                self.seleccionarEnvioDeRemesa()
                self.clickRadioBtn("Tesoro Intermedio")
                self.mostrarDestino("Tesoro Sucursal")
                self.mostrarMoneda(moneda)
                self.ingresarImporte(self.monedaSaldoCaf,moneda)
                self.seleccionarConfirmar()
                texto = ["Origen","Destino","Moneda","importe"]
                datos = ["Tesoro Intermedio","Tesoro Sucursal",moneda,self.monedaSaldoCaf]
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
        
        

if __name__ == "__main__":
    unittest.main()
