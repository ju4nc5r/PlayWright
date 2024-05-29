# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plRescate import plRescate as RES
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stRescate(menu):
    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(RES.select_cuentaComitente, cuenta)
            self.capture_image(msgOk)

    def seleccionarFondo(self, fondo):
        accion = u'Seleccionar fondo a rescatar'
        with self.step(accion):
            xpath = RES.opcion_fondoSeleccionable.format(opcion=fondo)
            self.selectElement(xpath, '', '')

    def seleccionarCuentaAcred(self, cuenta):
        accion = u'Seleccionar cuenta acreditación'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(RES.select_cuentaAcreditacion, cuenta)
            self.capture_image(msgOk)
            self.wait(.5)

    def seleccionarMontoARescatar(self, monto):
        accion = u'Seleccionar radio monto a rescatar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.radio_monto, '', '', to)
            self.write(RES.input_monto, monto, to)
            self.capture_image(msgOk)

    def seleccionarCuotaparteParcial(self, monto):
        accion = u'Seleccionar radio cuotaparte parcial'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.radio_cuota, '', '', to)
            self.write(RES.input_montoParcial, monto, to)
            self.capture_image(msgOk)

    def seleccionarTotalCuotaPartes(self, monto):
        accion = u'Seleccionar radio total cuotapartes'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.radio_total, '', '', to)
            self.write(RES.input_totalCuotaparte, monto, to)
            self.capture_image(msgOk)

    def seleccionarBotonValorCuotaparte(self):
        accion = u'Seleccionar botón valor cuotaparte'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.button_valorCuotaparte, '', '', to)
            if self.visibility_element(RES.table_valorCuotaparte, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarModificar(self):
        accion = u'Seleccionar botón modificar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.button_modificar, '', '', to)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        accion = u'Seleccionar botón continuar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.button_continuar, '', '', to)
            xpath1 = RES.textarea_info
            xpath2 = RES.div_errorPanel
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg('Se muestra mensaje de error')

    def seleccionarConfirmar(self):
        accion = u'Seleccionar el botón confirmar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(RES.button_confirmar, '', '', to)
            self.capture_image(msgOk)

    # Verificacion de pantalla
    def verificarPantallaRescate(self):
        self.verificarSelectCuenta()
        self.verificarTexto1()
        self.verificarTexto2()
        self.verificarTexto3()
        self.verificarBotonCancelar()

    def verificarPantallaConfirmacion(self):
        self.verificarCuentaComitente()
        self.verificarFondoARescatar()
        self.verificarMoneda()
        self.verificarCantidadCuotaparte()
        self.verificarCuentaAcreditacion()
        self.verificarFechaAcreditacion()
        self.verificarTextoInfo()
        self.verificarDeclaracionJurada()

    def verificarPantallaResultado(self):
        self.verificarTicket()
        self.verificarCheckMail()
        self.verificarNuevaOperacion()
        self.verificarBotonDescargar()
        self.verificarContinuar()

    # Verificacion de elememtos
    def verificarSelectCuenta(self):
        accion = u'Verificar select de cuenta comitente'
        with self.step(accion):
            self.checkElement(RES.select_cuentaComitente, accion)

    def verificarTexto1(self):
        accion = u'Verificar texto 1'
        texto = "El Sistema cumple con las Normas de la CNV."
        with self.step(accion):
            xpath = RES.span_texto1
            text = self.get_element_text(xpath)
            if texto == text:
                self.checkElement(xpath, accion)
            else:
                self.fail_msg('El texto mostrado no es el esperado')

    def verificarTexto2(self):
        accion = u'Verificar texto 2'
        texto = "AGENTE NRO. 551 INSCRIPTO ANTE MERCADO ABIERTO ELECTRÓNICO S.A. - ENTIDAD AUTORREGULADA POR LA CNV RESOLUCIÓN NRO. 9934/93."
        with self.step(accion):
            xpath = RES.span_texto2
            text = self.get_element_text(xpath)
            if texto == text:
                self.checkElement(xpath, accion)
            else:
                self.fail_msg('El texto mostrado no es el esperado')

    def verificarTexto3(self):
        accion = u'Verificar texto 3'
        texto = "Macro BMA es Agente de Custodia de Productos de Inversión Colectiva de Fondos Comunes de Inversión, inscripta en el Registro de CNV bajo número 07."
        with self.step(accion):
            xpath = RES.span_texto3
            text = self.get_element_text(xpath)
            if texto == text:
                self.checkElement(xpath, accion)
            else:
                self.fail_msg('El texto mostrado no es el esperado')

    def verificarSinTenencia(self):
        accion = u'Verificar Popup sin tenencia'
        with self.step(accion):
            self.checkElement(RES.tabla_alertaSinTenencia, accion)

    def verificarBotonCancelar(self):
        accion = u'Verificar botón cancelar'
        with self.step(accion):
            self.checkElement(RES.button_cancelar, accion)

    def verificarTablaFondos(self):
        accion = u'Verificar que se muestra la tabla de fondos'
        with self.step(accion):
            self.checkElement(RES.table_fondosSeleccionables, accion)

    def verificarBotonCerrar(self):
        accion = u'Verificar que se muestra el botón cerrar'
        with self.step(accion):
            self.checkElement(RES.button_cerrar, accion)

    def verificarCuentaComitente(self):
        accion = u'Verificar cuenta comitente'
        with self.step(accion):
            self.checkElement(RES.span_cuentaComitente, accion)

    def verificarFondoARescatar(self):
        accion = u'Verificar Fondo a rescatar'
        with self.step(accion):
            self.checkElement(RES.span_fondoRescatar, accion)

    def verificarMoneda(self):
        accion = u'Verificar el tipo de moneda'
        with self.step(accion):
            self.checkElement(RES.span_moneda, accion)

    def verificarCantidadCuotaparte(self):
        accion = u'Verificar la cantidad de cuotaparte a rescatar'
        with self.step(accion):
            self.checkElement(RES.span_cantCuotaparte, accion)

    def verificarCuentaAcreditacion(self):
        accion = u'Verificar la cuenta de acreditacion'
        with self.step(accion):
            self.checkElement(RES.span_cuentaAcred, accion)

    def verificarFechaAcreditacion(self):
        accion = u'Verificar la fecha estimada de acreditación'
        with self.step(accion):
            self.checkElement(RES.span_fechaEstimada, accion)

    def verificarTextoInfo(self):
        accion = u'Verificar el texto con información'
        with self.step(accion):
            xpath = RES.textarea_info
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion)

    def verificarDeclaracionJurada(self):
        accion = u'Verificar texto de la declaración jurada'
        with self.step(accion):
            xpath = RES.span_declaracionSubtitulo
            self.go_to_xpath(xpath)
            text = self.get_element_text(xpath)
            texto_esperado = "DD Jurada de origen de los fondos:"
            if texto_esperado in text:
                self.checkElement(xpath, accion)
            else:
                self.fail_msg('El subtítulo no es el esperado')
            xpath = RES.span_declaracionTexto
            text = self.get_element_text(xpath)
            texto_esperado = ((
                u"En cumplimiento de las disposiciones reglamentarias "
                u"vigentes en materia de prevención de lavado de activos de "
                u"origen delictivo y del financiamiento del terrorismo, "
                u"manifiesto en carácter de declaración jurada, que los "
                u"fondos y/o bienes y/o valores con los que se realiza esta "
                u"operación, son provenientes de actividades lícitas y/o "
                u"relacionadas con mi actividad principal."
            ).encode('utf-8')).decode('utf-8')
            if texto_esperado in text:
                self.checkElement(xpath, accion)
            else:
                self.fail_msg('El text no es el esperado')

    def verificarTicket(self):
        accion = u'Verificar que se muestra el ticket'
        to = 10
        with self.step(accion):
            xpath = RES.img_ticket
            self.checkElement(xpath, accion, to)

    def verificarCheckMail(self):
        accion = u'Verificar que se muestre el checkbox de enviar por mail'
        to = 10
        with self.step(accion):
            xpath = RES.checkbox_mail
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarNuevaOperacion(self):
        accion = u'Verificar el botón de Nueva Operación'
        to = 10
        with self.step(accion):
            xpath = RES.button_nuevaOperacion
            self.checkElement(xpath, accion, to)

    def verificarBotonDescargar(self):
        accion = u'Verificar que se muestre el botón de descargar'
        to = 10
        with self.step(accion):
            xpath = RES.button_descargar
            self.checkElement(xpath, accion, to)

    def verificarContinuar(self):
        accion = u'Verificar que se muestre el botón de continuar'
        to = 10
        with self.step(accion):
            xpath = RES.button_continuar
            self.checkElement(xpath, accion, to)
