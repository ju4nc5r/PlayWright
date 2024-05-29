# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaTransferencia import (
    locConsultaTransferencia as locCT
)
from SeleniumFramework.common_functions import get_msg


class stConsultaTransferencia(stLogin, menu):
    # Pasos
    def seleccionarTipoCuenta(self, tipo):
        accion = 'Seleccionar tipo de transferencia'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locCT.sel_tipoTransferencia
            self.selectListByPartialText(xpath, tipo)
            self.capture_image(msgOk)

    def seleccionarOperacion(self, numero):
        accion = 'Seleccionar operacion'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locCT.tr_opcionesTabla
            opciones = self.search_elements(xpath, to)
            opciones[numero].click()
            self.log.info('Se selecciona la opcion {}'.format(numero))
            self.verifySelection(locCT.lbl_cuentaDeb, msgOk, to)

    # Verificacion en conjunto
    # Verificacion de la pagina de consulta
    def verificarPrimeraPagina(self):
        self.verificarTitulo()
        self.verificarLabelTipoTransferencia()
        self.verificarSelectTipoTransferencia()
        self.verificarBotonVolver()
        self.verificarBotonProgTransferencia()

    # Verificacion de la pagina con la operacion
    def verificarPaginaOperacion(self):
        self.verificarCuentaDebito()
        self.verificarCuentaAcreditada()
        self.verificarFechaSolicitud()
        self.verificarPeriodicidad()
        self.verificarRepeticiones()
        self.verificarImporte()

    # Verificacion por pasos
    def verificarTitulo(self):
        accion = 'Visualizar el titulo'
        with self.step(accion):
            xpath = locCT.titulo
            self.checkElement(xpath, accion)

    def verificarLabelTipoTransferencia(self):
        accion = 'Visualizar label tipo de transferencia'
        with self.step(accion):
            xpath = locCT.lbl_tipoTransferencia
            self.checkElement(xpath, accion)

    def verificarSelectTipoTransferencia(self):
        accion = 'Visualizar select del tipo de transferencia'
        with self.step(accion):
            xpath = locCT.sel_tipoTransferencia
            self.checkElement(xpath, accion)

    def verificarBotonVolver(self):
        accion = 'Visualizar boton de volver'
        with self.step(accion):
            xpath = locCT.btn_volver
            self.checkElement(xpath, accion)

    def verificarBotonProgTransferencia(self):
        accion = 'Visualizar boton de programar transferencia'
        with self.step(accion):
            xpath = locCT.btn_programarTransferencia
            self.checkElement(xpath, accion)

    def verificarTablaResultados(self):
        accion = 'Visualizar tabla de resultados'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath1 = locCT.tbl_tablaResultados
            xpath2 = locCT.lbl_sinOperacion
            if self.double_visibility_element(xpath1, xpath2, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarCuentaDebito(self):
        accion = 'Visualizar cuenta debito'
        with self.step(accion):
            xpath = locCT.txt_cuentaDeb
            self.checkElement(xpath, accion)

    def verificarCuentaAcreditada(self):
        accion = 'Visualizar cuenta acreditada'
        with self.step(accion):
            xpath = locCT.txt_cuentaAcred
            self.checkElement(xpath, accion)

    def verificarFechaSolicitud(self):
        accion = 'Visualizar la fecha de la solicitud'
        with self.step(accion):
            xpath = locCT.txt_fechaSolicitud
            self.checkElement(xpath, accion)

    def verificarPeriodicidad(self):
        accion = 'Visualizar periodicidad'
        with self.step(accion):
            xpath = locCT.txt_periodicidad
            self.checkElement(xpath, accion)

    def verificarRepeticiones(self):
        accion = 'Visualizar repeticiones'
        with self.step(accion):
            xpath = locCT.txt_repeticioens
            self.checkElement(xpath, accion)

    def verificarImporte(self):
        accion = 'Visualizar importe'
        with self.step(accion):
            xpath = locCT.txt_importe
            self.checkElement(xpath, accion)
