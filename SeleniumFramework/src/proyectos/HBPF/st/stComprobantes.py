# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.loc.locComprobantes import locComprobantes as LC
from SeleniumFramework.common_functions import get_msg


class stComprobantes(stLogin, menu):
    def verificarCampos(self):
        """Metodo para verificar todos los campos del comprobante"""
        self.verificarOperaciones()
        self.verificarFechaDesde()
        self.verificarFechaHasta()
        self.verificarCanal()
        self.verificarNumOperacion()
        self.capture_image('Se verifica que se muestre todos los campos')

    def verificarOperaciones(self):
        """Metodo para verificar que se muestre el campo operaciones"""
        accion = 'Verificar que se muestra el campo operaciones'
        _, msgFail = get_msg(accion)
        to = 10
        xpath_label = LC.txt_operaciones
        xpath_select = LC.sel_operaciones
        if (self.visibility_element(xpath_label, to) and
                self.visibility_element(xpath_select, to)):
            return True
        self.fail_msg(msgFail)
        return False

    def verificarFechaDesde(self):
        """
        Metodo para verificar que se esten mostrando los campos de la fecha
        desde
        """
        accion = 'Verificar que se muestran los campos de fecha desde'
        _, msgFail = get_msg(accion)
        to = 10
        xpath_label = LC.txt_fecha_desde
        xpath_input = LC.inp_fecha_desde
        if (self.visibility_element(xpath_label, to) and
                self.visibility_element(xpath_input, to)):
            return True
        self.fail_msg(msgFail)
        return False

    def verificarFechaHasta(self):
        """
        Metodo para verificar que se esten mostrando los campos de la fecha
        hasta
        """
        accion = 'Verificar que se muestran los campos de la fecha hasta'
        _, msgFail = get_msg(accion)
        to = 10
        xpath_label = LC.txt_fecha_hasta
        xpath_input = LC.inp_fecha_hasta
        if (self.visibility_element(xpath_label, to) and
                self.visibility_element(xpath_input, to)):
            return True
        self.fail_msg(msgFail)
        return False

    def verificarCanal(self):
        """
        Metodo para verificar que se esten mostrando los elementos del
        campo canal
        """
        accion = 'Verificar que se muestran los campos del canal'
        _, msgFail = get_msg(accion)
        to = 10
        xpath_label = LC.txt_canal
        xpath_select = LC.sel_canal
        if (self.visibility_element(xpath_label, to) and
                self.visibility_element(xpath_select, to)):
            return True
        self.fail_msg(msgFail)
        return False

    def verificarNumOperacion(self):
        """
        Metodo para verificar que se esten mostrando los elementos del campo
        numero de operacion
        """
        accion = u'Verificar que se muestra el campo del número de operaciones'
        _, msgFail = get_msg(accion)
        to = 10
        xpath_label = LC.txt_num_op
        xpath_input = LC.inp_num_op
        if (self.visibility_element(xpath_label, to) and
                self.visibility_element(xpath_input, to)):
            return True
        self.fail_msg(msgFail)
        return False

    def seleccionarOperacion(self, opcion):
        """
        Metodo para seleccionar la opcion deseada en el select de operaciones
        """
        accion = u'Seleccionar la opción del select'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = LC.sel_operaciones
            self.select_by_text(xpath, opcion)
            self.capture_image(msgOk)

    def ingresarFechaDesde(self, fecha):
        """ Metodo para ingresar la fecha desde """
        accion = 'Ingresar la fecha desde'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = LC.inp_fecha_desde
            self.write(xpath, fecha, to)
            self.capture_image(msgOk)

    def ingresarFechaHasta(self, fecha):
        """ Metodo para ingresar la fecha hasta """
        accion = 'Ingresar la fecha hasta'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = LC.inp_fecha_hasta
            self.write(xpath, fecha, to)
            self.capture_image(msgOk)

    def seleccionarCanal(self, opcion):
        """
        Metodo para seleccionar el tipo de canal
        :param opcion: Integer. Indice de la opcion que se quiere seleccionar
        """
        accion = 'Seleccionar canal'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = LC.sel_canal
            self.select_by_text(xpath, opcion)
            self.capture_image(msgOk)

    def seleccionarBuscar(self):
        """Metodo para seleccionar el boton buscar"""
        accion = u'Seleccionar botón buscar'
        to = 10
        with self.step(accion):
            xpath = LC.boton_buscar
            self.selectElement(xpath, '', '', to)
            xpath_tabla = LC.tbl_comprobantes
            xpath_error = LC.div_error
            xpath_sin_comprobante = LC.tbl_sin_comprobantes
            elem_list = [xpath_tabla, xpath_error, xpath_sin_comprobante]
            numero = self.array_visibility(elem_list, to)
            if numero == 0:
                # self.go_to_xpath(xpath_tabla)
                self.capture_image('Se muestra la tabla con los resultados')
            elif numero == 1:
                self.fail_msg(u'Se está mostrando un error')
            elif numero == 2:
                self.fail_msg(u'No se está mostrando ningún comprobante')

    def seleccionarPrimerPdf(self):
        """Metodo para seleccionar el icono de pdf del primer comprobante"""
        accion = 'Seleccionar comprobante'
        to = 10
        with self.step(accion):
            xpath = LC.icono_primer_pdf
            if self.visibility_element(xpath, to):
                # self.go_to_xpath(xpath)
                self.selectElement(xpath, '', '', to)
            else:
                self.fail_msg(u'No se está mostrando el elemento')

    def verificarComprobante(self):
        """Metodo para comprobar si se muestra el comprobante o no """
        pass
    
    def verTicket(self):
        u"Metodo para visualizar que se esta mostrando la imagen del ticket"
        to = 10
        accion = u'Ver Ticket'
#         accion = 'Ver Ticket'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = LC.image_ticket
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)