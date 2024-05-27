# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaTC import locConsultaTC as TC
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plAdhesionDebAuto import plAdhesionDebAuto
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaTC(stLogin, menu):
    def seleccionarTarjeta(self, tarjeta):
        """
        Metodo para seleccionar la tarjeta a utilizar
        """
        accion = 'Seleccionar la tarjeta {}'.format(tarjeta)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.sel_tarjeta
            if self.selectListByPartialText(xpath, tarjeta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarVolver(self):
        """
        Metodo para seleccionar el boton volver en la pantalla de consulta
        """
        accion = u'Seleccionar el botón volver'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_volver
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(TC.titulo_inicio):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarBloqueo(self):
        """
        Metodo para seleccionar el boton de bloqueo
        """
        accion = u'Seleccionar el botón de bloqueo'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_bloqueo
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(TC.tabla_bloqueo, to):
                self.capture_image(msgOk)
            self.fail_msg(msgFail)

    def seleccionarReposicion(self):
        """
        Metodo para seleccionar el boton de reposicion
        """
        accion = u'Seleccionar el botón de reposición'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_reposicion
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(TC.titulo_reposicion, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarPagar(self):
        """
        Metodo para seleccionar el boton de pagar
        """
        accion = u'Seleccionar el botón pagar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_pagar
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(TC.titulo_pagar):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarPagosRealizadosPesos(self):
        accion = u'Seleccionar pagos realizados en pesos'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.href_pagosPesos
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = TC.tabla_pagosRealizados
            xpath2 = TC.div_error
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
                self.seleccionarCerrar()
            else:
                self.capture_image('Se muestra mensaje de error')

    def seleccionarPagosRealizadosDolar(self):
        accion = u'Seleccionar pagos realizados en dólar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.href_pagosDolares
            self.selectElement(xpath, msgOk, msgFail, to)
            if self.visibility_element(TC.tabla_pagosRealizados, to):
                self.capture_image(msgOk)
                self.seleccionarCerrar()
            else:
                self.fail_msg(msgFail)

    def seleccionarCerrar(self):
        accion = u'Seleccionar botón cerrar'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_cerrar
            self.selectElement(xpath, '', '', to)
            self.capture_image(msgOk)

    def seleccionarAdherirseDebAuto(self):
        accion = u'Seleccionar botón de adhesión al débito automático'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_adherirDebAuto
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(plAdhesionDebAuto.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCancelarBloqueo(self):
        accion = u'Seleccionar botón cancelar bloqueo de tarjeta'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_cancelarBloq
            self.selectElement(xpath, msgOk, msgFail, to)
            if self.visibility_element(TC.sel_tarjeta, to):
                self.capture_image(accion)
            else:
                self.fail_msg(msgFail)

    def seleccionarCancelarAdherirDebAuto(self):
        accion = u'Seleccionar botón cancelar adherir debito automatico'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.btn_cancelarAdherirDebAuto
            self.selectElement(xpath, msgOk, msgFail, to)
            self.wait(1)
            self.capture_image(msgOk)

    # Verificacion de pantalla
    def verificarPantallaConsulta(self):
        """
        Metodo para verificar todos los elementos que se muestran en la
        pantalla de consulta
        """
        self.verificarTarjetas()
        self.verificarDetalle()
        self.verificarAdhesionDebAuto()
        self.verificarStopDeb()
        self.verificarLimCompra()
        self.verificarBotonVolver()
        self.verificarBotonBloqueo()
        self.verificarBotonReposicion()
        self.verificarBotonPagar()

    # Verificacion de elementos
    def verificarTarjetas(self):
        accion = u'Se verifica el select de tarjetas'
        to = 10
        with self.step(accion):
            xpath = TC.sel_tarjeta
            self.checkElement(xpath, accion, to)

    def verificarDetalle(self):
        accion = u'Verificar la tabla de detalle'
        to = 10
        with self.step(accion):
            xpath = TC.tbl_detalle
            self.checkElement(xpath, accion, to)

    def verificarAdhesionDebAuto(self):
        accion = u'Verificar débito automático'
        to = 10
        with self.step(accion):
            xpath = TC.txt_debAuto
            self.checkElement(xpath, accion, to)

    def verificarStopDeb(self):
        accion = u'Verificar stop deb'
        to = 10
        with self.step(accion):
            xpath = TC.txt_stopDeb
            self.checkElement(xpath, accion, to)

    def verificarLimCompra(self):
        accion = u'Verificar límite de compra'
        to = 10
        with self.step(accion):
            xpath = TC.txt_limCompra
            self.checkElement(xpath, accion, to)

    def verificarBotonVolver(self):
        accion = u'Verificar botón volver'
        to = 10
        with self.step(accion):
            xpath = TC.btn_volver
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarBotonBloqueo(self):
        accion = u'Verificar botón bloqueo'
        to = 10
        with self.step(accion):
            xpath = TC.btn_bloqueo
            self.checkElement(xpath, accion, to)

    def verificarBotonPagar(self):
        accion = u'Verificar botón pagar'
        to = 10
        with self.step(accion):
            xpath = TC.btn_pagar
            self.checkElement(xpath, accion, to)

    def verificarBotonReposicion(self):
        accion = u'Verificar botón reposicion'
        to = 10
        with self.step(accion):
            xpath = TC.btn_reposicion
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarBotonDebAuto(self):
        accion = u'Verificar botón débito automático'
        to = 10
        with self.step(accion):
            xpath = TC.btn_adherirDebAuto
            self.checkElement(xpath, accion, to)

    def verificarAdicionales(self, ignora=False):
        accion = 'Verificar tarjetas adicionales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.titulo_adicionales
            if ignora:
                if self.visibility_element(xpath):
                    self.fail_msg(msgOk)
                else:
                    self.capture_image(msgFail)
            else:
                if self.visibility_element(xpath):
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)

    def verificarEstadoDebitoAutomatico(self, estado_esperado):
        accion = u'Verficar el estado del debito automatico'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = TC.span_modif_debito
            estado = self.get_element_text(xpath)
            print(estado_esperado)
            print(xpath)
            if estado_esperado in estado:
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
