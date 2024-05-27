# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Inte.pageLoc.pl_ICajaInicio import pl_ICajaInicio
from SeleniumFramework.src.proyectos.Caja_Inte.st.pasos import abrirNavegador
# from proyectos.Caja_Homo.constants.constants import (
#     USUARIO_INVALIDO, USUARIO_BLOQUEADO, USUARIO_YA_LOGUEADO, CLAVE_VENCIDA,
#     INTENTAR, REVISAR, LOGUEADO
# )
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys



class stICajaInicio(abrirNavegador):

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
            if self.write(pl_ICajaInicio.ipt_usuario, user, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def completarTerminalLogin(self, terminal):
        to = 10
        accion = 'Completar terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(pl_ICajaInicio.ipt_terminal, terminal, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def validar_terminal_Login(self):
        to = 10
        accion = 'validar terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            import socket
            terminal = socket.gethostname()
            print (terminal)

                
    def completarClaveLogin(self,clave):
        accion = 'Completar clave'
        with self.step(accion):
            xpath = pl_ICajaInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(accion)

    def seleccionarIngresarLogin(self):
        to = 10
        accion = 'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.btn_Ingresar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionarAceptarError(self):
        to = 10
        accion = 'Seleccionar Aceptar en mensaje.Hubo un error al obtener la terminal del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            msg = "Hubo un error al obtener la terminal del usuario"
            xpath = pl_ICajaInicio.msg_errorTerminalUser.format(msg)
            xpath2 = pl_ICajaInicio.btn_aceptar2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                self.selectElement(xpath2, "Se hace click en boton Aceptar", msgFail, to)
                self.capture_image(msgOk)
            else:
                pass


    # def verificarMensajeErrorLogin(self, msjError):
    #     to = 10
    #     accion = 'Verificar error login'
    #     msgOk, msgFail = get_msg(accion)
    #     with self.step(accion):
    #         xpath = pl_ICajaInicio.msj_error
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
#         to = 60
        to = 10
        accion = u'Validar legajo del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.txt_datos_Legajo.format(msjEsperado)
            # txt_xpath = self.get_element_text(xpath)
            if self.visibility_element(xpath,to):
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
                #self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    
    def validarUsuario(self, msjEsperado):
        to = 10
        accion = 'Validar nombre del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.txt_usuario            
            if self.visibility_element(xpath):
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
    
    def validarTerminal(self, msjEsperado):
        to = 10
        accion = u'Validar terminal del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.txt_datos_Terminal.format(msjEsperado)          
            if self.visibility_element(xpath):
                print(xpath)
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)            
            else:
                self.fail_msg(msgFail)
    
    def validarSucursal(self, msjEsperado):
        to = 10
        accion = u'Validar sucursal del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.txt_datos_Sucursal.format(msjEsperado)      
            if self.visibility_element(xpath):
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
                
    def validarHolaUsuario(self, msjEsperado):
        to = 20
        accion = u'Validar Hola,'+str(self.user)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.lbl_holaUsuario            
            if self.visibility_element(xpath,to):
                print(msjEsperado)
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)

    def validarMsgCajaCerrada(self):
        to = 2
        accion = u'Validar mensaje Caja Cerrada '
        msgOk, msgFail = get_msg(accion)
        msjEsperado = 'Sucursal Cerrada, es necesario la apertura previa para operar'
        msjEsperado2 = 'No se puede realizar la apertura de caja el dia de hoy, ya fue cerrada'           
        xpath = pl_ICajaInicio.msg_sucursalCerrada.format(msjEsperado)
        xpath2 = pl_ICajaInicio.msg_sucursalCerrada.format(msjEsperado2)    
        if self.visibility_element(xpath,to): 
            self.highlight(xpath, msgOk)
            self.skip_msg(msjEsperado)                                                              
        elif self.visibility_element(xpath2,to):    
            self.highlight(xpath2, msgOk)
            self.skip_msg(msjEsperado2)
        else:
            pass

                
# Cerrar Sesión
    
    
    
    
    def seleccionarIconoVcard(self):
        to = 10
        accion = u'Seleccionar icono vcard'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.icn_vcard
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def CerrarDatosOperador(self):
        to = 2
        accion = u'Hacer clic en el recuadro Hola, UIC10009 para que desaparezca los datos del operador'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):     
            import os
            self.wait(to)
            os.system(r'C:\ITAU_Tools\QA_Automation\workspace\Fram27\src\proyectos\Caja_Homo\test\escape.bat') 
            self.wait(to)            
            self.capture_image(msgOk)
    

#     def CerrarDatosOperador(self):
#         to = 10
#         accion = u'Hacer clic en el recuadro Hola, UIC10009 para que desaparezca los datos del operador'
#         msgOk, msgFail = get_msg(accion)
#         with self.step(accion):
#             xpath = pl_ICajaInicio.cdk_overlay_backdrop
#             self.driver.self.driver.find_element(by=By.XPATH, value=xpath).send_key(Keys.ESCAPE)
#             if self.visibility_element(xpath, to):
#                 self.capture_image(msgOk)
#             else:
#                 self.fail_msg(msgFail)    
   
          
           
           
           
           
    def seleccionarCerrarSesion(self):
        to = 10
        accion = 'Seleccionar cerrar sesión'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.btn_cerrarSesion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
    
    # Salir y Logout
    
    
    def cerrarSesion(self):
        self.seleccionarIconoVcard()
        self.seleccionarCerrarSesion()
          
                
    def seleccionarSalirApp(self):
        to = 10
        accion = 'Seleccionar salir aplicacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_ICajaInicio.btn_salir
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
            xpath = pl_ICajaInicio.btn_salir
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    
                
                