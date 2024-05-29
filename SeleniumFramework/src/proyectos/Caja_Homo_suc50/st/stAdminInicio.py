# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.pageLoc.plAdminInicio import plAdminInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.pasos import abrirNavegador
from selenium.webdriver.common.by import By


# from proyectos.Caja_Homo_suc50.constants.constants import (
#     USUARIO_INVALIDO, USUARIO_BLOQUEADO, USUARIO_YA_LOGUEADO, CLAVE_VENCIDA,
#     INTENTAR, REVISAR, LOGUEADO
# )
from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.proyectos.Caja_Homo_suc50 import settings

class stAdminInicio(abrirNavegador):

    # login
    
    def login(self):
        self.msj_problema_con_la_terminal()  
        self.completarUsuarioLogin(self.user)
        self.completarTerminalLogin(self.terminal)
        self.completarClaveLogin(self.clave)
        self.seleccionarIngresarLogin()
     
#         self.wait(10)
#         self.validarNombreCajero("Hola {}  !".format(self.user))

    def completarUsuarioLogin(self, user):
        to = 10
        accion = 'Completar Usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAdminInicio.ipt_usuario, user, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def completarTerminalLogin(self, terminal):
        to = 10
        accion = 'Completar terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAdminInicio.ipt_terminal, terminal, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def completarClaveLogin(self, clave):
        accion = 'Completar clave'
        with self.step(accion):
            xpath = plAdminInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(accion)

    def seleccionarIngresarLogin(self):
        to = 10
        accion = 'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_aceptar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                pass

    # def verificarMensajeErrorLogin(self, msjError):
    #     to = 10
    #     accion = 'Verificar error login'
    #     msgOk, msgFail = get_msg(accion)
    #     with self.step(accion):
    #         xpath = plAdminInicio.msj_error
    #         txt_xpath = self.get_element_text(xpath)
    #         if self.visibility_element(xpath):
    #             if txt_xpath == msjError:
    #                 self.highlight(xpath, accion)
    #                 self.capture_image(msgOk)
    #             else:
    #                 self.fail_msg(msgFail)
    #         else:
    #             self.fail_msg(msgFail)

    # login

    # validar datos usuario
    
    def validarNombreCajero(self, msjEsperado):
        to = 60
        accion = 'Validar nombre del cajero'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.txt_name_cajero.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def msj_problema_con_la_terminal(self):
        to = 60
        accion = 'Validar nombre del cajero'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.msj_error_terminal
            if self.visibility_element(xpath):
                self.highlight(xpath, accion)
                self.selectElement(plAdminInicio.btn_aceptar_2, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
    
    def validarUsuario(self, msjEsperado):
        to = 10
        accion = 'Validar nombre del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
#             xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
            xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    def validarTerminal(self, msjEsperado):
        to = 10
        accion = 'Validar terminal del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    def validarSucursal(self, msjEsperado):
        to = 10
        accion = 'Validar sucursal del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    # validar datos usuario

    # menu

    def seleccionarConsultas(self):
        to = 10
        accion = u'Seleccionar menu - consultas'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consultas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    
    
    def seleccionarOperadoresRegis(self):
        to = 10
        accion = 'Seleccionar consultas - operadores registrados'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_operadores
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarTerminalesregistradas(self):
        to = 10
        accion = 'Seleccionar consultas - Terminales registrados'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_terminales_regis
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)                      
                
    def seleccionarSaldosCajas(self):
        to = 10
        accion = u'Seleccionar consultas -saldos de caja'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_saldos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTotalesIngresEgresos(self):
        to = 10
        accion = 'Seleccionar consultas - totales ingresos, egresos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_TotalesIngresos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarListadosMultiples(self):
        to = 10
        accion = 'Seleccionar consultas - Listado multiples'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_ListadoMultiples
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarListadosTickets(self):
        to = 10
        accion = 'Seleccionar consultas - Listado tickets'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_ListadoTickets
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarMovimientosdecaja(self):
        to = 10
        accion = 'Seleccionar consulta - Movimientos de caja'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_consulta_MovDeCajas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)              
    
    def seleccionarTerminales(self):
        to = 10
        accion = 'Seleccionar menu - terminales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_terminales
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    

    def seleccionarBajaTerminales(self):
        to = 10
        accion = 'Seleccionar baja terminales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_terminales_baja
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarParametria(self):
        to = 10
        accion = 'Seleccionar menu - parametria'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_parametria
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarLimitesMaxMin(self):
        to = 10
        accion = 'Seleccionar limites maximos y minimos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_limites_maxmin
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarSucursales(self):
        to = 10
        accion = 'Seleccionar menu - Sucursales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_sucursales
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarApertura(self):
        to = 10
        accion = 'Seleccionar apertura - Sucursales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_apertura
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
            accion = 'verificar mensaje No se puede abrir la sucursal, ya se encuentra abierta'            
            msgOk, msgFail = get_msg(accion)
            xpath = plAdminInicio.msjSucursalYaEstaAbierta          
                                                 
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                
                btnAceptar = plAdminInicio.btn_aceptar                      
                accionBtn = "hacer click en boton aceptar"            
                msgOk, msgFail = get_msg(accionBtn)
                if self.visibility_element(btnAceptar, to):               
                    self.selectElement(btnAceptar, msgOk, msgFail, to)
                    self.wait(1)
                    self.capture_image(msgOk)
                    self.skip = True
                    self.finalizo = False                    
                    self.skip_msg("No se puede abrir la sucursal, ya se encuentra abierta")
                else:
                    self.fail_msg(msgFail)             
    # menu
                
    def seleccionarSalirApp(self):
        to = 10
        accion = 'Seleccionar salir aplicacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_salir
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def deslogueo(self):
        to = 20
        accion = 'Desloguear de la aplicacion'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = plAdminInicio.btn_salir
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def verificarValoresEnCeros(self, reales, euros, dolares, pesos, user):
        accion = u'Visualizar los saldos de todas las monedas en cero'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            self.verificarSaldosEnCeros(reales,user)
            self.wait(1)
            self.verificarSaldosEnCeros(euros,user)
            self.wait(1)
            self.verificarSaldosEnCeros(dolares,user)
            self.wait(1)
            self.verificarSaldosEnCeros(pesos,user)
    
   
    def loguinAdmincaja(self, user, terminal, clave):
        self.openAdminCaja2()
        self.completarUsuarioCierre(user)
        self.completarTerminalCierre(terminal)
        self.completarClaveCierra(clave)
        self.seleccionarIngresarCierre()
        self.validarNombreCajeroCierra(user)
     
    def openAdminCaja2(self):
        to = 10
        accion = u'Abrir Administracion de Caja'
        msgOk, msgFail = get_msg(accion)  
        with self.step(accion):
            try:              
                self.driver.execute_script("window.open('');")
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.wait(to)
                self.driver.get(settings.url_adminCaja)
                self.wait(2)
                self.capture_image(msgOk)
            except Exception:
                self.fail_msg(msgFail)


    def completarUsuarioCierre(self, user):
        to = 10
        accion = u'Completar Usuario '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAdminInicio.ipt_usuario, user, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def completarTerminalCierre(self, terminal):
        to = 10
        accion = 'Completar terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAdminInicio.ipt_terminal, terminal, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def completarClaveCierra(self, clave):
        accion = u'Completar clave'
        with self.step(accion):
            xpath = plAdminInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(accion)
            
            
    def seleccionarIngresarCierre(self):
        to = 30
        accion = u'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.btn_aceptar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validarNombreCajeroCierra(self, msjEsperado):
        to = 60
        accion = u'Validar nombre del cajero'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.txt_name_cajero.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)


    def obtenerSaldoDeCaja(self, moneda, user):
        to = 30
        accion = u'Obtener Saldo de la Caja ' + moneda
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            if user == 'UIC10022':
                xpath = plAdminInicio.cell_saldoSupervisor.format(moneda)
            else:   
                xpath = plAdminInicio.cell_saldoCajero.format(moneda)
            if self.visibility_element(xpath, to):   
                self.importeCierre = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')     
                if self.importeCierre:
                    print("Importe en " + moneda + " :" + self.importeCierre)
                    self.highlight(xpath, accion)     
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def verificarSaldosEnCeros(self, moneda, user):
        to = 30
        accion = u'Verificar Importes en 0 De la moneda  ' + moneda
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            if user == 'UIC10022':
                xpath = plAdminInicio.cell_saldoSupervisor.format(moneda)
            else:   
                xpath = plAdminInicio.cell_saldoCajero.format(moneda)
            if self.visibility_element(xpath, to):   
                self.importeCierre = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')  
                if self.importeCierre == " 0,00 ":
                    print("Importe en " + moneda + " :" + self.importeCierre)
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
                
    def obtener_Valores(self):
        to = 10
        accion = 'Obtener Datos de la tabla de cajas '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            nombres = ['terminal', 'operador', 'sucursal', 'pesos', 'dolares', 'euros', 'reales']
            xpath = plAdminInicio.cell_preba.format('pesos')
            if self.visibility_element(xpath, to):
                celdas = len(self.driver.find_elements_by_xpath(xpath))
                for n in range (1, celdas):
                        terminal = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[0]) + "')])[" + str(n) + "]").get_property('innerText') 
                        operador = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[1]) + "')])[" + str(n) + "]").get_property('innerText')
                        sucursal = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[2]) + "')])[" + str(n) + "]").get_property('innerText')
                        saldo_pesos = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[3]) + "')])[" + str(n) + "]").get_property('innerText')
                        saldo_dolares = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[4]) + "')])["+ str(n) + "]").get_property('innerText')
                        saldo_euros = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[5]) + "')])[" + str(n) + "]").get_property('innerText')
                        saldo_reales = self.driver.find_element_by_xpath("(//td[contains(@class,'" + str(nombres[6]) + "')])[" + str(n) + "]").get_property('innerText') 
                        lista = [('Terminal: ', terminal), ('Operador: ', operador), ('sucursal:', sucursal), ('Importe Pesos: ', saldo_pesos), (' Importe Dolares: ', saldo_dolares), ('Importe Euros: ', saldo_euros), ('Importe Resles:', saldo_reales)]
                        print(lista)
#                         print('Terminal: ' + terminal +' '+ 'operador: ' + operador +' '+ 'sucural: ' + sucursal +' ',
#                               'saldo en pesos: '+  saldo_pesos +' '+ 'saldo en dolares: ' + saldo_dolares +' ',
#                               'saldo en euros: ' + saldo_euros +' '+ 'saldo en reales: ' + saldo_reales)
            else: 
                self.fail_msg(msgFail)  
