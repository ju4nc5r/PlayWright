# -*- coding: utf-8 -*-
from sub import sub
from SeleniumFramework.src.proyectos.HBPF.pageLoc.Inicio import Inicio
from SeleniumFramework.common_functions import get_msg


class stVerificarPersonalBank(sub):

    def verificarPersonalBank(self):
        accion = "Verificar Personal Bank"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.wait(5)
            if self.is_displayed(Inicio.span_identificador_PersonalBank_xp):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
