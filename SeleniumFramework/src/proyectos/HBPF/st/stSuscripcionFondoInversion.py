# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudFondoInversion import (
    plSolicitudFondoInversion as SFI
)
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.common_functions import get_msg
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudFondoInversion import plSolicitudFondoInversion


class stSuscripcionFondoInversion(menu):
    def seleccionarCuentaComitente(self, cuenta):
        accion = u'Seleccionar cuenta comitente'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SFI.select_cuentaComitente, cuenta)
            self.capture_image(msgOk)

    def seleccionarFondo(self, Fondo):
        listaFondos = [1,2,3,4,5]
        tipoFondo = Fondo
    #Consultar si es necesario que se prueben todos los fondos. 
        for tipoFondo in listaFondos: 
            if tipoFondo == 1: 
                accion = u'Seleccionar opción válida de fondos'
                to = 10
                
                with self.step(accion):
                    xpath = SFI.button_goalpesos_A
                    self.selectElement(xpath, accion , to)

    def seleccionarCuentaDebito(self, index=1):
        accion = u'Seleccionar Cuenta Debito'
        with self.step(accion):
            xpath = SFI.cuentaDebito
            self.go_to_xpath(xpath)
            self.select_by_index(xpath, index)
            self.wait(1)
            self.capture_image(accion)
    
    def seleccionarImporte(self):
        accion = 'Ingresar importe'
        valor = 100
        importe = str(valor)
        to = 2
        # msgOk= accion
        # msgFail = 'No se pudo %s' % msgOk
        xpath = plSolicitudFondoInversion.importe
        with self.step(accion):
            self.write(xpath,importe,to)
            #self.select_by_index(locTransferenciasTerceros.moneda, 0)
            self.capture_image(accion)  
    
    def seleccionarCheck(self):
        accion = 'Seleccionar check'
        msgOk, _ = get_msg(accion)
        xpath = SFI.check_acuerdo
        to = 2
        with self.step(accion):
            self.selectElement(xpath, msgOk,to)
            self.capture_image(accion)
    
    def seleccionarContinuar(self):
        to = 10
        accion = 'Seleccionar Continuar'
        msgOk, _ = get_msg(accion)
        xpath = SFI.continuar
        with self.step(accion):
            self.selectElement(xpath, msgOk, to)
            self.capture_image(accion)
    
    def seleccionarConfirmar(self):
        to = 10
        accion = 'Seleccionar Confirmar'
        msgOk, _ = get_msg(accion)
        xpath = SFI.button_confirmar
        with self.step(accion):
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, to)
            self.capture_image(accion)
         
    # Verificar Pantalla
    def verificarPantallaSolicitud(self):
        self.verificarSelectCuentaComitente()
        self.verificarCancelar()
        self.verificarContinuar()
    #   self.verificarTexto0()
    #   self.verificarTexto1()
    #   self.verificarTexto2()

    def verificarPantallaFondosOpciones(self):
        self.verificarFondos()
        #self.verificarBotonCaracteristica()

    # Verificacion elementos
    def verificarSelectCuentaComitente(self):
        accion = u'Verificar select de cuenta comitente'
        to = 10
        with self.step(accion):
            self.checkElement(SFI.select_cuentaComitente, accion, to)

    def verificarCancelar(self):
        accion = u'Verificar botón cancelar'
        to = 10
        with self.step(accion):
            self.checkElement(SFI.button_cancelar, accion, to)
    
    def verificarContinuar(self):
        accion = u'Verificar botón continuar'
        to = 10
        with self.step(accion):
            self.checkElement(SFI.button_continuar, accion, to)

    def verificarTexto0(self):
        accion = u'Verificar segundo texto'
        to = 10
        with self.step(accion):
            xpath = SFI.span_texto0
            textoEsperado = (
                "De acuerdo a lo establecido en la normativa CNV 917 y a los efectos de tomar conocimiento"
                "de las condiciones necesarias para encontrarse enmarcado dentro de la misma usted podrá"
                "consultar dicha información correspondiente a cada fondos común de inversión en particular"
                "en FondosItau"
            )
            texto = self.get_element_text(xpath)
            if texto == textoEsperado:
                self.checkElement(xpath, accion, to)
            else:
                self.fail_msg('El texto esperado, es diferente')
    
    def verificarTexto1(self):
        accion = u'Verificar primer texto'
        to = 10
        with self.step(accion):
            xpath = SFI.span_texto1
#             textoEsperado = (
#                 "Banco Itaú Argentina es Agente de Custodia de Productos de "
#                 "Inversión Colectiva de Fondos Comunes de Inversión, "
#                 "inscripta en el Registro de CNV bajo número 07."
#             ).decode('utf-8')
            textoEsperado = (
                "Banco Itaú Argentina es Agente de Custodia de Productos de "
                "Inversión Colectiva de Fondos Comunes de Inversión, "
                "inscripta en el Registro de CNV bajo número 07."
            )
            texto = self.get_element_text(xpath)
            if texto == textoEsperado:
                self.checkElement(xpath, accion, to)
            else:
                self.fail_msg('El texto esperado, es diferente')

    def verificarTexto2(self):
        accion = u'Verificar segundo texto'
        to = 10
        with self.step(accion):
            xpath = SFI.span_texto2
#             textoEsperado = (
#                 "AGENTE N° 551 INSCRIPTO ANTE MERCADO ABIERTO ELECTRÓNICO "
#                 "S.A. - ENTIDAD AUTOREGULADA POR LA CNV RESOLUCION N°9934/93."
#             ).decode('utf-8')
#                      NO ES MAS NECESARIO HACER EL .decode('utf-8'
            textoEsperado = (
                "AGENTE N° 551 INSCRIPTO ANTE MERCADO ABIERTO ELECTRÓNICO "
                "S.A. - ENTIDAD AUTOREGULADA POR LA CNV RESOLUCION N°9934/93."
            )
            texto = self.get_element_text(xpath)
            if texto == textoEsperado:
                self.checkElement(xpath, accion, to)
            else:
                self.fail_msg('El texto esperado, es diferente')

    def verificarFondos(self):
        self.verificarFondosLiquidez()
        self.verificarFondosRentaFija()
        self.verificarFondosRentaVariable()
            
    def verificarFondosLiquidez(self):
        accion = u'Verifica fondos de liquidez'
        to = 10
        with self.step(accion):
            self.checkElement(SFI.goal_pesos_A, accion, to)
            self.go_to_xpath(SFI.goal_pesos_A)
    
    def verificarFondosRentaFija(self):
        accion = u'Verificar fondos de renta fija'
        accion2 = u'Verificar que no hay fondos de renta fija'
        to = 10
        xpath = SFI.noHayFondos.format("Renta Fija")
        if self.visibility_element(xpath, to):
            self.checkElement(xpath, accion2, to)
        with self.step(accion):
            self.go_to_xpath(SFI.goal_renta_pesos_clase_A)
            #self.checkElement(SFI.goal_renta_dolar_estrA, accion, to)
            self.checkElement(SFI.goal_renta_dolares_plus, accion, to)
            self.checkElement(SFI.goal_renta_dolares_A, accion, to)
            self.checkElement(SFI.goal_renta_pesos_clase_A, accion, to)
            self.checkElement(SFI.goal_renta_global, accion, to)
    
    def verificarFondosRentaVariable(self):
        accion = u'Verificar fondos de renta variable'
        accion2 = u'Verificar que no hay fondos de renta variable'
        to = 10
        xpath = SFI.noHayFondos.format("Renta Variable")
        if self.visibility_element(xpath, to):
            self.checkElement(xpath, accion2, to)
        
            
    
    def verificarBotonCaracteristica(self):
        accion = u'Verificar botón de característica'
        to = 10
        with self.step(accion):
            xpath = SFI.button_caracteristica
            self.go_to_xpath(xpath)
            self.checkElement(xpath, accion, to)
