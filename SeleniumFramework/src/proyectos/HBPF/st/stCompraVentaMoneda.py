# -*- coding: utf-8 -*-
import time
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.loc.locCompraVenta import locCompraVenta as CV
from SeleniumFramework.common_functions import get_msg


class stCompraVentaMoneda(stLogin, menu):

    def CompraVentaMoneda(self):
        """
        Metodo para ingresar a la pagina de compra y venta de monedas.
        Realizando los pasos necesarios para finalizar la compra de las
        monedas
        """
        self.seleccionarMenuProductos()
        self.seleccionarCompraVenta()
        self.seleccionarCtaDebito()
        self.seleccionarCtaAcreditacion()
        self.completarImporte()
        # N/A la seleccion de moneda esta en pesos por default
        # self.seleccionarMoneda()
        if (self.tipoCuentaDebito == "CA $" and
            self.tipoCuentaAcredita == 'CA U$S'):
            self.seleccionarCheckboxAceptar()
        self.seleccionarContinuar_compra_venta()
        self.verificarConfirmacion()
        self.seleccionarConfirmar()
        self.verificarResultado()

    def seleccionarCtaDebito(self):
        accion = 'Seleccionar Cta. Debito'
        with self.step(accion):
            xpath = CV.ctaDebito
            self.selectListByPartialText(xpath, self.tipoCuentaDebito)
            
    def seleccionarCtaComitente(self):
        accion = u'Seleccionar Cta. Comitente'
        msgOk = u'Se pudo {}'.format(accion.lower())
        msgFail = u'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = CV.ctaComitente
            cuenta = 'MAX'
            #self.selectElement(xpath, msgOk, msgFail)
            self.selectListByPartialText(xpath, cuenta)

    def seleccionarCtaAcreditacion(self):
        accion = 'Seleccionar Cta. Acreditacion'
        msgOk = accion
        with self.step(accion):
            xpath = CV.ctaAcreditacion
            self.capture_image(accion)
            self.selectListByPartialText(xpath, self.tipoCuentaAcredita)
            time.sleep(2)  # Tiempo de espera para que responda la aplicacion
            self.capture_image(msgOk)

    def completarImporte(self, importe=10000):
        to = 10
        accion = 'Completar Importe'
        with self.step(accion):
            xpath = CV.importe
            self.write(xpath, importe, to)
            
    def completarMonto(self, monto=10000):
        to = 10
        accion = 'Completar Monto'
        with self.step(accion):
            xpath = CV.monto
            self.write(xpath, monto, to)

    def seleccionarMoneda(self, text):
        # to = 10
        accion = 'Seleccionar Moneda'
        # msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = CV.tipoMoneda
            self.select_by_text(xpath, text)
            self.capture_image(
                'Se selecciona el tipo de moneda: {}'.format(text)
            )

    def seleccionarCheckboxAceptar(self):
        accion = 'Seleccionar checkbox de acpeto'
        with self.step(accion):
            xpath = CV.input_acepto
            self.selectElement(xpath, '', '')
            self.capture_image(accion)

    def seleccionarContinuar_compra_venta(self, falla=False):
        to = 10
        accion = 'Seleccionar Continuar'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = CV.cmdContinuar
            self.capture_image(accion)
            self.selectElement(xpath, msgOk, msgFail, to)
            # Se tiene que verificar que se muestra el
            # elemento esperado o error
            xpath1 = CV.cmdConfirmar
            xpath2 = CV.msj_error
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image('Se pudo {}'.format(accion.lower()))
            else:
                # Si se muestra el msj de error y es un elemento esperado
                if falla:
                    if self.compareText(xpath2, self.mensaje_esperado):
                        self.capture_image('Se muestra el mensaje deseado')
                    else:
                        self.fail_msg('No se esta mostrando el mensaje deseado')
                else:
                    self.fail_msg(u'Se está mostrando el mensaje de error')

    def verificarConfirmacion(self):
        to = 10
        accion = 'Verificar Confirmacion'
        # msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            verificar_xpath = CV.cmdConfirmar
            self.verifySelection(verificar_xpath, accion, to)

    def seleccionarConfirmar(self):
        to = 10
        accion = 'Seleccionar Confirmar'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = CV.cmdConfirmar
            verificar_xpath = CV.spanResultado
            if self.selectElement(xpath, msgOk, msgFail, to):
                if self.visibility_element(verificar_xpath, to):
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def verificarResultado(self):
        """Metodo para verificar que se esta mostrando la imagen del ticket"""
        to = 10
        accion = u'Validar Ticket'
#         accion = 'Verificar Resultado'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = CV.image_ticket
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
#                 self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
            self.go_to_xpath(CV.cmdContinuar_a_Ctas)

    def seleccionarLimiteDiario(self):
        to = 10
        accion = 'Seleccionar limite diario'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = CV.boton_limite_diarios
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(CV.boton_cerrar, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCerrar(self):
        """Metodo para seleccionar el boton cerrar"""
        to = 10
        accion = u'Seleccionar botón cerrar'
        msgOk = u'Se pudo {}'.format(accion.lower())
        msgFail = u'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = CV.boton_cerrar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarBtnDescargar(self):
        """Metodo para verificar que se muestra el boton de descarga"""
        accion = "Verificar que se muestra el boton de descarga"
        msgOk = u'Se pudo {}'.format(accion.lower())
        to = 10
        xpath = CV.btn_descarga
        if self.visibility_element(xpath, to):
            self.highlight(xpath, msgOk)
            self.go_to_xpath(xpath)
            return True
        
        self.fail_msg(u'No se está mostrando el boton de descarga')
        return False

    def seleccionarDescargar(self):
        """Metodo para seleccionar el boton descargar"""
        to = 10
        accion = u'Seleccionar botón descargar'
        msgOk = u'Se pudo {}'.format(accion.lower())
        msgFail = u'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = CV.btn_descarga
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    

    def verificarNuevaTransferencia(self):
        """
        Metodo para verificar que se muestra el boton de nueva
        transferencia
        """
        to = 10
        xpath = CV.boton_nueva_transf
        if self.visibility_element(xpath, to):
            self.go_to_xpath(xpath)
            return True
        self.fail_msg(u'No se está mostrando el boton de nueva transferencia')
        return False

    def seleccionarContinuar(self):
        """
        Metodo para seleccionar el boton continuar en la pagina de resultado
        """
        to = 10
        accion = 'Seleccionar el boton continuar'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = CV.cmdContinuar
            self.go_to_xpath(xpath)
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(CV.titulo_esperado, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarBotonCancelar(self):
        """
        Metodo para verificar que se este mostrando el boton para cancelar
        """
        to = 10
        xpath = CV.btn_cancelar
        if self.visibility_element(xpath, to):
            self.go_to_xpath(xpath)
            return True
        self.fail_msg(u'No se está mostrando el botón para cancelar')
        return False

    def verificarBotonModificar(self):
        """
        Metodo para verificar que se este mostrando el boton para modificar
        """
        to = 10
        xpath = CV.btn_modificar
        if self.visibility_element(xpath, to):
            self.go_to_xpath(xpath)
            return True
        self.fail_msg(u'No se está mostrando el botón para modificar')
        return False

    def verificarCheckEnviarMail(self):
        """Metodo para chequear que se muestre el check para enviar el mail"""
        to = 10
        xpath = CV.inp_enviarMail
        if self.visibility_element(xpath, to):
            self.go_to_xpath(xpath)
            return True
        self.fail_msg(u'No se está mostrando el checkbox')
        return False

    def verificarUnicaVez(self):
        """
        Metodo para chequear que se muestra la tabla de transferencia
        programada
        """
        to = 10
        xpath = CV.tbl_fecha_prog
        if self.visibility_element(xpath, to):
            self.go_to_xpath(xpath)
            return True
        self.fail_msg(u'No se está mostrando la fecha programada')
        return False

    def verificarSemanal(self):
        """
        Metodo para verificar la pantalla de confirmacion con los campos de
        la transferencia programada semanalmente
        """
        to = 10
        if self.visibility_element(CV.tbl_primeraEjecucion, to):
            if self.visibility_element(CV.tbl_diasSemanales, to):
                if self.visibility_element(CV.tbl_repeticiones, to):
                    self.capture_image('Se muestran los campos deseados')
                    return True
        self.fail_msg(u'No se está mostrando los elementos deseados')
        return False

    def verificarMensual(self):
        """
        Metodo para verificar la pantalla de confirmacion con los campos de
        la transferencia programada mensualmente
        """
        to = 10
        if self.visibility_element(CV.tbl_primeraEjecucion, to):
            if self.visibility_element(CV.tbl_repeticiones, to):
                self.capture_image('Se muestran los campos deseados')
                return True
        self.fail_msg(u'No se está mostrando los elementos deseados')
        return False

    def verificarPantallaConfirmacion(self, prog=None):
        """
        Metodo para verificar que se muestran los elementos esperados en la
        pantalla de confirmacion.
        :param prog: String. String del tipo de periodo
        """
        accion = 'Se verifican los elementos'
        with self.step(accion):
            self.verificarBotonCancelar()
            self.verificarBotonModificar()
            if prog == u'Por única vez':
                self.verificarUnicaVez()
            elif prog == u'Semanalmente':
                self.verificarSemanal()
            elif prog == u'Mensualmente':
                self.verificarMensual()
            else:
                pass
            self.capture_image('Se muestran los elementos de la pantalla')

    def verificarPantallaResultados(self):
        """
        Metodo para verificar los elementos de la etapa resultados de la
        compra/venta de monedas
        """
        accion = 'Mostrar elementos de etapa resultado'
        with self.step(accion):
            self.verificarNuevaTransferencia()
            self.verificarBtnDescargar()
            self.verificarCheckEnviarMail()
            self.capture_image(accion)

    def seleccionarProgramar(self):
        """
        Metodo para seleccionar el checkbox para programar la compra/venta
        """
        accion = 'Seleccionar checkbox de programar transferencia'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            xpath = CV.inp_programar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCriterioProgramacion(self, opcion):
        """Metodo para seleccionar la periodicidad de la transferencia"""
        accion = 'Seleccionar la periodicidad deseada'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            xpath = CV.sel_programar
            if self.visibility_element(xpath, to):
                self.select_by_text(xpath, opcion)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarFechaProgramada(self, fecha):
        """Metodo para ingresar la fecha programada"""
        accion = 'Ingresar fecha programada'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            xpath = CV.inp_fechaProgramada
            if self.visibility_element(xpath, to):
                self.write(xpath, fecha, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def transferenciaUnica(self, periodo, fecha):
        """Metodo para programar la transferencia por unica vez"""
        self.seleccionarProgramar()
        self.seleccionarCriterioProgramacion(periodo)
        self.ingresarFechaProgramada(fecha)
        self.wait(1)

    def transferenciaSemanalMensual(self, periodo, fecha, repeticiones):
        """Metodo para programar la transferencia semanalmente"""
        self.seleccionarProgramar()
        self.seleccionarCriterioProgramacion(periodo)
        self.ingresarPrimeraEjecucion(fecha)
        self.seleccionarRepeticiones(repeticiones)

    def ingresarPrimeraEjecucion(self, fecha):
        """Metodo para ingresar la fehca de la primera ejecucion"""
        accion = 'Ingresar la fecha de la primera ejecucion'
        msgOk = 'Se pudo {}'.format(accion.lower())
        to = 10
        with self.step(accion):
            xpath = CV.inp_primeraFecha
            self.write(xpath, fecha, to)
            self.capture_image(msgOk)

    def seleccionarRepeticiones(self, repe):
        """Metodo para seleccionar la cantidad de repeticiones"""
        accion = 'Seleccionar la cantidad de ejecuciones'
        msgOk = 'Se pudo {}'.format(accion.lower())
        with self.step(accion):
            xpath = CV.sel_cantRepe
            self.select_by_value(xpath, str(repe))
            self.capture_image(msgOk)

    def aceptarDeclaracionJurada(self):
        """
        Metodo para seleccionar el checkbox para aceptar la declaracion jurada
        """
        accion = 'Seleccionar checkbox para aceptar la declaracion jurada'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            xpath = CV.btn_declaracion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def mostrarTipoMonedas(self):
        to = 10
        accion = 'mostrar Monedas'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = CV.tipoMoneda
            if self.visibility_element(xpath, to):
                self.selectElement(xpath,msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTipoMoneda(self, moneda):
        to = 10
        accion = 'mostrar Monedas'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = CV.slc_tipoMoneda.format(moneda)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

            