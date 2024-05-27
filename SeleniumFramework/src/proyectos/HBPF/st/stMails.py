# -*- coding: utf-8 -*-
from SeleniumFramework.sub import sub
from SeleniumFramework.src.utils.settings import usermail, mail_pass
from SeleniumFramework.src.proyectos.HBPF.loc.locMails import locMails


class stMails(sub):
    def obtener_codigo(self):
        self.abrir_url()
        xpath1 = locMails.input_mail
        xpath2 = locMails.mail_clave
        if self.double_visibility_element(xpath1, xpath2, 10):
            self.ingresar_usuario_mail()
            self.ingresar_contrasena_mail()
            self.seleccionar_iniciar_mail()
        else:
            pass
        self.seleccionar_mail()
        self.obtener_clave()
        
    def obtener_codigoRecupero(self):
        self.abrir_url()
        xpath1 = locMails.input_mail
        xpath2 = locMails.mail_clave
        if self.double_visibility_element(xpath1, xpath2, 10):
            self.ingresar_usuario_mail()
            self.ingresar_contrasena_mail()
            self.seleccionar_iniciar_mail()
        else:
            pass
        self.seleccionar_mailRecupero()
        self.obtener_clave()
        self.logoutMail()

    def abrir_url(self):
        url = "https://correo.sis.ad.bia.itau/owa"
        self.new_tab(url)

    def ingresar_usuario_mail(self):
        to = 10
        accion = 'Se ingresa el usuario'
        self.write(locMails.input_mail, usermail, to)
        self.capture_image(accion)

    def ingresar_contrasena_mail(self):
        to = 10
        self.write(locMails.input_pass, mail_pass, to)

    def seleccionar_iniciar_mail(self):
        to = 20
        accion = 'Seleccionar Inicio y bandeja de entrada'
        msgOk, msgFail = self.msg(accion)
        self.selectElement(locMails.btn_sesion, msgOk, msgFail, to)
        if self.visibility_element(locMails.btn_band_entrada, to):
            self.capture_image(accion)
            self.selectElement(locMails.btn_band_entrada, msgOk, msgFail, to)
        else:
            self.fail_msg(msgFail)

    def seleccionar_mail(self):
        to = 10
        accion = 'Se selecciona el mail'
        msgOk, msgFail = self.msg(accion)
        self.selectElement(locMails.mail_clave, msgOk, msgFail,to)
        self.capture_image(accion)

    def seleccionar_mailRecupero(self):
        to = 10
        accion = 'Se selecciona el mail'
        msgOk, msgFail = self.msg(accion)
        self.selectElement(locMails.lbl_asuntoMailCodActivRecupero, msgOk, msgFail, to)
        self.capture_image(accion)


    def obtener_clave(self):
        # to = 10
        # accion = u'Se obtiene la clave de activación'
        # msgOk, msgFail = self.msg(accion)
        texto = self.get_element_text(locMails.lbl_clave_activacio)
#         clave = texto.split(':')[1]
        clave = texto
#         self.codigo = clave.replace(' ', '')
        self.codigo = clave
        

    def msg(self, accion):
        msgOk = 'Se pudo %s' % accion.lower()
        msgFail = 'No %s' % msgOk.lower()
        return msgOk, msgFail
    
    def logoutMail(self):
        self.seleccionarIcnUsuario()
        self.seleccionarBtnCerrar()
        
    def seleccionarIcnUsuario(self):
        to = 10
        accion = 'Se selecciona Icono Usuario'
        msgOk, msgFail = self.msg(accion)
        self.selectElement(locMails.icnUsuario, msgOk, msgFail, to)
        self.capture_image(accion)
            
    def seleccionarBtnCerrar(self):    
        to = 10
        accion = 'Se selecciona boton Cerrar'
        msgOk, msgFail = self.msg(accion)
        self.selectElement(locMails.btnCerrar, msgOk, msgFail, to)
        