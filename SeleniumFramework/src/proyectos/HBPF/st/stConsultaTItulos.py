# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaTitulo import plConsultaTitulo as CT
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaTitulo(menu):
    def seleccionarTitulo(self, cuenta, titulo):
        accion = u'Seleccionar titulo a visualizar'
        to = 10
        msgOk, msgFail = get_msg(accion)
        xpath = CT.option_cuentaTitulo.format(cuenta=cuenta, opcion=titulo)
        with self.step(accion):
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(CT.span_cuentaComitente):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificacion de pantalla
    def verificarPantallaConsulta(self):
        self.verificarTablaTitulos()
        self.verificarBotonVolver()

    def verificarPantallaDetalle(self):
        self.verificarCuentaComitente()
        self.verificarEspecie()
        self.verificarCodigoEspecie()
        self.verificarCupon()
        self.verificarSaldoValorizado()
        self.verificarTasaAmortizacion()
        self.verificarValorNominal()
        self.verificarValorResidual()
        self.verificarFechaUltCotizacion()
        self.verificarUltimaCotizacion()

    # Verificacion de elementos
    def verificarTablaTitulos(self):
        accion = u'Verificar la tabla de titulos'
        with self.step(accion):
            self.checkElement(CT.table_cuenta, accion)

    def verificarBotonVolver(self):
        accion = u'Verificar botón volver'
        with self.step(accion):
            xpath = CT.button_volver
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion)

    def verificarSinTitulos(self):
        accion = u'Verificar mensaje que no posee títulos'
        with self.step(accion):
            self.checkElement(CT.sapn_sinProductos, accion)

    def verificarCuentaComitente(self):
        accion = u'Verificar cuenta comitente'
        with self.step(accion):
            self.checkElement(CT.span_cuentaComitente, accion)

    def verificarEspecie(self):
        accion = u'Verificar especie'
        with self.step(accion):
            self.checkElement(CT.span_especie, accion)

    def verificarCodigoEspecie(self):
        accion = u'Verificar código de especie'
        with self.step(accion):
            self.checkElement(CT.span_codEspecie, accion)

    def verificarCupon(self):
        accion = u'Verificar cupón'
        with self.step(accion):
            self.checkElement(CT.span_cupon, accion)

    def verificarSaldoValorizado(self):
        accion = u'Verificar saldo valorizado'
        with self.step(accion):
            self.checkElement(CT.span_saldoValorizado, accion)

    def verificarTasaAmortizacion(self):
        accion = u'Verificar tasa de amortización'
        with self.step(accion):
            self.checkElement(CT.span_tasaAmortizacion, accion)

    def verificarValorNominal(self):
        accion = u'Verificar valor normal'
        with self.step(accion):
            self.checkElement(CT.span_valorNominal, accion)

    def verificarValorResidual(self):
        accion = u'Verificar valor residual'
        with self.step(accion):
            self.checkElement(CT.span_valorResidual, accion)

    def verificarFechaUltCotizacion(self):
        accion = u'Verificar fecha de última cotización'
        with self.step(accion):
            self.checkElement(CT.span_fechaUltCotizacion, accion)

    def verificarUltimaCotizacion(self):
        accion = u'Verificar última cotización'
        with self.step(accion):
            self.checkElement(CT.span_ultimaCotizacion, accion)
