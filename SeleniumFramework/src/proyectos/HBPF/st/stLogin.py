# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plLogin import plLogin
from SeleniumFramework.src.proyectos.HBPF.st.stMails import stMails
from SeleniumFramework.src.proyectos.HBPF.st.stBrowser import stBrowser
from selenium.webdriver.common.action_chains import ActionChains
from SeleniumFramework.src.proyectos.HBPF.constants.constants import (
    USUARIO_INVALIDO, USUARIO_BLOQUEADO, CLAVE_VENCIDA, INTENTAR, REVISAR,
    LOGUEADO
)
from SeleniumFramework.common_functions import desbloqueoUsuarios, get_msg


class stLogin(stBrowser, stMails):

    def login(self):
        self.completarUsuarioLogin(self.user)
        self.completarClaveLogin(self.clave)
        self.seleccionarIngresarLogin()
        self.verificarCartelDeRegistro()    
        estado = self.verificarLogin_estado()
        return estado
    
    def loginClaveNueva(self):
        accion="Login con nueva clave"
        with self.simple_step(accion):
            self.completarUsuarioLogin(self.user)
            self.completarClaveLogin(self.clave_nueva)
            self.seleccionarIngresarLogin()
            estado = self.verificarLogin_estado()
            return estado    

    def check_login(self, estado=None):
        """Metodo para realizar el login y decir si se pudo loguear o no"""
        self.completarUsuarioLogin(self.user)
        self.completarClaveLogin(self.clave)
        self.seleccionarIngresarLogin()
        return self.verificar_login(estado)

    def first_login(self):
        accion = 'Se realiza el login del usuario'
        with self.simple_step(accion):
            self.completarUsuarioLogin(self.user)
            # self.seleccionarContinuarLogin()
            self.completarClaveLogin(self.clave)
            self.seleccionarIngresarLogin()
            self.ingresar_clave_activacion()
            self.seleccionarContinuarLogin()
            self.verifySelection(locLogin.titulo_esperado,'Se logro realizar el login', 30)
            self.paso = 1

    def desbloquarUsuario(self, documento):
        desbloqueoUsuarios(documento)

    def completarUsuarioLogin(self, user):
        to = 10
        accion = 'Completar Usuario'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            if self.write(locLogin.inputUsuario, user, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuarLogin(self):
        to = 10
        accion = 'Seleccionar Continuar'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = locLogin.cmdContinuar
            self.visibility_element(xpath, to)
            self.selectElement(xpath, msgOk, msgFail, to)

    def completarClaveLogin(self, clave):
        accion = 'Completar clave'
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        with self.step(accion):
            xpath = locLogin.inputClave
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(accion)

    def seleccionarIngresarLogin(self):
        accion = 'Seleccionar Ingresar'
        to = 10
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        with self.step(accion):
            xpath_select = locLogin.cmdIngresar
            msgOk = "seleccionar cmdIngresar"
            msgFail = "No se pudo " + msgOk
            self.selectElement(xpath_select, msgOk, msgFail, to)

    def seleccionarReingresarLogin(self):
        accion = 'Seleccionar Reingresar'
        to = 10
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        with self.step(accion):
            xpath_select = locLogin.button_reingreso
            msgOk = "seleccionar Reingresar"
            msgFail = "No se pudo " + msgOk
            self.selectElement(xpath_select, msgOk, msgFail, to)
                
    def verificarLogin_estado(self):
        to = 10
        accion = 'Verificar Login'
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        with self.step(accion):
            xpath = locLogin.lblError_msg
            xpath_verif = locLogin.titulo_esperado
            if self.double_visibility_element(xpath_verif, xpath, to):
                self.capture_image('Se pudo realizar el login')
            else:
                estado = self.chequeo_mensaje_login()
                self.capture_image(estado)
                self.fail_msg(estado)

    def chequeo_mensaje_login(self):
        """
        Metodo para chequear si se esta mostrando alguna alerta luego de
        realizar el login
        """
        to = 10
        xpath = locLogin.lblError_msg
        if self.visibility_element(xpath, to):
            texto = self.get_element_text(xpath)
            if 'Usuario bloqueado.' in texto:
                estado = USUARIO_BLOQUEADO
            elif (u'La clave y/o el usuario que ingresaste no son válidos.'
                  in texto):
                estado = USUARIO_INVALIDO
            elif (u'La operación no pudo ser realizada '
                    'en este momento.' in texto):
                estado = INTENTAR
            else:
                print (
                    u'Revisar el texto de la alerta. '
                    'Texto mostrado:\n{}'.format(texto)
                )
                estado = REVISAR
            return estado
        else:
            return None

    def verificar_login(self, estado_esperado):
        """
        Metodo para chequear todas las posibilidades luego del login, se busca
        un conjunto de mensajes, y dependiendo de los mensajes encontrados,
        se define el estado del login del usuario
        """
        accion = u'Verificación del estado del usuario'
        timeout = 15
        titulo = locLogin.titulo_esperado
        clave_vencida = locLogin.clave_vencida
        label_error = locLogin.lblError_msg
        lista = [titulo, clave_vencida, label_error]
        indice = self.array_visibility(lista, timeout)
        if indice == 0:
            estado = LOGUEADO
        elif indice == 1:
            estado = CLAVE_VENCIDA
        elif indice == 2:
            estado = self.chequeo_mensaje_login()
        #if estado is not None:
        #    with self.step(accion):
        #        if estado == estado_esperado:
        #            self.capture_image(estado)
        #        else:
        #            self.fail_msg('El estado de la cuenta no es el deseado')
        return estado

    def verificarLogin_estado_usuario(self, user, dict_var_excel):
        if self.resultado:
            self.escritura_usuario(self.dict_var_excel, user[0], 4,
                                   'USUARIO LOGUEADO', 'GREEN')
        else:
            status_login = self.chequeo_mensaje_login()
            self.escritura_usuario(self.dict_var_excel, user[0], 4,
                                   status_login, 'RED')

    def ingresar_clave_activacion(self):
        to = 10
        accion = 'Se ingresa el codigo de activacion'
        xpath = locLogin.input_cod_activacion
        if not self.visibility_element(xpath, to):
            self.fail_msg('No se esta mostrando el input del cod de activacion')
        # Se esperan dichos segundos para que se envie correctamente el mail
        self.wait(15)
        self.obtener_codigo()
        self.close_tab()
        self.write(xpath, self.codigo, to)
        self.capture_image(accion, 2)
        # Aca tengo q capturar el mensaje de error
    
    def verificarCartelDeRegistro(self):
        accion = u'Mostrar el cartel de registro'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locLogin.boton_noregistrar
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
                self.cerrarCartelDeRegistro()
            else:
                pass

    def cerrarCartelDeRegistro(self):
        accion = u'Cerrar el cartel de la tarjeta con debito automatico'
        msgOk, msgFail = get_msg(accion)
        to = 5
        with self.step(accion):
            xpath = locLogin.boton_noregistrar
            if not self.selectElement(xpath, msgOk, msgFail, to):
                self.fail_msg(msgFail)

    def aceptarTerminosYCondiciones(self):
        accion = u'Aceptar términos y condiciones'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(plLogin.chk_acepto_xpath, '', '', to)
            self.capture_image(msgOk)
            self.selectElement(plLogin.btn_Aceptar_xpath, '', '', to)

    def deslogueo(self):
        ''' Metodo para realizar el logout de la aplicacion de homebanking '''
        accion = u'Desloguear de la aplicacion'
        xpath1 = locLogin.btnConfig
        xpath = locLogin.btnSalir
        msgOk, msgFail = get_msg(accion)
        to = 3
        with self.step(accion):
            self.selectElement(xpath1, msgOk, msgFail, to)
            self.select_by_text(xpath, "Cerrar Sesión")
            #self.select_option(xpath, msgOk, msgFail, to, "Cerrar Sesión")
            #self.selectListByPartialText(xpath, "Cerrar Sesión")

    def seg_login(self):
        self.seg_CompletarUsuarioLogin(self.username)
        self.seg_CompletarClaveLogin(self.claveRandom)
        self.seg_SeleccionarIngresarLogin()

    def seg_CompletarUsuarioLogin(self, username):
        to = 10
        accion = 'Completar Usuario'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            if self.write(locLogin.seg_user, username, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seg_CompletarClaveLogin(self, claveRandom):
        accion = 'Completar clave'
        #         msgOk=accion
        #         msgFail='No se pudo ' + lower(msgOk)
        with self.step(accion):
            xpath = locLogin.seg_pass
            to = 10
            self.visibility_element(xpath, to)
            self.write(xpath, claveRandom, to)
            self.capture_image(accion)

    def seg_SeleccionarIngresarLogin(self):
        accion = 'Seleccionar Ingresar'
        to = 10
        with self.step(accion):
            xpath_select = locLogin.seg_buttonSingIn
            msgOk = "seleccionar Ingresar"
            msgFail = "No se pudo " + msgOk
            self.selectElement(xpath_select, msgOk, msgFail, to)