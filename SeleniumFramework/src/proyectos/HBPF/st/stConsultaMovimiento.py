# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaMovimientos import (
    locConsultaMovimiento as locCM)
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaMovimientos(stLogin, menu):
    # Steps
    def seleccionarMovimiento(self, movimiento):
        accion = 'Seleccionar tipo de movimiento'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(locCM.sel_movimiento, movimiento)
            self.capture_image(msgOk)

    def seleccionarBuscar(self, sinMov=False, msjEsperado=None):
        accion = 'Seleccionar el boton buscar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.btn_buscar
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath1 = locCM.tbl_movimiento
            xpath2 = locCM.tbl_sinResultado
            xpath3 = locCM.div_error
            array_elem = [xpath1, xpath2, xpath3]
            numero = self.array_visibility(array_elem, to)
            if numero == 0:
                self.capture_image('Se muestra la tabla de resultados')
            elif numero == 1:
                # Si el mensaje de sin movimientos, es esperado o no
                if sinMov:
                    msg = 'Se muestra el elemento esperado'
                    self.checkElement(locCM.tbl_sinResultado, msg)
                else:
                    self.fail_msg('No se muestra la tabla con movimientos')
            elif numero == 2:
                if msjEsperado is None:
                    self.fail_msg('Se muestra mensaje de error')
                else:
                    msg = 'Se muestra el mensaje de error'
                    self.capture_image(msg)

    def ingresarFechas(self, desde, hasta):
        self.ingresarFechaDesde(desde)
        self.ingresarFechaHasta(hasta)

    def ingresarImportes(self, desde, hasta):
        self.ingresarImporteDesde(desde)
        self.ingresarImporteHasta(hasta)

    def ingresarFechaDesde(self, fecha):
        accion = 'Ingresar fecha desde'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.inp_fechaDesde
            self.write(xpath, fecha, to)
            self.capture_image(msgOk)

    def ingresarFechaHasta(self, fecha):
        accion = 'Ingresar fecha hasta'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.inp_fechaHasta
            self.write(xpath, fecha, to)
            self.capture_image(msgOk)

    def ingresarImporteDesde(self, desde):
        accion = 'Ingresar importe desde'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.inp_importeDesde
            self.write(xpath, desde, to)
            self.capture_image(msgOk)

    def ingresarImporteHasta(self, hasta):
        accion = 'Ingresar importe hasta'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.inp_importeHasta
            self.write(xpath, hasta, to)
            self.capture_image(msgOk)

    def seleccionarVisualizar(self, opcion):
        accion = 'Visualizar el detalle del movimiento'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.opc_visualizar.format(opcion)
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(locCM.titulo_detalle, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarVolverDetalle(self):
        accion = 'Seleccionar el boton volver en pantalla de detalle'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.seleccionarVolver(to)
            if self.visibility_element(locCM.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarVolverMovimientos(self):
        accion = 'Seleccionar el boton volver en la pantalla de movimientos'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.seleccionarVolver(to)
            self.capture_image(msgOk)

    def seleccionarVolver(self, to=10):
        xpath = locCM.btn_volver
        self.selectElement(xpath, '', '', to)

    def seleccionarCAsinMovimientos(self):
        accion = 'Seleccionar CA sin movimientos'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCM.sel_cuenta
            self.selectElement(xpath, '', '', to)
            xpath2 = locCM.segunda_cuenta
            if self.visibility_element(xpath2, to):
                self.selectElement(xpath2, '', '', to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                

    # Verificacion de pantalla
    def verificarPantallaConsultaMov(self):
        self.verificarSelectCuenta()
        self.verificarSelectMovimiento()
        self.verificarBotonVolver()

    def verificarPantallaDefinirConsulta(self):
        self.verificarImporteDesdeHasta()
        self.verificarFechaDesdeHasta()

    def verificarPantallaDetalle(self):
        self.verificarOperacion()
        self.verificarFechaRealizacion()
        self.verificarHoraRealizacion()
        self.verifcarFechaImputacion()
        self.verificarCuenta()
        # self.verificarTerminal()
        self.verificarCanal()
        self.verificarNumReferencia()
        self.verificarMoneda()
        self.verificarDebCred()
        self.verificarImporte()

    # Verificacion de los elementos
    def verificarSelectCuenta(self):
        accion = 'Verificar que se muestre el select de cuenta'
        with self.step(accion):
            xpath = locCM.sel_cuenta
            self.checkElement(xpath, accion)

    def verificarSelectMovimiento(self):
        accion = 'Verificar que se muestre el select del movimiento'
        with self.step(accion):
            xpath = locCM.sel_movimiento
            self.checkElement(xpath, accion)

    def verificarBotonVolver(self):
        accion = 'Verificar que se muestre el boton volver'
        with self.step(accion):
            xpath = locCM.btn_volver
            self.checkElement(xpath, accion)

    def verificarImporteDesdeHasta(self):
        accion = 'Verificar que se muestre el input para el importe desde'
        with self.step(accion):
            xpath = locCM.inp_importeDesde
            self.checkElement(xpath, accion)
        accion = 'Verificar que se muestre el input para el importe hasta'
        with self.step(accion):
            xpath = locCM.inp_importeHasta
            self.checkElement(xpath, accion)

    def verificarFechaDesdeHasta(self):
        accion = 'Verificar que se muestre el input para la fecha hasta'
        with self.step(accion):
            xpath = locCM.inp_fechaDesde
            self.checkElement(xpath, accion)
        accion = 'Verificar que se muestre el input para la fecha hasta'
        with self.step(accion):
            xpath = locCM.inp_fechaHasta
            self.checkElement(xpath, accion)

    def verificarBotonBuscar(self):
        accion = 'Verificar que se muestre el boton buscar'
        with self.step(accion):
            xpath = locCM.btn_buscar
            self.checkElement(xpath, accion)

    def verificarOperacion(self):
        accion = 'Verificar que se muestre el tipo de operacion'
        with self.step(accion):
            xpath = locCM.txt_operacion
            self.checkElement(xpath, accion)

    def verificarFechaRealizacion(self):
        accion = 'Verificar que se muestra la fecha de realizacion'
        with self.step(accion):
            xpath = locCM.txt_fechaRealizacion
            self.checkElement(xpath, accion)

    def verificarHoraRealizacion(self):
        accion = 'Verificar que se muestra la hora de realizacion'
        with self.step(accion):
            xpath = locCM.txt_horaRealizacion
            self.checkElement(xpath, accion)

    def verifcarFechaImputacion(self):
        accion = 'Verificar que se muestra la fecha de imputacion'
        with self.step(accion):
            xpath = locCM.txt_fechaImputacion
            self.checkElement(xpath, accion)

    def verificarCuenta(self):
        accion = 'Verificar que se muestra el numero de cuenta'
        with self.step(accion):
            xpath = locCM.txt_cuenta
            self.checkElement(xpath, accion)

    def verificarTerminal(self):
        accion = 'Verificar que se muesta la terminal'
        with self.step(accion):
            xpath = locCM.txt_terminal
            self.checkElement(xpath, accion)

    def verificarCanal(self):
        accion = 'Verificar que se muesta la terminal'
        with self.step(accion):
            xpath = locCM.txt_canal
            self.checkElement(xpath, accion)

    def verificarNumReferencia(self):
        accion = 'Verificar que se mueste el numero de referencia'
        with self.step(accion):
            xpath = locCM.txt_numReferencia
            self.checkElement(xpath, accion)

    def verificarMoneda(self):
        accion = 'Verificar que se muestre el tipo de moneda de la operacion'
        with self.step(accion):
            xpath = locCM.txt_moneda
            self.checkElement(xpath, accion)

    def verificarDebCred(self):
        accion = 'Verificar que se muestre si es debito o credito'
        with self.step(accion):
            xpath = locCM.txt_debCred
            self.checkElement(xpath, accion)

    def verificarImporte(self):
        accion = 'Verificar que se muestre el importe'
        with self.step(accion):
            xpath = locCM.txt_importe
            self.checkElement(xpath, accion)

    def verificarNoMivimientos(self):
        accion = "Verificar que se muestre: no se registran movimientos"
        with self.step(accion):
            xpath = locCM.no_movimientos
            self.checkElement(xpath, accion)