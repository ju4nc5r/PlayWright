# -*- coding: utf-8 -*-s
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
              NUMERO_TAS,CUENTA_VALIDAR1, NOMBRE_APELLIDO1, CUENTA1,\
              MONEDA, IMPORTE, MSJ_ESPERADO,SUCURSAL_DEST,IMPORTE1,IMPORTE2,\
              IMPORTE_VALIDAR_1,OPERACION1,TITULO_ESPERADO,NUMERO_TAS,OPERACION_A_VALIDAR,\
              SUC_JOB        

@allure.feature(u'TAS')
@allure.story(u'TAS Liberaciones')
@allure.testcase(u"ICaja - SUC-T867 - TAS Liberaciones Deposito Cheque Otros Bancos")
@allure.title(u'SUC-T867 - TAS Liberaciones Deposito Cheque Otros Bancos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ingresar a la pagina Icaja: https://fe-icaja-dist-icaja-front-homo.ocprch.sis.ad.bia.itau/#/login</br>
2.-Realizar login e ingresar los datos del operador Legajo:UIC10021 / Terminal:IA0500821   / Contraseña:Ingreso21</br>
3.-Hacer clic en el botón "INGRESAR"</br>
4.-Validar nombre del Operador "Hola, UIC10021</br>
5.-Hacer clic en la Transacción "TAS Liberaciones"</br>
6.-Seleccionar la transaccion "Deposito Cheque Propio"</br>
7.-Seleccionar Número de TAS "04651"</br>
8.-Validar Moneda "Pesos"</br>
9.-Ingresar numero de cuenta "00000331009"</br>
10.-Hacer clic en el Botón ver Firmantes.</br>
11.-Visualizar la firma</br>
12.-Hacer clic en el Botón "SIGUIENTE"</br>
13.-Ingresar importe "5000"</br>
14.-Ingresar los datos de cheque: Banco:059 / Suc:047 / CP:1030 / Numero:12345678 / Cuenta:98765432101</br>
15.-Hacer clic en cualquier espacio de la pantalla
16.-Visualizar en la parte inferior de la pantalla los datos del cheque depositado</br>
17.-Hacer clic en el Botón "FIN DE CARGA"</br>
18.-Visualizar los datos de la Transacción y hacer clic en el Botón "CONFIRMAR"</br>
19.-Visualizar la impresión del ticket</br>
20.-Visualizar el mensaje "Operación realizada con éxito"</br>
21.-Hacer clic en Botón "VALIDAR CHEQUE"</br>
22.-Visualizar el mensaje "Cheque timbrado con éxito" y hacer clic en el Botón "FINALIZAR"</br>
23.-Visualizar la impresión del ticket</br>
24.-Hacer clic en Botón "FINALIZAR"</br>   
"""
)
class SUC_T867(unittest.TestCase, stICajaInicio, stICaja, stICajaTickets):
    def setUp(self):
        inicioICaja(self)
        
    def test_SUC_T867(self):
        try:
            self.usuario = get_user_caja_homo_suc_50(self._testMethodName)
            self.getDatos()
            self.login()
            self.seleccionarTasLiberaciones()
            self.mostrarTiposDeOperacion()
            self.seleccionarTipoOperacion(self.operacion)
            self.mostrar_seleccionar_nro_tas(self.nro_tas)
            self.ingresar_cuenta3(self.cuenta1)  
            self.seleccionarSiguiente()
            self.ingresarImporte3(self.importe1,self.tipoMoneda)
            self.ingresar_cuenta4(self.cuenta1)
            self.ingresar_datos_chequera_otros_bancos2()    
            self.seleccionarFindeCarga()
            self.validar_sucursal(self.sucursal)
            self.validar_transaccion(self.operacion)
            self.validar_nro_tas(self.nro_tas) 
            self.validar_cuenta_deposito(self.cuenta_validar1)
            self.validar_nombre(self.nombre_y_apellido)
            self.validarCantidadDeCheques()
            self.validar_moneda(self.tipoMoneda)
            self.validar_importe_total_a_liberar(self.importeValidar1)       
            self.seleccionarConfirmar()
            self.seleccionarValidarCheques()
            self.visualizarMensajeExito() 
            self.verificar_exito_tas(self.mensaje)
            self.visualizarTicket2  
            self.cerrarSesion()
            self.finalizo = True
        except Exception:
            self.error = traceback.format_exc()
            
            
    def tearDown(self):
        fin(self)  
          
    def getDatos(self):
        self.sucursal = self.usuario.get(SUC_JOB)
        self.user = self.usuario.get(USUARIO)
        self.clave = self.usuario.get(CLAVE)
        self.legajo = self.usuario.get(LEGAJO)
        self.terminal = self.usuario.get(TERMINAL)
        self.tipoMoneda = self.usuario.get(MONEDA)
        self.sucudestino = self.usuario.get(SUCURSAL_DEST)
        self.nro_tas = self.usuario.get(NUMERO_TAS)
        self.valor = self.usuario.get(IMPORTE)
        self.mensaje = self.usuario.get(MSJ_ESPERADO)
        self.operacion = self.usuario.get(OPERACION1)
        self.operacionValidar = self.usuario.get(OPERACION_A_VALIDAR)
        self.importe1 = self.usuario.get(IMPORTE1)
        self.importe2 = self.usuario.get(IMPORTE2)
        self.importeValidar1 = self.usuario.get(IMPORTE_VALIDAR_1)
        self.cuenta_validar1 = self.usuario.get(CUENTA_VALIDAR1)
        self.msg_imprecion = self.usuario.get(TITULO_ESPERADO)
        self.numeroTas = self.usuario.get(NUMERO_TAS)
        self.cuenta1 =self.usuario.get(CUENTA1)
        self.nombre_y_apellido = self.usuario.get(NOMBRE_APELLIDO1)

        #self.mensaje = "La operacion finalizo correctamente"   
        

if __name__ == "__main__":
    unittest.main()
