# -*- coding: utf-8 -*-
from sub import sub
from SeleniumFramework.src.proyectos.HBPF.pageLoc.Inicio import Inicio


class stVerificaCuenta310(sub):
    def verificarCuenta310(self):
        self.circuito()

    def circuito(self):
        # Inicia el circuito de verificacion
#         self.verificaCuenta310()
        self.verificaTarjeta310()
#         self.verificaInversiones310()   SE COMENTAN PORQUE LO UNICO QUE PIDE EL CASO ES QUE ESTÉ LA SOLAPA DE TARJETA DESPLEGADA
#         self.verificaPrestamos310()
#         self.verificaSeguros310()
#         self.verificaCaja310()

    def verificaCuenta310(self):
        accion = 'Verificar Cuenta 310'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            self.wait(5)
            # verifica que sea cuenta 310
            # verifica cuentas
            if (self.is_displayed(Inicio.span_identificador_310_xp)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificaTarjeta310(self):
        # verifica tarjetas
        accion = 'Verificar tarjetas cuenta 310'         
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            if (self.is_displayed(Inicio.span_identificador_310_xp)):
                self.verifySelection_highlight(Inicio.span_identificador_310_xp, accion, sleep=2)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificaInversiones310(self):
        # Verifica inversiones
        accion = 'Verificar inversiones cuenta 310'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        self.selectElement(Inicio.btn_Inversiones_despliegue_xp, msgOk,
                           msgFail)
        self.wait(5)
        with self.step(accion):
            if (self.is_displayed(Inicio.span_Inversiones_310_xp)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificaPrestamos310(self):
        # verifica prestamos
        accion = 'Verificar prestamos cuenta 310'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            self.selectElement(Inicio.btn_Prestamos_despliegue_xp, msgOk,
                               msgFail)
            self.wait(5)
            if (self.is_displayed(Inicio.span_Prestamos_310_xp)):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificaSeguros310(self):
        # verifica seguros
        accion = 'Verificar seguros cuenta 310'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        self.selectElement(Inicio.btn_Seguros_despliegue_xp, msgOk, msgFail)
        self.wait(5)
        if(self.is_displayed(Inicio.lbl_Seguros_310_xp)):
            self.capture_image(msgOk)
        else:
            self.fail_msg(msgFail)

    def verificaCaja310(self):
        # verifica cajas de seguridad
        accion = 'Verificar cajas de seguridad cuenta 310'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        self.selectElement(Inicio.btn_Caja_despliegue_xp, msgOk, msgFail)
        self.wait(5)
        if (self.is_displayed(Inicio.lbl_Caja_No_Disponible_xp)):
            self.capture_image('Caja no disponible')
        elif(self.is_displayed(Inicio.lbl_Sin_Cajas_xp)):
            self.capture_image(msgOk)
        else:
            self.fail_msg(msgFail)
        # todas las previas verificaciones observan si no tiene cuenta asignada
        # ej: Abr� tu cuenta Ita� de manera f�cil y r�pida, completa la
        #  solicitud online y empez� a disfrutar de los beneficios que
        #  tenemos para vos.
        # buscar sus respectivos xpath
