# -*- coding: utf-8 -*-
import allure
from SeleniumFramework.sub import sub
from SeleniumFramework.src.proyectos.HBPF.loc.locMenu import locMenu
from SeleniumFramework.src.proyectos.HBPF.loc.locPagoTC import locPagoTC
from SeleniumFramework.src.proyectos.HBPF.loc.locPlazoFijo import locPlazoFijo
from SeleniumFramework.src.proyectos.HBPF.loc.locCompraVenta import locCompraVenta
from SeleniumFramework.src.proyectos.HBPF.loc.locResumenesAnteriores import locResumenesAnteriores
from SeleniumFramework.src.proyectos.HBPF.loc.locTransferenciasOtroBanco import (
    locTransferenciasOtroBanco
)
from SeleniumFramework.src.proyectos.HBPF.loc.locTransferenciasProgramadas import (
    locTransferenciasProgramadas
)
from SeleniumFramework.src.proyectos.HBPF.loc.locUltimosConsumos import locUltimosConsumos
from SeleniumFramework.src.proyectos.HBPF.loc.locTransferenciaTerceros import locTransferenciasTerceros
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaTransferencia import locConsultaTransferencia
from SeleniumFramework.src.proyectos.HBPF.loc.locComprobantes import locComprobantes
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaMovimientos import locConsultaMovimiento
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudChequera import plSolicitudChequera
from SeleniumFramework.src.proyectos.HBPF.loc.locConsultaCBUyAlias import locConsultaCBUyAlias
# from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudSeguroTarjeta import (
#     plSolicitudSeguroTarjeta
# )
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaFondoInversion import (
    plConsutalFondoInversion
)
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudFondoInversion import (
    plSolicitudFondoInversion
)
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plRescate import plRescate
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudSeguro import plSolicitudSeguro
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaTitulo import plConsultaTitulo
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaEcheq import plConsultaEcheq
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plCompraTitulos import plCompraTitulo
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plVentaTitulos import plVentaTitulos
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudPrestamo import plSolicitudPrestamo
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plDetalleUltResumen import plDetalleUltResumen
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plExtracciones import plExtracciones
from SeleniumFramework.src.proyectos.HBPF.constants.tarj_coordenadas import coordenadas, HBPFpin28, tercerCuarto28
from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.utils.settings import url_hb, url_backoffice
from SeleniumFramework.src.proyectos.HBPF.loc.locRecargaCelulares import locRecargaCelulares
from SeleniumFramework.src.proyectos.HBPF.loc.locProxVencimDebAutom import locProxVtosDebAutom
from SeleniumFramework.src.proyectos.HBPF.loc.locResumenDigital import locResumenDigital
from SeleniumFramework.src.proyectos.HBPF.loc import locProxVencimDebAutom
from time import sleep


class abrirNavegador(sub):
    def openHB(self):
        accion = 'Abrir Home Banking'
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        self.paso = 0
        with self.step(accion):
            self.openChrome(url_hb)
            msg = "Open Chrome"
            self.capture_image(msg)

    def openBackOffice(self):
        accion = 'Abrir Back Office'
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        self.paso = 0
        with allure.step(accion):
            self.openChrome(url_backoffice)
            msg = "Open Chrome"
            self.capture_image(msg)

    def recharge_hb(self):
#         accion = 'Volver a abrir la pagina de homeoffice'
        accion = 'Volver a abrir la pagina de homebanking'
        with self.simple_step(accion):
            self.set_url(url_hb)

    def recharge_BO(self):
        accion = 'Volver a abrir Back Office'
        with self.simple_step(accion):
            self.set_url(url_backoffice)


class menu(sub):
    def seleccionarMenuProductos(self):
        to = 10
        accion = "Seleccionar Menu Productos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.menuProductos
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(accion)
    
    def seleccionarMenuInversiones(self):
        to = 10
        accion = "Seleccionar Menu Inversiones"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.menuInversiones
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(accion)
            sleep(3)
    
    def seleccionarMasSoluciones(self):
        to = 10
        accion = "Seleccionar Mas Soluciones"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.masSoluciones
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(accion)
    
    def seleccionarConstitucionDePlazoFijo(self):
        to = 10
        accion = "Seleccionar Constituir en el menú Plazo Fijo"
        self.seleccionarMenuInversiones()
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.subMenuConstituir
            verificar_xpath = locPlazoFijo.titulo_plazoFijo
            self.selectElement(xpath, msgOk, msgFail, to)
            self.verifySelection(verificar_xpath, accion, to)

    def seleccionarConsultaCanjePuntos(self):
        to = 10
        accion = "Seleccionar consulta y canje de puntos"
        self.seleccionarMenuProductos()
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.subMenuConsultaCajePuntos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(accion)


    def seleccionarCompraVenta(self):
        to = 5
        accion = "Seleccionar Constituir"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.subMenuComprarVender
            verificar_xpath = locCompraVenta.titulo_compraVenta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            self.verifySelection(verificar_xpath, accion, to)
    
    def seleccionarMonedaExtranjera(self):
        to = 5
        accion = "Seleccionar Moneda Extranjera"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.subMenuMonedaExtranjera
            #verificar_xpath = locCompraVenta.titulo_compraVenta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            #self.verifySelection(verificar_xpath, accion, to)
            
    def seleccionarDolarMep(self):
        to = 5
        accion = "Seleccionar Dolar Mep"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.subMenuDolarMep
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                sleep(5)
            else:
                self.jsClick(xpath)
    
    def seleccionarComprarMep(self):
        to = 5
        accion = u'Seleccionar botón comprar mep'
        msgOk = u'Se pudo {}'.format(accion.lower())
        msgFail = u'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = locMenu.subMenuComprarDolarMep
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
    
    def seleccionarVenderMep(self):
        to = 5
        accion = u'Seleccionar botón vender mep'
        msgOk = u'Se pudo {}'.format(accion.lower())
        msgFail = u'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = locMenu.subMenuVenderDolarMep
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
                


    def seleccionarUltimosConsumos(self):
        to = 5
        accion = "Seleccionar Ultimos Consumos"
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        with self.step(accion):
            xpath = locMenu.submenuUltimosConsumos
            verificar_xpath = locUltimosConsumos.titulo_ultimosC
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            self.verifySelection(verificar_xpath, accion, to)

    def seleccionarMenuPagos(self):
        to = 10
        accion = u"Seleccionar Menu Pagos"
#         accion = "Seleccionar Menu Productos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.menuPagos
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(accion)

    def seleccionarPagoTC(self, ignorarFalla=False):
        to = 10
        accion = u"Seleccionar Pago de tarjeta de crédito"
#         accion = "Seleccionar Menu Productos"
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuPagos()
        with self.step(accion):
            xpath = locMenu.subMenuPagoTC
            self.selectElement(xpath, msgOk, msgFail, to)
            if(ignorarFalla):
                verificar_xpath = locPagoTC.tituloPagoTC
                self.verifySelection(verificar_xpath, accion, to)

    def seleccionarMenuTransferencias(self):
        to = 10
        accion = "Seleccionar Menu Transferencias"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.menuTransferencias
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(accion)
    
    def seleccionar_a_cuentas_propias(self):
        to = 10
        accion = "Seleccionar a cuentas propias"
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuTransferencias()
        with self.step(accion):
            xpath = locMenu.subMenu_transf_a_cuentas_propias
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            # verificar_xpath = locTransferenciasOtroBanco.Titulo
            # self.verifySelection(verificar_xpath, accion, to)

#     def seleccionar_a_otros_bancos(self):
#         to = 10
#         accion = "Seleccionar a otros bancos"
#         msgOk, msgFail = get_msg(accion)
#         self.seleccionarMenuTransferencias()
#         with self.step(accion):
#             xpath = locMenu.subMenu_transf_a_otros_bcos
#             if self.visibility_element(xpath, to):
#                 self.selectElement(xpath, msgOk, msgFail, to)
#             else:
#                 self.jsClick(xpath)
#             verificar_xpath = locTransferenciasOtroBanco.Titulo
#             self.verifySelection(verificar_xpath, accion, to)

    def seleccionar_a_programadas(self):
        to = 10
        accion = "Seleccionar programar transferencias"
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuTransferencias()
        with self.step(accion):
            xpath = locMenu.subMenu_transf_programadas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            verificar_xpath = locTransferenciasProgramadas.Titulo_programar
            self.verifySelection(verificar_xpath, accion, to)

    def seleccionar_cliente_itau(self):
        to = 10
        accion = 'Seleccionar a Terceros ITAU'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuTransferencias()
        with self.step(accion):
            xpath = locMenu.subMenu_transf_a_cliente_itau
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            self.verifySelection(locTransferenciasTerceros.Titulo, accion, to)

    def seleccionar_a_terceros(self):
        to = 10
        accion = 'Seleccionar a Terceros'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuTransferencias()
        with self.step(accion):
            xpath = locMenu.subMenu_transf_a_terceros
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            # self.verifySelection(locTransferenciasTerceros.Titulo_terceros, accion, to)
    
    def seleccionarAgendaCuentas(self):
        to = 10
        accion = 'Seleccionar agenda de cuentas'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuTransferencias()
        with self.step(accion):
            xpath = locMenu.subMenu_transf_agenda
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)

    def seleccionarMenuConsultaComprobante(self):
        to = 10
        accion = 'Seleccionar la opcion Consulta de comprobante'
        #self.seleccionarMenuServicios()
        with self.step(accion):
            xpath = locMenu.subMenu_consulta_comprobante
            if not self.selectElement(xpath, '', '', to):
                self.jsClick(xpath)
            self.verifySelection(locComprobantes.titulo, accion, to)

    def seleccionarMenuServicios(self):
        accion = 'Posicionar puntero sobre la opcion Servicios'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locMenu.menuServicios
            self.mouse_over_xpath(xpath)
            self.capture_image(msgOk)

    def seleccionarConsultaTransferencia(self):
        accion = ('Seleccionar la opcion de consulta de '
                  'transferencias programadas')
        self.seleccionarMenuTransferencias()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenu_consultaTransferencia
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            self.verifySelection(locConsultaTransferencia.titulo, accion, to)

    def seleccionarConsultarMovimiento(self):
        accion = (u'Seleccionar la opción de consulta de movimientos')
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuConsultarMov
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            self.verifySelection(locConsultaMovimiento.titulo, accion, to)

    def seleccionarSolicitudChequera(self):
        accion = u'Seleccionar solicitud de chequera'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuSoliChequera
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plSolicitudChequera.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarSolicitudSeguro(self):
        accion = u'Seleccionar solicitud de seguro'
        msgOk, msgFail = get_msg(accion)
        to = 10
        self.seleccionarMenuProductos()
        with self.step(accion):
            xpath = locMenu.submenuSoliSeguro
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plSolicitudSeguro.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarConsultarResumenesAnteriores(self):
        accion = u'Seleccionar resumenes anteriores'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuResumenesAnteriores
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(
                        locResumenesAnteriores.tituloAnteriores, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarDetalleTarjetaCredito(self):
        accion = u'Seleccionar ultimo resumen'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenudetalleTarjetaCredito
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            #else:
            #    self.jsClick(xpath)
            #if self.visibility_element(
            #            plDetalleUltResumen.lbl_tituloUltimoResumen, to):
            #    self.capture_image(msgOk)
            #else:
            #    self.fail_msg(msgFail)

    def seleccionarConsultaFondosInversion(self):
        accion = u'Seleccionar consulta de fondos de inversión'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuInversiones()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuConsultaTenencia
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(
                            plConsutalFondoInversion.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarSolicitudFondosInversion(self):
        accion = u'Seleccionar solicitud de fondos de inversión'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuInversiones()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuSolicitudFondos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(
                            plSolicitudFondoInversion.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarRescatar(self):
        accion = u'Seleccionar opción de rescatar fondos comunes de inversión'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuInversiones()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuRescate
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plRescate.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Consulta de ECheq
    def seleccionarConsultaECheq(self):
        accion = u'Seleccionar consulta de cheques electronicos'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuConsultaEcheq
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plConsultaEcheq.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Titulos y acciones
    def seleccionarConsultaTitulosYAcciones(self):
        accion = u'Seleccionar opción de consulta de título y acciones'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuInversiones()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuConsultaTitulos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plConsultaTitulo.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarComprarTitulos(self):
        accion = u'Seleccionar opción para comprar títulos'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuInversiones()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuCompraTitulos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plCompraTitulo.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarVentaTitulos(self):
        accion = u'Seleccionar opción de venta de títulos'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuInversiones()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuVentaTitulos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plVentaTitulos.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # Prestamos
    def seleccionarSolicitudPrestamo(self):
        accion = u'Seleccionar opción de solicitud de préstamo'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuSolicituPrestamo
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plSolicitudPrestamo.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # extracciones
    def seleccionarExtraccionesSinTarjeta(self):
        accion = u'Seleccionar extracciones sin tarjeta'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuNuevaSolicitud
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(plExtracciones.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarNuevasSolicitudes(self):
        accion = u'Seleccionar nuevas solicitudes'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.submenuConsultaSolicitud
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarBlanqueoClaveCajero(self):
        accion = u'Seleccionar blanqueo de clave del cajero automatico'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuBlanqueoClaveCajero
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
        # Consulta de CBU y Alias
    def seleccionarConsultaCBUyAlias(self):
        accion = u'Seleccionar consulta de CBU y alias'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuConsultaCBUyAlias
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(locConsultaCBUyAlias.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

        # Recarga de Celulares
    def seleccionarRecargaCelulares(self):
        accion = u'Seleccionar Recarga de celular'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuPagos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuRecargaCelulares
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(locRecargaCelulares.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

        # Proximos vencimientos debito automatico
    def seleccionarProximosVtosDebAut(self):
        accion = u'Seleccionar Proximos Vencimientos Debito Automatico'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuPagos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuProxVtosDebAut
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(locProxVtosDebAutom.lbTituloProxVtos, to):
                self.highlight(xpath,accion)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
        # Resumen digital
    def seleccionarMenuResumenDigitalCtas(self):
        accion = u'Seleccionar Recarga de celular'
        msgOk, msgFail = get_msg(accion)
        self.seleccionarMenuProductos()
        to = 10
        with self.step(accion):
            xpath = locMenu.subMenuResumenDigitalCtas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, '', '', to)
            else:
                self.jsClick(xpath)
            if self.visibility_element(locResumenDigital.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
class Transferencia(sub):
    def completarCoordenadas(self):
        self.continuar()
#         accion = 'Se ingresa las coordenadas de la tarjeta de coordenadas'
#         with self.step(accion):
#             self.ingresar_coordenadas()
#             self.capture_image(u'Se ingresó las coordenadas y el pin')

    def ingresar_coordenadas(self):
        """ Metodo para el ingresar las coordenadas"""
        to = 10
        accion = 'Ingresar Coordenadas'
        msgOk, msgFail = get_msg(accion)
        xpath = locTransferenciasTerceros.indiceCoordenadas
        if self.visibility_element(xpath, to):
            # Se obtiene los indices que se tienen que ingresar
            cord = [x.text for x in self.search_elements(xpath, to)]
            # Se trata de obtener los valores en los indices que se muestran
            coordenadas = self.obtener_coordenadas(cord)
            # Se escribe el primer valor
            xpath = locTransferenciasTerceros.primeraCoordenada
            self.write(xpath, coordenadas[0], to)
            # Se escribe el segundo valor
            xpath = locTransferenciasTerceros.segundaCoordenada
            self.write(xpath, coordenadas[1], to)
            # Se ingresa el tercer cuarto 
            self.write(locTransferenciasTerceros.fechaVenc, tercerCuarto28, to)
            self.capture_image(accion, 0)
            # Se ingresa el numero de pin
            self.write(locTransferenciasTerceros.clave, HBPFpin28, to)
            self.capture_image(accion, 0)
            xpath = locTransferenciasTerceros.boton_confirmar
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(msgOk)
        else:
            self.fail_msg(msgFail)

    def obtener_coordenadas(self, cord):
        """ Metodo para obtener las coordenadas correspondientes
        :param cord: Array. Coordenadas que se tiene que obtener el valor
        :Return valores: Array. Valores que le corresponde a la
        coordenada buscada
        """
        valores = []  # Se inicializa el array
        for cordenada in cord:
            letra = cordenada[0]  # Se obtiene la letra de la coordenada
            numero = cordenada[1]  # Se obtiene el numero de la coordenada
            # BUsco en el diccionario generado en constants.tarj_coordenadas
            valor = coordenadas[letra][int(numero)-1]
            valores.append(valor)
        return valores

