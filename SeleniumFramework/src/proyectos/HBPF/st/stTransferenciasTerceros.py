# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu, Transferencia
from SeleniumFramework.src.proyectos.HBPF.loc.locTransferenciaTerceros import locTransferenciasTerceros
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.common_functions import get_msg


class stTransferenciaTerceros(stLogin, menu, Transferencia):

    def TransferenciaTerceros(self):
        self.completarFormulario()
        self.finalizar_transferencia()

    def TransferenciaTerceroConCheck(self):
        self.completarFormulario()
        self.seleccionar_check_concepto()
        self.finalizar_transferencia()

    def completarFormulario(self):
        # self.seleccionarMenuTransferencias()
        self.seleccionar_cliente_itau()
        self.seleccionarCuentaDebito()
        self.ingresarCuentaDestino()
        self.seleccionarConcepto()
        self.seleccionarImporte()

    def finalizar_transferencia(self):
        self.continuar()
        self.completarCoordenadas()
        self.finalizarTransferencia()
        self.comprobar_tabla_cuenta()

    def seleccionarCuentaDebito(self, index=1):
        accion = "Seleccionar Cuenta Debito"
        with self.step(accion):
            xpath = locTransferenciasTerceros.ctaDebito
            self.select_by_index(xpath, index)
            self.wait(1)
            self.capture_image(accion)
    
    def seleccionarCuentaCorriente(self):
        to = 10
        accion = 'Seleccionar cuenta corriente'
        msgOk = accion
        msgFail = 'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.ctaDebito
            xpath_cuenta = locTransferenciasTerceros.opt_cta.format(self.cuentaDeb)
            self.selectElement(xpath, msgOk, msgFail, to)
            self.selectElement(xpath_cuenta, msgOk, msgFail, to)
            self.capture_image(accion)

    def ingresarCuentaDestino(self):
        to = 10
        accion = 'Seleccionar cuenta acreditacion'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.botonAgenda
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.listaCuentaDestino
            self.visibility_element(xpath, to)
            xpath = locTransferenciasTerceros.opcion1CuentaDestino
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.botonContinuar
            self.selectElement(xpath, msgOk, msgFail, to)
            self.wait(2)
            self.capture_image(accion)

    def ingresarCuentaDestinoCases(self, cuenta):
        """
        Metodo para ingresar la cuenta destino en el campo de cuenta
        acreditacion
        """
        to = 10
        accion = 'Ingresar cuenta acreditacion'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasTerceros.ctaAcreditacion
            self.write(xpath, cuenta, to)
            self.capture_image(msgOk)

    def verAgenda(self):
        to = 10
        accion = 'Ver agenda destinatarios'
        msgOk, msgFail = get_msg(accion)
        # msgFail = 'No se pudo '+ msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.botonAgenda
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(msgOk)

    def seleccionarDestinatario(self, destinatario):
        to = 10
        accion = 'Seleccionar destinatario'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasTerceros.optionCuentaVarible.format(destinatario)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, destinatario)
                # radioButtonCuenta
                xpath_final = xpath + locTransferenciasTerceros.radioButtonCuenta
                self.selectElement(xpath_final, msgOk, '', to)
                xpath = locTransferenciasTerceros.botonContinuar
                self.selectElement(xpath, msgOk, '', to)
                self.capture_image(msgOk)

    def seleccionarConcepto(self):
        to = 10
        accion = u'Seleccionar concepto'
        msgOk = accion
        msgFail = u'No se pudo %s'%msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.concepto
            xpath_concepto = locTransferenciasTerceros.opt_concepto.format(self.concepto)
            xpath_concepto2 = locTransferenciasTerceros.opt_concepto2        
            if self._testMethodName == "test_HB_T122" or self._testMethodName == "test_HB_T135":
                xpath_concepto = xpath_concepto2
            self.verifySelection(xpath_concepto, accion, to)
#             self.selectElement(xpath, msgOk, msgFail, to)
            self.selectElement(xpath_concepto, msgOk, msgFail, to)
            self.capture_image(accion)

    def seleccionarImporte(self):
        to = 10
        accion = 'Ingresar importe'
        # msgOk= accion
        # msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            self.write(locTransferenciasTerceros.importe, self.importe, to)
            self.select_by_index(locTransferenciasTerceros.moneda, 0)
            self.capture_image(accion)

    def enviarAvisoDestinatario(self, email, comentario):
        to = 10
        accion = 'Ingresar importe'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.checkEnviarAviso
            self.selectElement(xpath, msgOk, msgFail, to)
            self.write(locTransferenciasTerceros.email, email, to)
            self.write(locTransferenciasTerceros.comentario, comentario, to)
            self.capture_image(accion)

    def programarTransferencia(self, periodicidad, fecha, opcion=None):
        to = 10
        accion = 'Programar transferencia'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.programar
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.periodicidad
            self.select_by_index(xpath, periodicidad)
            self.wait(5)
            xpath = locTransferenciasTerceros.dia_programado
            self.go_to_xpath(xpath)
            self.write(xpath, fecha, to)
            if (opcion is not None and (periodicidad == 2 or
                                        periodicidad == 3)):
                xpath = locTransferenciasTerceros.repeticiones
                self.select_by_index(xpath, opcion)
            self.capture_image(accion)
    
    def programarTransferenciaSinFecha(self, periodicidad, opcion=None):
        to = 10
        accion = 'Programar transferencia'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.programar
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.periodicidad
            self.select_by_index(xpath, periodicidad)
            self.wait(5)
            if (opcion is not None and (periodicidad == 2 or
                                        periodicidad == 3)):
                xpath = locTransferenciasTerceros.repeticiones
                self.select_by_index(xpath, opcion)
            self.capture_image(accion)

    def seleccionarProgramarTransferencia(self):
        to = 10
        accion = 'Programar transferencia'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.programar
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(msgOk)

    def seleccionarDeclaracionJurada(self):
        to = 10
        accion = 'Aceptar declaracion jurada'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.declaracion
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(msgOk)
            

    def seleccionarDiaAnterior(self,diaAnterior):
        to = 10
        accion = "Seleccionar dia anterior"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = locTransferenciasTerceros.input_fecha
            self.write(xpath, diaAnterior, to)
            self.capture_image(msgOk)

    def continuar(self):
        to = 10
        accion = 'Continuar transferencia'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.continuar
            self.go_to_xpath(xpath)
            self.verifySelection(xpath, accion, to)
            self.selectElement(xpath, msgOk, msgFail, to)

    def cancelar(self):
        to = 10
        accion = 'Cancelar transferencia'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.cancelar
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarLimitesDiarios(self):
        to = 10
        accion = 'Visualizar limites diarios'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.limitesDiarios
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.titulo_tipo_cambio
            self.verifySelection(xpath, accion, to)
            xpath = locTransferenciasTerceros.cerrar
            self.selectElement(xpath, msgOk, msgFail, to)
            self.wait(2)
            self.capture_image(accion)

    def seleccionarCotizacion(self):
        to = 10
        accion = 'Vizualizar cotizaciones'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.cotizaciones
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.titulo_tipo_cambio
            self.verifySelection(xpath, accion, to)
            xpath = locTransferenciasTerceros.cerrar
            self.selectElement(xpath, msgOk, msgFail, to)
            self.wait(2)
            self.capture_image(accion)

# ######################### Tercera pagina ###########################
    def finalizarTransferencia(self):
        to = 20
        msgOk = u"Seleccionar boton confirmar"
        msgFail = 'No se pudo %s' % msgOk
        xpath = locTransferenciasTerceros.boton_confirmar
        self.selectElement(xpath, msgOk, msgFail, to)
        
        accion = u'Validar ticket'
#         accion = 'Se finaliza la transferencia' 
        xpath = locTransferenciasTerceros.comprobante
        self.verifySelection(xpath, accion, to)        
        self.continuar()

    def nueva_transferencia(self):
        to = 10
        accion = 'Nueva transferencia'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.boton_nueva_transferencia
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.Titulo
            self.verifySelection(xpath, accion, to)
            self.capture_image(accion)

    def seleccionarDescargar(self):
        to = 10
        accion = 'Descargar comprobante'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.boton_descargar
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionar_enviar_mail(self, mail, comentario=None):
        to = 10
        accion = 'Enviar mail'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.enviar_mail
            self.go_to_xpath(xpath)
            self.verifySelection(xpath, accion, to)
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.input_enviar_mail
            self.write(xpath, mail, to)
            xpath = locTransferenciasTerceros.input_comentario
            self.write(xpath, comentario, to)
            self.capture_image(accion)

    def seleccionar_enviar_aviso(self, mail, comentario=None):
        to = 10
        accion = 'Enviar mail'
        msgOk = accion
        msgFail = 'No se pudo %s' % msgOk
        with self.step(accion):
            xpath = locTransferenciasTerceros.enviar_aviso
            self.go_to_xpath(xpath)
            self.verifySelection(xpath, accion, to)
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = locTransferenciasTerceros.input_aviso_email
            self.write(xpath, mail, to)
            xpath = locTransferenciasTerceros.input_aviso_comentario
            self.write(xpath, comentario, to)
            self.capture_image(accion)

    def seleccionar_check_concepto(self):
        to = 10
        accion = 'Seleccionar checkbox del concepto'
        msgFail = 'No se pudo {}'.format(accion)
        with self.step(accion):
            xpath = locTransferenciasTerceros.checkConcepto
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, accion, msgFail, to)
                self.capture_image(accion)
            else:
                self.fail_msg(msgFail)

    def comprobar_tabla_cuenta(self):
        to = 20
        accion = 'Comprobar que se vuelve a la home'
        msgFail = 'No se pudo {}'.format(accion)
        with self.step(accion):
            xpath_comprobar = locTransferenciasTerceros.tabla_Cuentas
            if self.visibility_element(xpath_comprobar, to):
                self.capture_image(accion)
            else:
                self.fail_msg(msgFail)

    def validarErrorCuenta(self):
        accion = 'Cuenta de acreditacion incorrecta'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasTerceros.validacion_error_cuenta
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    def validarErrorEmail(self):
        accion = 'Email invalido'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasTerceros.validacion_email
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    def validarCompletarFecha(self,mensaje= None):
        to = 10
        accion = "Mostrar error:" + mensaje
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasTerceros.validacion_error_dia
            if mensaje is not None:
                texto = self.get_element_text(xpath)
                if mensaje in texto:
                    self.capture_image(msgOk)
                else:
                    self.fail_msg('El mensaje no es el esperado')
            else:
                self.fail_msg('Se muestra mensaje de error')
    
    def validarFechaMayorA(self,mensaje= None):
        accion = "Mostrar error:" + mensaje
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasTerceros.validacion_fecha_mayor
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')