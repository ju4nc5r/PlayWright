# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import Transferencia
from SeleniumFramework.src.proyectos.HBPF.loc.locTransferenciasOtroBanco import (
    locTransferenciasOtroBanco
)
# from SeleniumFramework.src.proyectos.HBPF.constants.tarj_coordenadas import *
from SeleniumFramework.common_functions import get_msg


class stTransferenciaOtroBanco(stLogin, menu, Transferencia):

    def TransferenciaOtroBanco(self):
        """ Metodo para realizar la transferencia a otro banco con el CBU"""
        self.completar_formulario()
        self.finalizar_formulario()

    def TransferenciaOtroBancoAlias(self):
        """ Metodo para realizar la transferencia a otro banco con el alias """
        self.completar_formulario_alias()
        self.finalizar_formulario()

    def TransferenciaOtroBancoConCheck(self):
        """
        Metodo para realizar la transferencias a otro banco con CBU.
        En este caso, hay que hacer un check sobre un checkbox
        """
        self.completar_formulario()
        self.seleccionar_check_concepto()
        self.finalizar_formulario()

    def completar_formulario(self):
        """
        Metodo para ingresar a la pantalla de transferencia.
        Rellenar el fomulario de transferencia.
        """
        self.seleccionarMenuTransferencias()
        self.seleccionar_a_otros_bancos()
        self.seleccionarCuentaDebito()
        self.seleccionarMedioCuentaDestino()
        self.ingresarCuentaDestino()
        self.completarCaractCuentaAcreditacion()
        self.seleccionarConcepto()
        self.completarImporte()

    def completar_formulario_alias(self):
        """
        Metodo para ingresar a la pantalla de transferencia.
        Rellenar el fomulario de transferencia utilizando el alias
        """
        self.seleccionarMenuTransferencias()
        self.seleccionar_a_otros_bancos()
        self.seleccionarCuentaDebito()
        self.seleccionarMedioCuentaDestino('Alias')
        self.ingresarCuentaDestino()
        self.completarCaractCuentaAcreditacion()
        self.seleccionarConcepto()
        self.completarImporte()

    def completar_formulario_no_inmediata(self):
        """
        Metodo para ingresar a la pantalla de transferencia.
        Se selecciona el radiobutton de Transferencias no inmediatas y se
        rellena el correspondiente formulario
        """
        self.seleccionarMenuTransferencias()
        self.seleccionar_a_otros_bancos()
        self.seleccionarCuentaDebito()
        self.seleccionarTransNoIndemdiata()
        self.seleccionarMedioCuentaDestino()
        self.ingresarCuentaDestino()
        self.completarCaractCuentaAcreditacion()
        self.seleccionarConcepto()
        self.completarImporte()

    def finalizar_formulario(self):
        """
        Metodo para finalizar la transferencia.
        Se completa las coordenadas y se comprueba que se muestre la tabla
        correspondiente
        """
        self.seleccionarContinuar()
        self.completarCoordenadas()
        self.seleccionarContinuar()
        self.comprobar_tabla_cuenta()

    def seleccionarCuentaDebito(self, find_text='0000067'):
        accion = "Seleccionar Cuenta Debito"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.ctaDebito
            self.selectListByPartialText(xpath, find_text)
            self.capture_image(msgOk)

    def seleccionarTransNoIndemdiata(self):
        to = 10
        accion = "Seleccionar transferencia no inmediata"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.TransfNoInmediata
            self.selectElement(xpath, accion, to)
            self.capture_image(msgOk)

    def ingresarCuentaDestino(self):
        """ Metodo para ingresar cbu o alias en el input correspondiente"""
        to = 10
        accion = "Ingresar Cuenta Destino"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.inputCbuAlias
            self.write(xpath, self.CBU, to)
            self.capture_image(msgOk)

    def seleccionarMedioCuentaDestino(self, opcion='CBU'):
        """Metodo para seleccionar en la opcion de CBU o alias"""
        accion = "Seleccionar cuenta destino"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.cbuAliasDestino
            self.selectListByPartialText(xpath, opcion)
            self.capture_image(msgOk)

    def completarCaractCuentaAcreditacion(self, caracteristica='Otra cuenta propia'):
        to = 10
        accion = "Seleccionar Caracteristica Cuenta Acreditacion: {}".format(caracteristica)
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.caractCtaAcreditacion
            if self.visibility_element(xpath, to):
                self.select_by_text(xpath, caracteristica)
                self.capture_image(msgOk)
            else:
                xpath1 = locTransferenciasOtroBanco.caractCtaAcreditacion_uno
                self.select_by_text(xpath1, caracteristica)
                self.capture_image(msgOk)

    def seleccionarConcepto(self):
        accion = "Seleccionar Concepto: {}".format(self.concepto)
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.concepto
            self.select_by_text(xpath, self.concepto)
            self.capture_image(msgOk)

    def completarConcepto(self):
        accion = "Completar Concepto"
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.concepto
            self.select_by_index(xpath, 1)

    def completarImporte(self):
        to = 10
        accion = "Completar Importe"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.importe
            self.go_to_xpath(xpath)
            self.write(xpath, self.importe, to)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        to = 10
        accion = "Seleccionar Continuar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath_select = locTransferenciasOtroBanco.continuar
            self.selectElement(xpath_select, msgOk, msgFail, to)

    def ingresarNumeroCBU(self):
        to = 10
        accion = "Ingresar CBU"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.cbu_no_inmediata
            self.write(xpath, self.CBU, to)
            self.capture_image(msgOk)

    def completarCuil(self):
        to = 10
        accion = "Ingresar CUIL"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.cuil_no_inmediata
            self.write(xpath, self.cuil, to)
            self.capture_image(msgOk)

    def completarConceptoNoInmediato(self):
        accion = (
            "Seleccionar concepto: {}".format(self.concepto)
        )
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.concepto_no_inmediata
            self.select_by_text(xpath, self.concepto)
            self.capture_image(msgOk)

    def completarImporteNoInmediato(self):
        to = 10
        accion = "Completar Importe"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.importe_no_inmediata
            self.go_to_xpath(xpath)
            self.write(xpath, self.importe, to)
            self.capture_image(msgOk)

    def seleccionarContinuarNoInmediato(self):
        to = 10
        accion = "Seleccionar Continuar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath_select = locTransferenciasOtroBanco.continuar_no_inmediata
            self.selectElement(xpath_select, msgOk, msgFail, to)

    def seleccionarConfirmar(self):
        to = 10
        accion = "Seleccionar Continuar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath_select = locTransferenciasOtroBanco.confirmar
            xpath_verif = None
            self.retrySelection(xpath_select, xpath_verif, accion,
                                msgOk, msgFail, to)

    def seleccionar_check_concepto(self):
        to = 10
        accion = 'Seleccionar checkbox del concepto'
        msgFail = 'No se pudo {}'.format(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.checkConcepto
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, accion, msgFail, to)
                self.capture_image(accion)
            else:
                self.fail_msg(msgFail)

    # Verificacion de pantalla
    def verificarPantallaConfirmacion(self):
        """
        Metodo para verificar la pantalla de confirmacion de la
        transferencia. Se busca los eleementos y se los remarca en rojo
        """
        self.verificarTipoTransferencia()
        self.verificarCuentaDebito()
        self.verificarCbuAcreditacion()
        self.verificarCaracteristica()
        self.verificarTitular()
        self.verificarCuil()
        self.verificarConcepto()
        self.verificarImporte()

    # Verificacion de los campos
    def verificarTipoMoneda(self, moneda):
        accion = 'Verificar el tipo moneda'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.moneda
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                texto = self.get_element_text(xpath)
            else:
                self.fail_msg('No se muestra el elemento')
            if texto == moneda:
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)

    def comprobar_tabla_cuenta(self):
        to = 20
        accion = 'Comprobar que se vuelve a la home'
        msgFail = 'No se pudo {}'.format(accion)
        with self.step(accion):
            xpath_comprobar = locTransferenciasOtroBanco.tabla_Cuentas
            if self.visibility_element(xpath_comprobar, to):
                self.capture_image(accion)
            else:
                self.fail_msg(msgFail)

    def verificarTextoError(self, textoEsperado=None):
        accion = 'Verificar el campo del error'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.div_error
            if self.visibility_element(xpath, to):
                if textoEsperado is None:
                    self.capture_image(msgOk)
                else:
                    texto = self.get_element_text(xpath)
                    if textoEsperado in texto:
                        self.capture_image(msgOk)
                    else:
                        self.fail_msg('El texto esperado es diferente')
            else:
                self.fail_msg(msgFail)

    def verificarTipoTransferencia(self):
        accion = 'Verificar el campo tipo de transferencia'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_tipoTransferencia
            self.checkElement(xpath, accion)

    def verificarCuentaDebito(self):
        accion = u'Verificar el campo cuenta débito'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_cuentaDebito
            self.checkElement(xpath, accion)

    def verificarCbuAcreditacion(self):
        accion = u'Verificar el campo CBU de acreditación'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_cbuAcred
            self.checkElement(xpath, accion)

    def verificarCaracteristica(self):
        accion = u'Verificar el campo característica'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_caracteristica
            self.checkElement(xpath, accion)

    def verificarTitular(self):
        accion = 'Verificar el campo titular'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_titular
            self.checkElement(xpath, accion)

    def verificarCuil(self):
        accion = 'Verificar el campo CUIL'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_cuil
            self.checkElement(xpath, accion)

    def verificarConcepto(self):
        accion = 'Verificar Concepto'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_concepto
            self.checkElement(xpath, accion)

    def verificarImporte(self):
        accion = 'Verificar el campo importe'
        with self.step(accion):
            xpath = locTransferenciasOtroBanco.txt_importe
            self.checkElement(xpath, accion)
