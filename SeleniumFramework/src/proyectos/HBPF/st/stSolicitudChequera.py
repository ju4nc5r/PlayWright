# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudChequera import plSolicitudChequera as SC
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stSolicitudChequera(menu):
    def solicitarChequera(self, cuenta, cant, tipo):
        self.seleccionarCuenta(cuenta)        
#         if self.verify(SC.msgSolicitudExistente):
#             self.capture_image(u"Click continuar si hay mensaje solicitud existente", 3)
#             self.jsClick(SC.btnContinuarSiHaySolicitudExistente)        
        self.ingresarCantidadChequera(cant)
        self.seleccionarTipoCantCheques(tipo)

    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = SC.select_cuenta
            self.selectListByPartialText(xpath, cuenta)
            if self.verify(SC.msgSolicitudExistente):
                self.capture_image(u"Click continuar si hay mensaje solicitud existente", 3)
                self.jsClick(SC.btnContinuarSiHaySolicitudExistente)        
            self.capture_image(msgOk)

    def ingresarCantidadChequera(self, cant):
        accion = u'Ingresar cantidad de chequeras'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SC.input_chequerasPedir
            self.write(xpath, cant, to)
            self.capture_image(msgOk)

    def seleccionarTipoCantCheques(self, tipo):
        accion = u'Seleccionar el tipo y cantidad de cheques'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = SC.select_tipoCheques
            self.selectListByPartialText(xpath, tipo)
            self.capture_image(msgOk)

    def seleccionarEnvioDomPart(self):
        accion = u'Seleccionar envio a domicilio particular'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SC.input_domicilioParticular
            self.selectElement(xpath, '', '', to)
            self.capture_image(msgOk)

    def seleccionarRetiroSucu(self):
        accion = u'Seleccionar envio a sucursal'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SC.input_RetiroSucu
            self.selectElement(xpath, '', '', to)
            self.capture_image(msgOk)

    def seleccionarSucursal(self, codigo):
        accion = u'Seleccionar sucursal deseada'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SC.input_sucursal.format(codigo=codigo)
            self.selectElement(xpath, '', '', to)
            self.capture_image(msgOk)

    def seleccionarVolver(self):
        accion = u'Seleccionar botón volver'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SC.button_volver, '', '', to)
            self.capture_image(msgOk)

    def seleccionarAceptar(self):
        accion = u'Seleccionar el botón aceptar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SC.button_aceptar, '', '', to)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        accion = u'Seleccionar botón continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SC.button_continuar, '', '', to)
            xpath1 = SC.span_cuenta
            xpath2 = SC.div_error
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificacion de pantallas
    def verificarPantallaSolicitud(self):
        accion = u'Verificar pantalla de solicitud de chequera'
        with self.step(accion):
            self.verificarSelectCuenta()
            self.verificarInputChequerasAPedir()
            self.verificarSelectTipoCantCheques()
            self.verificarFormaEnvio()
            
    def ingresarTercerGrupo4digTarj(self, tercerGrupo4dig):
        accion = u'Ingresar Tercer grupo de cuatro dígitos de la tarjeta'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SC.input_3erGrupo4digTarj
            self.write(xpath, tercerGrupo4dig, to)
            self.capture_image(msgOk)

    def ingresarClaveCajero(self, claveCajero):
        accion = u'Ingresar clave del cajero'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SC.input_claveCajero
            self.write(xpath, claveCajero, to)
            self.capture_image(msgOk)

    def verificarPantallaConfirmacion(self):
        accion = u'Verificar la pantalla de confirmacion'
        with self.step(accion):
            self.verificarCuenta()
            self.verificarCantidadChequeras()
            self.verificarTipoCheques()
            self.verificarLugarEnvio()

    def seleccionarConfirmar(self):
        accion = u'Seleccionar botón Confirmar'
        msgOk, msgFail = get_msg(accion)        
        to = 10
        with self.step(accion):
            self.selectElement(SC.btnConfirmar,msgOk,msgFail, to)
            self.capture_image(msgOk)


    # Verificacion de elementos
    def verificarSelectCuenta(self):
        accion = u'Verificar select de cuenta'
        self.checkElement(SC.select_cuenta, accion)

    def verificarInputChequerasAPedir(self):
        accion = u'Verificar input de cantidad de chqueras a pedir'
        self.checkElement(SC.input_chequerasPedir, accion)

    def verificarSelectTipoCantCheques(self):
        accion = u'Verificar select de tipo y cantidad de cheques'
        self.checkElement(SC.select_tipoCheques, accion)

    def verificarFormaEnvio(self):
        accion = u'Verificar tabla de forma de envío'
        self.checkElement(SC.table_formaEntrega, accion)

    def verificarCuenta(self):
        accion = u'Verificar cuenta'
        self.checkElement(SC.span_cuenta, accion)

    def verificarCantidadChequeras(self):
        accion = u'Verificar Cantidad de chequeras a pedir'
        self.checkElement(SC.span_cantChequera, accion)

    def verificarTipoCheques(self):
        accion = u'Verificar tipo y cantidad de cheques'
        self.checkElement(SC.span_tipoCantCheques, accion)

    def verificarLugarEnvio(self):
        accion = u'Verificar lugar de envío'
        self.checkElement(SC.table_lugarEntrega, accion)

    def verificarTicketSolicChequera(self):
        accion = u'Verificar Ticket'
        self.checkElement(SC.imgTicketSolicChequera, accion)
        
    def validarMensajeDeErrorClaveCajero(self):
        accion = u'Validar Mensaje error Clave Cajero'
        self.checkElement(SC.msgErrorClaveCajaero, accion)