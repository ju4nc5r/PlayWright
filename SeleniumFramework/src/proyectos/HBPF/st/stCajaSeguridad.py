# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plCajaSeguridad import plCajaSeguridad as CS
from sub import sub


class stCajaSeguridad(sub):
    # verificacion de pantalla
    def verificarPantallaCajaSeguridad(self):
        self.verificarSucursal()
        self.verificarTamano()
        self.verificarVencimiento()
        self.verificarPeriodo()
        self.verificarDebito()

    # Verificacion de elementos
    def verificarSucursal(self):
        accion = u'Verificar Sucursal'
        with self.step(accion):
            self.checkElement(CS.span_sucursal, accion)

    def verificarTamano(self):
        accion = u'Verificar tamaño'
        with self.step(accion):
            self.checkElement(CS.span_tamano, accion)

    def verificarVencimiento(self):
        accion = u'Verificar vencimiento'
        with self.step(accion):
            self.checkElement(CS.span_vencimiento, accion)

    def verificarPeriodo(self):
        accion = u'Verificar periodo'
        with self.step(accion):
            self.checkElement(CS.span_periodo, accion)

    def verificarDebito(self):
        accion = u'Verificar débito'
        with self.step(accion):
            self.checkElement(CS.span_debito, accion)
