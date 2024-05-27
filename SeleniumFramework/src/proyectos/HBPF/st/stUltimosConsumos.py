# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.proyectos.HBPF.loc.locUltimosConsumos import locUltimosConsumos
# from proyectos.CRM import loc


class stUltimosConsumos(menu, stLogin):
    def seleccionarTarjeta(self, tarjeta, sinConsumos=False):
        accion = 'Seleccionar Tarjeta'
        with self.step(accion):
            xpath = locUltimosConsumos.combo_Tarjetas
            self.selectListByPartialText(xpath, tarjeta)
            self.capture_image(accion)
            if (sinConsumos):
                self.verificarSinUltimosConsumos()
            else:
                self.verificarConsumosTarjeta()

    def verificarSinUltimosConsumos(self):
        to = 5
        accion = 'Verificar Tarjeta sin ultimos consumos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locUltimosConsumos.lbl_SinConsumos
            if(self.visibility_element(xpath, to)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarConsumosTarjeta(self):
        to = 5
        accion = 'Verificar ultimos consumos de tarjeta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locUltimosConsumos.lbl_TConsumos
            if(self.visibility_element(xpath, to)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarDetalleConsumo(self, elemento):
        to = 5
        accion = 'Seleccionar un consumo para ver detalle'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locUltimosConsumos.tbl_Consumos1.format(elemento)
            self.selectElement(xpath, msgOk, msgFail, to)
            verificar_xpath = locUltimosConsumos.lbl_DetalleConsumo
            if(self.verifySelection(verificar_xpath, accion, to)):
                self.capture_image(msgOk)
                self.cerrarDetalleConsumo()

    def cerrarDetalleConsumo(self):
        to = 5
        accion = 'Cerrar el detalle de consumo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locUltimosConsumos.cmd_CerrarDetalleConsumo
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarVolver(self):
        to = 10
        accion = 'Seleccionar volver'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locUltimosConsumos.cmd_Volver
            self.selectElement(xpath, msgOk, msgFail, to)
