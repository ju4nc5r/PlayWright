# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plCompraTitulos import plCompraTitulo as CT
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg
from error_management import errors
from search import  search


class stCompraTitulos(menu,search,errors):
    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta comitente'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(CT.select_cuentaComitente, cuenta)
            self.capture_image(msgOk)

    def seleccionarTitulos(self):
        accion = u'Seleccionar radiobutton de títulos'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectElement(CT.radio_bonosTitulos, '', '', to)
            self.capture_image(msgOk)

    def seleccionarAcciones(self):
        accion = u'Seleccionar radiobutton de acciones'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectElement(CT.radio_acciones, '', '', to)
            self.capture_image(msgOk)

    def ingresarLetras(self, letras):
        accion = u'Ingresar las letras de la especie'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.write(CT.input_letrasEspecie, letras, to)
            self.capture_image(msgOk)

    def seleccionar_btn_buscar(self):
        to = 10
        accion = u'Seleccionar botón buscar'
        msgOk = accion
        msgFail = u"No se pudo",msgOk
        msgOk, _ = get_msg(accion)
        xpath = CT.button_buscar
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                self.selectElement(xpath,msgOk,msgFail,to)
            else:
                self.fail_test(msgFail)


    def seleccionarBuscar(self):
        accion = u'Seleccionar botón buscar'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectElement(CT.button_buscar, '', '', to)
            xpath1 = CT.tabla_titulos
            xpath2 = CT.div_error
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(u'Se está mostrando un mensaje de error')

    def seleccionarTituloAComprar(self, titulo):
        accion = u'Seleccionar título a comprar'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = CT.opcion_titulo.format(opcion=titulo)
            self.selectElement(xpath, '', '', to)
            self.capture_image(msgOk)

    def ingresarCantidadNominales(self, cantidad):
        accion = u'Ingresar la cantidad de nominales a comprar'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.write(CT.input_cantidadNominales, cantidad, to)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        accion = u'Seleccionar el botón continuar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.selectElement(CT.button_continuar, '', '', to)
            xpath1 = CT.input_precioCompra
            xpath2 = CT.checkbox_terminosCond
            xpath3 = CT.div_error
            elem_list = [xpath1, xpath2, xpath3]
            numero = self.array_visibility(elem_list, to)
            if numero in (0, 1):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarPrecio(self, precio):
        accion = u'Ingresar el precio'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.write(CT.input_precioCompra, precio, to)
            self.capture_image(msgOk)

    def seleccionarCantidadRueda(self, cantidad):
        accion = u'Seleccionar cantidad de ruedas'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = CT.select_cantRueda
            self.go_to_xpath(xpath)
            self.select_by_text(xpath, cantidad)
            self.capture_image(msgOk)

    def seleccionarCuentaDebito(self, cuenta):
        accion = u'Seleccionar cuenta débito'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = CT.select_cuentaDebito
            self.go_to_xpath(xpath)
            self.selectListByPartialText(xpath, cuenta)
            self.capture_image(msgOk)

    def seleccionarAceptarCondiciones(self):
        accion = u'Seleccionar checkbox de aceptar condiciones'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = CT.checkbox_aceptarTerminos
            self.go_to_xpath(xpath)
            self.selectElement(xpath, '', '')
            self.capture_image(msgOk)

    def seleccionarConfirmar(self):
        accion = u'Seleccionar el botón de confirmar'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = CT.button_confirmar
            self.go_to_xpath(xpath)
            self.selectElement(xpath, '', '')
            self.capture_image(msgOk)

    def seleccionarNuevaOperacion(self):
        accion = u'Seleccionar el botón nueva operación'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = CT.button_nuevaOperacion
            self.go_to_xpath(xpath)
            self.selectElement(xpath, '', '')
            if self.visibility_element(CT.select_cuentaComitente, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificar pantallas
    def verificarPantallaCargaDatos(self):
        """
        Metodo para verificar los elementos que se encuentran en la
        pantalla de carga de datos
        """
        self.verificarSelectCuenta()
        self.verificarRadioTitulo()
        self.verificarRadioAcciones()
        self.verificarBotonCancelar()

    def verificarPantallaConfirmacion(self):
        """
        Metodo para verificar los elementos que se encuentran en la
        pantalla de confirmacion.
        """
        self.verificarEspecie()
        self.verificarCantidadNominales()
        self.verificarPrecio()
        self.verificarMonto()
        self.verificarCantidadRuedas()
        self.verificarComisionBanco()
        self.verificarComisionMinima()
        self.verificarComisionMercado()
        self.verificarCuentaDebito()
        self.verificarCuentaComitente()

    def verificarPantallaResultado(self):
        """
        Metodo para verificar los elementos que se encuentran en la pnatalla
        de resultado
        """
        self.verificarNumeroOrden()
        self.verificarFechaHora()

    # Verificar elementos
    def verificarSelectCuenta(self):
        accion = u'Verificar select de cuenta comitente'
        to = 10
        with self.step(accion):
            self.checkElement(CT.select_cuentaComitente, accion, to)

    def verificarRadioTitulo(self):
        accion = u'Verificar radiobutton de título'
        to = 10
        with self.step(accion):
            self.checkElement(CT.radio_bonosTitulos, accion, to)

    def verificarRadioAcciones(self):
        accion = u'Verificar radiobutton de acciones'
        to = 10
        with self.step(accion):
            self.checkElement(CT.radio_acciones, accion, to)

    def verificarBotonCancelar(self):
        accion = u'Verificar botón cancelar'
        to = 10
        with self.step(accion):
            self.checkElement(CT.button_cancelar, accion, to)

    def verificarLetrasEspecie(self):
        accion = u'Verificar input de las 3 letras de la especie'
        to = 10
        with self.step(accion):
            self.checkElement(CT.input_letrasEspecie, accion, to)

    def verificarEspecie(self):
        accion = u'Verificar el texto de la especie'
        with self.step(accion):
            self.checkElement(CT.span_especie, accion)

    def verificarCantidadNominales(self):
        accion = u'Verificar el texto de la cantidad de nominales'
        with self.step(accion):
            self.checkElement(CT.span_cantNominales, accion)

    def verificarPrecio(self):
        accion = u'Verificar el texto del precio límite'
        with self.step(accion):
            self.checkElement(CT.span_precioCompra, accion)

    def verificarMonto(self):
        accion = u'Verificar el texto del monto'
        with self.step(accion):
            self.checkElement(CT.span_montoEstimado, accion)

    def verificarCantidadRuedas(self):
        accion = u'Verificar el texto de la cantidad de ruedas'
        with self.step(accion):
            self.checkElement(CT.span_cantRueda, accion)

    def verificarComisionBanco(self):
        accion = u'Verificar el texto de la comisión del banco'
        with self.step(accion):
            self.checkElement(CT.span_comisionBanco, accion)

    def verificarComisionMinima(self):
        accion = u'Verificar el texto de la comisión mínima'
        with self.step(accion):
            self.checkElement(CT.span_comisionMinima, accion)

    def verificarComisionMercado(self):
        accion = u'Verificar el texto de la comisión del mercado'
        with self.step(accion):
            self.checkElement(CT.span_comisionMercado, accion)

    def verificarCuentaDebito(self):
        accion = u'Verificar el texto de la cuenta de débito'
        with self.step(accion):
            self.checkElement(CT.span_cuentaDebito, accion)

    def verificarCuentaComitente(self):
        accion = u'Verificar el texto de la cuenta comitente'
        with self.step(accion):
            self.checkElement(CT.span_cuentaComitente, accion)

    def verificarAceptarTerminos(self):
        accion = u'Verificar el checkbox para aceptar términos y condiciones'
        with self.step(accion):
            self.checkElement(CT.checkbox_terminosCond, accion)

    def verificarNumeroOrden(self):
        accion = u'Verificar el número de orden'
        with self.step(accion):
            self.checkElement(CT.span_nroOrden, accion)

    def verificarFechaHora(self):
        accion = u'Verificar fecha y hora de compra'
        with self.step(accion):
            self.checkElement(CT.span_fechaHora, accion)
            
    def verificar_advertencia(self):
        accion = u"Verificar advertencia: La especie ingresada no pudo ser encontrada. Por favor intentá nuevamente o comunicate con el Centro de Inversiones Itaú llamando al 0810-345-4900 "
        msgOk = accion
        msgFail = u"Nose pudo ",msgOk
        to = 2
        xpath = CT.p_warnig
        with self.step(msgOk):
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_test(msgFail)
            
                

        
        
