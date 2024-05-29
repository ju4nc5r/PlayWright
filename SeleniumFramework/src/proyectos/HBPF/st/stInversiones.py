# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plInversiones import plInversiones
from SeleniumFramework.common_functions import get_msg
from sub import sub


class stInversiones(sub):
    def seleccionarTasasVigentes(self):
        accion = u'Seleccionar botón tasas vigentes'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.cmdButton_tasasVigentes
            self.selectElement(xpath, msgOk, msgFail, to)
        self.verificarPanelTasasVigentes()

    def cerrarTasasVigentes(self):
        accion = u'Seleccionar botón cerrar tasas vigentes'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.cmdButton_cerrar_TasasVigentes
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarVolverAInicio(self):
        accion = u'Seleccionar botón volver'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.cmdButton_Volver_aInicio
            self.selectElement(xpath, msgOk, msgFail, to)

    # Verificar Pantallas
    def verificarPantallaPlazoFijo(self):
        accion = u'Verificar la pantalla detalle de plazo fijo'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.label_titulo_PlazoFijo
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarPantallaDetallePlazoFijo(self):
        """ Metodo para verificar que se muestran los campos del plazo fijo"""
        self.verificarTipoPlazoFijo()
        self.verificarNumeroPlazoFijo()
        self.verificarFechaConstitucion()
        self.verificarFechaVencimiento()
        self.verificarPlazo()
        self.verificarRenovacionAutomatica()
        self.verificarTNA()
        self.verificarTEA()
        self.verificarMontoInicial()
        self.verificarIntereses()
        self.verificarMontoAlVencimiento()

    # Verificar elementos
    def verificarPanelTasasVigentes(self):
        accion = u'Verificar el panel de tasas vigentes'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = plInversiones.label_titulo_TasasVigentes
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def verificarTipoPlazoFijo(self):
        accion = u'Verificar el texto del tipo de plazo fijo'
        with self.step(accion):
            self.checkElement(plInversiones.span_tipoPlazoFijo, accion)

    def verificarNumeroPlazoFijo(self):
        accion = u'Verificar el número de plazo fijo'
        with self.step(accion):
            self.checkElement(plInversiones.sapn_numeroPlazoFijo, accion)

    def verificarFechaConstitucion(self):
        accion = u'Verificar la fecha de constitución'
        with self.step(accion):
            self.checkElement(plInversiones.span_fechaConstitucion, accion)

    def verificarFechaVencimiento(self):
        accion = u'Verificar la fecha del vencimiento'
        with self.step(accion):
            self.checkElement(plInversiones.span_fechaVencimiento, accion)

    def verificarPlazo(self):
        accion = u'Verificar el plazo'
        with self.step(accion):
            self.checkElement(plInversiones.span_plazo, accion)

    def verificarRenovacionAutomatica(self):
        accion = u'Verificar renovación automática'
        with self.step(accion):
            self.checkElement(plInversiones.span_renovacionAutomatica, accion)

    def verificarTNA(self):
        accion = u'Verificar TNA'
        with self.step(accion):
            self.checkElement(plInversiones.span_TNA, accion)

    def verificarTEA(self):
        accion = u'Verificar TEA'
        with self.step(accion):
            self.checkElement(plInversiones.span_TEA, accion)

    def verificarMontoInicial(self):
        accion = u'Verificar monto inicial'
        with self.step(accion):
            self.checkElement(plInversiones.span_montoInicial, accion)

    def verificarIntereses(self):
        accion = u'Verificar intereses a devegar'
        with self.step(accion):
            self.checkElement(plInversiones.span_interesesDevegar, accion)

    def verificarMontoAlVencimiento(self):
        accion = u'Verificar monto al vencimiento'
        with self.step(accion):
            self.checkElement(plInversiones.span_montoAlVencimiento, accion)

    def verificarCuentaDebito(self):
        accion = u'Verificar cuenta débito'
        with self.step(accion):
            self.checkElement(plInversiones.span_cuentaDebito, accion)

    def verificarCuentaAcreditacion(self):
        accion = u'Verificar cuenta acreditación'
        with self.step(accion):
            self.checkElement(plInversiones.span_cuentaAcreditacion, accion)
