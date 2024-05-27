# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plAdmAlerta import plAdmAlert as AA
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.common_functions import get_msg
from sub import sub


class stAdmAlerta(sub):
    def seleccionarContinuar(self):
        accion = u'Seleccionar botón continuar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.selectElement(AA.button_continuar, '', '', to)
            xpath1 = AA.input_debitoAuto
            xpath2 = locLogin.titulo_esperado
            elem_array = [xpath1, xpath2]
            indice = self.array_visibility(elem_array, to)
            if indice in (0, 1):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCancelar(self):
        accion = u'Seleccionar botón cancelar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(AA.button_cancelar, '', '', to)
            if self.visibility_element(locLogin.titulo_esperado, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarAlertas(self, alertas):
        """Metodo para seleccionar las diferentes alertas
        :param alertas: Array. Array de string de las alertas que se quieren
                        seleccionar
        """
        alerta_dict = {
            u'Débito automático': self.seleccionarDebitoAutomatico,
            u'Devolución de débito automático': (
                self.seleccionarDevolucionDebAuto
                ),
            u'Rechazo de Débito Automático': self.seleccionarRechazoDebAuto,
            u'Acreditación de sueldo': self.seleccionarAcreditacionSueldo,
            u'Uso de acuerdo': self.seleccionarUsoAcuerdo,
            u'Vencimiento de plazo fijo': self.seleccionarVencimientoPlazoFijo,
            u'Recepción de transferencia': (
                self.seleccionarRecepcionTransferencia
                ),
            u'Cheques rechazados': self.seleccionarChequesRechazados,
            u'Pago de cheques': self.seleccionarPagoCheques,
            u'Extracciones': self.seleccionarExtracciones,
            u'Depósitos': self.seleccionarDepositos,
            u'Compras con tarjeta de débito': self.seleccionarCompraDebito,
            u'Vencimiento de cuota préstamo': (
                self.seleccionarVencimientoPrestamo
                ),
            u'Vencimiento de tarjeta Visa': self.seleccionarVencimientoVisa,
            u'Vencimiento de tarjeta MasterCard': (
                self.seleccionarVencimientoMaster
                ),
            u'Vencimiento PIN de tarjeta de debito': (
                self.seleccionarVencimientoPIN)
        }
        for alerta in alertas:
            alert = alerta_dict[alerta]
            if alert is None:
                self.log.warning(u"La alerta {} no es válida".format(alert))
            else:
                alert()

    def seleccionarTodoCuenta(self):
        accion = u'Seleccionar "Seleccionar todos" de la cuentas'
        with self.step(accion):
            self.selectElement(AA.input_seleccionarTodosCuentas, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarDebitoAutomatico(self):
        accion = u'Seleccionar débito automático'
        with self.step(accion):
            self.selectElement(AA.input_debitoAuto, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarDevolucionDebAuto(self):
        accion = u'Seleccionar devolución débito automático'
        with self.step(accion):
            self.selectElement(AA.input_devolucionDebAuto, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarRechazoDebAuto(self):
        accion = u'Seleccionar rechazo de débito automático'
        with self.step(accion):
            self.selectElement(AA.input_RechazoDebAuto, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarAcreditacionSueldo(self):
        accion = u'Seleccionar acreditación de sueldo'
        with self.step(accion):
            self.selectElement(AA.input_acredSueldo, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarUsoAcuerdo(self):
        accion = u'Seleccionar uso de acuerdo'
        with self.step(accion):
            self.selectElement(AA.input_usoAcuerdo, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarVencimientoPlazoFijo(self):
        accion = u'Seleccionar vencimiento de plazo fijo'
        with self.step(accion):
            self.selectElement(AA.input_vencimientoPlazoFijo, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarRecepcionTransferencia(self):
        accion = u'Seleccionar recepción de transferencia'
        with self.step(accion):
            self.selectElement(AA.input_recepcionTransferencia, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarChequesRechazados(self):
        accion = u'Seleccionar chequese rechazados'
        with self.step(accion):
            self.selectElement(AA.input_chequesRechazados, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarPagoCheques(self):
        accion = u'Seleccionar pago de cheques'
        with self.step(accion):
            self.selectElement(AA.input_pagoCheques, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarExtracciones(self):
        accion = u'Seleccionar Extracciones'
        with self.step(accion):
            self.selectElement(AA.input_extracciones, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarDepositos(self):
        accion = u'Seleccionar depósitos'
        with self.step(accion):
            self.selectElement(AA.input_depositos, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarCompraDebito(self):
        accion = u'Seleccionar compras con tarjeta de débito'
        with self.step(accion):
            self.selectElement(AA.input_comprasDebito, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarVencimientoPrestamo(self):
        accion = u'Seleccionar vencimiento de prestamo'
        with self.step(accion):
            self.selectElement(AA.input_vencimientoPrestamo, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarTodoTarjetas(self):
        accion = u'Seleccionar "Seleccionar todo" de las tarjetas'
        with self.step(accion):
            self.selectElement(AA.input_seleccionarTodosTarjetas, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarVencimientoVisa(self):
        accion = u'Seleccionar vencimiento de tarjeta VISA'
        with self.step(accion):
            self.selectElement(AA.input_vencimientoVisa, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarVencimientoMaster(self):
        accion = u'Seleccionar vencimiento de tarjeta MASTER'
        with self.step(accion):
            self.selectElement(AA.input_vencimientoMaster, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarVencimientoPIN(self):
        accion = u'Seleccionar vencimiento de PIN'
        with self.step(accion):
            self.selectElement(AA.input_vencimientoPIN, '', '')
            self.capture_image(accion, 0.1)

    def seleccionarConfirmar(self):
        accion = u'Seleccionar botón de confirmación'
        msgOk, msgFail = get_msg(accion)
        to = 20
        with self.step(accion):
            self.selectElement(AA.button_confirmacion, '', '')
            if self.visibility_element(AA.img_ticket, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarModificar(self):
        accion = u'Seleccionar botón de modificar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(AA.button_modificar, '', '')
            if self.visibility_element(AA.input_debitoAuto, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificacion de pantallas
    def verificarPantallaConfirmacion(self):
        xpath1 = AA.table_alertas
        xpath2 = AA.span_sinAlertas
        to = 10
        if self.double_visibility_element(xpath1, xpath2, to):
            self.verificarTablaAlertas()
        else:
            self.verificarSinAlertas()
        self.verificarBotonModificar()
        self.verificarBotonConfirmar()

    def verificarPantallaResultados(self):
        self.verificarTicket()
        self.verificarNuevaAlerta()
        self.verificarDescargar()
        self.verificarBotonContinuar()

    # Verificacion de elementos
    def verificarSinAlertas(self):
        accion = u'Verificar mensaje de sin alertas'
        to = 10
        with self.step(accion):
            self.checkElement(AA.span_sinAlertas, accion, to)

    def verificarTablaAlertas(self):
        accion = u'Verificar tabla de alertas'
        to = 10
        with self.step(accion):
            self.checkElement(AA.table_alertas, accion, to)

    def verificarBotonModificar(self):
        accion = u'Verificar botón modificar'
        to = 10
        with self.step(accion):
            self.checkElement(AA.button_modificar, accion, to)

    def verificarBotonConfirmar(self):
        accion = u'Verirficar botón confirmar'
        to = 10
        with self.step(accion):
            self.checkElement(AA.button_confirmacion, accion, to)

    def verificarTicket(self):
        accion = u'Verificar que se muestra el ticket'
        to = 10
        with self.step(accion):
            self.checkElement(AA.img_ticket, accion, to)

    def verificarNuevaAlerta(self):
        accion = u'Verificar botón Nueva alerta'
        to = 10
        with self.step(accion):
            self.go_to_xpath(AA.button_nuevaAlerta)
            self.checkElement(AA.button_nuevaAlerta, accion, to)

    def verificarDescargar(self):
        accion = u'Verificar botón descargar'
        to = 10
        with self.step(accion):
            self.checkElement(AA.button_descargar, accion, to)

    def verificarBotonContinuar(self):
        accion = u'Verificar botón continuar'
        to = 10
        with self.step(accion):
            self.checkElement(AA.button_continuar, accion, to)

    def chequeoAlerta(self, alerta):
        to = 10
        alertas = self.search_elements(AA.option_alertas, to)
        valores = [x.text for x in alertas]
        if alerta in valores:
            return True
        return False

    def verificarAlertas(self, alertas):
        accion = 'Verificar alertas'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            for alerta in alertas:
                if self.chequeoAlerta(alerta):
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)

    def verificarAlertaNoPresente(self, alertas):
        accion = u'Verificar que no se encuentre la alerta'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath1 = AA.span_sinAlertas
            xpath2 = AA.table_alertas
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
                return True
            # Si se muestra la tabla de alertas
            for alerta in alertas:
                if self.chequeoAlerta(alerta):
                    self.fail_msg(msgFail)
            self.capture_image(msgOk)
            return True
