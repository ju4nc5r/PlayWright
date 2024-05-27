# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stInicio import stInicio
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaTD import locConsultaTD as TD
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudSeguroTarjeta import plSolicitudSeguro as SS
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plBloqueo import plBloqueo as plB
from SeleniumFramework.common_functions import get_msg


class stConsultaTD(stLogin, stInicio):
    def seleccionarBotonVolver(self):
        accion = u'Seleccionar botón volver'
        to = 10
        with self.step(accion):
            xpath = TD.btn_volver
            self.selectElement(xpath, '', '', to)

    def seleccionarSolicitarSeguro(self):
        accion = u'Seleccionar solicitar seguro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(TD.btn_solicitarSeguro, '', '', to)
            if self.visibility_element(SS.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarBloqueo(self):
        accion = u'Seleccionar botón bloqueo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(TD.btn_bloqueo, '', '', to)
            if self.visibility_element(plB.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Verificacion de pantalla
    def verificarPantallaConsulta(self, seguro):
        """
        Metodo para verificar que se muestre todos los elementos de la
        pantalla de consulta de la tarjeta de debito
        """
        self.verificarNumTarjeta()
        self.verificarNombreApellido()
        self.verificarLimDiario()
        self.verificarSeguroContraRobo()
        self.verificarBotonVolver()
        self.verificarBotonBloqueo()
        self.verificarBotonReposicion()
        self.verificarBotonCuentaExterior()
        self.verificarBotonSolicitarSeguro(seguro)

    # Verificar elementos
    def verificarNumTarjeta(self):
        accion = u'Verificar número de tarjeta'
        to = 10
        with self.step(accion):
            self.checkElement(TD.txt_numTarjeta, accion, to)

    def verificarNombreApellido(self):
        accion = u'Verificar nombre y apellido'
        to = 10
        with self.step(accion):
            self.checkElement(TD.txt_nomApellido, accion, to)

    def verificarLimDiario(self):
        accion = u'Verificar límite diario'
        to = 10
        with self.step(accion):
            self.checkElement(TD.txt_limDiario, accion, to)

    def verificarSeguroContraRobo(self):
        accion = u'Verificar seguro contra robo'
        to = 10
        with self.step(accion):
            self.checkElement(TD.txt_seguroContraRobo, accion, to)

    def verificarBotonVolver(self):
        accion = u'Verificar botón volver'
        to = 10
        with self.step(accion):
            self.checkElement(TD.btn_volver, accion, to)

    def verificarBotonBloqueo(self):
        accion = u'Verificar botón bloqueo'
        to = 10
        with self.step(accion):
            self.checkElement(TD.btn_bloqueo, accion, to)

    def verificarBotonReposicion(self):
        accion = u'Verificar botón reposición'
        to = 10
        with self.step(accion):
            self.checkElement(TD.btn_reposicion, accion, to)

    def verificarBotonCuentaExterior(self):
        accion = u'Verificar botón de cuenta exterior'
        to = 10
        with self.step(accion):
            self.checkElement(TD.btn_cuentaExterior, accion, to)

    def verificarBotonSolicitarSeguro(self, estado_seguro):
        accion = u'Verificar botón en solicitar seguro'
        to = 10
        with self.step(accion):
            texto = self.get_element_text(TD.txt_seguroContraRobo).lower()
            # Si el texto esta en 'NO', no se muestra el boton
            if texto == estado_seguro.lower():
                if texto == 'no':
                    self.checkElement(TD.btn_solicitarSeguro, accion, to)
                else:
                    msg = (
                        u'El seguro esta como SI, por ende no se muestra '
                        u'el elemento'
                    )
                    self.log.warning(msg)
                    self.capture_image(msg)
            else:
                self.fail_msg('No es el estado esperado')
