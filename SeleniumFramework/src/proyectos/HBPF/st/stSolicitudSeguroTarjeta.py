# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudSeguroTarjeta import (
    plSolicitudSeguroTarjeta as SS
)
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stSolicitudSeguroTarjeta(menu):
    def seleccionarMedioPago(self, medio):
        accion = u'Seleccionar método de pago'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SS.select_medioDePago, medio)
            self.capture_image(msgOk)

    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SS.select_cuenta, cuenta)
            self.capture_image(msgOk)

    def seleccionarTermCond(self):
        accion = u'Seleccionar Términos y condiciones'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.input_terminosYCondicion, '', '', to)
            self.capture_image(msgOk)

    def seleccionarCancelar(self):
        accion = u'Seleccionar botón cancelar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.button_cancelar, '', '', to)
            if self.visibility_element(locLogin.titulo_esperado, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuar(self):
        accion = u'Seleccionar botón continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.button_continuar, '', '', to)
            if self.visibility_element(SS.subtitulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarModificar(self):
        accion = u'Seleccionar botón modificar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.button_modificar, '', '', to)
            self.capture_image(msgOk)

    # Verificacion de la pantalla
    def verificarPantallaSolicitudSeguro(self):
        self.verificarNombre()
        self.verificarTipoDoc()
        self.verificarNumeroDoc()
        self.verificarLineaProducto()
        self.verificarProducto()
        self.verificarMedioPago()
        self.verificarTermCond()
        self.verificarBotonCancelar()
        self.verificarBotonModificar()
        self.verificarBotonContinuar()

    def verificarPantallaConfirmacion(self):
        self.verificarPlan()
        self.verificarSumaAsegurada()
        self.verificarCosto()
        self.verificarMedioDePago()

    # Verificacion de los elementos
    def verificarNombre(self):
        accion = u'Verificar el nombre del usuario'
        with self.step(accion):
            self.checkElement(SS.span_nombre, accion)

    def verificarTipoDoc(self):
        accion = u'Verificar tipo de documento'
        with self.step(accion):
            self.checkElement(SS.span_tipoDoc, accion)

    def verificarNumeroDoc(self):
        accion = u'Verificar el numero de documento'
        with self.step(accion):
            self.checkElement(SS.span_numDoc, accion)

    def verificarLineaProducto(self):
        accion = u'Verificar línea producto'
        with self.step(accion):
            self.checkElement(SS.span_lineaProducto, accion)

    def verificarProducto(self):
        accion = u'Verificar Producto'
        with self.step(accion):
            self.checkElement(SS.span_producto, accion)

    def verificarMedioPago(self):
        accion = u'Verificar select de medio de pago'
        with self.step(accion):
            self.checkElement(SS.select_medioDePago, accion)

    def verificarTermCond(self):
        accion = u'Verificar checkbox de términos y condiciones'
        with self.step(accion):
            self.checkElement(SS.input_terminosYCondicion, accion)

    def verificarBotonCancelar(self):
        accion = u'Verificar el botón Cancelar'
        with self.step(accion):
            self.checkElement(SS.button_cancelar, accion)

    def verificarBotonModificar(self):
        accion = u'Verificar el botón modificar'
        with self.step(accion):
            self.step(accion)
            self.checkElement(SS.button_modificar, accion)

    def verificarBotonContinuar(self):
        accion = u'Verificar el botón continuar'
        with self.step(accion):
            self.checkElement(SS.button_continuar, accion)

    def verificarPlan(self):
        accion = u'Verficar plan'
        with self.step(accion):
            self.checkElement(SS.span_plan, accion)

    def verificarSumaAsegurada(self):
        accion = 'Verificar suma asegurada'
        with self.step(accion):
            self.checkElement(SS.span_sumaAsegurada, accion)

    def verificarCosto(self):
        accion = u'Verificar costo'
        with self.step(accion):
            self.checkElement(SS.span_costo, accion)

    def verificarMedioDePago(self):
        accion = u'Verificar medio de pago'
        with self.step(accion):
            self.checkElement(SS.span_medioDePago, accion)
