# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebInicio import pl_MesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.pasos import abrirNavegador
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.utils.settings  import cca_user,cca_pass


class stMesaWebInicio(abrirNavegador):

    # login
    
    def login(self):
#         self.seleccionarAceptarError()
        self.completarUsuarioLogin()
        self.completarClaveLogin()
        self.wait(2)
        self.seleccionarIngresarLogin()   
        self.validarHolaUsuario('Hola,')


    def login_2(self):
        self.ingresar_usuario()
        self.ingresar_clave()
        self.wait(2)
        self.seleccionarIngresarLogin()   

    def completarUsuarioLogin(self):
        to = 10
        accion = 'Completar Usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(pl_MesaWebInicio.ipt_usuario,"srv_homo", to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def ingresar_usuario(self):
        to = 10
        accion = 'Completar Usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write_2(pl_MesaWebInicio.ipt_usuario,"FO433151", to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    

    def completarClaveLogin(self):
        accion = 'Completar clave'
        with self.step(accion):
            xpath = pl_MesaWebInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, "Wjsow2JwosAa#$", to)
            self.capture_image(accion)
            
    def ingresar_clave(self):
        accion = 'Completar clave'
        with self.step(accion):
            xpath = pl_MesaWebInicio.ipt_clave
            to = 10
            self.visibility_element(xpath, to)
            self.write_2(xpath, "Febrero2024", to)
            self.capture_image(accion)
            

    def seleccionarIngresarLogin(self):
        to = 10
        accion = 'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebInicio.btn_Ingresar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
             
                




     
    def validarUsuario(self, msjEsperado):
        to = 10
        accion = 'Validar nombre del usuario'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebInicio.txt_usuario            
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
            xpath = pl_MesaWebInicio.txt_datos_Terminal.format(msjEsperado)          
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
            xpath = pl_MesaWebInicio.txt_datos_Sucursal.format(msjEsperado)      
            if self.visibility_element(xpath):
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
                
    def validarHolaUsuario(self, msjEsperado):
        to = 20
        accion = u'Validar Hola,'+str(cca_user)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebInicio.lbl_holaUsuario            
            if self.visibility_element(xpath,to):
                print(msjEsperado)
                self.compareText(xpath, msjEsperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)


                
# Cerrar Sesión
    
    
    
    
                

    

          
           
           
           
           
    def seleccionarCerrarSesion(self):
        to = 10
        accion = 'Seleccionar cerrar sesión'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebInicio.btn_cerrarSesion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
    
    # Salir y Logout
    
    
    def cerrarSesion(self):
        self.seleccionarCerrarSesion()
          
                
    def seleccionarSalirApp(self):
        to = 10
        accion = 'Seleccionar salir aplicacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebInicio.btn_salir
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
            xpath = pl_MesaWebInicio.btn_salir
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    
                
                