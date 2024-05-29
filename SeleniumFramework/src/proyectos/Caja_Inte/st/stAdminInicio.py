# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Inte.pageLoc.plAdminInicio import plAdminInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.pasos import abrirNavegador
from SeleniumFramework.common_functions import get_msg

class stAdminInicio(abrirNavegador):

    # login
    
    def login(self):
        self.seleccionarAceptarError()
        self.completarUsuarioLogin(self.user.strip())
        self.validar_terminal_Login()
        self.completarTerminalLogin(self.terminal.strip())
        self.completarClaveLogin(self.clave.strip())
        self.seleccionarIngresarLogin()
        self.validarMsgCajaCerrada()       
        self.validarHolaUsuario('Hola, '+ self.user)
        
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
    
    def completarClaveLogin(self,clave):
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
                self.fail_msg(msgFail)

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
    
    def validarLegajo(self, msjEsperado):
        to = 60
        accion = 'Validar legajo del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath,to):
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    def validarUsuario(self, msjEsperado):
        to = 10
        accion = 'Validar nombre del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
#             xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
            xpath = plAdminInicio.txt_usuario
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath):
                self.compareText(xpath, msjEsperado)
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
                self.compareText(xpath, msjEsperado)
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
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    # validar datos usuario

    # menu

    def seleccionarConsultas(self):
        to = 10
        accion = 'Seleccionar menu - consultas'
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
        accion = 'Seleccionar consultas -saldos de caja'
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
               
    
                
                