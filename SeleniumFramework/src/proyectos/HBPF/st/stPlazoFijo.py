# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.pageLoc.PlazoFijo import PlazoFijo as PF
from SeleniumFramework.common_functions import get_msg


class stPlazoFijo(stLogin, menu):

    def constituirPlazoFijo(self, nroCuenta, monto, plazo, tipo):
        # self.seleccionarMenuProductos()
        self.completarFormulario(nroCuenta, monto, plazo, tipo)
        self.seleccionarSimular()
        self.seleccionarConstituirPlazoFijo()
        self.seleccionarConfirmarPlazo()
        self.verificarMjeAltaOK()

    def completarFormulario(self, nroCuenta, monto, plazo, tipo):
        self.seleccionarConstitucionDePlazoFijo()
        self.seleccionarCuenta(nroCuenta)
        self.seleccionarTipoPlazoFijo(tipo='CLASICO')
        self.completarCampoPlazo(str(plazo))
        self.completarMontoinicial(str(monto))

    def seleccionarCuenta(self, cuenta):
        accion = "Seleccionar Constituir"
        with self.step(accion):
            xpath = PF.select_cuenta
            self.selectListByPartialText(xpath, cuenta)

    def seleccionarTipoPlazoFijo(self, tipo):
        accion = "Seleccionar Tipo Plazo Fijo"
        to=3
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = PF.tipo_plazoFijo
            self.wait(to)  # Tiempo de espera a que reaccione la aplicacion
            if tipo == 'FLEXIBLE':
                self.selectListByPartialText(xpath, "PF SELECTA FLEXIBLE")
            if tipo == 'CLASICO':
                self.selectListByPartialText(xpath, "CLASICO SELECTA")
            if tipo == 'PRECANCELABLE':
                self.selectListByPartialText(xpath, "UVA - LEY 25.827 - PRECANCELABLE")
            if tipo == 'CANCELABLE':
                self.selectListByPartialText(xpath, "UVA - LEY 25.827 - NO PRECANCELABLE")

    def completarCampoPlazo(self, plazo):
        to = 10
        accion = "Seleccionar Tipo Plazo Fijo"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = PF.input_plazo
            if self.visibility_element(xpath, to):
                self.write(xpath, plazo, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def completarFechaVencimiento(self, fecha):
        to = 10
        accion = "Completar Fecha Vencimiento"
        with self.step(accion):
            xpath = PF.input_vencimiento
            self.write(xpath, fecha, to)

    def completarMontoinicial(self, monto):
        to = 10
        accion = "Completar Monto Inicial"
        with self.step(accion):
            xpath = PF.input_montoInicial
            self.write(xpath, monto, to)
            self.capture_image(accion)

    def seleccionarSimular(self, msjEsperado=None):
        to = 10
        accion = "Seleccionar Simular"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = PF.button_simular
            self.selectElement(xpath, '', '', to)

            xpath1 = PF.button_constituir
            xpath2 = PF.div_error
            if self.double_visibility_element(xpath1, xpath2, to):
                if msjEsperado is None:
                    self.capture_image(msgOk)
                else:
                    self.fail_msg('No se muestra mensaje esperado')
            else:
                if msjEsperado is not None:
                    texto = self.get_element_text(xpath2)
                    if msjEsperado in texto:
                        self.capture_image('Se muestra el mensaje esperado')
                    else:
                        self.fail_msg('No se muestra el mensaje esperado')
                else:
                    self.fail_msg(msgFail)

    def seleccionarConstituirPlazoFijo(self):
        to = 10
        accion = "Seleccionar Constituir Plazo Fijo"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.selectElement(PF.button_constituir, '', '', to)
            if self.visibility_element(PF.button_confirmar, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarConfirmar(self, msjEsperado=None):
        to = 10
        accion = "Seleccionar Constituir Plazo Fijo"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            self.selectElement(PF.button_confirmar, '', '', to)
            xpath1 = PF.span_mensajeExito
            xpath2 = PF.div_error_confirmacion
            if self.double_visibility_element(xpath1, xpath2, to):
                if msjEsperado is None:
                    self.capture_image(msgOk)
                else:
                    self.fail_msg('No se esta mostrando el mensaje esperado')
            else:
                if msjEsperado is not None:
                    texto = self.get_element_text(xpath2)
                    if msjEsperado in texto:
                        self.capture_image('Se muestra el mensaje de error')
                    else:
                        self.fail_msg('El mensaje de error no es el esperado')
                else:
                    self.fail_msg(msgFail)
    
    def seleccionarConfirmarPlazo(self):
        to = 10
        accion = "Seleccionar Constituir Plazo Fijo"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = PF.button_confirmar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def verificarMjeAltaOK(self):
        accion = u'Verificar mensaje El plazo fijo fue dado de Alta'
        with self.step(accion):
            self.checkElement(PF.msgAltaOK, accion)


    def seleccionarTasas(self, msjEsperado=None):
        to = 10
        accion = "Seleccionar Tasas vigentes"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = PF.button_tasas
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = PF.table_tasas
            xpath2 = PF.div_error
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                if msjEsperado is not None:
                    texto = self.get_element_text(xpath2)
                    if msjEsperado in texto:
                        self.capture_image(msgFail)
                    else:
                        self.fail_msg('El mensaje no es el esperado')
                else:
                    self.fail_msg('Se muestra mensaje de error')

    def cerrarTasas(self):
        to = 10
        accion = "Cerrar las tasas vigentes"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = PF.button_cerrar
            self.selectElement(xpath, msgOk, msgFail, to)
            

    def seleccionarNuevoPlazoFijo(self):
        to = 10
        accion = "Seleccionar el boton nuevo plazo fijo"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = PF.button_nuevoPlazoFijo
            self.selectElement(xpath, msgOk, msgFail, to)
            if self.visibility_element(PF.title_h1_constitucionPlazoFijo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificar pantallas
    def verificarPantallaSimulacion(self, tipoCuenta):
        """
        Se muestran diferentes elementos en la simulacion, dependiendo del
        tipo de plazo fijo que se selecciona
        """
        if tipoCuenta == 'UVA':
            self.verificarPantallaUVA()
        else:
            self.verificarPantallaClasicoCustodia()

    def verificarPantallaClasicoCustodia(self):
        self.verificarTNA()
        self.verificarTEA()
        self.verificarIntereses()
        self.verificarMontoVencimiento()

    def verificarPantallaUVA(self):
        self.verificarMontoInicial()
        self.verificarValorUVA()
        self.verificarTNA()
        self.verificarTEA()
        self.verificarIntereses2()
        self.verificarIIGG()
        self.verificarMontoVencimiento2()

    def verificarPantallaConfirmacion(self, tipoCuenta):
        self.verificarTipoPlazoFijo()
        self.verificarFechaConstitucion()
        self.verificarFechaVencimiento()
        self.verificarPlazoInicial()
        self.verificarTNA()
        self.verificarTEA()
        self.verificarMontoInicial()
        self.verificarIntereses2()
        self.verificarMontoVencimiento2()
        self.verificarCuentaDebito()
        self.verificarCuentaAcreditacion()
        if tipoCuenta == 'UVA':
            self.verificarMontoInicialUVA()
            self.verificarValorUVA()
            self.verificarIIGG()

    # Verificar elementos
    def verificarDiaNoHabil(self):
        accion = u'Verificar día no hábil'
        with self.step(accion):
            self.checkElement(PF.span_diaNoHabil, accion)

    def verificarTNA(self):
        accion = u'Verificar el texto de TNA'
        with self.step(accion):
            self.go_to_xpath(PF.span_tna)
            self.checkElement(PF.span_tna, accion)

    def verificarTEA(self):
        accion = u'Verificar el texto del TEA'
        with self.step(accion):
            self.checkElement(PF.span_tea, accion)

    def verificarIntereses(self):
        accion = u'Verificar intereses'
        with self.step(accion):
            self.checkElement(PF.table_intereses, accion)

    def verificarMontoVencimiento(self):
        accion = u'Verificar el monto al vencimiento'
        with self.step(accion):
            self.checkElement(PF.table_montoVencimiento, accion)

    def verificarMontoInicial(self):
        accion = u'Verificar monto inicial'
        with self.step(accion):
            self.go_to_xpath(PF.span_montoInicial)
            self.checkElement(PF.span_montoInicial, accion)

    def verificarMontoInicialUVA(self):
        accion = u'Verificar monto inicial UVA'
        with self.step(accion):
            self.checkElement(PF.span_montoInicialUVA, accion)

    def verificarValorUVA(self):
        accion = u'Verificar valor UVA'
        with self.step(accion):
            self.checkElement(PF.span_valorUVA, accion)

    def verificarIntereses2(self):
        """ Verificacion de intereses para los plazo fijos UVA"""
        accion = u'Verificar intereses UVA'
        with self.step(accion):
            self.checkElement(PF.span_intereses2, accion)

    def verificarMontoVencimiento2(self):
        """ Verificacion del monto al vencimiento de los plazo fijos UVA"""
        accion = u'Verificar el monto al vencimiento UVA'
        with self.step(accion):
            self.checkElement(PF.span_montoVencimiento2, accion)

    def verificarIIGG(self):
        accion = u'Verificar IIGG'
        with self.step(accion):
            self.checkElement(PF.span_IIGG, accion)

    def verificarTipoPlazoFijo(self):
        accion = u'Verificar tipo de plazo fijo'
        with self.step(accion):
            self.checkElement(PF.span_tipoPlazoFijo, accion)

    def verificarFechaConstitucion(self):
        accion = u'Verificar la fecha de constitución'
        with self.step(accion):
            self.checkElement(PF.span_fechaConstitucion, accion)

    def verificarFechaVencimiento(self):
        accion = u'Verificar la fecha de vencimiento'
        with self.step(accion):
            self.checkElement(PF.span_fechaVencimiento, accion)

    def verificarPlazoInicial(self):
        accion = u'Verificar el plazo inicial'
        with self.step(accion):
            self.checkElement(PF.span_plazoInicial, accion)

    def verificarCuentaDebito(self):
        accion = u'Verificar la cuenta débito'
        with self.step(accion):
            self.checkElement(PF.span_cuentaDebito, accion)

    def verificarCuentaAcreditacion(self):
        accion = u'Verificar la cuenta acreditación'
        with self.step(accion):
            self.checkElement(PF.span_cuentaAcreditacion, accion)

    def verificarImpuestoSello(self):
        accion = u'Verificar impuesto a los sellos'
        with self.step(accion):
            self.checkElement(PF.span_impuestoSello, accion)

    def verificarImpuestoSelloConfirmacion(self):
        accion = u'Verificar impuesto a los sellos'
        with self.step(accion):
            self.checkElement(PF.span_impuestoSelloConfirmacion, accion)
