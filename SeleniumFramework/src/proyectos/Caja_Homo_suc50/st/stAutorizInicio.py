# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.pageLoc.plAutorizInicio import plAutorizInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.pasos import abrirNavegador
from selenium.webdriver.common.by import By
from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.proyectos.Caja_Homo_suc50 import settings

class stAutorizInicio(abrirNavegador):

    # login
    
    def login(self):
        self.msj_error()
        self.completarUsuarioLogin(self.user)
        self.completarTerminalLogin(self.terminal)
        self.completarClaveLogin(self.clave)        
        self.seleccionarIngresarLogin()
        

    def completarUsuarioLogin(self, user):
        to = 10
        accion = 'Completar Usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAutorizInicio.ipt_usuario, user, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def completarTerminalLogin(self, terminal):
        to = 10
        accion = 'Completar terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAutorizInicio.ipt_terminal, terminal, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def completarClaveLogin(self,clave):
        accion = 'Completar clave'
        with self.step(accion):
            xpath = plAutorizInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(accion)

    def seleccionarIngresarLogin(self):
        to = 10
        accion = 'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAutorizInicio.btn_ingresar
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
    
    def validarHolaUsuario(self, msjEsperado):
        to = 20
        accion = u'Validar ' + msjEsperado
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAutorizInicio.lbl_holaUsuario            
            if self.visibility_element(xpath,to):
                print(msjEsperado)
                text = self.get_element_text(xpath)
                print('valor obtenido '+ text )
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
    
    
    
    
    
#     def validarNombreCajero(self, msjEsperado):
#         to = 60
#         accion = 'Validar nombre del cajero'
#         msgOk, msgFail = get_msg(accion)
#         with self.step(accion):
#             xpath = plAutorizInicio.txt_name_cajero.format(msjEsperado)
#             # txt_xpath = self.get_element_text(xpath)
#             if self.visibility_element(xpath):
#                 self.highlight(xpath, accion)
#             else:
#                 self.fail_msg(msgFail)
#     
#     def validarUsuario(self, msjEsperado):
#         to = 10
#         accion = 'Validar nombre del usuario'
#         msgOk, msgFail = get_msg(accion)
#         with self.step(accion):
# #             xpath = plAdminInicio.txt_datos_user.format(msjEsperado)
#             xpath = plAutorizInicio.txt_datos_user.format(msjEsperado)
#             # txt_xpath = self.get_element_text(xpath)
#             if self.visibility_element(xpath):
#                 self.highlight(xpath, accion)
#             else:
#                 self.fail_msg(msgFail)
#     
#     def validarTerminal(self, msjEsperado):
#         to = 10
#         accion = 'Validar terminal del usuario'
#         msgOk, msgFail = get_msg(accion)
#         with self.step(accion):
#             xpath = plAutorizInicio.txt_datos_user.format(msjEsperado)
#             # txt_xpath = self.get_element_text(xpath)
#             if self.visibility_element(xpath):
#                 self.highlight(xpath, accion)
#             else:
#                 self.fail_msg(msgFail)
#     
#     def validarSucursal(self, msjEsperado):
#         to = 10
#         accion = 'Validar sucursal del usuario'
#         msgOk, msgFail = get_msg(accion)
#         with self.step(accion):
#             xpath = plAutorizInicio.txt_datos_user.format(msjEsperado)
#             # txt_xpath = self.get_element_text(xpath)
#             if self.visibility_element(xpath):
#                 self.highlight(xpath, accion)
#             else:
#                 self.fail_msg(msgFail)
#     
    # validar datos usuario


    
                
    def seleccionarbtnSalir(self):
        to = 60
        accion = u'Seleccionar salir aplicacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAutorizInicio.btn_salir
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def validarNroAutorizacion(self):
        to = 2
        accion = u'Validar el numero de autorizacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.lbl_nroAutorizacion.format(self.numeroDeAutorizacion) 
            if self.visibility_element(xpath, to):
                print(u"Numero de autorizacion:{}".format(self.numeroDeAutorizacion))
                self.capture_image(msgOk, to)
            else:
                self.fail_msg(msgFail)
                
                               
    def seleccionarIcnAutorizar(self):
        to = 20
        accion = u'Hacer clic en el Tilde verde de autorizacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.chk_autorizar.format(self.numeroDeAutorizacion)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)
  
    def seleccionarIcnDenegar(self):
        to = 20
        accion = u'Hacer clic en la X roja de Denegacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.chk_denegar.format(self.numeroDeAutorizacion)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)


  
  
    def seleccionarIcnAutorizarLinea1(self):
        to = 60
        accion = u'Hacer clic en el Tilde verde de autorizacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.chk_autorizar2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                                                
    def seleccionarIcnDenegarLinea1(self):
        to = 60
        accion = u'Hacer clic en el X Roja de Denegacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.chk_denegar2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

 
    def seleccionarBtnAutorizar(self):
        to = 60
        accion = u'Hacer clic en Boton Autorizar'
        msgOk = accion
        msgOk2 = u'Operacion Autorizada' 
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.btn_autorizar
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)                
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk2)
            else:
                self.fail_msg(msgFail)
 
 
    def seleccionarBtnRechazar(self):
        to = 60
        accion = u'Hacer clic en el boton rechazar'
        msgOk = accion
        msgOk2 = u'Operacion Rechazada' 
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.btn_rechazar
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)                
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk2)
            else:
                self.fail_msg(msgFail)
                

    def validarNroSucursalOrg(self):
        to = 60
        accion = u'Validar Nuemero de Sucursal de Origen'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.lbl_sucursalOrg.format(self.sucursalOrg)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
                
                
    def validarNroSucursalDtn(self):
        to = 60
        accion = u'Validar Nuemero de Sucursal de Destino'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.lbl_sucursalDtn.format(self.sucursalDtn)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
                
    
    def validarNroControl(self):
        to = 60
        accion = u'Validar Nuemero de Control'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.lbl_nroControl.format(self.Nrocontrol)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
 
 
    def validarTerminalDetransaccion(self):
        to = 60
        accion = u'Validar Terminal '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.lbl_terminall.format(self.terminal)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
 
    def seleccionarCheckSupervisor(self):
        to = 60
        accion = u'Hacer Click en el Check box de Supervisor'
        msgOk = accion
        msgOk2 = u'Operacion Rechazada' 
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.rbt_supervisor
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk2)
            else:
                self.fail_msg(msgFail)

    def verificarCheckGerente(self):
        to = 60
        accion = u'Verificar Check box de Gerente'
        msgOk = accion
        msgOk2 = u'Operacion Rechazada' 
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plAutorizInicio.rtb_gerente
            if self.visibility_element(xpath, to):
                dato = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                print(dato) 
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                



     
    def autorizarOperacion(self):#,usuario="UIC10022",term="IA0500822 �",clave="Ingreso22")  
        self.abrirAdmAutorizaciones()
        self.msj_error()
        self.completarUsuarioLoginAut(self.user_auto)
        self.completarTerminalLoginAut(self.terminal_auto)
        self.completarClaveLoginAut(self.clave_auto)        
        self.seleccionarIngresarLoginAut()
#         self.validarHolaUsuarioAut(self.user_auto)
        self.seleccionarCheckSupervisor()
        self.validarNroAutorizacion()
        self.seleccionarIcnAutorizar()
        self.validarNroSucursalOrg()
        self.validarNroSucursalDtn()
        self.validarNroControl()
        self.validarTerminalDetransaccion()
        self.seleccionarBtnAutorizar()
        self.seleccionarbtnSalir()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        
    def autorizarOperacionPg(self):#,usuario="UIC10022",term="IA0500822 �",clave="Ingreso22"):
        self.abrirAdmAutorizaciones()
        self.msj_error()
        self.completarUsuarioLoginAut(self.user_auto)
        self.completarTerminalLoginAut(self.terminal_auto)
        self.completarClaveLoginAut(self.clave_auto)        
        self.seleccionarIngresarLoginAut()
#         self.validarHolaUsuarioAut(self.user_auto)
        self.seleccionarCheckSupervisor()
        self.validarNroAutorizacion()
        self.seleccionarIcnAutorizar()
        self.seleccionarBtnAutorizar()
        self.seleccionarbtnSalir()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    
    def autorizarOperacionSucursal50(self):#,usuario="UIC10023",term="IBA0023",clave="Ingreso23"):
        self.abrirAdmAutorizaciones()
        self.msj_error()
        self.completarUsuarioLoginAut(self.user_auto)
        self.completarTerminalLoginAut(self.terminal_auto)
        self.completarClaveLoginAut(self.clave_auto)        
        self.seleccionarIngresarLoginAut()
#         self.validarHolaUsuarioAut(self.user_auto)
        self.seleccionarCheckSupervisor()
        self.validarNroAutorizacion()
        self.seleccionarIcnAutorizar()
        self.seleccionarBtnAutorizar()
        self.seleccionarbtnSalir()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])




    def autorizarPagoDeCheque(self):#,usuario="UIC10022",term="IA0500822 �",clave="Ingreso22"):
        self.abrirAdmAutorizaciones()
        self.msj_error()
        self.completarUsuarioLoginAut(self.user_auto)
        self.completarTerminalLoginAut(self.terminal_auto)
        self.completarClaveLoginAut(self.clave_auto)        
        self.seleccionarIngresarLoginAut()
#         self.validarHolaUsuarioAut(self.user_auto)
        self.verificarCheckGerente()
        self.validarNroAutorizacion()
        self.seleccionarIcnAutorizar()
        self.seleccionarBtnAutorizar()
        self.seleccionarbtnSalir()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        
    def autorizar_pago_plazo_fijo(self):#,usuario="UIC10022",term="IA0500822 �",clave="Ingreso22"):
        self.abrirAdmAutorizaciones()
        self.msj_error()
        self.completarUsuarioLoginAut(self.user_auto)
        self.completarTerminalLoginAut(self.terminal_auto)
        self.completarClaveLoginAut(self.clave_auto)        
        self.seleccionarIngresarLoginAut()
#         self.validarHolaUsuarioAut(self.user_auto)
        self.verificarCheckGerente()
        self.validarNroAutorizacion()
        self.seleccionarIcnAutorizar()
        self.seleccionarBtnAutorizar()
        self.seleccionarbtnSalir()
        self.driver.switch_to.window(self.driver.window_handles[0])



    def rechazarOperacion(self):#,usuario="UIC10022",term="IA0500822 �",clave="Ingreso22"):
        self.abrirAdmAutorizaciones()
        self.msj_error()
        self.completarUsuarioLoginAut(self.user_auto)
        self.completarTerminalLoginAut(self.terminal_auto)
        self.completarClaveLoginAut(self.clave_auto)        
        self.seleccionarIngresarLoginAut()
#         self.validarHolaUsuarioAut(self.user_auto)
        self.seleccionarCheckSupervisor()
        self.validarNroAutorizacion()
        self.seleccionarIcnDenegar()
        self.validarNroSucursalOrg()
        self.validarNroSucursalDtn()
        self.validarNroControl()
        self.validarTerminalDetransaccion()
        self.seleccionarBtnRechazar()
        self.seleccionarbtnSalir()
        self.driver.switch_to.window(self.driver.window_handles[0])

  
  
     
    def abrirAdmAutorizaciones(self):
        to = 10
        accion = u'Abrir Administracion de Autorizaciones'
        msgOk, msgFail = get_msg(accion)  
        with self.step(accion):
            try:              
                self.driver.execute_script("window.open('');")
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.wait(to)
                self.driver.get(settings.url_autorizCaja)
                self.wait(2)
                self.capture_image(msgOk)
            except Exception:
                self.fail_msg(msgFail)
        
 
    def completarUsuarioLoginAut(self, user):
        to = 60
        accion = u'Completar Usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAutorizInicio.ipt_usuario, user, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
  
    def completarTerminalLoginAut(self, terminal):
        to = 60
        accion = u'Completar terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAutorizInicio.ipt_terminal, terminal, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
     
          
    def completarClaveLoginAut(self,clave):
        accion = u'Completar clave'
        with self.step(accion):
            xpath = plAutorizInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(accion)
            
            
    def seleccionarIngresarLoginAut(self):
        to = 10
        accion = u'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAutorizInicio.btn_ingresar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def msj_error(self):
        to = 20
        accion = u'Validar mensaje  '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAutorizInicio.msj_error_2            
            if self.visibility_element(xpath,to):
                self.highlight(xpath, msgOk)
                self.selectElement(plAutorizInicio.btn_aceptar, msgOk, msgFail, to)      
            else:
                pass
                

    def validarHolaUsuarioAut(self, msjEsperado):
        to = 20
        accion = u'Validar ' + msjEsperado
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAutorizInicio.lbl_holaUsuario            
            if self.visibility_element(xpath,to):
                print(msjEsperado)
                text = self.get_element_text(xpath)
                print(u'valor obtenido '+ text )
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
    
        
        
#         try:
#             to = 3 
#             accion = u"Realizar la autorizacion de la Tx mediante el modulo de autorizaciones" 
#             msgOk = accion
#             msgFail = u"no se pudo " +  msgOk.lower()
#             with self.step(accion):
#                 self.driver.execute_script("window.open('');")
#                 self.driver.switch_to.window(self.driver.window_handles[1])
#                 self.wait(to)
#                 self.driver.get(settings.url_autorizCaja)
#                 self.wait(to)
#                 usuario = self.driver.find_element_by_xpath(plAutorizInicio.ipt_usuario)       
#                 usuario.send_keys("UIC10022")
#                 self.wait(to)
#                 terminal = self.driver.find_element_by_xpath(plAutorizInicio.ipt_terminal)
#                 terminal.send_keys("IA0500822 �")
#                 self.wait(to)
#                 clave = self.driver.find_element_by_xpath(plAutorizInicio.ipt_clave)
#                 clave.send_keys("Ingreso22")
#                 self.wait(to)
#                 btn_aceptar = self.driver.find_element_by_xpath(plAutorizInicio.btn_aceptar)
#                 btn_aceptar.click()
#                 self.wait(to)
#                 chk_autorizar = self.driver.find_element_by_xpath(plAutorizInicio.chk_autorizar_linea1) 
#                 chk_autorizar.click()
#                 self.wait(to)
#                 btn_autorizar = self.driver.find_element_by_xpath(plAutorizInicio.btn_autorizar)
#                 btn_autorizar.click()
#                 self.wait(to)
#                 btn_Salir = self.driver.find_element_by_xpath(plAutorizInicio.btn_salir)
#                 btn_Salir.click()
#                 self.driver.switch_to.window(self.driver.window_handles[0])
#         except Exception:
#             print(msgFail)
            
             
        
        
        
#     def deslogueo(self):
#         to = 20
#         accion = 'Desloguear de la aplicacion'
#         msgOk = 'Se pudo {}'.format(accion.lower())
#         msgFail = 'No {}'.format(msgOk.lower())
#         with self.step(accion):
#             xpath = plAdminInicio.btn_salir
#             if self.visibility_element(xpath, to):
#                 self.selectElement(xpath, msgOk, msgFail, to)
#                 self.capture_image(msgOk)
#             else:
#                 self.fail_msg(msgFail)
#                 
#     
#                 


#                 