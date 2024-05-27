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
@allure.story(u'Envio de Remesa')
@allure.testcase(u"ICaja - SUC-T807 - Envió de Remesa - Tesorero (Sucursal - Intermedio - Caja)")
@allure.title(u'ICaja -SUC-T807 - Envió de Remesa - Tesorero (Sucursal - Intermedio - Caja)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10022 / Terminal:IA0500822   / Contraseña:Ingreso22</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar el nombre de usuario "Hola, UIC10022</br>
5.-Hacer clic en la Transacción - Envio de Remesa</br>
8.-Tildar la opción "Tesoro Sucursal"</br>
9.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"</br>
10.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Pesos"</br>
11.-Visualizar en pantalla el recuadro Importe y agregar "10.000"</br>
12.-Hacer clic en boton "CONFIRMAR"</br>
13.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
14.-Visualizar el mensaje "Operación realizada con éxito"</br>
15.-Hacer clic en boton "FINALIZAR"</br>
16.-Visualizar la impresion del ticket</br>
17.-Hacer clic en la Transacción - Envio de Remesa</br>
18.-Tildar la opción "Tesoro Intermedio"</br>
19.-Visualizar en pantalla el recuadro Destino y Seleccionar "Caja"</br>
20.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Pesos"</br>
21.-Visualizar en pantalla el recuadro Importe y agregar "10.000"</br>
22.-Hacer clic en boton "CONFIRMAR"</br>
23.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
24.-Visualizar el mensaje "Operación realizada con éxito"</br>
25.-Hacer clic en boton "FINALIZAR"</br>
26.-Visualizar la impresion del ticket</br>
27.-Hacer clic en la Transacción - Envio de Remesa</br>
28.-Tildar la opción "Tesoro Sucursal"</br>
29.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"</br>
30.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Dolares"</br>
31.-Visualizar en pantalla el recuadro Importe y agregar "100"</br>
32.-Hacer clic en boton "CONFIRMAR"</br>
33.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
34.-Visualizar el mensaje "Operación realizada con éxito"</br>
35.-Hacer clic en boton "FINALIZAR"</br>
36.-Visualizar la impresion del ticket</br>
37.-Hacer clic en la Transacción - Envio de Remesa</br>
38.-Tildar la opción "Tesoro Intermedio"</br>
39.-Visualizar en pantalla el recuadro Destino y Seleccionar "Caja"</br>
40.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Dolares"</br>
41.-Visualizar en pantalla el recuadro Importe y agregar "100"</br>
42.-Hacer clic en boton "CONFIRMAR"</br>
43.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
44.-Visualizar el mensaje "Operación realizada con éxito"</br>
45.-Hacer clic en boton "FINALIZAR"</br>
46.-Visualizar la impresion del ticket</br>
47.-Hacer clic en la Transacción - Envio de Remesa</br>
48.-Tildar la opción "Tesoro Sucursal"</br>
49.-Visualizar en pantalla el recuadro Destino y Seleccionar "Tesoro Intermedio"</br>
50.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Euros"</br>
51.-Visualizar en pantalla el recuadro Importe y agregar "100"</br>
52.-Hacer clic en boton "CONFIRMAR"</br>
53.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
54.-Visualizar el mensaje "Operación realizada con éxito"</br>
55.-Hacer clic en boton "FINALIZAR"</br>
56.-Visualizar la impresion del ticket</br>
57.-Hacer clic en la Transacción - Envio de Remesa</br>
58.-Tildar la opción "Tesoro Intermedio"</br>
59.-Visualizar en pantalla el recuadro Destino y Seleccionar "Caja"</br>
60.-Visualizar en pantalla el recuadro Moneda y Seleccionar "Euros"</br>
61.-Visualizar en pantalla el recuadro Importe y agregar "100"</br>
62.-Hacer clic en botón "CONFIRMAR"</br>
63.-Visualizar los datos de la Transacción y hacer clic en el boton "CONFIRMAR"</br>
64.-Visualizar el mensaje "Operación realizada con éxito"</br>
65.-Hacer clic en botón "FINALIZAR"</br>
66.-Visualizar la impresión del ticket</br>
    """
)
class SUC_T807(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T807(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()  
            self.monedas = ["Pesos","Dolares","Euros"]
            self.posiciones = ["1","2","3"]
            self.posiciones1 = ["1","2","3"]
            self.seleccionarConsultaDeSaldo()
            for posicion in self.posiciones:       
                self.obeneterSaldoTesoroSucursal(posicion)       
                if self.monedaSaldoTroSucursal == "0,00" and posicion =='1':
                    self.monedas.remove("Pesos")
                    self.posiciones1.remove('1')
                    print("se elimina Moneda Pesos de la lista")           
                elif self.monedaSaldoTroSucursal == "0,00" and posicion =='2':
                    self.monedas.remove("Dolares")
                    self.posiciones1.remove('2')
                    print("se elimina Moneda dolares de la lista")
                elif self.monedaSaldoTroSucursal == "0,00" and posicion =='3':
                    self.monedas.remove("Euros")
                    self.posiciones1.remove('3')
                    print("se elimina Moneda Euros de la lista")          
                    print(self.monedas)       
            if self.monedas == []:
                self.skip_msg(u"Los saldos de las monedas en Caja Estan En ceros,No se puede hacer el pase sin saldos{}".format(self.monedas))         
            monedas = ["Pesos","Dolares","Euros"]
            importes = ["10.000,00","2.000,00","1.000,00"]
        
            self.seleccionarSalir()            

            for moneda,importe,in zip(monedas,importes):        
                self.seleccionarEnvioDeRemesa()
                self.wait(1)
                self.clickRadioBtn("Tesoro Sucursal")
                self.mostrarDestino("Tesoro Intermedio")
                self.mostrarMoneda(moneda)
                self.ingresarImporte(importe,moneda)
                self.seleccionarConfirmar()
                self.validar_origen("Tesoro Sucursal")
                self.validar_destino("Tesoro Intermedio")
                self.validar_moneda(moneda)
                self.validar_importe(importe)
                self.seleccionarConfirmar3() 
                self.verificarMensajeExitoExtracciones(self.mensaje)                         
                self.wait(3)                
                self.seleccionarEnvioDeRemesa()
                self.wait(3)
                self.clickRadioBtn("Tesoro Intermedio")
                self.mostrarDestino("Caja")
                self.mostrarMoneda(moneda)
                self.ingresarImporte(importe,moneda)
                self.seleccionarConfirmar()
                self.validar_origen("Tesoro Intermedio")
                self.validar_destino("Caja")
                self.validar_moneda(moneda)
                self.validar_importe(importe)
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
