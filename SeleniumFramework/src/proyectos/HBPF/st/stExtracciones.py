# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plExtracciones import plExtracciones
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stExtracciones(menu):

    def seleccionarOtraPersona(self):
        accion = u'Seleccionar otra persona'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.btn_otra_persona
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarMonto(self, monto):
        to = 10
        accion = 'Ingresar monto a retirar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plExtracciones.ipt_monto
            if self.visibility_element(xpath, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarDocumento(self, doc):
        to = 10
        accion = 'Ingresar numero de documento'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plExtracciones.ipt_num_dc
            if self.visibility_element(xpath, to):
                self.write(xpath, doc, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarRandomRegistro(self):
        accion = u'Seleccionar random registro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.row_random
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def seleccionarPrimerRegistro(self):
        accion = u'Seleccionar primer registro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.first_row_registros
            tit = plExtracciones.titulo_consulta
            self.go_to_xpath(tit)
            if self.visibility_element(xpath, to):
                # self.selectElement(xpath, msgOk, msgFail, to)
                self.highlight(xpath, accion)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)             
    
    def seleccionarSegundoRegistro(self):
        accion = u'Seleccionar segundo registro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.second_row_registros
            tit = plExtracciones.titulo_consulta
            self.go_to_xpath(tit)
            if self.visibility_element(xpath, to):
                # self.selectElement(xpath, msgOk, msgFail, to)
                self.highlight(xpath, accion)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuar(self):
        accion = u'Seleccionar botón de continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.btn_continuar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 

    def seleccionarContinuar2(self):
        accion = u'Seleccionar botón de continuar 2'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.btn_continuar_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 

    def seleccionarConfirmar(self):
        accion = u'Seleccionar botón de confirmar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.btn_confirmar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def aceptarTerminosCondiciones(self):
        accion = u'Seleccionar aceptar términos y condiciones'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.input_checkboxTerminos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarTicket(self):
        accion = u'Verificar imagen del ticket de resultado'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.img_ticket
            if self.visibility_element(xpath, to):
               self.highlight(xpath,accion)
            else:
                self.fail_msg(msgFail)
    
    def verificarPendiente(self):
        accion = u'Verificar label pendiente'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.row_pendiente
            if self.visibility_element(xpath, to):
               self.highlight(xpath,accion)
            else:
                self.fail_msg(msgFail)

    def seleccionarVolver(self):    
        accion = "Seleccionar volver"
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plExtracciones.btn_volver
            if self.visibility_element(xpath, to):
               self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
