# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plVentaTitulos import plVentaTitulos as VT
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plCompraTitulos import plCompraTitulo
from SeleniumFramework.src.proyectos.HBPF.st.stCompraTitulos import stCompraTitulos
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stVentaTitulos(stCompraTitulos):
    def seleccionarContinuar(self):
        accion = u'Seleccionar el botón continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plCompraTitulo.button_continuar
            self.selectElement(xpath, '', '', to)
            xpath1 = plCompraTitulo.tabla_titulos
            xpath2 = plCompraTitulo.input_precioCompra
            xpath3 = plCompraTitulo.span_especie
            xpath4 = VT.span_sinTitulos
            xpath5 = VT.table_acciones
            elem_list = [xpath1, xpath2, xpath3, xpath4, xpath5]
            numero = self.array_visibility(elem_list, to)
            if numero == 2:
                self.fail_msg(msgFail)
            else:
                self.capture_image(msgOk)

    def seleccionarCuentaAcreditacion(self, cuenta):
        accion = u'Seleccionar la cuenta de acreditación'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = VT.select_cuentaAcreditacion
            self.selectListByPartialText(xpath, cuenta)
            self.capture_image(msgOk)

    def seleccionarAccionesAVencer(self, acciones):
        accion = u'Seleccionar las acciones a vender'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = VT.option_accion.format(accion=acciones)
            self.selectElement(xpath, '', '', to)
            self.capture_image(msgOk)

    # Verificara pantalla
    def verificarPantallaConfirmacion(self):
        self.verificarEspecie()
        self.verificarCantidadNominales()
        self.verificarPrecioVenta()
        self.verificarMonto()
        self.verificarCantidadRuedas()
        self.verificarComisionBanco()
        self.verificarComisionMinima()
        self.verificarComisionMercado()
        self.verificarCuentaAcreditacion()
        self.verificarCuentaComitente()

    def verificarCantidadNominales(self):
        accion = u'Verificar el texto de la cantidad de nominales'
        with self.step(accion):
            self.checkElement(VT.span_cantNominales, accion)

    def verificarPrecioVenta(self):
        accion = u'Verificar el texto del precio limite de venta'
        with self.step(accion):
            self.checkElement(VT.span_precioVenta, accion)

    def verificarMonto(self):
        accion = u'Verificar el texto del monto'
        with self.step(accion):
            self.checkElement(VT.span_montoEstimado, accion)

    def verificarCuentaAcreditacion(self):
        accion = u'Verificar el texto de la cuenta de acreditación'
        with self.step(accion):
            self.checkElement(VT.span_cuentaAcreditacion, accion)
