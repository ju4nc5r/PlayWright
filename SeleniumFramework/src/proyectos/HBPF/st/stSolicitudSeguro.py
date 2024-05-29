# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plSolicitudSeguro import plSolicitudSeguro as SS
from SeleniumFramework.src.proyectos.HBPF.st.pasos import menu
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.common_functions import get_msg
import os
import pytest
import shutil


class stSolicitudSeguro(menu):
    
    def seleccionar_btn_seccion_seguro(self,seccion):
        to = 10
        accion = u"Dirigirse a la sección " + seccion
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):            
            xpath = SS.btn_seccion_seguro.format(seccion)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def seleccionar_btn_contratar_tipo(self,tipo_seguro):
        to = 10
        accion = u"Seleccionar boton contratar " + tipo_seguro
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):            
            xpath = SS.btn_contratar_tipo_seguro.format(tipo_seguro)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)                   
                    
       
    def solicitarSeguro(self, seguro, plan, medio, cuenta):
#         self.seleccionarSeguro(seguro)
        self.seleccionarPlan(plan)
        self.seleccionarContinuar()
        self.seleccionarMedioDePago(medio)
        if medio == 'Visa' or medio == 'Master':
            self.seleccionarTarjeta(cuenta)
        else:
            self.seleccionarCuenta(cuenta)
        self.seleccionarTerminosYCondiciones()
        self.seleccionarContinuar()
    
    def solicitarSeguroSinPlan(self, seguro, medio, cuenta):
        self.seleccionarSeguro(seguro)
        # self.seleccionarPlan(plan)
#         self.seleccionarContinuar()
        self.seleccionarMedioDePago(medio)
        if medio == 'Visa' or medio == 'Master':
            self.seleccionarTarjeta(cuenta)
        else:
            self.seleccionarCuenta(cuenta)
        self.seleccionarTerminosYCondiciones()
        self.seleccionarContinuar()

    def seleccionarSeguro(self, seguro):
        accion = u'Seleccionar seguro'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SS.select_seguro, seguro)
            self.capture_image(msgOk)
    
    def seleccionarSeguroOk(self, seguro):
        to = 10
        accion = "Seleccionar seguro"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath1 = SS.select_seguro
            self.selectElement(xpath1, msgOk, msgFail, to)
            xpath = SS.btn_seguro_option.format(seguro)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarPlan(self, plan):
        accion = u'Seleccionar tipo de plan'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SS.option_plan.format(plan)
            if self.selectElement(xpath, '', '', to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarMedioDePago(self, medio):
        accion = u'Seleccionar medio de pago'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SS.select_medioPago, medio)
            self.capture_image(msgOk)

    def seleccionarCuenta(self, cuenta):
        accion = u'Seleccionar cuenta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SS.select_cuenta, cuenta)
            self.capture_image(msgOk)

    def seleccionarTerminosYCondiciones(self):
        accion = u'Seleccionar el checkbox de términos y condiciones'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.checkbox_termycond, '', '', to)
            self.capture_image(msgOk)

    def seleccionarTarjeta(self, tarjeta):
        accion = u'Seleccionar tarjeta'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.selectListByPartialText(SS.select_tarjeta, tarjeta)
            self.capture_image(msgOk)

    def seleccionarModificar(self):
        accion = u'Seleccionar el botón modificar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.button_modificar, '', '', to)
            self.capture_image(msgOk)

    def seleccionarCancelar(self):
        accion = u'Seleccionar el botón cancelar'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.button_cancelar, '', '', to)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        accion = u'Seleccionar el botón continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(SS.button_continuar, '', '', to)
            xpath1 = SS.select_medioPago
            xpath2 = SS.span_plan
            xpath3 = SS.div_error
            elem_list = [xpath1, xpath2, xpath3]
            value = self.array_visibility(elem_list, to)
            if value == 0 or value == 1:
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarConfirmar(self):
        accion = 'Seleccionar el boton confirmar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath1 = SS.button_confirmar
            if self.visibility_element(xpath1, to):
                self.selectElement(xpath1, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarIgualTitualar(self):
        accion = u'Seleccionar checkbox de igual al titular'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SS.checkbox_igualTitular
            self.selectElement(xpath, '', '', to)
            self.wait(1)  # Tiempo de espera a que responda la aplicacion
            self.go_to_xpath(xpath)
            self.capture_image(msgOk)

    def ingresarDatosHogar(self, calle, numero, codPostal, localidad,
                           piso=None, dpto=None):
        self.ingresarCalle(calle)
        self.ingresarNumero(numero)
        self.ingresarPiso(piso)
        self.ingresarDpto(dpto)
        self.ingresarCodigoPostal(codPostal)
        self.selectElement(SS.input_calle, '', '')
        self.wait(1)
        self.seleccionarLocalidad(localidad)

    def ingresarCalle(self, calle):
        accion = u'Ingresar calle'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SS.input_calle, calle, to)
            self.capture_image(msgOk)

    def ingresarNumero(self, numero):
        accion = u'Ingresar número de calle'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SS.input_numero, numero, to)
            self.capture_image(msgOk)

    def ingresarPiso(self, piso):
        accion = u'Ingresar piso'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SS.input_piso, piso, to)
            self.capture_image(msgOk)

    def ingresarDpto(self, dpto):
        accion = u'Ingresar departamento'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SS.input_depto, dpto, to)
            self.capture_image(msgOk)

    def ingresarCodigoPostal(self, codPostal):
        accion = u'Ingresar código postal'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            self.write(SS.input_codPostal, codPostal, to)
            self.capture_image(msgOk)

    def seleccionarLocalidad(self, localidad):
        accion = u'Seleccionar localidad'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.select_by_text(SS.select_localidad, localidad)
            self.wait(1)
            self.go_to_xpath(SS.select_localidad)
            self.capture_image(msgOk)

    # Verificacion de pantallas
    def verificarPantallaSolicitudSeguro(self):
        accion = u'Verificar pantalla de solicitud seguro'
        with self.step(accion):
            self.verificarNombre()
            self.verificarNumDocumento()
            self.verificarSelSeguro()
            self.verificarBotonCancelar()

    def verificarPantallaSeleccionSeguro(self):
        accion = u'Verificar pantalla de selección de seguro'
        with self.step(accion):
            self.verificarLineaProducto()
            self.verificarProducto()
            self.verificarTablaPlanes()

    def verificarPantallaConfirmacion(self):
        accion = u'Verificar pantalla de confirmación'
        with self.step(accion):
            self.validar_nombre()
            self.wait(1)
            self.validar_linea_producto()
            self.wait(1)
            self.validar_producto()
            self.wait(1)
            self.verificarPlan()
            self.wait(1)
            self.verificarSumaAsegurada()
            self.wait(1)
            self.verificarCosto()
            self.wait(1)
            self.verificarMedioPago()

    # Verificacion de elementos
    def verificarNombre(self):
        accion = u'Verificar el nombre'
        self.checkElement(SS.span_nombre, accion)

    def verificarNumDocumento(self):
        accion = u'Verificar numero de documento'
        self.checkElement(SS.span_numDoc, accion)

    def verificarSelSeguro(self):
        accion = u'Verificar select de seguro'
        self.checkElement(SS.select_seguro, accion)

    def verificarBotonCancelar(self):
        accion = u'Verificar botón de cancelar'
        self.checkElement(SS.button_cancelar, accion)

    def verificarLineaProducto(self):
        accion = u'Verificar lina de producto'
        self.checkElement(SS.span_lineaProd, accion)

    def verificarProducto(self):
        accion = u'Verificar seguro'
        self.checkElement(SS.span_producto, accion)

    def verificarTablaPlanes(self):
        accion = u'Verificar tabla de planes'
        self.checkElement(SS.table_planes, accion)

    def validar_nombre(self):
        accion = u'Validar elemento campo nombre'
        self.checkElement(SS.span_nombre, accion)

    def validar_linea_producto(self):
        accion = u'Validar elemento campo linea producto'
        self.checkElement(SS.span_lineaProd, accion)

    def validar_producto(self):
        accion = u'Validar elemento campo producto'
        self.checkElement(SS.span_producto, accion)
    
    def verificarPlan(self):
        accion = u'Validar elemento campo plan seleccionado'
#         accion = u'Verificar plan seleccionado'
        self.checkElement(SS.span_plan, accion)

    def verificarSumaAsegurada(self):
        accion = u'Validar elemento campo suma asegurada'
#         accion = u'Verificar suma asegurada'
        self.checkElement(SS.span_sumaAsegurada, accion)

    def verificarCosto(self):
        accion = u'Validar elemento campo costo'
#         accion = u'Verificar costo'
        self.checkElement(SS.span_costo, accion)

    def verificarMedioPago(self):
        accion = u'Validar elemento campo medio de pago'
#         accion = u'Verificar medio de pago'
        self.checkElement(SS.span_medioPago, accion)

    def verificarTablaHogar(self):
        accion = u'Verificar elemento talba datos del hogar asegurado'
        xpath = SS.table_hogarAseguado
        self.go_to_xpath(xpath)
        self.checkElement(xpath, accion)

    def verificarSeguro(self, seguro):
        accion = u'Verificar  elemento campo seguro'
        msgOk, _ = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath = SS.span_seguro.format(seguro)
            self.highlight(xpath, accion)
    
            
    def validar_ticket(self):
        accion = u'Validar elemento Ticket'
        self.checkElement(SS.img_ticket, accion)  
        
    def seleccionar_boton_descargar(self):
        to = 10
        accion = u"Seleccionar boton Descargar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):            
            xpath = SS.btn_descargar()
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def validar_descarga_comprobante(self):       
        to = 10
        accion = u'Validar descarga comprobante'
        msgOk, msgFail = get_msg(accion) 
        with self.step(accion):                       
            self.wait(10) #  se espera descarga
            usuario = os.getlogin()   
            dirFile = "C:/Users/" + str(usuario) + "/Downloads"
            nameFile = "comprobante_alta_seguros.pdf"            
          
            t=0
            while not os.path.isfile(dirFile + "/" + nameFile):
                self.wait(10)
                t=t+10
                print("Wait  :" + str(t))
                if t == 60:
                    pytest.skip(u"El archivo no se descargó")
            self.driver.execute_script("window.open('');")
            self.wait(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(dirFile + "/" + nameFile)
            self.wait(2) 
            self.capture_image(accion, 10)
            self.wait(1)
            self.driver.switch_to.window(self.driver.window_handles[0])           
            self.wait(1)
            os.remove(dirFile + "/" + nameFile)


    def seleccionar_btn_continuar(self):
        accion = u'Seleccionar el boton Continuar'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath1 = SS.button_continuar
            if self.visibility_element(xpath1, to):
                self.selectElement(xpath1, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)               
        pass                
    
    def validar_pagina_posicion_consolidada(self):
        accion = u'Validar estar en posicion consolidada'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):        
            self.checkElement(locLogin.titulo_esperado, accion)
        
        
    def verificar_salto_a_itau_seguros(self):
        accion = u'Verificar salto a https://www.itau.com.ar/seguros/Paginas/seguros-para-tu-patrimonio.aspx'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):  
            self.wait(10)
            self.driver.switch_to.window(self.driver.window_handles[1])        
            self.checkElement(SS.lb_titulo_itau_seguros, accion)
            self.driver.switch_to.window(self.driver.window_handles[0])  
            
    def verificar_salto_a_itau_seguros_negocios(self):
        accion = u'Verificar que se realice el salto de sito ahttps://www.itau.com.ar/Documents/Seguros%20Home%20banking/Manual%20de%20Producto%20Pyme%20Express%20%20Banco%20Itau.pdf'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):  
            self.wait(10)
            self.driver.switch_to.window(self.driver.window_handles[1])        
            self.checkElement(SS.lb_titulo_itau_seguros_negocios, accion)
            self.driver.switch_to.window(self.driver.window_handles[0])        
            
    def verificar_salto_a_itau_seguros_empresa(self):
        accion = u'Verificar que se realice el salto de sito a https://www.itau.com.ar/Documents/Seguros%20Home%20banking/Manual%20de%20Producto%20Pyme%20Express%20%20Banco%20Itau.pdf'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):  
            self.wait(10)
            self.driver.switch_to.window(self.driver.window_handles[1])        
            self.checkElement(SS.pdf_itau_seguros_pyme, accion)
            self.driver.switch_to.window(self.driver.window_handles[0])      
            
    def verificar_salto_a_itau_seguros_consorcios(self):
        accion = u'Verificar que se realice el salto de sito a https://www.itau.com.ar/consorcios/Paginas/default.aspx'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):  
            self.wait(10)
            self.driver.switch_to.window(self.driver.window_handles[1])        
            self.checkElement(SS.lb_titulo_itau_seguros_consorcios, accion)
            self.driver.switch_to.window(self.driver.window_handles[0])              

        
