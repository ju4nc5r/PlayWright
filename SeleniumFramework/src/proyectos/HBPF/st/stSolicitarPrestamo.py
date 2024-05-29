# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudPrestamo import plSolicitudPrestamo as SP
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stSolicitudPrestamo(menu):
    def seleccionarPrestamoSoli(self, prestamo):
        accion = u'Seleccionar prestamo'
        to = 10
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = SP.select_prestamo3.format(prestamo)
            self.selectElement(xpath, msgOk, msgFail, to)
            # self.select_by_text(SP.select_prestamo, texto)
            # xpath1 = SP.span_lineaProducto
            # xpath2 = SP.table_prestamoNoDisponible
            # if self.double_visibility_element(xpath1, xpath2, to):
            #     self.capture_image(msgOk)
            # else:
            #     self.fail_msg(msgFail)

    def seleccionarTipoPrestamo(self, prestamo):
        accion = u'Seleccionar tipo préstamo'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SP.select_prestamo2, prestamo)
            self.capture_image(msgOk)

    def seleccionarCantidadCuotas(self, cuotas):
        accion = u'Seleccionar cantidad de cuotas'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SP.select_cuotas, cuotas)
            self.capture_image(msgOk)      

    def ingresarMontoSolicitado(self, monto):
        accion = u'Ingresar el monto solicitado'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SP.input_montoSolicitado, monto, to)
            self.capture_image(msgOk)

    def ingresarMontoASolicitar(self, monto):
        accion = u'Ingresar el monto a solicitar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SP.ipt_a_solicitar, monto, to)
            self.capture_image(msgOk)
            

    def seleccionarDiaVencimiento(self, dia):
        accion = u'Seleccionar día de vencimineto de cuotas'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SP.select_vencimientoCuotas, dia)
            self.capture_image(msgOk)

    def seleccionarCuentaAcreditacion(self, cuenta):
        accion = u'Seleccionar cuenta de acreditación'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SP.select_cuentaAcred, cuenta)
            self.capture_image(msgOk)

    def seleccionarCuentaDebito(self, cuenta):
        accion = u'Seleccionar cuenta de débito de cuotas'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SP.select_cuentaDeb, cuenta)
            self.capture_image(msgOk)

    def seleccionarDestinoPrestamo(self, destino):
        accion = u'Seleccionar destino del préstamo'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SP.select_destinoPrestamo, destino)
            self.capture_image(msgOk)

    def aceptarTerminosCondiciones(self):
        accion = u'Seleccionar aceptar términos y condiciones'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SP.input_checkboxTerminos, '', '', to)
            self.capture_image(msgOk)

    def seleccionarSimular(self):
        accion = u'Seleccionar botón simular'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SP.button_simular, '', '', to)
            if self.visibility_element(SP.label_tituloTablaSimulacion, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarComposicionCuotas(self):
        accion = u'Seleccionar botón composición de cuotas'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SP.button_composicionCuota, '', '', to)
            if self.visibility_element(
                                SP.label_tituloTablaComposicionCuotas, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarContinuar(self):
        accion = u'Seleccionar botón de continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SP.button_continuar, '', '', to)
            xpath1 = SP.input_pin
            xpath2 = ''
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarContinuarSolo(self):
        accion = u'Seleccionar botón de continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SP.button_continuar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificar Pantallas
    def verificarPantallaSolicitud(self):
        self.verificarNombre()
        self.verificarNumDocumento()
        self.verificarSelectPrestamo()
        self.verificarVolver()

    def verificarPantallaCargaDatos(self):
        self.verificarLineaProducto()
        self.verificarProducto()
        self.verificarCuenta()
        self.verificarPrestamo()
        self.verificarMoneda()
        self.verificarSelectCantidadCuotas()
        self.verificarMontoMaximo()
        self.verificarMontoSolicitado()
        self.verificarSelectVencimiento()
        self.verificarSelectCuentaAcred()
        self.verificarSelectCuentaDebito()
        self.verificarSelectDestinoPrestamo()
        self.verificarTerminosCondiciones()
        self.verificarBotonCancelar()
        self.verificarBotonSimular()
        self.verificarBotonComposicionCuota()
        self.verificarBotonContinuar()

    def verificarPantallaConfirmacion(self):
        self.verificarPrestamoConfirmacion()
        self.verificarMonedaConfirmacion()
        self.verificarCantidadCuotasConfirmacion()
        self.verificarMontoSolicitadoConfirmacion()
        self.verificarImportePrimCuota()
        self.verificarVencimientoPrimCuota()
        self.verificarTasaPrestamo()
        self.verificarGastos()
        self.verificarIVA()
        self.verificarMonto()
        self.verificarCuentaAcreditacion()
        self.verificarCuentaDebito()
        self.verificarDiaVencimiento()
        self.verificarDestionoPrestamo()
        self.verificarTNA()
        self.verificarTEA()
        self.verificarCFTEA()

    # Verificar elementos
    def verificarNombre(self):
        accion = u'Verificar el texto del nombre'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_nombre, accion, to)

    def verificarNumDocumento(self):
        accion = u'Verificar el texto del número del documento'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_numeroDocu, accion, to)

    def verificarSelectPrestamo(self):
        accion = u'Verificar el select de préstamos'
        to = 10
        with self.step(accion):
            self.checkElement(SP.select_prestamo, accion, to)

    def verificarVolver(self):
        accion = u'Verificar botón volver'
        to = 10
        with self.step(accion):
            self.checkElement(SP.button_volver, accion, to)

    def verificarLineaProducto(self):
        accion = u'Verificar texto línea de producto'
        to = 10
        with self.step(accion):
            xpath = SP.span_lineaProducto
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarProducto(self):
        accion = u'Verificar texto producto'
        to = 10
        with self.step(accion):
            xpath = SP.span_producto
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarCuenta(self):
        accion = u'Verificar cuenta'
        to = 10
        with self.step(accion):
            xpath = SP.span_cuenta
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarPrestamo(self):
        accion = u'Verificar select del préstamo'
        to = 10
        with self.step(accion):
            xpath = SP.select_prestamo2
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarMoneda(self):
        accion = u'Verificar tipo moneda'
        to = 10
        with self.step(accion):
            xpath = SP.span_moneda
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarSelectCantidadCuotas(self):
        accion = u'Verificar select de cantidad de cuotas'
        to = 10
        with self.step(accion):
            xpath = SP.select_cuotas
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarMontoMaximo(self):
        accion = u'Verificar texto de monto máximo'
        to = 10
        with self.step(accion):
            xpath = SP.span_montoMaximo
            # self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarMontoSolicitado(self):
        accion = u'Verificar input monto solicitado'
        to = 10
        with self.step(accion):
            xpath = SP.input_montoSolicitado
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarSelectVencimiento(self):
        accion = u'Verificar select de día de vencimiento de cuotas'
        to = 10
        with self.step(accion):
            xpath = SP.select_vencimientoCuotas
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarSelectCuentaAcred(self):
        accion = u'Verificar select de cuenta de acreditación'
        to = 10
        with self.step(accion):
            xpath = SP.select_cuentaAcred
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarSelectCuentaDebito(self):
        accion = u'Verificar select de cuenta débito'
        to = 10
        with self.step(accion):
            xpath = SP.select_cuentaDeb
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarSelectDestinoPrestamo(self):
        accion = u'Verificar select de destino préstamo'
        to = 10
        with self.step(accion):
            xpath = SP.select_destinoPrestamo
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarTerminosCondiciones(self):
        accion = u'Verificar checkbox de aceptar términos y condiciones'
        to = 10
        with self.step(accion):
            xpath = SP.input_checkboxTerminos
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarBotonCancelar(self):
        accion = u'Verificar botón de cancelar'
        to = 10
        with self.step(accion):
            self.checkElement(SP.button_cancelar, accion, to)

    def verificarBotonSimular(self):
        accion = u'Verificar botón de simular'
        to = 10
        with self.step(accion):
            self.checkElement(SP.button_simular, accion, to)

    def verificarBotonComposicionCuota(self):
        accion = u'Verificar botón composición cuota'
        to = 10
        with self.step(accion):
            self.checkElement(SP.button_composicionCuota, accion, to)

    def verificarBotonContinuar(self):
        accion = u'Verificar botón continuar'
        to = 10
        with self.step(accion):
            self.checkElement(SP.button_continuar, accion, to)

    def verificarTablaSimulacion(self):
        accion = u'Verificar tabla de simulación'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            if self.visibility_element(SP.label_tituloTablaSimulacion, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarTablaComposicionCuotas(self):
        accion = u'Verificar tabla de composición de cuotas'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            if self.visibility_element(
                                SP.label_tituloTablaComposicionCuotas, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarPrestamoConfirmacion(self):
        accion = u'Verificar tipo de préstamo'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_prestamo, accion, to)

    def verificarMonedaConfirmacion(self):
        accion = u'Verificar el tipo de moneda'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_moneda, accion, to)

    def verificarCantidadCuotasConfirmacion(self):
        accion = u'Verificar las cantidades de cuotas seleccionado'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_cuotas, accion, to)

    def verificarMontoSolicitadoConfirmacion(self):
        accion = u'Verificar monto solicitado'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_montoSolicitado, accion, to)

    def verificarImportePrimCuota(self):
        accion = u'Verificar el importe de la primera cuota'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_importePrimCuota, accion, to)

    def verificarVencimientoPrimCuota(self):
        accion = u'Verificar fecha del primer vencimiento'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_vencimientoPrimCuota, accion, to)

    def verificarTasaPrestamo(self):
        accion = u'Verificar tasa del préstamo'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_tasaPrestamo, accion, to)

    def verificarGastos(self):
        accion = u'Verificar otros gastos e impuestos'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_gastosImpuestos, accion, to)

    def verificarIVA(self):
        accion = u'Verificar IVA sobre gastos'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_iva, accion, to)

    def verificarMonto(self):
        accion = u'Verificar monto a acreditar'
        to = 10
        with self.step(accion):
            xpath = SP.span_montoAcreditar
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarCuentaAcreditacion(self):
        accion = u'Verificar cuenta de acreditación'
        to = 10
        with self.step(accion):
            xpath = SP.span_cuentaAcred
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)

    def verificarCuentaDebito(self):
        accion = u'Verificar cuenta de débito'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_cuentaDeb, accion, to)

    def verificarDiaVencimiento(self):
        accion = u'Verificar día de vencimiento de cuotas'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_diaVencimiento, accion, to)

    def verificarDestionoPrestamo(self):
        accion = u'Verificar el destino del préstamo'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_destinoPrestamo, accion, to)

    def verificarTNA(self):
        accion = u'Verificar el TNA'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_tna, accion, to)

    def verificarTEA(self):
        accion = u'Verificar el TEA'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_tea, accion, to)

    def verificarCFTEA(self):
        accion = u'Verificar CFTEA'
        to = 10
        with self.step(accion):
            self.checkElement(SP.span_cftea, accion, to)

    def ingresarTercerCuarto(self, tercerCuarto):
        accion = u'Ingresar tercer cuarto'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SP.input_tercerCuarto, tercerCuarto, to)
            self.capture_image(msgOk)

    def ingresarPin(self, pin):
        accion = u'Ingresar pin'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SP.input_pin, pin, to)
            self.capture_image(msgOk)        

    def seleccionarConfirmar(self):
        accion = u'Seleccionar botón de confirmar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SP.btn_confirmar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificacion de elementos
    def verificarTicket(self):
        accion = u'Verificar imagen del ticket de resultado'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SP.img_ticket
            if self.visibility_element(xpath, to):
               self.highlight(xpath,accion)
            else:
                self.fail_msg(msgFail)

    def seleccionarCantidadCuotasAPagar(self, cuotas):
        accion = u'Seleccionar cantidad de cuotas a pagar'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SP.slc_a_pagar, cuotas)
            self.capture_image(msgOk)          