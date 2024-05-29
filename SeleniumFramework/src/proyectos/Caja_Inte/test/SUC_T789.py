# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
from proyectos.Caja_Inte.pageLoc.plCajaInicio import plCajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaInicio import stICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICaja import stICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st.stICajaTickets import stICajaTickets
from SeleniumFramework.src.proyectos.Caja_Inte.st import inicioICaja
from SeleniumFramework.src.proyectos.Caja_Inte.st import fin
from SeleniumFramework.common_functions import get_user_caja_inte
from SeleniumFramework.constants.excel_constants import USUARIO, LEGAJO, TERMINAL, SUCURSAL,CLAVE,\
              APELLIDO, TIPO_DOC_CLIENTE, NRO_DOC_CLIENTE, NOMBRE, CUENTA,\
              MONEDA, IMPORTE, MSJ_ESPERADO,CUENTA1,CUENTA2,CUENTA3,MONEDA1,MONEDA2,MONEDA3,\
              IMPORTE1,IMPORTE2,IMPORTE3,CUENTA_VALIDAR1,CUENTA_VALIDAR2,CUENTA_VALIDAR3,\
              IMPORTE_VALIDAR_1,IMPORTE_VALIDAR_2,IMPORTE_VALIDAR_3,NOMBRE_APELLIDO1,NOMBRE_APELLIDO2,NOMBRE_APELLIDO3,\
              DOCUMENTO1,DOCUMENTO2,DOCUMENTO3,INDENTIFICADOR1,INDENTIFICADOR2,INDENTIFICADOR3,\
              OPERACION1,OPERACION2,OPERACION3
             

@allure.feature(u'Transferencias')
@allure.story(u'Transferencias Entre Cuentas Propias')
@allure.testcase(u"ICaja - SUC-T789 - Transferencias Entre Cuentas Propias")
@allure.title(u'SUC-T789 - Transferencias Entre Cuentas Propias')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-icaja-front-inte.apps.ocp-np.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0460809 / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Hacer clic en el recuadro "Hola, UIC10021 y visualizar los datos del operador UIC10021</br>
5.-Hacer clic en el recuadro Hola, UIC10021 para que desaparezca los datos del operador</br>
6.-Hacer clic en la Transacción - Transferencias Entre Cuentas Propias</br>
7.-Visualizar en pantalla el Recuadro identificar cliente</br>
8.-Ingresar los datos del cliente</br>
9.-Seleccionar Tipo de Documento "DNI"</br>
10.-Ingresar Numero de Documento "25227274"</br>
11.-Hacer clic en el Botón "IDENTIFICAR"</br>
12.-Hacer clic en el Boton SIN CLAVE</br>
13.-Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada.</br>
14.-Hacer clic en el recuadro "Cuenta Débito"</br>
15.-Seleccionar cuenta "CA $ 0444583-301/7"</br>
16.-Hacer clic en el recuadro cuenta credito y Agregar la cuenta - CC $ 0444445-100/1</br>
17.-Hacer clic en el recuadro "Importe" e ingresar "4000"</br>
18.-Hacer clic en "SIGUIENTE"</br>
19.-Marcar el check si coincide la firma y hacer clic en el boton "SIGUIENTE"</br>
20.-Visualizar los datos de la Transaccion y hacer clic en el boton "CONFIRMAR"</br>
21.-Visualizar la impresion del ticket</br>
22.-Visualizar el mensaje "Operación realizada con éxito" y hacer clic en el boton "FINALIZAR" </br>
23.-Visualizar la impresion del ticket </br>
24.-Hacer clic en boton "FINALIZAR" </br>
25.-Hacer clic en el recuadro Hola, UIC10021 </br>
26.-Hacer clic en CERRAR SESIÓN </br>
 </br>
"""
)
class SUC_T789(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
        
    def test_SUC_T789(self):
        try:
            self.usuario = get_user_caja_inte(self._testMethodName)
            self.getDatos()
            self.login()                   
            self.seleccionarTrasferenciaEntreCuentas()
            self.identificarCliente() 
            self.seleccionarRecuadroCuentasCliente2(self.cuenta1)
            self.seleccionarRecuadroCuentasCliente3(self.cuenta2)
            self.ingresarImporte(self.importe1,self.moneda1)
            self.wait(1)
            self.seleccionarSiguiente4()
            self.wait(1)
            self.seleccionarConfirmarFirma()
            self.seleccionarSiguiente()
            self.validar_cuenta_debito(self.cuenta1)
            self.validar_cuenta_credito(self.cuenta2)
            self.validar_nombre(self.nombreYApellido1)
            self.validar_nombre_2(self.nombreYApellido2)
            self.validar_importe_total_a_liberar(self.importeValidar1)        
            self.seleccionarConfirmar()
            self.verificarMensajeExitoExtracciones(self.mensaje)
            self.visualizarTicket()
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
        self.importe = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.cuenta1 = self.usuario.get(CUENTA1)
        self.cuenta2 = self.usuario.get(CUENTA2)
        self.cuenta3 = self.usuario.get(CUENTA3)
        self.idenificandor1 = self.usuario.get(INDENTIFICADOR1)
        self.idenificandor2 = self.usuario.get(INDENTIFICADOR2)
        self.idenificandor3 = self.usuario.get(INDENTIFICADOR3)
        self.documento1 = self.usuario.get(DOCUMENTO1)
        self.documento2 = self.usuario.get(DOCUMENTO2)
        self.documento3 = self.usuario.get(DOCUMENTO3)
        self.operacion1 = self.usuario.get(OPERACION1)
        self.operacion2 = self.usuario.get(OPERACION2)
        self.operacion3 = self.usuario.get(OPERACION3)
        self.moneda1 = self.usuario.get(MONEDA1)
        self.moneda2 = self.usuario.get(MONEDA2)
        self.moneda3 = self.usuario.get(MONEDA3)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importe3 = self.usuario.get(IMPORTE3)
        self.nombreYApellido1 = self.usuario.get(NOMBRE_APELLIDO1)
        self.nombreYApellido2 = self.usuario.get(NOMBRE_APELLIDO2)
        self.nombreYApellido3 = self.usuario.get(NOMBRE_APELLIDO3)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.importeValidar2 = self.usuario.get(IMPORTE_VALIDAR_2)
        self.importeValidar3 = self.usuario.get(IMPORTE_VALIDAR_3)
        self.cuentaValidar1 = self.usuario.get(CUENTA_VALIDAR1)
        self.cuentaValidar2 = self.usuario.get(CUENTA_VALIDAR2)
        self.cuentaValidar3 = self.usuario.get(CUENTA_VALIDAR3)
     
     
     
     
     
    def validarDatos(self, dato,tex):
        to = 30
        accion = u'validar Datos de la Operacion: ' + u' '+tex
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_datoValidar1.format(dato)
            xpath2 = plCajaInicio.lbl_datoValidar2.format(dato)
            if self.frecuencia.count(dato)==2:
                datos_validar = self.driver.find_element_by_xpath(xpath2).get_property('innerHTML')
                if dato in datos_validar:                        
                    print(datos_validar)
                    self.highlight(xpath2, accion)             
            else: 
                datos_validar = self.driver.self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')                 
                if dato in datos_validar:        
                    print(datos_validar)
                    self.highlight(xpath, accion)     
                else:
                    self.fail_msg(msgFail)
           

 

                


# self.mensaje = "La operacion finalizo correctamente"
        
        

if __name__ == "__main__":
    unittest.main()
