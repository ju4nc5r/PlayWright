# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.loc.locPagoTC import locPagoTC
from SeleniumFramework.src.proyectos.HBPF.pageLoc.Inicio import Inicio
from SeleniumFramework.common_functions import get_msg
import pytest
#from py._code._assertionold import getmsg


class stPagosTC(stLogin, menu):
    def pagoTC(self, tarjeta, importe):
        self.seleccionarPagoTC()
        self.seleccionarTarjeta(tarjeta)
        self.verificarCartelDebitoAutomatico()

    def seleccionarAnularPago(self):
        accion = 'Seleccionar Anulacion de Pago TC'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.anularPagoTC
            self.selectElement(xpath, msgOk, msgFail, 2)
            self.selectListByPartialText(xpath, "MasterCard")
            self.capture_image(accion)

    def controlPagoTC(self, tarjeta, cuenta, importe):
        accion = "Verificar cambio pagos procesados hasta la fecha"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.seleccionarPagoTC()
            self.seleccionarTarjeta(tarjeta)
            self.verificarCartelDebitoAutomatico()
            self.seleccionarCuentaDebito(cuenta)
            xpath = locPagoTC.txt_pesosHastaFecha
            verificar = self.get_element_text(xpath)
            self.completarOtroImporte(importe)
            self.seleccionarContinuar_PagoTc()
            self.seleccionarConfirmar()
            self.seleccionarNuevoPago()
            self.seleccionarTarjeta(tarjeta)
            self.verificarCartelDebitoAutomatico()
            self.seleccionarCuentaDebito(cuenta)
            if (self.get_element_text(xpath) == verificar):
                self.fail_msg(msgFail)
            else:
                self.capture_image(msgOk)

    def seleccionarTarjeta(self, tarjeta):
        accion = 'Seleccionar Tarjeta'
        with self.step(accion):
            xpath = locPagoTC.tarjeta
            self.selectListByPartialText(xpath, tarjeta)
            self.capture_image(accion)

            
    def seleccionarSaldoPesos(self):
        accion = 'Seleccionar Saldo en pesos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.saldopesos
            self.selectElement(xpath, msgOk, msgFail)
            self.capture_image(accion)
    
    def seleccionarSaldoDolares(self, tarjeta):
        accion = 'Seleccionar Saldo en dolares'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.saldodolares
            self.selectElement(xpath, msgOk, msgFail)
            self.capture_image(accion) 

    def seleccionarCuentaDebito(self, cuenta):
        to=5
        accion = 'Seleccionar Cuenta Debito'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cuentaDebito
            self.selectElement(xpath, msgOk, msgFail, to)
            self.selectListByPartialText(xpath, cuenta)
            self.capture_image(accion)

    def seleccionarPagoMinimo(self):
        to = 10
        accion = 'Seleccionar Pago Minimo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.opt_ImporteMinimo
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(accion)
            else:
                self.fail_msg(msgFail)

    def seleccionarOtroImporte(self):
        to = 10
        accion = 'Seleccionar Otro Importe'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.opt_OtroImporte
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def completarOtroImporte(self, importe):
        to = 10
        accion = 'Completar Otro Importe'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.input_OtroImporte
            self.write(xpath, importe, to)
            self.capture_image(msgOk)

    def seleccionarImporteTotalDolar(self):
        to = 10
        accion = 'Seleccionar Importe Total'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.opt_importeTotalDolar
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(accion)
    
    def seleccionarContinuar(self):
        to = 10
        accion = 'Seleccionar continuar para concretar la operacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cmdContinuar
            self.selectElement(xpath, msgOk, msgFail, to)
            verificar_xpath = Inicio.lbl_Titulo_Cuentas_xp
            if self.verifySelection(verificar_xpath, accion, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuar_PagoTc(self, msjEsperado=None):
        to = 10
        accion = u'Continuar con el pago'
#         accion = 'Completar Otro Importe'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cmdContinuar
            self.selectElement(xpath, msgOk, msgFail, to)
            if msjEsperado is not None:
                xpath = locPagoTC.errorPanel
                texto = self.get_element_text(xpath)
                if msjEsperado in texto:
                    self.capture_image('Se muestra el mensaje de error')
                else:
                    self.fail_msg('El mensaje mostrado, es otro')
            else:
                self.verificarCartelSaldoMayor()
                #verificar_xpath = locPagoTC.cmdConfirmar
                #self.verifySelection(verificar_xpath, accion, to)

    def seleccionarConfirmar(self, msjEsperado=None):
        to = 10
        accion = u'Seleccionar botón confirmar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cmdConfirmar
            self.selectElement(xpath, msgOk, msgFail, to)
#             xpath1 = locPagoTC.img_ticket
#             xpath2 = locPagoTC.diverrorCollection
#             if self.double_visibility_element(xpath1, xpath2, to):
#                 if msjEsperado is None:
#                     self.capture_image(msgOk)
#                 else:
#                     self.fail_msg('No se esta mostrando el mensaje de error')
#             else:
#                 if msjEsperado is None:
#                     self.fail_msg(msgFail)
#                 else:
#                     text = self.get_element_text(xpath2)
#                     msg = 'Se muestra mensaje de error'
#                     if msjEsperado in text:
#                         self.capture_image(msg)
#                     else:
#                         self.fail_msg(msg)

    def seleccionarNuevoPago(self):
        to = 10
        accion = 'Seleccionar nuevo pago'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cmdNuevoPago
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail, to)
            if self.visibility_element(locPagoTC.tarjeta):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuarAlInicio(self):
        to = 10
        accion = 'Seleccionar continuar para volver al inicio'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cmdInicio
            self.selectElement(xpath, msgOk, msgFail, to)
            verificar_xpath = Inicio.lbl_Titulo_Cuentas_xp
            if self.verifySelection(verificar_xpath, accion, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def getCuentas(self):
        # Metodo para obtener los cuentas que posse el usuario
        xpath = locPagoTC.cuentaDebito
        cuentas = self.obtain_select(xpath).options
        cuentas = [i.text for i in cuentas]
        return cuentas

    # Verificacion de pantalla
    def verificarPantallaResultado(self):
        if self.verificarExitoSinTkt():
            self.finalizo=False                    
        else:
            self.verificarTicket()
            self.verificarEnviarMail()
            self.verificarNuevoPago()
            self.verificarcmdDescargar()


    # Verificacion de elementos
    def verificarExitoSinTkt(self):
        accion = u'Verificar mensaje Exito sin Ticket'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.visibility_element(locPagoTC.msg_exitoSinTkt):
                self.capture_image(msgOk)
                pytest.fail(u"Mensaje la operación finalizó con exito pero no se pudo generar el ticket")
               
              

    # Verificacion de elementos
    def verificarTicket(self):
        accion = u'Verificar imagen del ticket de resultado'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.visibility_element(locPagoTC.img_ticket):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarcmdDescargar(self):
        accion = u'Verificar botón descargar'
        with self.step(accion):
            xpath = locPagoTC.cmdDescargar
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion)

    def verificarEnviarMail(self):
        accion = u'Verificar checkbox de enviar por mail'
        with self.step(accion):
            xpath = locPagoTC.checkbox_mail
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion)

    def verificarNuevoPago(self):
        accion = u'Verificar nuevo Pago'
        with self.step(accion):
            xpath = locPagoTC.cmdNuevoPago
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion)

    def verificarFaltaTC(self):
        to = 10
        accion = 'Verificar la falta de Tarjeta de Credito'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            verificar_xpath = locPagoTC.tblSinTC
            self.checkElement(verificar_xpath, accion)
            xpath = locPagoTC.button_cerrar
            self.selectElement(xpath, msgOk, msgFail, to)

    def verificarImportesTotales(self, cuentaDeb):
        accion = u'Verificar radiobutton de importe totales'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            if "CA $" in cuentaDeb:
                xpath = locPagoTC.opt_importeTotalPesos
            elif "CA U$S" in cuentaDeb:
                xpath = locPagoTC.opt_importeTotalDolar
            else:
                self.fail_msg(u'La cuenta ingresada no es válida')
            if self.is_enabled(xpath):
                self.capture_image(msgOk)
            else:
                self.fail_msg('El radiobutton, esta deshabilitado')

    def verificarCartelDebitoAutomatico(self):
        accion = u'Verificar si la tarjeta tiene debito automatico'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath1 = locPagoTC.tblAutoDebActivo
            xpath2 = locPagoTC.cuentaDebito
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
                self.cerrarCartelDebitoAutomatico()
            else:
                pass

    def cerrarCartelDebitoAutomatico(self):
        accion = u'Cerrar el cartel de la tarjeta con debito automatico'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cerrarTbl
            if not self.selectElement(xpath, msgOk, msgFail):
                self.fail_msg(msgFail)
                
    def verificarCartelSaldoMayor(self):
        accion = u'Verificar si aparece el cartel de que el saldo a pagar es mayor al total'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath1 = locPagoTC.tblSaldoMayor
            xpath2 = locPagoTC.cuentaDebito
            if self.visibility_element(xpath1, to):
                self.capture_image(msgOk)
                self.cerrarCartelSaldoMayor()
            else:
                pass

    def cerrarCartelSaldoMayor(self):
        accion = u'Cerrar el cartel que informa que el saldo a pagar es mayor al saldo total'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.cerrarTblSaldoMayor
            if not self.selectElement(xpath, msgOk, msgFail):
                self.fail_msg(msgFail)
    
    def seleccionarContinuar(self):
        to = 10
        accion = 'Seleccionar continuar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locPagoTC.btn_continuar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)