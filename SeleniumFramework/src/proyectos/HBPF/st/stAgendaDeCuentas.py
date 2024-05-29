# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu, Transferencia
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plAgendaDeCuentas import plAgendaDeCuentas
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.common_functions import get_msg


class stAgendaDeCuentas(stLogin, menu, Transferencia):
    
    def seleccionarAlta(self):
        to = 10
        accion = "Seleccionar Alta"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.btn_alta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
    
    def seleccionarClienteOtroBanco(self):
        to = 10
        accion = "Seleccionar Cliente Otro Banco"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.rbtClienteOtroBanco
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
    

    def seleccionarContinuar(self):
        to = 10
        accion = "Seleccionar Continuar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.btn_alta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
    
    def seleccionarConfirmar(self):
        to = 10
        accion = "Seleccionar confirmar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.btn_alta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
    
    def seleccionarEliminar(self):
        to = 10
        accion = "Seleccionar eliminar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.btn_alta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
                
                
    def seleccionarModificar(self):
        to = 10
        accion = "Seleccionar modificar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.btn_modif
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
    
    
    def ingresarCuenta(self, cuenta):
        to = 10
        accion = "Ingresar Cuenta"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ipt_cuenta
            if self.visibility_element(xpath, to):
                self.write(xpath, cuenta, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)
    
    
    def ingresarCuentaDestinoCases(self, cuenta):
        """
        Metodo para ingresar el cbu en agenda de cuenta
        """
        to = 10
        accion = 'Ingresar CBU'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ipt_cbu
            self.write(xpath, cuenta, to)
            self.capture_image(msgOk)            
                
                
    def ingresarDescripcion(self, desc):
        to = 10
        accion = "Ingresar Descripcion"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ipt_desc
            if self.visibility_element(xpath, to):
                self.write(xpath, desc, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)

    def ingresarDescripcionModif(self, desc):
        to = 10
        accion = "Ingresar Descripcion modificada"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ipt_descModif
            if self.visibility_element(xpath, to):
                self.write(xpath, desc, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)

    def ingresarEmail(self, email):
        to = 10
        accion = "Ingresar Email"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ipt_email
            if self.visibility_element(xpath, to):
                self.write(xpath, email, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)

    def validarTicket(self):
        to = 10
        accion = u'Validar ticket'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ticket
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarClienteNuevo(self, desc):
        to = 10
        accion = "seleccionar cliente nuevo"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.cliente_nuevo.format(desc)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarClienteOtroBanco(self, desc):
        to = 10
        accion = "seleccionar cliente otro banco"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.rbtClienteOtroBanco.format(desc)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarBtnAlta(self):
        to = 10
        accion = "seleccionar boton alta"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.btn_alta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    
                
    def seleccionarOtroBanco(self):
        to = 10
        accion = "seleccionar cliente otro banco"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAgendaDeCuentas.ipt_otroBanco
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
