# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locRecupero import locRecupero
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.src.proyectos.HBPF.st.stRegistro import stRegistro
from SeleniumFramework.common_functions import get_msg


class stRecupero(stRegistro):
    def recupero_310(self, pregunta=False):
        """
        Metodo para realizar los pasos para el recupero de un usuario 310
        Si se ingresa por la opcion de los datos, se tiene que contestar unas
        preguntas acerca de las tarjetas.
        :param pregunta: Boolean. Si esta en True, se selecciona el radiobutton
                         de contestar preguntas de seguridad.
        """
        accion = 'Recupero de clave usuario 310'
        with self.simple_step(accion):
            self.primera_pagina(pregunta)
            # Segunda pag
            if pregunta:
                self.contestar_preguntas_riesgoNet(self.tipoDoc, self.nroDoc)
            else:
                self.ingresar_digitos()
                self.ingresar_fecha()
                self.contestar_preguntas()
            self.seleccionar_continuar()
            # Tercera pag
            # Aca puede pasar 2 cosas, o se muestra la sig pag o se vuelve a
            # realizar una pregunta nueva
            if self.double_visibility_element(locRecupero.input_usuario,
                                              locRecupero.ultima_pregunta,
                                              10):
                pass
            else:
                # me falta realizar pruebas con esta funcion
                self.contestar()
                self.seleccionar_continuar()
            self.completar_datos()
        self.paso = 1

    def recupero(self, pregunta=False):
        """
        Metodo para realizar los pasos para el recupero de un usuario personal
        bank o cartera general.
        :param pregunta: Boolean. Si esta en True, se selecciona el radiobutton
                         de contestar preguntas de seguridad
        """
        accion = 'Recupero de clave del usuario'
        with self.simple_step(accion):
            self.primera_pagina(pregunta)
            if pregunta:
                self.contestar_preguntas_riesgoNet(self.tipoDoc, self.nroDoc)
            else:
                self.ingresar_digitos()
                self.ingresar_fecha()
                self.ingresar_pin()
            self.seleccionar_continuar()
            self.completar_datos()      
#         self.paso = 1

    def primera_pagina(self, pregunta):
        """
        Metodo para acceder a aplicacion de recuperar usuario. Se completa la
        primera pagina, que es el ingreso de documento. Luego, dependiendo
        el valor del parametro pregunta se selecciona el radiobutton para
        contestar las preguntas de seguridad o contestar los datos de la
        tarjeta.
        :param pregunta: Boolean. Si esta en True, se selecciona el radiobutton
                        de contestar preguntas de seguridad
        """
        # Metodo principal
        self.seleccionar_recupero()
        self.log.info('Se intenta dar de alta un usuario')
        # Primera pag
        self.seleccionar_tipo_documento()
        self.ingresar_documento()
        self.seleccionar_continuar()
        # Aca falta buscar cuando se muestre el mensaje de usuario bloqueado
        xpath1 = locRecupero.radio_tarjetas
        xpath2 = locRecupero.msg_error
        if self.double_visibility_element(xpath1, xpath2, 20):
            if pregunta:
                self.seleccionarRadioPreguntas()
            else:
                self.seleccionarRadioTarjetas()
            self.seleccionar_continuar()
        else:
            texto = self.get_element_text(xpath2)
            if 'Aviso de bloqueo' in texto:
                self.fail_msg('El usuario se encuentra bloqueado')
            else:
                self.fail_msg(
                    'Se muestra error para modificar al usuario.\n'
                    'El usuario no se encuentra dado de alta'
                )

    def completar_datos(self):
        """
        Metodo para completar los datos de la cuarta pantalla, en donde
        se solicita el nombre de usuario y clave.
        """
        self.ingresar_usuario()
#         self.ingresar_pass()
        self.ingresar_nueva_pass()
        self.wait(1)
        self.aceptar_terminos()
        self.seleccionar_continuar()
        if self.clave_repetida():
            self.fail_msg('Ya se utilizo la nueva clave, ingrese otra')
        self.ingresarCodigoActivacionRecupero()
        self.seleccionar_continuar()
        self.seleccionarAccederAhora()
            
    def ingresar_nueva_pass(self):
        accion = 'Ingresar nueva contrasena'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(locRecupero.input_pass, self.clave_nueva, to):
                self.write(locRecupero.input_pass_confirmar, self.clave_nueva, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def clave_repetida(self):
        if self.visibility_element(locRecupero.msg_clave_repe, 5):
            text = self.get_element_text(locRecupero.msg_clave_repe)
            if 'es igual a una de las anteriores' in text:
                return True
            return False
        else:
            return False

    def seleccionar_recupero(self):
        accion = 'Seleccionar el boton de registro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(msgOk):
            xpath = locLogin.boton_recupero
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locRecupero.titulo_registro
            self.verifySelection(xpath, msgOk, to)
            self.log.info(msgOk)

    def contestar(self):
        accion = 'Responder ultima pregunta'
        # to = 10
        with self.step(accion):
            pregunta = self.get_element_text(locRecupero.label_preguntas)
            respuesta = self.get_respuesta(pregunta)
            self.responder(respuesta, locRecupero.opciones_preg_5)
            self.capture_image(accion)

    def contestar_preguntas(self):
        """
        Metodo para contestar las preguntas del usuario 310, sobre los datos
        de las tarjetas
        """
        accion = "Responder las preguntas"
        to = 10
        with self.step(accion):
            preguntas = self.search_elements(locRecupero.label_preguntas, to)
            preguntas = [x.text for x in preguntas]
            respuestas = [
                self.get_respuesta(pregunta) for pregunta in preguntas
            ]
            self.responder(respuestas[0], locRecupero.opciones_preg_1)
            self.responder(respuestas[1], locRecupero.opciones_preg_2)
            self.responder(respuestas[2], locRecupero.opciones_preg_3)
            self.responder(respuestas[3], locRecupero.opciones_preg_4)
            self.capture_image(accion)

    def seleccionarAccederAhora(self):
        accion = u'Validar mensaje "Ya podes acceder nuevamente" y seleccionar el botón "acceder ahora" luego ingreso cod.activacion'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRecupero.btn_accederAhora
            if self.visibility_element(locRecupero.msgYaPodesAcceder, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
            self.selectElement(xpath, '', '')
            
    def validErrClteNoRegistrado(self):
        accion = u'Validar mensaje de error cliente no registrado'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRecupero.msg_errorClteNoRegistrado
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)            

    def seleccionarBtnCerrar(self):    
        to = 10
        accion = 'Se selecciona boton Cerrar'
        msgOk, msgFail = self.msg(accion)
        self.selectElement(locRecupero.btnCerrar, msgOk, msgFail, to)