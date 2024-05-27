# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.stMails import stMails
from SeleniumFramework.src.proyectos.HBPF.loc.locRegistro import locRegistro
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from proyectos.VisualizadorLogs.st.stObtenerRespuestas import stRespuestas
from SeleniumFramework.src.proyectos.HBPF.constants.Preguntas_registro import preguntas as list_preg
from SeleniumFramework.common_functions import get_msg


class stRegistro(stMails, stRespuestas):
    def registro_310(self, preguntas=False):
        """
        Metodo para realizar los pasos para el registro de un usuario 310
        Si se ingresa por la opcion de los datos, se tiene que contestar unas
        preguntas acerca de las tarjetas.
        :param pregunta: Boolean. Si esta en True, se selecciona el radiobutton
                         de contestar preguntas de seguridad.
        """
        accion = 'Registro del usuario 310'
        with self.simple_step(accion):
            if preguntas:
                self.primera_pagina_registro(preguntas)
                self.contestar_preguntas_riesgoNet(self.tipoDoc, self.nroDoc)
                self.seleccionar_continuar()
                self.ingresar_numero_tramite() 
                self.seleccionar_continuar()
                self.completar_datos_registro()   
#                 self.seleccionar_continuar()
            else:
                self.primera_pagina_registro(preguntas)
                # Segunda pag
                self.ingresar_digitos()
                self.ingresar_fecha()
                self.contestar_preguntas()
                self.seleccionar_continuar()
                # Tercera pag
                # Aca puede pasar 2 cosas, o se muestra la sig pag o se vuelve a
                # realizar una pregunta nueva
                xpath = '//span[@id="textField0"]'
                if self.double_visibility_element(locRegistro.input_usuario,
                                                  xpath, 10):
                    pass
                else:
                    self.contestar_registro()
                    self.seleccionar_continuar()
                self.completar_datos_registro()           
#             self.paso = 1


    def         registro(self, preguntas=False):
        """
        Metodo para realizar los pasos para el registro de un usuario personal
        bank o cartera general.
        :param pregunta: Boolean. Si esta en True, se selecciona el radiobutton
                         de contestar preguntas de seguridad
        """
        accion = 'Registro del usuario'
        with self.simple_step(accion):
            self.primera_pagina_registro(preguntas)
            if preguntas:
                self.contestar_preguntas_riesgoNet(self.tipoDoc, self.nroDoc)
                self.seleccionar_continuar()
                self.ingresar_numero_tramite() 
            else:
                self.ingresar_digitos()
                self.ingresar_fecha()
                self.ingresar_pin()
            self.seleccionar_continuar()
            self.completar_datos_registro()
        self.paso = 1

    def registroDocViejo (self, preguntas=False):
        """
      Metodo que selecionar un documento viejo para inggrsar el numero de tramite"
        """
        accion = 'Registro del usuario'
        with self.simple_step(accion):
            self.primera_pagina_registro(preguntas)
            if preguntas:
                self.contestar_preguntas_riesgoNet(self.tipoDoc, self.nroDoc)
                self.seleccionar_continuar()
                self.selecionarDocViejo()
                self.ingresar_numero_tramite() 
            else:
                self.ingresar_digitos()
                self.ingresar_fecha()
                self.ingresar_pin()
            self.seleccionar_continuar()
            self.completar_datos_registro()
        self.paso = 1


    def primera_pagina_registro(self, preguntas):
        """
        Metodo para acceder a aplicacion de registro usuario. Se completa la
        primera pagina, que es el ingreso de documento. Luego, dependiendo
        el valor del parametro pregunta se selecciona el radiobutton para
        contestar las preguntas de seguridad o contestar los datos de la
        tarjeta.
        :param pregunta: Boolean. Si esta en True, se selecciona el radiobutton
                        de contestar preguntas de seguridad
        """
        # Metodo principal
        self.seleccionar_registrarme()
        self.log.info('Se intenta dar de alta un usuario')
        # Primera pag
        self.seleccionar_tipo_documento()
        self.ingresar_documento()
        self.seleccionar_continuar()
        # Aca falta buscar cuando se muestre el mensaje de usuario bloqueado
        xpath1 = locRegistro.radio_tarjetas
        xpath2 = locRegistro.msg_error
        if self.double_visibility_element(xpath1, xpath2, 20):
            if preguntas:
                self.seleccionarRadioPreguntas()
            else:
                self.seleccionarRadioTarjetas()
            self.seleccionar_continuar()
        else:
            texto = self.get_element_text(xpath2)
            if 'Aviso de bloqueo' in texto or 'inhabilitado' in texto:
                self.fail_msg('El usuario se encuentra bloqueado')
            else:
                self.fail_msg('Se muestra error para dar de alta al usuario.')

    def completar_datos_registro(self):
        """
        Metodo para completar los datos de la cuarta pantalla, en donde
        se solicita el nombre de usuario, clave y mail. Luego, ingresa la
        clave de activacion, buscandola dentro de los mails enviado
        """
        self.ingresar_usuario()
        self.ingresar_pass()
        self.ingresar_mail()
        # self.seleccionar_avatar()
        self.aceptar_terminos()
        self.seleccionar_continuar()
        # Cuarta pag
        # obtener el cod.activacion
        self.ingresarCodigoActivacion()
        self.seleccionarContinuarCodAct()
        self.seleccionarIngresarDespuesRegistro()
        
    def seleccionar_registrarme(self):
        accion = 'Seleccionar el boton de registro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(msgOk):
            xpath = locLogin.boton_registro
            if self.selectElement(xpath, msgOk, msgFail, to):
                xpath = locRegistro.titulo_registro
                self.verifySelection(xpath, msgOk, to)
                self.log.info(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarRadioPreguntas(self):
        accion = (
            u'Seleccionar radiobutton de Respondiendo preguntas de seguridad'
        )
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locRegistro.radio_preguntas
            self.selectElement(xpath, '', '')
            self.capture_image(msgOk)

    def seleccionarRadioTarjetas(self):
        accion = (
            u"Seleccionar el radiobutton de 'Con información de mi tarjeta "
            u"itaú'"
        )
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locRegistro.radio_tarjetas
            self.selectElement(xpath, '', '')
            self.capture_image(msgOk)

    def seleccionar_tipo_documento(self):
        accion = 'Seleccionar el tipo de documento'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.select_tipo_doc
            if self.select_by_text(xpath, self.tipoDoc):
                self.verifySelection(xpath, msgOk, to)
                self.log.info(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_documento(self):
        accion = 'Ingresar numero de documento'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.input_documento
            if self.write(xpath, self.nroDoc, to):
                self.verifySelection(xpath, msgOk, to)
                self.log.info(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_continuar(self):
        accion = 'Seleccionar continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.boton_continuar
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.verifySelection(xpath, accion, to)
                self.log.info(msgOk)
            else:
                self.fail_msg(msgFail)

    def get_respuesta(self, pregunta):
        """ Metodo para obtener la respuesta para el usuario 310 """
        for x in list_preg:
            if x[0].upper() in pregunta:
                return x[1]
        return None

    def responder(self, respuesta, xpath):
        """ Metodo para obtener las opciones para responder la pregunta.
        Se le pasa como parametro la respuesta y se la busca dentro de las
        opciones de respuestas para esa pregunta
        :param respuesta: String. Respuesta de la pregunta
        :param xpath: String. Xpath del conjunto de opciones de respuestas
        """
        opciones = self.search_elements(xpath, 10)
        encontre = False
        for option in opciones:
            if respuesta in option.text:
                option.find_element_by_tag_name('td').click()
                encontre = True
                break
        # Si no es ninguna de las opciones mostradas, elijo
        # "NINGUNA DE LAS ANTERIORES"
        if not encontre:
            opciones[4].find_element_by_tag_name('td').click()

    def contestar_registro(self):
        accion = 'Responder ultima pregunta'
        # to = 10
        with self.step(accion):
            pregunta = self.get_element_text(locRegistro.label_preguntas)
            respuesta = self.get_respuesta(pregunta)
            self.responder(respuesta, locRegistro.opciones_preg_1)
            self.capture_image(accion)

    def contestar_preguntas(self):
        accion = "Responder las preguntas"
        to = 10
        with self.step(accion):
            preguntas = self.search_elements(locRegistro.label_preguntas, to)
            preguntas = [x.text for x in preguntas]
            respuestas = [
                self.get_respuesta(pregunta) for pregunta in preguntas
            ]
            self.responder(respuestas[0], locRegistro.opciones_preg_1)
            self.responder(respuestas[1], locRegistro.opciones_preg_2)
            self.responder(respuestas[2], locRegistro.opciones_preg_3)
            self.responder(respuestas[3], locRegistro.opciones_preg_4)
            self.capture_image(accion)
            
    def ingresar_numero_tramite(self):
        accion = "Ingresar los digitos del nro tramite RNP "
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(locRegistro.input_num_RNP, self.Numero_RNP, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_digitos(self):
        accion = "Ingresar los digitos de la tarjeta"
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(locRegistro.input_4_digitos, self.NUMERO_TC, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_fecha(self):
        accion = "Ingresar la fecha de nacimiento"
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(locRegistro.input_fecha_nac, self.FECHA_NAC, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_usuario(self):
        accion = 'Ingresar nuevo usuario'
        to = 20
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(locRegistro.input_usuario, self.user, to):
                # self.write(locRegistro.input_usuario_confirmar, self.user, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_pass(self):
        accion = 'Ingresar nueva contrasena'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(locRegistro.input_pass, self.clave, to):
                self.write(locRegistro.input_pass_confirmar, self.clave, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_mail(self):
        accion = 'Ingresar mail'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            mail = self.get_attribute(locRegistro.input_mail, 'value')
            if self.write(locRegistro.input_mail, mail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def aceptar_terminos(self):
        accion = 'Aceptar terminos y condiciones'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.selectElement(locRegistro.check_terminos,
                                  msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_avatar(self):
        accion = 'Seleccionar avatar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.visibility_element(locRegistro.lista_avatares, to):
                avatares = self.search_element_by_xpath(
                                            locRegistro.lista_avatares)
                avatar = avatares.find_element_by_tag_name('img')
                avatar.click()
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_pin(self):
        accion = 'Ingresar PIN'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locRegistro.input_pin
            if self.write(xpath, self.PIN, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarCodigoActivacion(self):
        accion = u'Ingresar código de activación'
        to = 10
        with self.step(accion):
            self.wait(5)
            self.obtener_codigo()
            self.close_tab()
            xpath = locRegistro.input_codActivacion
            self.write(xpath, self.codigo, to)
            self.capture_image(accion)
            
    def ingresarCodigoActivacionRecupero(self):
        accion = u'Ingresar código de activación'
        to = 10
        with self.step(accion):
            self.wait(5)
            self.obtener_codigoRecupero()
            self.close_tab()
            xpath = locRegistro.input_codActivacion
            self.write(xpath, self.codigo, to)
            self.capture_image(accion)

    def seleccionarContinuarCodAct(self):
        accion = u'Seleccionar el botón de continuar luego ingreso cod.activacion'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.button_continuarCodAct
            self.selectElement(xpath, '', '')
            if self.visibility_element(locRegistro.span_registrado, to) and self.visibility_element(locRegistro.span_registrado2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarIngresarDespuesRegistro(self):
        accion = u'Seleccionar el botón Ingresar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.btnIngresar
            self.selectElement(xpath, '', '')
            if self.visibility_element(locLogin.inputUsuario, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)            
    
    def contestar_preguntas_riesgoNet(self, tipo, docu):
        """
        Metodo para contestar las preguntas de seguridad, utiliza el
        proceso para solicitar las respuestas en el servicio de riesgo net
        """
        accion = u'Contestar preguntas de riesgo net'
        with self.step(accion):
#             accion = u'Contestar preguntas de riesgo net'
            respuestas = self.obtenerRespuestas('asd', '123', tipo, docu)
            self.responder(respuestas[0], locRegistro.opciones_preg_1)
            self.responder(respuestas[1], locRegistro.opciones_preg_2)
            self.responder(respuestas[2], locRegistro.opciones_preg_3)
            self.responder(respuestas[3], locRegistro.opciones_preg_4)
            self.capture_image(accion)
    
    def selecionarDocViejo(self):
        accion = (
            u'Seleccionar radiobutton Documento Viejo'
        )
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locRegistro.radio_doc_viejo
            self.selectElement(xpath, '', '')
            self.capture_image(msgOk)

        
            
        
    def validErrProcOper(self):
        accion = u'Validar Error No podemos procesar operacion'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.msgErrNoPodProcOperac
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)            
                
    def seleccionarBtnCancelar(self):
        accion = 'Seleccionar boton Cancelar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.btnCancelar
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.verifySelection(xpath, accion, to)
                self.log.info(msgOk)
            else:
                self.fail_msg(msgFail)     
                
    def validarRedireccionLogin(self):
        accion = u'Validar redireccionamiento a pantalla Login'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locLogin.inputUsuario
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)       
        
        
    def validErrYaAdherido(self):
        accion = u'Validar Error cliente ya adherido'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locRegistro.msgYaAdherido
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)            
    