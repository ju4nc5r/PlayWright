# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaEcheq import plConsultaEcheq
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg


class stConsultaECheq(menu):
    def verificarEcheqs(self):
        accion = 'Verificar tabla de ECheqs'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plConsultaEcheq.tbl_echeqs
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(accion)

    def seleccionarEcheqEstado(self, estado):
        accion = 'seleccionar ECheq con estado'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plConsultaEcheq.col_estado.format(estado)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(accion)

    def verDetalle(self):
        accion = 'Ver detalle ECheq'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plConsultaEcheq.tbl_detalles
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(accion)