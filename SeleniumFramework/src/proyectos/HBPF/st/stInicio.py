# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.Inicio import Inicio
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaTD import locConsultaTD
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaTC import locConsultaTC
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plCajaSeguridad import plCajaSeguridad
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plAdmAlerta import plAdmAlert
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaMovimientos import plConsultaMovimientos
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plDetallePrestamo import plDetallePrestamo
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plInversiones import plInversiones
from SeleniumFramework.common_functions import get_msg
from sub import sub


class stInicio(sub):
    def seleccionarCuentaInicio(self, cuenta='301/8'):
        accion = 'Seleccionar una cuenta'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.tbl_Contenedor_Cuentas_xp.format(cuenta)
            self.selectElement(xpath, msgOk, msgFail, to)
            if self.visibility_element(plConsultaMovimientos.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarDisplayInversiones(self):
        accion = 'Desplegar/plegar las inversiones'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Inversiones_despliegue_xp
            if self.selectElement(xpath, msgOk, msgFail, to):
                if self.visibility_element(Inicio.table_inversiones, to):
                    self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarDisplayPrestamos(self):
        accion = 'Desplegar/plegar los prestamos'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Prestamos_despliegue_xp
            if self.selectElement(xpath, msgOk, msgFail, to):
                xpath1 = Inicio.table_prestamos
                xpath2 = Inicio.table_sin_prestamos
                if self.double_visibility_element(xpath1, xpath2, to):
                    self.capture_image(msgOk)
                else:
                    self.capture_image(u'El usuario no posee préstamos')
            else:
                self.fail_msg(msgFail)

    def seleccionarDisplaySeguros(self):
        accion = 'Desplegar/plegar los seguros'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Seguros_despliegue_xp
            if self.selectElement(xpath, msgOk, msgFail, to):
                xpath1 = Inicio.table_seguros
                xpath2 = Inicio.table_sin_seguros
                if self.double_visibility_element(xpath1, xpath2, to):
                    self.capture_image(msgOk)
                else:
                    self.capture_image(u'El usuario no posee seguros')
            else:
                self.fail_msg(msgFail)

    def seleccionarDisplayCajasSeguridad(self):
        accion = 'Desplegar/plegar las cajas de seguridad'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Caja_despliegue_xp
            if self.selectElement(xpath, msgOk, msgFail, to):
                xpath1 = Inicio.table_cajasSeguridad
                xpath2 = Inicio.lbl_Caja_No_Disponible_xp
                if self.double_visibility_element(xpath1, xpath2, to):
                    self.capture_image(msgOk)
                else:
                    self.capture_image(
                        u'El usuario no posee cajas de seguridad'
                    )
            else:
                self.fail_msg(msgFail)

    def plegarCuentas(self):
        accion = 'Plegar el menu cuentas del inicio'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Cuentas_pliegue_xp
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.wait(5)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def plegarTarjetas(self):
        accion = 'Plegar el menu tarjetas del inicio'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Tarjetas_pliegue_xp
            if(self.selectElement(xpath, msgOk, msgFail, to)):
                self.wait(5)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarTarjetaDebito(self, numTarjeta):
        accion = u'Seleccionar tarjeta de débito'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.span_tarjetaDebito.format(numTarjeta)
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(locConsultaTD.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarTarjetaCredito(self, numTarjeta):
        accion = u'Seleccionar tarjeta de crédito'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.span_tarjetaCredito.format(numTarjeta)
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(locConsultaTC.titulo_consultaTC, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCajaSeguridad(self, caja):
        accion = u'Seleccionar caja de seguridad'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.option_cajaSeguridad.format(caja=caja)
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(plCajaSeguridad.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarAdministracionAlerta(self):
        accion = u'Seleccionar administración de alerta'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.option_administracionAlertas
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(plAdmAlert.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarDetallePrestamo(self):
        accion = u'Seleccionar detalle préstamo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plDetallePrestamo.colTable_inicio_prestamo
            self.selectElement(xpath, msgOk, msgFail, to)
            if self.visibility_element(
                    plDetallePrestamo.label_tituloDetallePrestamo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarPrestamo(self, prestamo):
        accion = u'Seleccionar préstamo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = Inicio.span_prestamos.format(prestamo=prestamo)
            self.selectElement(xpath, '', '', to)
            if self.visibility_element(
                    plDetallePrestamo.label_tituloDetallePrestamo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarPlazoFijoInversiones(self, pf):
        accion = u'Seleccionar {} plazo fijo de sección Inversiones'.format(pf)
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.td_plazoFijo.format(pf)
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarFondoComunInversiones(self, fc):
        accion = (
            u'Seleccionar fondo común {} de sección inversiones'.format(fc)
        )
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.td_fondosComunes.format(fc)
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarTitulosYValoresInversiones(self, tyv):
        accion = u'Seleccionar tyv {} de sección inversiones'.format(tyv)
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.td_TitulosValores.format(tyv)
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarPlazoFijoEfectivoInversiones(self, pfe):
        accion = (
            u"""Seleccionar plazo fijo en efectivo {} de seccion
            inversiones""".format(pfe)
        )
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.td_plazoFijo_Efectivo.format(pfe)
            self.selectElement(xpath, msgOk, msgFail, to)

    # Verificar Pantalla
    def verificarPantallaInicio(self):
        accion = u'Verificar pantalla de posición consolidada'
        to = 5
        with self.step(accion):
            msg = 'Verificar Bloque Cuentas'
            xpath1 = Inicio.btn_Cuentas_despliegue
            xpath2 = Inicio.btn_Cuentas_pliegue_xp
            if self.double_visibility_element(xpath1, xpath2, to):
                self.desplegarCuenta()
            self.checkElement(xpath2, msg, to)
            msg = 'Verificar Bloque Tarjetas'
            self.checkElement(Inicio.btn_Tarjetas_pliegue_xp, msg, to)
            msg = 'Verificar Bloque Inversiones'
            self.go_to_xpath(Inicio.btn_Inversiones_despliegue_xp)
            self.checkElement(Inicio.btn_Inversiones_despliegue_xp, msg, to)
            msg = u'Verificar Bloque Préstamos'
            self.checkElement(Inicio.btn_Prestamos_despliegue_xp, msg, to)
            msg = 'Verificar Bloque Seguros'
            self.checkElement(Inicio.btn_Seguros_despliegue_xp, msg, to)
            msg = 'Verificar Bloque Caja de seguridad'
            self.checkElement(Inicio.btn_Caja_despliegue_xp, msg, to)

    def seleccionarVencimientos(self):
        accion = u'Seleccionar botón Vencimientos'
        to = 10
        with self.step(accion):
            xpath = Inicio.btn_Vencimientos
            self.selectElement(xpath, '', '', to)

    def desplegarCuenta(self):
        accion = u'Desplegar bloque cuentas'
        to = 10
        with self.step(accion):
            self.selectElement(Inicio.btn_Cuentas_despliegue, '', '', to)
            self.capture_image(accion, 2)
