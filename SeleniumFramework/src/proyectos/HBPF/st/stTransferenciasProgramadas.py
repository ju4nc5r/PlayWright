# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.pasos import Transferencia
from SeleniumFramework.src.proyectos.HBPF.loc.locTransferenciasProgramadas import (
    locTransferenciasProgramadas
)
from SeleniumFramework.src.proyectos.HBPF.constants.tarj_coordenadas import *
from SeleniumFramework.common_functions import get_msg


class stTransferenciasProgramadas(stLogin, menu, Transferencia):


    def seleccionarPeriodoUnicaVez(self):
        to = 10
        accion = "Seleccionar periodo unica vez"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath_select = locTransferenciasProgramadas.periodo_unica_vez
            # xpath_verif = locTransferenciasProgramadas.confirmar
            self.selectElement(xpath_select, msgOk, msgFail, to)
            self.select_by_text(xpath_select, "nica vez")
    
    def seleccionarPeriodoSemanalmente(self):
        to = 10
        accion = "Seleccionar realizar transferencia semanalmente"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath_select = locTransferenciasProgramadas.periodo_semanalmente
            # xpath_verif = locTransferenciasProgramadas.confirmar
            self.selectElement(xpath_select, msgOk, msgFail, to)
            self.select_by_text(xpath_select, "Semanalmente")
    
    def seleccionarPeriodoMensualmente(self):
        to = 10
        accion = "Seleccionar realizar transferencia mensualmente"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath_select = locTransferenciasProgramadas.periodo_mensualmente
            # xpath_verif = locTransferenciasProgramadas.confirmar
            self.selectElement(xpath_select, msgOk, msgFail, to)
            self.select_by_text(xpath_select, "Mensualmente")
    
    def verCalendario(self):
        to = 10
        accion = "Mostrar calendario"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath_select = locTransferenciasProgramadas.calendario
            # xpath_verif = locTransferenciasProgramadas.confirmar
            self.selectElement(xpath_select, msgOk, msgFail, to)
    
    def seleccionarDiaProgramado(self):
        to = 10
        accion = "Seleccionar dia a programar"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        self.verCalendario()
        with self.step(accion):
            xpath_select = locTransferenciasProgramadas.dia_unica_vez
            # xpath_verif = locTransferenciasProgramadas.confirmar
            self.selectElement(xpath_select, msgOk, msgFail, to)
    
    def seleccionarDiaAnterior(self,diaAnterior):
        to = 10
        accion = "Seleccionar dia anterior"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = locTransferenciasProgramadas.input_fecha
            self.write(xpath, diaAnterior, to)
            self.capture_image(msgOk)

    
    def seleccionarTipoTransfer(self):
        to = 10
        accion = "Seleccionar transferencia a otro banco"
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = locTransferenciasProgramadas.trans_otro_banco
            self.selectElement(xpath, msgOk, msgFail, to)
    
    def continuarProgramado(self):
        to = 10
        accion = "Seleccionar transferencia a otro banco"
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = locTransferenciasProgramadas.continuar_programado
            self.selectElement(xpath, msgOk, msgFail, to)
    
    def seleccionarCuentaDebito(self, find_text='0000067'):
        accion = "Seleccionar Cuenta Debito"
        with self.step(accion):
            xpath = locTransferenciasProgramadas.ctaDebito
            self.selectListByPartialText(xpath, find_text)
            self.capture_image(accion)

    def ingresarNumeroCBU(self):
        to = 10
        accion = "Ingresar CBU"
        msgOk = accion
        with self.step(accion):
            xpath = locTransferenciasProgramadas.cbu_no_inmediata
            self.write(xpath, self.CBU, to)
            self.capture_image(msgOk)

    def completarCaractCuentaAcreditacion(self):
        accion = "Seleccionar Caracteristica Cuenta Acreditacion: {}".format(
                                                        self.caracteristica
                                                        )
        msgOk = accion
        with self.step(accion):
            xpath = locTransferenciasProgramadas.caracte_no_inmediata
            self.select_by_text(xpath, self.caracteristica)
            self.capture_image(msgOk)

    def completarCuil(self):
        to = 10
        accion = "Ingresar CUIL"
        msgOK = accion
        with self.step(accion):
            xpath = locTransferenciasProgramadas.cuil_no_inmediata
            self.write(xpath, self.cuil, to)

    def completarConceptoNoInmediato(self):
        accion = "Seleccionar concepto: {}".format(
                                            self.concepto
                                            )
        msgOk = accion
        with self.step(accion):
            xpath = locTransferenciasProgramadas.concepto_no_inmediata
            self.select_by_text(xpath, self.concepto)
            self.capture_image(msgOk)

    def completarImporteNoInmediato(self):
        to = 10
        accion = "Completar Importe"
        msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = locTransferenciasProgramadas.importe_no_inmediata
            self.go_to_xpath(xpath)
            self.write(xpath, self.importe, to)
            self.capture_image(msgOk)

    def seleccionarContinuarNoInmediato(self):
        to = 10
        accion = "Seleccionar Continuar"
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath_select = locTransferenciasProgramadas.continuar_no_inmediata
            # xpath_verif = locTransferenciasProgramadas.confirmar
            self.selectElement(xpath_select, msgOk, msgFail, to)

    # no inmediata

    def finalizar_formulario(self):
        self.completarCoordenadas()
        self.seleccionarContinuarNoInmediato()

    # Verificacion de pantalla
    
    def verificarTitulo(self):
        accion = 'Verificar titulo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.Titulo_programar
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                texto = self.get_element_text(xpath)
            else:
                self.fail_msg('No se muestra el elemento')
            if texto == 'Programar transferencia':
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
    
    def verificarPeriodoTransfer(self):
        accion = 'Verificar input de periodo de tiempo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.select_periodo
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    def verificarCalendario(self):
        accion = 'Verificar calendario'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.calendario
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    def verificarDiasRepeticion(self):
        accion = 'Verificar dias de repeticion'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.dias_repeticiones
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    def verificarInputTransferencias(self):
        accion = 'Verificar input transferencias a otro banco'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.trans_otro_banco
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')

    def verificarTituloCargaDato(self):
        accion = 'Verificar que se encuentre parado en la carga de datos'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.validacion_carga_datos
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    def verificarConfirmacionDato(self):
        accion = 'Verificar que se encuentre parado en la confirmacion'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.validacion_confirmacion
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')
    
    # validar error
    
    def validarCompletarFecha(self,mensaje= None):
        to = 10
        accion = "Mostrar error:" + mensaje
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locTransferenciasProgramadas.validacion_error_dia
            if mensaje is not None:
                texto = self.get_element_text(xpath)
                if mensaje in texto:
                    self.capture_image(msgOk)
                else:
                    self.fail_msg('El mensaje no es el esperado')
            else:
                self.fail_msg('Se muestra mensaje de error')
    
    def validarFechaMayorA(self,mensaje= None):
        accion = "Mostrar error:" + mensaje
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = locTransferenciasProgramadas.validacion_fecha_mayor
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg('No se muestra el elemento')