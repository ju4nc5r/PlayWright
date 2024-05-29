# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.pageLoc.plCajaInicio import plCajaInicio
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.pasos import abrirNavegador
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys

class stICaja(abrirNavegador):
    
    def identificarCliente(self):
#         self.seleccionarIdentificarCliente()
        self.visualizarCuadroIngresoDatosCliente()
        self.mostrarTiposDoc()
        self.seleccionarTipoDoc(self.tipoDoc)
        self.ingresarDocumento(self.documento)
        self.seleccionarIdentificar()
        self.visualizarRecuadroDatosCliente()
        self.seleccionarOperaSinClave() 
#         self.visualizarDatosRegFirma(self.nombreCliente, self.apellidoCliente) 
    
    
 
    def seleccionarIdentificarCliente(self):
        to = 10
        accion = u'Hacer clic en el Botón IDENTIFICAR CLIENTE'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_identificarClients
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

                
    def visualizarCuadroIngresoDatosCliente(self):
        to = 10
        accion = u'Visualizar el recuadro para ingresar los datos del cliente.'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_CuadroIngresoDatosCliente
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
     
     
    def mostrarTiposDoc(self):
        to = 10
        accion = u'Mostrar select tipos documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipoDoc
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
             
             
    def mostrarTiposDoc2(self):
        to = 10
        accion = u'Mostrar select tipos documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipoDocDepositante
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)        
                
                
                
    
    
    def mostrarTiposDoc3(self):
        to = 10
        accion = u'Mostrar select tipos documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipoDoc3
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 

    def mostrarIngresarManualmente (self):
        to = 10
        accion = u'Mostrar '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_selec_manual
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)                

 
 
    
    def seleccionarTipoDoc(self, tipoDoc):
        to = 10
        accion = u'Seleccionar : '  + str (tipoDoc)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_select.format(tipoDoc)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarTipoDoc2(self, TipoDocDepositante = None):
        to = 10
        accion = u'Seleccionar Tipo de Documento: ' + TipoDocDepositante
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_select.format(TipoDocDepositante)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarIngresarmanualmente(self ):
        to = 10
        accion = u'Seleccionar Tipo de Documento: '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_select2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)





    def ingresarDocumento(self, documento):
        to = 10
        accion = u'Ingresar numero de Documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_documento
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, documento, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    
    
    def ingresarNroDocDepositante(self, NroDniDepositante = None):
        to = 10
        accion = u'Ingresar numero de Documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_documento_Depositante
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, NroDniDepositante, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
                
                
    def ingresarNroDocOrdenante(self, NroDniDepositante = None):
        to = 10
        accion = u'Ingresar numero de Documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_documento_Ordenante
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, NroDniDepositante, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

                
    def ingresarNroDocTitular(self, documento):
        to = 10
        accion = u'Ingresar numero de Documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_documento2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, documento, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                


    def ingresarAlias(self,Alias):
        to = 10
        accion = u'Ingresar numero de Documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_Alias
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, Alias, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
                
    

    def seleccionarOperaSinClave(self):
        to = 10
        accion = u"Hacer clic en el Boton SIN CLAVE"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_operaSinClave
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarIdentificar(self):
        to = 10
        accion = u"Hacer clic en el Boton IDENTIFICAR"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_identificar
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
        
    def visualizarRecuadroDatosCliente(self):
        to = 10
        accion = u"Visualizar en pantalla el recuadro de los datos del cliente   "
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cntRecuadroDatosCliente
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)#         
            else:
                self.fail_msg(msgFail)   
                
    def visualizarDatosRegFirma(self, nombre, apellido):
        to = 10
        accion = u"Visualizar en la parte derecha de la pantalla los datos del cliente y firma asociada. "
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpathNomApeRegFirma = plCajaInicio.lblnomyApeRegFirma            
            if self.visibility_element(xpathNomApeRegFirma, to):
                nomApe = self.get_element_text(xpathNomApeRegFirma)            
                if nombre in nomApe and apellido in nomApe:
                    print (u"Se verifico que el nombre y apellido está en el label mostrado")
                    self.highlight(xpathNomApeRegFirma,msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                                
        accion = u"Verificar nro.documento en registro de firmas"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpathNroDocRegFirma = plCajaInicio.lblNroDocRegFirma            
            if self.visibility_element(xpathNroDocRegFirma, to):
                auxDNI = self.get_element_text(xpathNroDocRegFirma)
                if self.tipoDoc == "CUIT" or self.tipoDoc == "CUIL":
                    self.documento = self.documento [3:10]                          
                if self.documento in auxDNI:
                        self.highlight(xpathNroDocRegFirma, msgOk)
                        print (u"se verifico que el nro.documento está en el label mostrado")                        
                 
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)    
                   
        accion = u"Verificar imagen de firma en registro de firmas"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpathImgFirma = plCajaInicio.imgFirmaRegFirma            
            if self.visibility_element(xpathImgFirma, to):                
                    print (u"se verifico imagen firma en registro de firma")
                    self.highlight(xpathImgFirma, msgOk)
            else:
                self.fail_msg(msgFail)
             
    def seleccionarFinalizarIdentificacion(self):
        to = 10
        accion = u'Hacer clic en el Boton FINALIZAR  '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plCajaInicio.btn_FinalizarIdentificacion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
                                 
#     def seleccionarRegFirmaFinalizar(self):
#         to = 10
#         accion = 'Seleccionar Finalizar'
#         msgOk = accion
#         msgFail = 'No se pudo '+ msgOk.lower()
#         with self.step(accion):
#             xpath = plCajaInicio.btnRegFirmaFinalizar
#             if self.visibility_element(xpath, to):
#                 self.selectElement(xpath, msgOk, msgFail, to)
#                 self.capture_image(msgOk)
#             else:
#                 self.fail_msg(msgFail) 
        

    def cerrarIdefClient(self):
        to = 10
        accion = u'Cerrar Identificar Cliente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cerrar
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def minimizarFirma(self):
        to = 10
        accion = u'Minimizar ventana firma'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_minimizedFirma
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def desplazarSideBar(self):
        to = 10
        accion = u'Desplazar Side Bar'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_sidebar
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # botones de side bar
    
    
    
    def seleccionarOperacionesCaja(self):
        to = 10
        accion = u'Seleccionar operaciones de caja'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_operaciones
            if self.jsClick(xpath):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarClientes(self):
        to = 10
        accion = u'Seleccionar clientes'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_clientes
            if self.jsClick(xpath):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    # metodos de moneda extranjera


    def compraventaME(self, tipoOp_ME, moneda, pagTkt):      
        self.seleccionarMonedaExtranjera()
        self.seleccionarCompraVenta()
        self.seleccionarSolapaTipoOpME(tipoOp_ME)      
        self.mostrarTiposDeMoneda()
        self.seleccionarTipoDeMoneda(self.tipoMoneda)
        self.ingresarImporte(self.importe)
        self.mostrarTiposDocMoneda()
        self.seleccionarTipoDeDocMoneda(self.tipoDocMoneda)
        self.ingresarNroDoc(self.cuil)
        self.seleccionarSiguiente()
        self.visualizarDetalles(self.tipoMoneda, tipoOp_ME)
#         self.seleccionarSiguiente2()
        self.seleccionarFinalizar()
#         self.verificarMsjeExitoImpreOK("Impresion OK")
        self.verificarMensajeExito(self.mensaje)
        self.wait(5)
        if tipoOp_ME == u"Compra":
            self.visualizarTicket(pagTkt)
        self.wait(5)            

    def seleccionarMonedaExtranjera(self):
        to = 10
        accion = u'Seleccionar moneda extranjera'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_moneda_extranjera
            # if self.visibility_element(xpath, to):
            self.wait(2)
            self.jsClick(xpath)
            self.capture_image(msgOk)
            # else:
            #     self.fail_msg(msgFail)

    def seleccionarCompraVenta(self):
        to = 10
        accion = u'Seleccionar compra/venta moneda extranjera'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_compra_venta
            # if self.selectElement(xpath, msgOk, msgFail, to):
            self.jsClick(xpath)
            self.capture_image(msgOk)
            # else:
            #     self.fail_msg(msgFail)
            
    def seleccionarSolapaTipoOpME(self, tipoOpME):
        to = 10
        accion = u'Seleccionar Solapa Compra o Venta'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slp_compraventa_Ini + tipoOpME + plCajaInicio.slp_compraventa_Fin
            print (u"Xpath solapa compraventa: " + xpath)
            # if self.visibility_element(xpath, to):
            self.jsClick(xpath)
            self.capture_image(msgOk)
            # else:
            #     self.fail_msg(msgFail)  

    def mostrarTiposDeMoneda(self):
        to = 10
        accion = u'Hacer clic en el recuadro Monedas'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_moneda
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.go_to_xpath(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def mostrarTiposDeMonedaAtm(self):
        to = 10
        accion = u'Hacer clic en el recuadro Monedas'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_moneda3
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                self.jsClick(xpath)
                self.wait(1)
            else:
                self.fail_msg(msgFail)


    def mostrar_tipos_de_moneda_3(self):
        to = 10
        accion = u'Hacer clic en el recuadro Monedas'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_moneda4
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.go_to_xpath(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)




    def seleccionarTipoDeMoneda(self, moneda):
        to = 10
        accion = u'Seleccionar Moneda {} '.format(moneda)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_select.format(moneda)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarImporte(self, importe, moneda):
        to = 10
        accion = u'Ingresar importe '+u" " +u'en '+ moneda
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_importe
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, importe, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def ingresarImporte3(self, importe, moneda):
        to = 60
        accion = u'Ingresar importe '+ str(importe) + u" " + moneda
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_importe3
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, importe, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


                
    def ingresarImporteDepo3ros(self, importe):
        to = 10
        accion = u'Ingresar importe '+ str(importe) 
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_importeDepo3ros
            self.wait(2)
            if  self.write(xpath, importe, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)                
                              
                              
    def ingresarDatosDeCuenta(self, dato):
        to = 10
        accion = u'Ingresar '+ str(dato) 
#         accion = 'Ingresar importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_recuadroComun
#             if self.selectElement(xpath, msgOk, msgFail, to):
            if self.write(xpath, dato, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)      

          
    def ingresarCuenta(self, cuenta):
        to = 10
        accion = u'Ingresar numero de cuenta'+ str(cuenta) 
#         accion = 'Ingresar importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_recuadroComun
#             if self.selectElement(xpath, msgOk, msgFail, to):
            if self.write(xpath, cuenta, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def ingresarCBU(self, cbu):
        to = 10
        accion = u'Ingresar CBU' 
#         accion = 'Ingresar importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_CBU
#             if self.selectElement(xpath, msgOk, msgFail, to):
            if self.write(xpath, cbu, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def ingresarRaiz(self, Raiz):
        to = 10
        accion = u'Ingresar numero de cuenta' 
#         accion = 'Ingresar importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_Raiz
#             if self.selectElement(xpath, msgOk, msgFail, to):
            if self.write(xpath, Raiz, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def ingresarNombreyApellidoDepositante(self,NombreDelDopositante, ApellidoDelDepositante):
        to = 10
        accion = u'Ingresar Nombre y apellido Del Depositante ' 
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_nombreYapellido_Depositante
            if self.write(xpath, NombreDelDopositante  +  ApellidoDelDepositante, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def ingresarNombreyApellidoOrdenante(self,NombreDelDopositante, ApellidoDelDepositante):
        to = 10
        accion = u'Ingresar Nombre y apellido Del Depositante ' 
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_nombreYapellido_ordenante
            if self.write(xpath, NombreDelDopositante + ApellidoDelDepositante, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def mostrarTiposDocMoneda(self):
        to = 10
        accion = u'Mostrar select tipos de documentos'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipoDocMoneda
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarTipoDeDocMoneda(self, documento):
        to = 10
        accion = u'Seleccionar tipo de documento: '.format(documento)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_select.format(documento)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def ingresarNroDoc(self, documento):
        to = 10
        accion = u'Ingresar documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_nroDocMoneda
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, documento, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarSiguiente(self):
        to = 60
        accion = u'Hacer clic en el Boton SIGUIENTE'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_siguiente
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    



    def seleccionarSiguiente3ros(self):
        to = 60
        accion = u'Hacer clic en el Boton SIGUIENTE'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_sigiente_3ros
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def visualizarDatosOperacion(self,importe,cuenta,moneda):
        to = 10
        accion = u'Visualizar los datos de la operación'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.validarCuentaOperacion(cuenta, accion)
            self.wait(1)
            self.validarImporteOperacion(importe,moneda, accion)
            
    def visualizarDatosOperacion2(self,importe,cuenta,moneda):
        to = 10
        accion = u'Visualizar los datos de la operación'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.validarCuentaOperacion(cuenta, accion)
            self.wait(1)
            self.validarImporteOperacion2(importe,moneda, accion) 
            
            
                          
    def visualizarDatosDeposito(self,importe,cuentaDeposito,moneda):
        to = 10
        accion = u'Visualizar datos de Deposito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.validarCuentaDeposito(cuentaDeposito, accion)
            self.wait(1)
            self.validarImporteDeposito(importe,moneda, accion)
   
   
    def visualizarDatosDeposito3ros2(self,importe,cuentaDeposito,moneda):
        to = 10
        accion = u'Visualizar datos de Deposito Terceros'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.validarDatosCuenta(cuentaDeposito, accion)
            self.wait(1)
            self.validarImporteDeposito3ros2(importe,moneda, accion)
            self.validarMonedaDepo3ros(moneda,accion)
   
        
            
    def visualizarDatosDeposito3ros(self,importe,cuentaDeposito,moneda):
        to = 10
        accion = u'Visualizar datos de Deposito Terceros'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.validarDatosCuenta(cuentaDeposito, accion)
            self.wait(1)
            self.validarImporteDeposito3ros(importe,moneda, accion)
            self.validarMonedaDepo3ros(moneda,accion)
           
           
    def validarDetalleDeOperacion(self,cuentaDeposito,moneda,importe):
        to = 10
        accion = u'Validar el detalle de Operación: Cuenta - Moneda - Importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.validarDatosCuenta2(cuentaDeposito, accion)
            self.validarMonedaDepo3ros(moneda,accion)
            self.validarImporteDeposito3ros2(importe,moneda, accion)


    def validarDatosDepositos(self,part,dato):
        to = 30
        accion = u'validar Datos de la Operacion '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_validarDato.format(part)
            if  self.visibility_element(xpath, to):
                datos = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if dato in datos:
                    print(datos)
                    self.highlight(xpath, accion)     
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

                   
    def validarCuentaDeposito(self, cuenta,accion=None):
        to = 10
        accion = u'Validar cuenta de deposito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentadeposito
            if self.visibility_element(xpath, to):
                print(" Cuenta datos " +  cuenta)
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print(input_value)
                if cuenta in input_value:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
 
                 
    def validarDatosCuenta(self, cuenta, accion=None):
        to = 10
        accion = u'Validar los datos de la Cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cuentaDeposito
            if self.visibility_element(xpath, to):
                print(" Cuenta datos " +  str(cuenta))
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print(input_value)
                if cuenta in input_value:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)            


    def validarDatosCuenta2(self, cuenta, accion=None):
        to = 10
        accion = u'Validar los datos de la Cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cuentaDeposito2
            if self.visibility_element(xpath, to):
                print(" Cuenta datos " +  cuenta)
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print(input_value)
                if cuenta in input_value:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)            

  
    def validarDatosCUIL(self,NroDocIdentCliente):
        to = 10
        accion = u'Validar Datos de la  cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cuil
            if self.visibility_element(xpath, to):
                print(" CUIL " +  NroDocIdentCliente)
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print(input_value)
                if NroDocIdentCliente in input_value:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)            
 
    
    def visualizarRecuadroNroDocDepositante(self):
        to = 10
        accion = u'Validar Recuadro numero documento depositante'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_DocDepositante
            if self.visibility_element(xpath, to):
                    self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)            
    
    
    def validarImporteDeposito(self, importe, moneda, accion=None): 
        to = 10
        accion = accion + u" - validar importe"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            simboloMoneda = ""
            if moneda == "pesos":
                simboloMoneda = "$"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "dolares":
                simboloMoneda = "U$S"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "euros":
                simboloMoneda == "EUR"
                print ("simboloMoneda " + simboloMoneda )
            else:
                self.fail_msg("Moneda no definida")     
            xpath = plCajaInicio.ipt_importedeposito.format(simboloMoneda)
            print ("importe dato " + importe)
            if self.visibility_element(xpath, to):              
                importeMostrado = str(self.driver.find_element(by=By.XPATH, value=xpath).get_property('value'))
                print("importe mostrado " + importeMostrado)  
                
                               
                importeAux = str(float(importe)/100).replace(".",",")           
                print("Importe aux " + (importeAux)) 
                if importeAux in importeMostrado:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)    
                
                
    def validarImporteDeposito3ros(self, importe, moneda, accion=None): 
        to = 10
        accion = accion + u" - validar importe"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            simboloMoneda = ""
            if moneda == "pesos":
                simboloMoneda = "$"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Dolares":
                simboloMoneda = "U$S"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Euros":
                simboloMoneda == "EUR"
                print ("simboloMoneda " + simboloMoneda )
            else:
                self.fail_msg("Moneda no definida")     
            xpath = plCajaInicio.lbl_importeDeposito3ros.format(simboloMoneda)
            importeDatoInt = int(importe) 
            print ("importe dato int " + str(importeDatoInt))
            if self.visibility_element(xpath, to):              
#                  importeMostrado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                importeMostrado = str(self.driver.find_element(by=By.XPATH, value=xpath).get_property('value'))
                print("importe mostrado  " +str(importeMostrado))
                importeMostrado = str(importeMostrado)
                importeMostrado = importeMostrado.replace(".","")
                importeMostrado = importeMostrado.replace(",",".")
                importeMostradoFloat = float (importeMostrado)
                importeMostradoInt = int(importeMostradoFloat)   
                importeMostradoInt = (int(float(importeMostrado.replace(".",""))))          
                print("importe mostrado int " + str(importeMostradoInt))                 
#                 importeAux = str(float(importe)/100).replace(".",",")           
#                 print("Importe aux " + (importeAux)) 
#                 if importeAux in importeMostrado:
                if importeMostradoInt == int(importeDatoInt):  
                    self.highlight(xpath, accion)
                                
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)      
     
     
    def validarImporteDeposito3ros2(self, importe, moneda, accion=None): 
        to = 10
        accion = accion + u" - validar importe"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            simboloMoneda = ""
            if moneda == "pesos":
                simboloMoneda = "$"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Dolares":
                simboloMoneda = "U$S"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Euros":
                simboloMoneda == "EUR"
                print ("simboloMoneda " + simboloMoneda )
            else:
                self.fail_msg("Moneda no definida")     
            xpath = plCajaInicio.lbl_importeDeposito3ros.format(simboloMoneda)
            if self.visibility_element(xpath, to):              
                importeMostrado = str(self.driver.find_element(by=By.XPATH, value=xpath).get_property('value'))
                if importeMostrado in importe:
                    self.highlight(xpath, accion)
                                
            else:
                self.fail_msg(msgFail)      
       
          
    def validarMonedaDepo3ros(self , moneda , accion=None):
        to = 10
        accion = u'Validar moneda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_MonedaDepo3ros
            if self.visibility_element(xpath, to):
                print(" Cuenta datos " +  moneda)
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print(input_value)
                if moneda in input_value:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)            
     
          
    def seleccionarSiguiente2(self):
        to = 10
        accion = u'Hacer clic en el Boton SIGUIENTE'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_siguiente_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    
    def seleccionarSiguiente3(self):
        to = 60
        accion = u'Seleccionar siguiente 3'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_siguiente_3
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    
    def seleccionarFinalizar(self):
        to = 10
        accion = u'Seleccionar finalizar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_finalizar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarFinalizar2(self):
        to = 10
        accion = u'Seleccionar finalizar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_FinalizarTrx
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    # certificacion de firma

    def seleccionarCertificacionFirma(self):
        to = 10
        accion = u'Seleccionar certificacion de firma'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_certificacion_firma
            self.jsClick(xpath)
            self.capture_image(msgOk)

#     def ingresarCuenta(self, cuenta):
#         to = 10
#         accion = 'Ingresar cuenta'
#         msgOk = accion
#         msgFail = 'No se pudo '+ msgOk.lower()
#         with self.step(accion):
#             xpath = plCajaInicio.ipt_nroCuenta
#             if self.selectElement(xpath, msgOk, msgFail, to):
#                 xpath=plCajaInicio.mat_nroCuentaIni+self.cuenta+plCajaInicio.mat_nroCuentaFin
#                 self.selectElement(xpath, msgOk, msgFail, to)
# #                 self.write(xpath, cuenta, to)
#                 self.capture_image(msgOk)
#             else: 
#                 self.fail_msg(msgFail)

    
    def seleccionarCuenta(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_nroCuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
 
    
    def seleccionarAceptar(self):
        to = 10
        accion = u'Hacer clic en el Botón ACEPTAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_aceptar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarConfirmarFirma(self):
        to = 20
        accion = u'Tildar el recuadro Confirmar firma'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.chk_confirmar 
            self.wait(1)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
  
            
    def seleccionarBtnAqui(self):
        to = 20
        accion = u'Tildar el recuadro Confirmar firma'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_aqui 
            self.wait(1)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_imprimir_template(self):
        to = 20
        accion = u'Tildar el boton IMPRIMIR TEMPLATE DE FIRMAR'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_template 
            self.wait(1)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                                   
            
    def verificarMensajeExito(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito (Compra) o Transaccion no autorizada (Venta)'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
#             xpath = plCajaInicio.txt_exito
            xpath = plCajaInicio.txt_exito_cpravtaME
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                print ("texto obtenido " + message)
                print ("mensaje esperado " + mensaje)
                if message == mensaje:
                    self.highlight(xpath, accion)
#                     self.capture_image(msgOk)
                    xpath = plCajaInicio.btn_cerrarMjeExito
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
   
    
    def verificarMensajeExitoDeposito(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_exito_deposito.format(mensaje)
            print(xpath+" ################## ")
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                print('mensaje obtenido ' + message)
                print('mensaje Esperado ' + mensaje)               
                if message == mensaje:
                    self.highlight(xpath, accion)
                    xpath = plCajaInicio.btn_cerrarMjeExito_X
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
                
    
    
    def verificarMensajeExitoEgresoIngreso(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_exitoEI.format(mensaje)
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                if message == mensaje:
                    self.highlight(xpath, accion)
                    xpath = plCajaInicio.btn_cerrarMjeExito
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
    
    def verificarMensajeExitoDeposito2(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_exito_deposito2.format(mensaje)
            print(xpath+" ################## ")
            if self.visibility_element(xpath, to):
                msg = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                print('mensaje obtenido ' + msg)
                print('mensaje Esperado ' + mensaje)  
                if msg in mensaje:             
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
    
    def verificarMensajeExitoEgresoIngreso_X(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_exitoEI.format(mensaje)
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                if message == mensaje:
                    self.highlight(xpath, accion)
                    xpath = plCajaInicio.btn_AceptarComun
#                     xpath = plCajaInicio.btn_cerrarMjeExito_X
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
       
    def verificarMensajeExitoExtracciones(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_exito.format(mensaje)
            print(xpath+" ################## ")
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                print('mensaje obtenido ' + message)
                print('mensaje Esperado ' + mensaje)               
                if message == mensaje:
                    self.highlight(xpath, accion)
                    xpath = plCajaInicio.btn_FinalizarTrx
                    accion = u'Hacer clic en boton "FINALIZAR"'
                    self.highlight(xpath,accion )
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
  
    def verificar_exito_tas(self, mensaje):
        to = 30
        accion = u'Verificar mesaje {}'.format(mensaje)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_exito.format(mensaje)
            print(xpath+" ################## ")
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                print('mensaje obtenido ' + message)
                print('mensaje Esperado ' + mensaje)               
                if message == mensaje:
                    self.highlight(xpath, accion)
                    xpath = plCajaInicio.btn_Finalizar_tas
                    accion = u'Hacer clic en boton "FINALIZAR"'
                    self.highlight(xpath,accion )
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

                
    def verificarMsjeExitoImpreOK(self, mensaje):
        to = 30
        accion = u'Verificar y cerrar mensaje Impresion OK'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_ImpresionOK
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                if message == mensaje:
                    self.highlight(xpath, "Impresion OK")
                    self.capture_image(msgOk)
                    xpath = plCajaInicio.btn_cerrarMjeImpresionOK
                    if self.visibility_element(xpath, to):
                        self.go_to_xpath(xpath)
                        time.sleep(2)
                        self.selectElement(xpath, msgOk, msgFail, to)                        
                        self.jsClick(xpath)
# 
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def CerrarDialogoImpresion(self):
        to = 30
        accion = u'Cerrar dialogo Impresion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.wait(5)
            self.capture_image(msgOk)
            self.driver.execute_script("window.print=function(){};")      
#             self.send_key(xpath, key)
#             xpath = plCajaInicio.txt_ImpresionOK
#             if self.visibility_element(xpath, to):
#                 message = self.get_element_text(xpath)
#                 if message == mensaje:
#                     self.highlight(xpath, "Impresion OK")
#                     self.capture_image(msgOk)
#                     xpath = plCajaInicio.btn_cerrarMjeImpresionOK
#                     if self.visibility_element(xpath, to):
#                         self.go_to_xpath(xpath)
#                         time.sleep(2)
#                         self.selectElement(xpath, msgOk, msgFail, to)                        
#                         self.jsClick(xpath)
# # 
#                 else:
#                     self.fail_msg(msgFail)
#             else:
#                 self.fail_msg(msgFail)

  
    def visualizarDetallesExt(self, moneda, tipoOpMe):
        self.verificar
        self.validarCuentaDeposito(self.cuenta)

    
    def visualizarDetalles(self, moneda, tipoOpMe):
#         self.validarMoneda(moneda)
        self.validarImporte(moneda)
#         self.validarImporte()
#         self.visualizarCotizacionPizarra(tipoOpMe)
        self.visualizarCotizacionAplicada()
        self.validarImporteEnPesos(tipoOpMe)
        self.validarNumeroIdentifTributaria()

    
    def validarMoneda(self, moneda):
        to = 30
        accion = u'Validar moneda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_moneda
            print("--------------")
            print(moneda)
            print("--------------")
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print("--------------")
                print (input_value)
                print("--------------")
                if input_value == moneda:
                    self.highlight(xpath, "Moneda")
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    
    def validarImporte(self, moneda):
        to = 10
        accion = u'Validar el importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_importeCpraVta
#             xpath = plCajaInicio.ipt_importe2           
            aux_importe = self.importe[:-2]  + "," + self.importe[-2:]          
            print("----Importe getdatos----------")
            print(aux_importe)
            print("--------------")
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print("-----Importe ingresado mostrado ---------")
                print (input_value)
                print("--------------")
                if moneda == "Reales":
                    input_value = input_value[3:]
                else:
                    input_value = input_value[4:]
                print("-----Importe ingresado mostrado reformateado ---------")
                print (input_value)
                print("--------------")
                if input_value == aux_importe:
                    self.highlight(xpath, accion)
#                     self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
       
    def visualizarCotizacionPizarra(self,tipoOpMe):
        to = 10
        accion = u'Visualizar cotizacion ' + tipoOpMe
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            if self.tipoOpME == "Compra":
                xpath = plCajaInicio.txt_CotizComprador
            elif self.tipoOpME == "Venta":
                xpath = plCajaInicio.txt_CotizVendedor
            else: 
                self.fail_msg("No esta definido el tipo de operacion")
            if self.visibility_element(xpath, to): 
                self.highlight(xpath, "Cotizacion Pizarra")
                self.capture_image(msgOk)
            else:
                msgFail(msgFail)


    def visualizarCotizacionAplicada(self):
        to = 10
        accion = u'Visualizar cotizacion'
#         accion = 'Visualizar cotizacion aplicada'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.txt_Cotizacion
#             xpath = plCajaInicio.txt_CotizAplicada
            if self.visibility_element(xpath, to): 
                self.highlight(xpath,accion)
#                 self.highlight(xpath, "CotizaciÃ³n Aplicada")
#                 self.capture_image(msgOk)
            else:
                msgFail(msgFail)


    def visualizarCotizacionAplicadaExt(self):
        to = 10
        accion = u'Visualizar cotizacion'
#         accion = 'Visualizar cotizacion aplicada'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.txt_CotizAplicada
#             xpath = plCajaInicio.txt_CotizAplicada
            if self.visibility_element(xpath, to): 
                self.highlight(xpath,accion)
#                 self.highlight(xpath, "CotizaciÃ³n Aplicada")
#                 self.capture_image(msgOk)
            else:
                msgFail(msgFail)


    def validarImporteEnPesosExt(self,tipoOpME):
        to = 10
        accion = u'Validar el importe en Pesos'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):                        
            ImportePesosCalculado = self.calcularImportePesos() 
            print("----Valor importe en pesos calculado----------")
            print(ImportePesosCalculado)
            print("--------------")
            
#             print (self.tipoOpME)

#             if self.tipoOpME == "Compra":
#                 xpath = plCajaInicio.txt_importeEnPesosCompra
#             elif self.tipoOpME == "Venta":
#                 xpath = plCajaInicio.txt_importeEnPesosVenta
#             else: 
#                 self.fail_msg("No esta definido el tipo de operacion")
            xpath = plCajaInicio.txt_importeEnPesos
            if self.visibility_element(xpath, to):
                txt_importePesos = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if txt_importePesos[-2:-1] == ",":
                    txt_importePesos =  txt_importePesos[-17:-14] + txt_importePesos[-13:-10] + txt_importePesos[-9:-6]\
                     + txt_importePesos[-5:-2]  + "." + txt_importePesos[-1:]
                elif txt_importePesos[-3:-2] == ",":                     
                    txt_importePesos =  txt_importePesos[-18:-15] + txt_importePesos[-14:-11] + txt_importePesos[-10:-7]\
                     + txt_importePesos[-6:-3]  + "." + txt_importePesos[-2:]
                print("------txt importe en pesos mostrado--------")
                print (txt_importePesos)
                print("--------------")     
                val_txt_importePesos = float(txt_importePesos.replace("$","",1))
                print("------Valor importe en pesos mostrado--------")
                print (val_txt_importePesos)
                print("--------------")
                if ImportePesosCalculado == val_txt_importePesos:
                    self.highlight(xpath, "Importe en pesos")
#                     self.capture_image(msgOk)
                else:
                    self.fail_msg("Importe en pesos calculado no coincide con el mostrado")
            else:
                self.fail_msg(msgFail)


    def validarImporteEnPesos(self,tipoOpME):
        to = 10
        accion = u'Validar el importe en Pesos'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):                        
            ImportePesosCalculado = self.calcularImportePesos() 
            print("----Valor importe en pesos calculado----------")
            print(ImportePesosCalculado)
            print("--------------")
            
#             print (self.tipoOpME)
#             if self.tipoOpME == "Compra":
#                 xpath = plCajaInicio.txt_importeEnPesosCompra
#             elif self.tipoOpME == "Venta":
#                 xpath = plCajaInicio.txt_importeEnPesosVenta
#             else: 
#                 self.fail_msg("No esta definido el tipo de operacion")
            xpath = plCajaInicio.txt_importeEnPesos
            if self.visibility_element(xpath, to):
                txt_importePesos = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if txt_importePesos[-2:-1] == ",":
                    txt_importePesos =  txt_importePesos[-17:-14] + txt_importePesos[-13:-10] + txt_importePesos[-9:-6]\
                     + txt_importePesos[-5:-2]  + "." + txt_importePesos[-1:]
                elif txt_importePesos[-3:-2] == ",":                     
                    txt_importePesos =  txt_importePesos[-18:-15] + txt_importePesos[-14:-11] + txt_importePesos[-10:-7]\
                     + txt_importePesos[-6:-3]  + "." + txt_importePesos[-2:]
                print("------txt importe en pesos mostrado--------")
                print (txt_importePesos)
                print("--------------")     
                val_txt_importePesos = float(txt_importePesos.replace("$","",1))
                print("------Valor importe en pesos mostrado--------")
                print (val_txt_importePesos)
                print("--------------")
                if ImportePesosCalculado == val_txt_importePesos:
                    self.highlight(xpath, "Importe en pesos")
#                     self.capture_image(msgOk)
                else:
                    self.fail_msg("Importe en pesos calculado no coincide con el mostrado")
            else:
                self.fail_msg(msgFail)


    def calcularImportePesos(self):
        to = 10
        accion = u'Calcular importe en Pesos'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        
        xpath = plCajaInicio.txt_CotizAplicada
        cotizAplicada = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
        print ("Cotizacion Aplicada " + cotizAplicada)
        if cotizAplicada[-2:-1] == ",":
            cotizAplicada = cotizAplicada = cotizAplicada[:-2] + "." + cotizAplicada[-1:]
        elif cotizAplicada[-3:-2] == ",":
            cotizAplicada = cotizAplicada = cotizAplicada[:-3] + "." + cotizAplicada[-2:]
        elif cotizAplicada[-4:-3] == ",":
            cotizAplicada = cotizAplicada = cotizAplicada[:-4] + "." + cotizAplicada[-3:]
        else:     
            self.fail_msg("Cotizacion aplicada tiene mas de tres decimales")
        print ("Cotizacion aplicada formateado " + cotizAplicada)
        cotizAplicada = cotizAplicada.replace("$",'',1)   
#         val_CotizAplicada = round(float(cotizAplicada),2)
        val_CotizAplicada = round(float(cotizAplicada),3)
        print("---Cotiz.Aplicada-----------")
        print (val_CotizAplicada)
        print("--------------")
        val_importe = int(self.importe)/100
        val_importePesos = val_CotizAplicada * val_importe        
        return round((val_importePesos),2)
#         return(val_importePesos)        
    
       
    def validarNumeroIdentifTributariaExt(self):
        to = 30
        accion = u'Validar Numero Identificación tributaria'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            
            xpath = plCajaInicio.lbl_NroIdentifTributaria
            print("------------------------------------------------------------")
            print ("numero identificacion tributaria - datos " + self.cuil)
            print("-----------------------------------------------------------")       
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print("-----------------------------------------------------------")
                print ("numero identificacion tributaria en pantalla " + input_value)
                print("----------------------------------------------------------")
                if input_value == self.cuil:
                    self.highlight(xpath,"Numero Identificación tributaria")                  
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
  
    def validarNumeroIdentifTributaria(self):
        to = 30
        accion = u'Validar Numero Identificación tributaria'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):        
            xpath = plCajaInicio.lbl_NroIdentifTributaria
            print("------------------------------------------------------------")
            print ("numero identificacion tributaria - datos " + self.cuil)
            print("-----------------------------------------------------------")       
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print("-----------------------------------------------------------")
                print ("numero identificacion tributaria en pantalla " + input_value)
                print("----------------------------------------------------------")
                if input_value == self.cuil:
                    self.highlight(xpath,"Numero Identificación tributaria")                  
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)










                
    # Cotizacion Vendedor - 
    # Cotizacion Aplicada -  
    # Importe en Pesos de la Venta 

    # metodos de moneda extranjera


    # extracciones

    def seleccionarExtracciones(self):
        to = 10
        accion = u'Seleccionar extracciones'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_extracciones
            self.jsClick(xpath)
            self.capture_image(msgOk)
            


    def reverso(self,nro):
        self.seleccionarRevesoDeTrasaccion()
        self.ventana_saldo_excedido_en_caja_o_caf() 
        self.ingresarNroTranssaccion(nro)
        self.mostrarTiposDeMotivos()
        self.seleccionarMotivo("Error Carga Cajero")
        self.seleccionarConfirmar()
        self.obtenerNroDeAutorizacion()
        self.validarBotonAutorizacionesSolicitadas()
        self.autorizarOperacionPg()
        self.seleccionarAceptarAutoriz()         
            
    def Extraxiones(self):
        self.seleccionarExtracciones()
        self.ventana_saldo_excedido_en_caja_o_caf()
        self.identificarCliente() 
        self.seleccionarCuentaExtraccion("CA")
        self.mostrarTiposDeMoneda()
        self.seleccionarTipoDeMoneda("Pesos")
        self.ingresarImporte(self.importe,"Pesos")
        self.seleccionarSiguiente()                    
        self.seleccionarConfirmarFirma()
        self.seleccionarSiguiente2()
        self.seleccionarConfirmar() 
        self.obtenerNroDeAutorizacion()
        self.validarBotonAutorizacionesSolicitadas()
        self.autorizarOperacionPg()
        self.seleccionarAceptarAutoriz()

    def ExtraxionesSucursal_50(self):
        self.seleccionarExtracciones()
        self.identificarCliente() 
        self.seleccionarCuentaExtraccion("CA")
        self.mostrarTiposDeMoneda()
        self.seleccionarTipoDeMoneda("Pesos")
        self.ingresarImporte(self.importe,"Pesos")
        self.seleccionarSiguiente()                    
        self.seleccionarConfirmarFirma()
        self.seleccionarSiguiente2()
        self.seleccionarConfirmar() 
        self.obtenerNroDeAutorizacion()
        self.validarBotonAutorizacionesSolicitadas()
        self.autorizarOperacionSucursal50()
        self.seleccionarAceptarAutoriz()
            
    # def ingresarCuenta(self, cuenta):
    #     to = 10
    #     accion = 'Ingresar cuenta'
    #     msgOk = accion
    #     msgFail = 'No se pudo '+ msgOk.lower()
    #     with self.step(accion):
    #         xpath = plCajaInicio.ipt_cuentaCliente
    #         if self.selectElement(xpath, msgOk, msgFail, to):
    #             self.write(xpath, cuenta, to)
    #             self.capture_image(msgOk)
    #         else: 
    #             self.fail_msg(msgFail)
    
    def seleccionarCuentaExtraccion(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentaCliente
            self.jsClick(xpath)
            xpath = plCajaInicio.opt_nroCuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarConfirmar(self):
        to = 10
        accion = u'Hacer clic en el Boton CONFIRMAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_confirmar2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_salir(self):
        to = 10
        accion = u'Hacer clic en el Boton salir'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_salir
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)


    # extracciones

    #depositos
    
    def seleccionarDepositoCliente(self):
        to = 30
        accion = u'Hacer clic en la transacción Depósito de Cliente'
#         accion = 'Seleccionar deposito efectivo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_efectivo
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to): 
                self.selectElement(xpath, msgOk, msgFail, to)
#                 self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
  
    def buscarTransaccion(self,transaccion):
        to = 30
        accion = u'Hacer Buscar transaccion por buscador{}'.format(transaccion)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_transaccion
            if self.visibility_element(xpath, to):
                self.write(xpath, transaccion, to) 
                self.clickEnter()
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
        
        
                       
    def seleccionarDepositoTerceros(self):
        to = 10
        accion = u'Hacer clic en la transacción Depósito de Cliente'
#         accion = 'Seleccionar deposito efectivo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_tercero
            self.jsClick(xpath)
            self.capture_image(msgOk)
   
    
    def seleccionarRecuadroCuentasCliente(self):               
        to = 30
        accion = u'Hacer clic en el recuadro Cuentas Cliente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_cliente
            self.jsClick(xpath)
            self.capture_image(msgOk)
  
  
    def seleccionarRecuadroCuentasFirmas(self):               
        to = 10
        accion = u'Hacer clic en el recuadro cuentas'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cuenta_firma
            self.jsClick(xpath)
            self.capture_image(msgOk)

            
    def seleccionarRecuadro(self):               
        to = 10
        accion = u'Hacer clic en el recuadro Cuentas Cliente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_recuadroComun
            self.jsClick(xpath)
            self.capture_image(msgOk)
   
            
    def clickRadioBtn(self,descripcionBoton):               
        to = 10
        accion = u'Hacer clic en el recuadro Cuentas Cliente'.format(descripcionBoton)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_RadioBtn.format(descripcionBoton)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)  
            else:                
                self.fail_msg(msgFail)


    def clickRadioBtn2(self,Datos_Boton):               
        to = 10
        accion = u'Hacer clic en el recuadro Cuentas Cliente'.format(Datos_Boton)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_RadioBtn.format(Datos_Boton)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)  
            else:                
                self.fail_msg(msgFail)


    def seleccionarTiposDeDocumentos(self,documento):               
        to = 10
        accion = u'Hacer clic en el documento: '.format(documento)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_RadioBtn.format(documento)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)  
            else:                
                self.fail_msg(msgFail)
                
    def ingresarDatosDeCuentas(self,part,Dato):
        to = 10
        accion = u'Ingresar Dato de cuenta:'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_datos_comun.format(part)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, Dato, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)



    def seleccionarCuentaDeposito(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta: {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentaClienteDeposito
            self.jsClick(xpath)
            xpath = plCajaInicio.opt_nroCuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarCuenta3ros(self, cuenta):
        to = 30
        accion = u'Hacer clic en Cuenta Cliente y Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuenta_terceros
            self.wait(2)
            self.jsClick(xpath)
            xpath = plCajaInicio.opt_nroCuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarCuentaFirmas(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentadeposito
            self.jsClick(xpath)
            xpath = plCajaInicio.opt_cuentaFirma.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def seleccionarCuentaRaiz(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentadeposito
            self.jsClick(xpath)
            xpath = plCajaInicio.opt_cuentaFirma.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def mostrarTiposDeMonedaDeposito(self):
        to = 10
        accion = u'Mostrar select tipos de moneda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_monedaDeposito
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def ingresarImporteDeposito(self, importe):
        to = 10
        accion = u'Ingresar importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_valorDeposito
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, importe, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarContinuar(self):
        to = 10
        accion = u'Seleccionar continuar'
        msgOk = accion
        msgFail = u'No se pudo'+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_continuar
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def validarCuentaOperacion(self, cuenta, accion=None):
        to = 10        
        msgOk = accion + u" - validar cuenta"
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_NroDeCuenta.format(cuenta)
            print ("cuenta dato " + cuenta)
            if self.visibility_element(xpath, to):
                cuentaMostrada = str(self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent'))
                print("cuenta mostrada" + str(cuentaMostrada))
                if cuenta in cuentaMostrada:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

                
    def validarImporteOperacion(self, importe, moneda, accion=None): 
        to = 10
        accion = accion + u" - validar importe"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            simboloMoneda = ""
            if moneda == "Pesos":
                simboloMoneda = "$"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Dolares":
                simboloMoneda = "U$S"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Euros":
                simboloMoneda == "EUR"
                print ("simboloMoneda " + simboloMoneda )
            else:
                self.fail_msg("Moneda no definida")     
            xpath = plCajaInicio.lbl_Importe.format(simboloMoneda)
            print ("importe dato " + importe)
            if self.visibility_element(xpath, to):              
                importeMostrado = str(self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent'))
                print("importe mostrado " + importeMostrado)                 
                importeAux = str(float(importe)/100).replace(".",",")
                #Se agrega if para manejar las centenas  
                print ("float de importe:", float(importe))    
                
#               if float(importe) > 99.99 and float(importe) < 1000 :
#                     print ("float de importe cuando entra por  > 99.99 and < 1000:", float(importe))    
#                     importeAux = importeAux[:-4] + '.' + importeAux[-4:]                         
#               Se agrega if para poner el punto de los a cifras de miles
                if float(importe) > 99999.99999 and float(importe) < 100000000:   
                    print ("float de importe cuando entra por > 999.99 and float(importe) < 1000000:", float(importe)) 
                    importeAux = importeAux[:-5] + '.' + importeAux[-5:]
                    print("Importe aux " + (importeAux)) 
                    print ("------------------------------------------------------------------------")   
                if float(importe) > 999999.99 and float(importe) < 1000000000 :
                    importeAux = importeAux[:-5] + '.' + importeAux[-5:]   
                    importeAux = importeAux[:-9] + '.' + importeAux[-9:] 
                    print("Importe aux " + (importeAux))
                    print ("float de importe cuando entra por > 999999.99 and float(importe) < 1000000000:", float(importe))  
                    print ("------------------------------------------------------------------------") 
                           
                print("Importe aux " + (importeAux)) 
                if importeAux in importeMostrado:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
    def validarImporteOperacion2(self, importe, moneda, accion=None): 
        to = 10
        accion = accion + u" - validar importe"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            simboloMoneda = ""
            if moneda == "Pesos":
                simboloMoneda = "$"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Dolares":
                simboloMoneda = "U$S"
                print ("simboloMoneda " + simboloMoneda )
            elif moneda == "Euros":
                simboloMoneda == "EUR"
                print ("simboloMoneda " + simboloMoneda )
            else:
                self.fail_msg("Moneda no definida")     
                xpath = plCajaInicio.lbl_Importe.format(simboloMoneda)
                if self.visibility_element(xpath, to):
                    self.highlight(xpath, accion)
                

                
    def validarImporteIngresado(self, importe, accion=None):
        to = 10
        accion = accion + u"- validar importe"
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_Importe
            if self.visibility_element(xpath, to):
                print("importe dato" + importe)
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print("importe mostrado " + input_value)
                if importe in input_value:
#                 if input_value == importe:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def mostrarCuentas(self):
        to = 10
        accion = u'Hacer clic en el Cuentas'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_cuenta
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.go_to_xpath(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def mostrarCuentas2(self):
        to = 10
        accion = u'Hacer clic en el Cuentas'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_cuenta2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.go_to_xpath(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)




    #depositos

    # ingreso/egreso
    
    def seleccionarSolapaIngresoInternoNumerario(self):
        to = 10
        accion = u'Hacer clic en la opción Ingreso Interno del Numerario'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ingreso
            self.jsClick(xpath)
            self.capture_image(msgOk)
    
            
    def seleccionarSolapaIngresoExternoNumerario(self):
            to = 10
            accion = u'Seleccionar Solapa Ingreso Exerno del Numerario'
            msgOk = accion
            msgFail = u'No se pudo ' + msgOk.lower()
            with self.step(accion):
                xpath = plCajaInicio.slp_ingresoExtNumerario
                if self.visibility_element(xpath, to):
                    self.go_to_xpath(xpath)
                    self.jsClick(xpath)
                    self.capture_image(msgOk) 
                else: 
                    self.fail_msg(msgFail)
                 
                
    def seleccionarSolapaEgresoExternodelNumerario(self):
            to = 10
            accion = u'Seleccionar Solapa Ingreso Exerno del Numerario'
            msgOk = accion
            msgFail = u'No se pudo ' + msgOk.lower()
            with self.step(accion):
                xpath = plCajaInicio.slp_EgresoExtNumerio
                if self.visibility_element(xpath, to):
                    self.go_to_xpath(xpath)
                    self.jsClick(xpath)
                    self.capture_image(msgOk) 
                else:
                    self.fail_msg(msgFail)                
                          
           
    def ingresarNumeroControl(self, control):
        to = 10
        accion = u'Hacer clic en Numero de Control e Ingresar en numero control: ' + control
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_nrocontrol
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, control, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)                
  
                
    def ingresarNumeroControlEgr(self, control):
        to = 10
        accion = u'Hacer clic en Numero de Control e Ingresar en numero control: ' + control
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.Nrocontrol = control
            xpath = plCajaInicio.ipt_nrocontrolEgr
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, control, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def ingresarValor(self, valor):
        to = 10
        accion = u'Ingresar valor ' + valor
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        self.Monto = valor
        with self.step(accion):
            xpath = plCajaInicio.ipt_valor
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, valor, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
  
                  
    def validarSucursalOrigenIngr(self, sucursal):
        to = 10
        accion = u'11-Validar que la que sea la Sucursal de Origen'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_sucuorigen
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
                
    def validarSucursalOrigenEgr(self, sucursal):
        to = 10
        accion = u'Validar que la que sea la Sucursal de Origen ' + sucursal
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.sucursalOrg = sucursal
            xpath = plCajaInicio.ipt_sucuorigenEgr
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
            

    def validarSucursalDestinoIngr(self, sucursal):
        to = 10
        accion = u'Validar que la Sucursal Destino'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_sucudestino
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
  
    
    def validarSucursalDestinoEgr(self, sucursal):
        to = 10
        accion = u'Validar que la Sucursal Destino ' + sucursal
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.sucursalDtn = sucursal
            xpath = plCajaInicio.ipt_sucudestinoEgr
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
  

    def seleccionarMnuIngresoEgresoExterno(self):
        to = 10
        accion = u'-Hacer clic en la transacción "Ingreso/Egreso Externo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ingreso_egreso 
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
 
    def seleccionarSolapaEgresoExterno(self):
        to = 10
        accion = u'Seleccionar solapa egreso'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion): 
            xpath = plCajaInicio.slp_egreso_externo
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
                
    def mostrarTiposDeMonedaEgreso(self):
        to = 10
        accion = u'Mostrar select tipos de moneda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_monedaE
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def validarSucursalOrigenE(self, sucursal):
        to = 10
        accion = u'Validar sucursal de origen'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_sucuOrigenE
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
  
    
    def validarSucursalDestinoE(self, sucursal):
        to = 10
        accion = u'Validar sucursal de destino'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_sucuDestinoE
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def ingresarNroControlE(self, numero):
        to = 10
        accion = u'Ingresar nro de control'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_nroControlE
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, numero, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
    
    
    def ingresarValorE(self, valor):
        to = 10
        accion = u'Ingresar valor de egreso'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_valorE
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, valor, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)



    # botones de side bar
    
    
    
    
    #Ingreso Egreso Interno 
    
    def seleccionarMnuIngresoEgreso(self):
        to = 10
        accion = u'Seleccionar menu ingreso/egreso interno'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.mnu_Ingreso_Egreso_Interno
            self.jsClick(xpath)
            self.capture_image(msgOk)
            
            
    def seleccionarIngresoInternoNumerario(self):
        to = 10
        accion = u'Seleccionar solapa ingreso Interno Del Numerario'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slp_Ingreso_Interno_Del_Numerario
            self.jsClick(xpath)
            self.capture_image(msgOk)
       
    
    def seleccionarEgresoInternoNumerario(self):
        to = 10
        accion = u'Seleccionar solapa ingreso Interno Del Numerario'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slp_Egreso_Interno_Del_Numerario
            self.jsClick(xpath)
            self.capture_image(msgOk)
   
        
    def seleccionarAceptarComun(self):
        to = 10
        accion = u'Hacer clic en el Botón ACEPTAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_AceptarComun
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
#                 self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarAceptar2(self):
        to = 10
        accion = u'Hacer clic en el Botón ACEPTAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Aceptar2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
#                 self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

                
        
    def seleccionarAceptarAutoriz(self):
        to = 10
        accion = u'Hacer clic en el Botón ACEPTAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_aceptar_Autoriz
            self.wait(5)  
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
    
    def verificarMensajeExitoEgresoIngresoInterno(self, mensaje):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_operacion_Exitosa_.format(mensaje)
            if self.visibility_element(xpath, to):
                message = self.get_element_text(xpath)
                print("mensaje obtenido " + message )
                print("mensaje A comparar " + mensaje )
                if message == mensaje:
                    self.highlight(xpath, accion)
                    xpath = plCajaInicio.btn_cerrarMjeExito
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
#                     self.captureImage(msgFail)
#                     pytest.fail(msgFail)
                    
            else:
                self.fail_msg(msgFail)
#                 self.captureImage(msgFail)               
#                 pytest.fail(msgFail)


    def validarNombreApellidoTitular(self, nombre, apellido):
        to = 10
        accion = u"Validar Nombre y Apellido del Titular de la Cuenta. "
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_Nombre3ros            
            if self.visibility_element(xpath, to):
                print(u"Nombre y Apellido Dato" + nombre + " " + apellido)
                nombreYapellidoMostrado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print( u"Nombre y Apellido Mostrado" + nombreYapellidoMostrado)            
                if nombre in nombreYapellidoMostrado and apellido in nombreYapellidoMostrado:
                    print (u"Se verifico que el nombre y apellido está en el label mostrado")
                    self.highlight(xpath,msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def validarNombreDelTitular(self, nombre):
        to = 10
        accion = u"Validar Nombre y Apellido del Titular de la Cuenta. "
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_Nombre3ros            
            if self.visibility_element(xpath, to):
                print(u"Nombre y Apellido Dato" + nombre )
                nombreYapellidoMostrado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print( u"Nombre y Apellido Mostrado" + nombreYapellidoMostrado)            
                if nombre in nombreYapellidoMostrado:
                    print (u"Se verifico que el nombre y apellido está en el label mostrado")
                    self.highlight(xpath,msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)



    def validarNombreApellidoOrdenante(self, NombreDelDopositante, ApellidoDelDepositante):
        to = 10
        accion = u"Validar Nombre y Apellido del Titular de la Cuenta. "
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_NombreOrdenante            
            if self.visibility_element(xpath, to):
                print(u"Nombre y Apellido Dato" + NombreDelDopositante + " " + ApellidoDelDepositante)
                nombreYapellidoMostrado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print( u"Nombre y Apellido Mostrado" + nombreYapellidoMostrado)            
                if NombreDelDopositante in nombreYapellidoMostrado and ApellidoDelDepositante in nombreYapellidoMostrado:
                    print (u"Se verifico que el nombre y apellido está en el label mostrado")
                    self.highlight(xpath,msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

       
    def validarNombreApellidoDepositante(self, nombre, apellido):
        to = 10
        accion = u"Validar Nombre y Apellido del Titular de la Cuenta. "
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_Nombre3ros            
            if self.visibility_element(xpath, to):
                print(u"Nombre y Apellido Dato" + nombre + " " + apellido)
                nombreYapellidoMostrado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                print( u"Nombre y Apellido Mostrado" + nombreYapellidoMostrado)            
                if nombre in nombreYapellidoMostrado and apellido in nombreYapellidoMostrado:
                    print (u"Se verifico que el nombre y apellido está en el label mostrado")
                    self.highlight(xpath,msgOk)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
    
    def validarBotonAutorizacionesSolicitadas(self, boton = True):
        to = 10
        accion = u'Validar que el Boton Finalizar este deshabilitado'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Finalizar
            if self.visibility_element(xpath, to):
                input_disabled = self.driver.find_element(by=By.XPATH, value=xpath).get_property('disabled')
                if input_disabled == boton:
                    print(u"EL Boton Finalizar esta DesHabilitado")
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def obtenerNroDeAutorizacion(self):
        to = 10
        accion = u'Obtener numero de Autorizacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_Nro_Autorizacion
            if self.visibility_element(xpath, to):   
                self.numeroDeAutorizacion  = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')     
                if self.numeroDeAutorizacion:
                    print(u"Numero De Autorizacion:" + self.numeroDeAutorizacion)
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def visualizarRecuadroAutorz(self):
        to = 10
        accion = u'Validar Recuadro de autorizacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.recuadro_autoriz
            if self.visibility_element(xpath, to):
                    self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)           
                
                
##### CONSULTA DE POSICION DE CUENTA #######

    def seleccionarConsultaPocisionCuenta(self):
        to = 10
        accion = u'Seleccionar Consulta Posicion cuenta '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_consuta_posicion_cuenta
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail, to)
                    
                    
    def seleccionarRaices(self):               
        to = 10
        accion = u'Hacer clic en el recuadro "Raices"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_raices_Cliente
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail, to)
                
            
    def seleccionarCuentasRaices(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentaRaices.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarConsultar(self):
        to = 10
        accion = u'Hacer clic en "CONSULTAR"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_consultar
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
                              
    def seleccionarCancelar(self):
        to = 10
        accion = u'Hacer clic en "CANCELAR"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cancelar
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)    
                
    def seleccionarticket(self):
        to = 10
        accion = u'Hacer clic en TICKET'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ticked
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
        
             
    def visualizarMensajeExito(self):
        to = 60
        accion = u'Visualizar el Mensaje'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.msgExito_consulta
            if self.visibility_element(xpath, to):
                msj_esperado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                self.capture_image("Mensaje encontrado: {}".format(msj_esperado))
            else:
                msgFail(msgFail)
                

##### CONSULTA DE POSICION DE CUENTA #######

    def seleccionarConsultaSaldosCuenta(self):
        to = 10
        accion = u'Seleccionar Consulta Saldos cuenta '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_consuta_saldos_cuenta
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail, to)
                    
    def visualizarCuadroNecesitaIdentificarAlCliente(self):
        to = 10
        accion = u'Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?'
        accion2 = u'Hacer clic en "SI"'
        msgOk = accion
        msgOk2 = accion2
        msgFail = u'No se pudo ' + msgOk.lower()
        msgFail2 = u'No se pudo ' + msgOk2.lower()
        with self.step(accion and accion2):
            xpath = plCajaInicio.txt_cuadroNecesitaIdentificarse
            xpath2 = plCajaInicio.btn_SI
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                if self.visibility_element(xpath2, to):
                    self.jsClick(xpath2)
                else:
                    self.fail_msg(msgFail2)   
            else:
                self.fail_msg(msgFail)

    def visualizarCuadroNecesitaIdentificarAlCliente2(self):
        to = 10
        accion = u'Visualizar en pantalla el Recuadro ¿Necesita identificar al cliente?'
        accion2 = u'Hacer clic en "NO"'
        msgOk = accion
        msgOk2 = accion2
        msgFail = u'No se pudo ' + msgOk.lower()
        msgFail2 = u'No se pudo ' + msgOk2.lower()
        with self.step(accion and accion2):
            xpath = plCajaInicio.txt_cuadroNecesitaIdentificarse
            xpath2 = plCajaInicio.btn_NO
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                if self.visibility_element(xpath2, to):
                    self.jsClick(xpath2)
                else:
                    self.fail_msg(msgFail2)   
            else:
                self.fail_msg(msgFail)
                   
    def seleccionarRecuadroCuentas(self):               
        to = 10
        accion = u'Hacer clic en el recuadro "Cuentas Cliente"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_raices_Cliente
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail, to)
                             
    def seleccionarCuentaCliente(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuenta3.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
    def ingresarNroCuenta(self, cuenta):
        to = 10
        accion = u'Ingresar el numero de cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_cuentas
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, cuenta, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def validarBtnDeshabilitado(self, boton = True):
        to = 10
        accion = u'Validar que el Boton Consultar este deshabilitado'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_consultar2
            if self.visibility_element(xpath, to):
                input_disabled = self.driver.find_element(by=By.XPATH, value=xpath).get_property('disabled')
                if input_disabled == boton:
                    print(u"EL Boton Consultar esta DesHabilitado")
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
################ COBROS ##################

    def seleccionarCobrosVarios(self):
        to = 10
        accion = u'-Hacer clic en la Transaccion - "Cobros Varios'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cobrosVarios 
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)   
                           
    def seleccionarAceleramientoDeOficios(self):
        to = 10
        accion = u'-Hacer clic en la Transacción - Arancelamiento de Oficios'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_AceleramientoDeOficios 
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def VisualizarCantidadDeOficios(self,oficios):               
        to = 10
        accion = u'Visualizar el recuadro "Cantidad de Oficios"  E Ingresar "1"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cantidadDeOficios
            if self.visibility_element(xpath, to):
                accion = u'Se ingresa 1'
                self.jsClick(xpath)
                self.clear(xpath)
                self.write(xpath, oficios, to)
                self.highlight(xpath, accion)
            else:
                self.capture_image(msgFail, to)
                
    def visualizarLblDeshabilitado(self, boton = True):
        to = 10
        accion = u'Visualizar el importe total "25,00" Por defecto esta en gris'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_importeTotal
            if self.visibility_element(xpath, to):
                input_disabled = self.driver.find_element(by=By.XPATH, value=xpath).get_property('disabled')
                if input_disabled == boton:
                    print(u"Lbl importeTotal esta DesHabilitado y tiene el importe Solicitado")
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

 
 
    def seleccionarRecuadroTpdeOperacion(self):               
        to = 10
        accion = u'Hacer clic en el "Tipo de Operación"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_tipoDeOperacion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarTipoDeOperacion(self,operacion):               
        to = 10
        accion = u'Seleccionar el item '+ operacion
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_operacion2.format(operacion)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarComboBox(self):               
        to = 10
        accion = u'Hacer click en Combo moneda'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_moneda
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail, to)
              
    def seleccionarMoneda(self,moneda):               
        to = 10
        accion = u'Hacer clic en seleccionar Moneda a extraer' + moneda
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_moneda3.format(moneda)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail, to)

    def ingresarImporte2(self, importe):
        to = 10
        accion = u'Ingresar Importe'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.imput_importe
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, importe, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionarBtnSiguiente(self):               
        to = 10
        accion = u'seleccionar Siguiente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Siguiente
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
                self.jsClick(xpath)

            else:
                self.capture_image(msgFail, to)
 
    def validarTipoDeOperacion(self,operacion):
        to = 10
        accion = u'Validar Operacion '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_operacion.format(operacion)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == operacion:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
 
    def validarMonedaOpn(self, moneda):
        to = 10
        accion = u'Validar moneda de la operacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_moneda2.format(moneda)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == moneda:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def validarImporteOpn(self, importe):
        to = 10
        accion = u'Validar importe de la operacion{}'.format(importe)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_Importe2.format(importe)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == importe:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
  
    def seleccionarValidar(self):
        to = 60
        accion = u'Hacer clic en validar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_validar
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)
            
    def validarOficios(self,oficios):
        to = 10
        accion = u'Validar Cantidad de Oficios '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_operacion.format(oficios)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == oficios:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def visualizarMensajeExitoOpn(self, msg):
        to = 1
        accion = u'Visualizar el Mensaje "Timbrado de cobro con exito"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.msgExito_Operacion.format(msg)
            xpath2 = plCajaInicio.msgExito_Almacenamientos.format(msg)
            if self.visibility_element(xpath, to): 
                self.highlight(xpath,accion)
            elif self.visibility_element (xpath2,to):     
                self.highlight(xpath2,accion)  
            else:
                msgFail(msgFail)

############PAGOS###################

    def seleccionarPagosVarios(self):
        to = 10
        accion = u'Hacer clic en la Transaccion - "Pagos Varios"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_PagosVarios 
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


############## CIERRE DE CAJA

    def seleccionarCierreDeCaja(self):
        to = 10
        accion = u'Hacer clic en la Transaccion - "Cierre de caja"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cierreDeaCaja 
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def MensajeExitoCierreMoneda(self, moneda):
        to = 30
        accion = u'Verificar Mesaje de cierre de moneda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cierre_moneda.format(moneda)
            if self.visibility_element(xpath, to):          
                self.highlight(xpath, accion)
                xpath = plCajaInicio.btn_cerrarMjeExito_X
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)

    
    def MensajeExitoCierreCaja(self, moneda):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cierre_Caja.format(moneda)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                xpath = plCajaInicio.btn_cerrarMjeExito_X
                self.jsClick(xpath)
                
            else:
                self.fail_msg(msgFail)


    def MensajeExitoCierreSucursal(self, moneda):
        to = 30
        accion = u'Verificar mensaje de exito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cierre_Sucursal.format(moneda)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                xpath = plCajaInicio.btn_cerrarMjeExito_X
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)
            
    
    def cerrarCajaMoneda(self,moneda,user):
        u''' Metodo para cierre de cajas con sus respectivas monedas '''
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.seleccionarCierreDeCaja()
        self.mostrarTiposDeMoneda()
        self.seleccionarTipoDeMoneda(moneda)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.obtenerSaldoDeCaja(moneda,user)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.ingresarImporte(self.importeCierre,moneda)
        self.seleccionarConfirmar()            
        if moneda == 'reales' or moneda == 'euros' or  moneda == 'dolares':      
            self.MensajeExitoCierreMoneda(moneda.capitalize())           
        elif moneda == 'pesos':
            if user  == 'UIC10022':
                self.MensajeExitoCierreSucursal(moneda.capitalize())         
            else: 
                self.MensajeExitoCierreCaja(moneda.capitalize())               
        else:
            self.fail_msg(u"Moneda no definida ")

############## ATM BANELCO , LIVERACIONES 

    def seleccionarATMBanelco(self):
        to = 10
        accion = u'Seleccionar ATMBanelco'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ATMBanelco
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarATMLiveraciones(self):
        to = 10
        accion = u'Seleccionar ATMBanelco'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ATMLiveraciones
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
  

    def mostrarYSeleccionarTipoDeTransaccion(self,transaccion):
        to = 10
        accion = u'Seleccionar el item:' +u' '+transaccion
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_trassaccion
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
                xpath = plCajaInicio.opt_selectTransaccion.format(transaccion)
                if self.visibility_element(xpath, to):
                    accion = u"Selecionar Transsaccion"
                    self.selectElement(xpath, msgOk, msgFail, to)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)


    def mostrar_seleccionar_nro_tas(self,numeroTAS):
        to = 10
        accion = u'Hacer clic en el recuadro Numero TAS'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_selectnumeroATM
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
                xpath = plCajaInicio.slc_numeroTAS.format(numeroTAS)
                if self.visibility_element(xpath, to):
                    accion = u"Selecionar Numero TAS "
                    self.selectElement(xpath, msgOk, msgFail, to)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                


    
    def mostrarYSeleccionarNroAtm(self,numeroATM):
        to = 10
        accion = u'Hacer clic en el recuadro Numero ATM'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_selectnumeroATM
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
                xpath = plCajaInicio.slc_numeroATM.format(numeroATM)
                if self.visibility_element(xpath, to):
                    accion = u"Selecionar Numero ATM "
                    self.selectElement(xpath, msgOk, msgFail, to)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
                
                
    def visualizar_msj_atm_en_estado_cargado(self):
        to = 60
        accion = u'Visualizar el mensaje ATM en estado cargado'
        msgOk = accion
        with self.step(accion):            
            xpath = plCajaInicio.msj_atm_estado_cargado
            if self.visibility_element(xpath, to):
                self.skip_msg(u"ATM en estado cargado")
            else:
                pass


    def validar_operacion(self,operacion):
        to = 10
        accion = u'Validar se valida Operacion {} '.format(operacion)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_operacion.format(operacion)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad Operacion: {}".format(operacion))
                
            else:
                self.fail_msg(msgFail)

    def validar_numero_atm(self,numero_atm):
        to = 10
        accion = u'Validar se valida Numero ATM {} '.format(numero_atm)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_operacion.format(numero_atm)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad Numero ATM: {}".format(numero_atm))
                
            else:
                self.fail_msg(msgFail)

###########################################

    def validar_destino(self,destino):
        to = 10
        accion = u'Validar se valida destino de remesa {} '.format(destino)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(destino)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad destino de remesa: {}".format(destino))
                
            else:
                self.fail_msg(msgFail)

    def validar_origen(self,origen):
        to = 10
        accion = u'Validar se valida origen de remesa {} '.format(origen)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(origen)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad origen de remesa: {}".format(origen))
                
            else:
                self.fail_msg(msgFail)

                
    def validar_sucursal(self,sucursal):
        to = 10
        accion = u'Validar Sucursal {}'.format(sucursal)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_sucursal.format(sucursal)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == sucursal:
                    self.highlight(xpath, accion)
                    print(u"Se validad la sucursal: {}".format(sucursal))

                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
    def validar_importe_total(self,importe):
        to = 10
        accion = u'Validar importe total {}'.format(importe)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_importe_total.format(importe)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == importe:
                    self.highlight(xpath, accion)
                    print(u"Se validad la Importe Total a Liberar Rejectado: {}".format(importe))

                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def validar_importe_total_a_liberar(self,importe):
        to = 10
        accion = u'Validar importe total {}'.format(importe)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_importe_total_a_liberar.format(importe)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == importe:
                    self.highlight(xpath, accion)
                    print(u"Se validad la Importe Total a Liberar Rejectado: {}".format(importe))

                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
                
    def validar_moneda(self,moneda):
        to = 10
        accion = u'Validar moneda {} '.format(moneda)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_moneda.format(moneda)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la moneda: {}".format(moneda))
                
            else:
                self.fail_msg(msgFail)
                
    def validar_transaccion(self,transacion):
        to = 10
        accion = u'Validar transaccion {} '.format(transacion)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(transacion)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la trasaccion: {}".format(transacion))
                
            else:
                self.fail_msg(msgFail)

    def validar_cuenta_deposito(self,cuenta):
        to = 10
        accion = u'Validar cuenta deposito {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la cuenta deposito: {}".format(cuenta))
                
            else:
                self.fail_msg(msgFail)

    def validar_nro_tas(self,nro):
        to = 10
        accion = u'Validar Numero TAS {}'.format(nro)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(nro)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se valida Numero TAS: {}".format(nro))
                
            else:
                self.fail_msg(msgFail)
                         
                
    def validar_nombre_2(self,nombre):
        to = 10
        accion = u'Validar cuenta deposito {}'.format(nombre)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_nombre_2.format(nombre)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad el nombre del cliente: {}".format(nombre))
                
            else:
                self.fail_msg(msgFail)

    def validar_nombre(self,nombre):
        to = 10
        accion = u'Validar cuenta deposito {}'.format(nombre)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_nombre.format(nombre)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad el nombre del cliente: {}".format(nombre))
                
            else:
                self.fail_msg(msgFail)


    def validarDatos(self, dato,tex):
        to = 10
        accion = u'validar Datos de la Operacion: ' + u' '+tex
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_datoValidar1.format(dato)
            xpath2 = plCajaInicio.lbl_datoValidar2.format(dato)
#Valida que se repita 2 veces en la lista frecuencia, si se repite 2 lo manda al xpath2
            if self.frecuencia.count(dato)==2: 
                self.visibility_element(xpath2, to)
                datos_validar = self.driver.find_element_by_xpath(xpath2).get_property('innerHTML')
                if dato in datos_validar:                                  
                    print("Se valida: {}".format(tex),datos_validar)
                    self.go_to_xpath(xpath2)
                    self.highlight(xpath2, accion)             
            else: 
                if self.visibility_element(xpath, to):
                    datos_validar = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                    if dato in datos_validar: 
                        print(dato,datos_validar)     
                        print("Se valida: {}".format(tex),datos_validar)
                        self.go_to_xpath(xpath2)
                        self.highlight(xpath, accion)
                                         
                elif self.visibility_element(xpath2, to):
                    datos_validar = self.driver.find_element_by_xpath(xpath2).get_property('innerHTML')
                    if dato in datos_validar:        
                        print("Se valida: {}".format(tex),datos_validar)
                        self.go_to_xpath(xpath2)
                        self.highlight(xpath2, accion)     
                else:
                    self.fail_msg(msgFail)
                    
                    
    def validar_datos(self, dato,tex):
        to = 10
        accion = u'Validar datos de la operacion: ' + u' '+tex
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = "//h6[contains(.,'{}')]".format(dato)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_test(msgFail)
                    
 

########REMESAS

 

    def seleccionarEnvioDeRemesasDeCheques(self):
        to = 10
        accion = u'Seleccionar Envio de remesas de Cheques'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_EnvioDeRemesas
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

                
    def seleccionarConfirmar3(self):
        to = 10
        accion = u'Hacer clic en el Boton CONFIRMAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_confirmar3
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)

    def visualizar_msj_no_hay_operaciones_con_cheques(self):
        to = 10
        accion = u'No se registra ninguna operación con cheques'
        msgOk = accion
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_no_hay_operaciones_con_cheques
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.skip_msg(msgOk)
            else:
                pass
            


    def visualizar_msj_no_hay_suficiente_saldo(self):
        to = 10
        accion = u'No hay suficiente saldo en el tesoro/caja para la operacion'
        msgOk = accion
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_saldo_insuficiente
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.skip_msg(msgOk)
            else:
                pass

    def visualizar_msj_no_hay_suficiente_saldo_depositos(self):
        to = 10
        accion = u'saldo insuficiente en la caja en Deposito'
        msgOk = accion
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_saldo_insuficiente_depositos
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.skip_msg(msgOk)
            else:
                pass


    def envioDeRemesasDeChequesAntesDelCierre(self):
        self.seleccionarEnvioDeRemesasDeCheques()
        self.mostrarTiposDeMoneda()
        self.validar_lista_monedas()
        self.seleccionarTipoDeMoneda(self.tipoMoneda)
        self.ingresarImporte(self.saldoCheques,self.tipoMoneda)
        self.seleccionarConfirmar()
        datos = [self.tipoMoneda,self.saldoCheques.strip()]
        texto = ["Moneda", "Importe"]                                       
        self.frecuencia = []
        for dato,text in zip(datos,texto):
            self.frecuencia.append(dato)                
            self.validarDatos(dato,text)
        print(self.frecuencia)      
        self.seleccionarConfirmar3() 
        self.verificarMensajeExitoExtracciones("Operación realizada con éxito")

        
    def validar_importe(self,importe):
        to = 10
        accion = u'Validar importe: {}'.format(importe)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_importe.format(importe)
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                if input_value == importe:
                    self.highlight(xpath, accion)
                    print(u"Se validad Importe: {}".format(importe))

                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
#########CHEQUES


    def seleccionarDepositoDeCheques(self):
        to = 10
        accion = u'Seleccionar Deposito De Cheques '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_de_cheques
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarDepositoDeChequesPropios(self):
        to = 10
        accion = u'Seleccionar Deposito De Cheques Propios'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_de_chequesPropios
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    
    def ingresarDatos(self,dato,text):
        to = 10
        accion = u'Ingresarr:' + u' '+ text
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datos_cheques.format(dato)
            if self.visibility_element(xpath, to):
                if dato == "banco":
                    self.write(xpath,"259",to)           
                    self.capture_image(msgOk)      
                elif dato == "sucursal":
                    self.write(xpath,"046" ,to)           
                    self.capture_image(msgOk)      
                elif dato == "codigoPostal":
                    self.write(xpath,"1227",to)           
                    self.capture_image(msgOk)                   
                elif dato == "numeroCheque":
                    self.write(xpath,"00013452",to)           
                    self.capture_image(msgOk)
                elif dato == "numeroCuenta":
                    self.write(xpath,"00022611008",to)
                    self.capture_image(msgOk)
                else:
                    self.capture_image(msgOk)
                    self.fail_msg(msgFail) 
            else:
                self.capture_image(msgFail, to)
                self.fail_msg(msgFail)
    
    def ingresar_Datos_2(self,dato,text):
        to = 10
        accion = u'Ingresarr:' + u' '+ text
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datos_cheques.format(dato)
            if self.visibility_element(xpath, to):
                if dato == "banco":
                    self.write(xpath,"259",to)           
                    self.capture_image(msgOk)      
                elif dato == "sucursal":
                    self.write(xpath,"002" ,to)           
                    self.capture_image(msgOk)      
                elif dato == "codigoPostal":
                    self.write(xpath,"1227",to)           
                    self.capture_image(msgOk)                   
                elif dato == "numeroCheque":
                    self.write(xpath,"00068064",to)           
                    self.capture_image(msgOk)
                elif dato == "numeroCuenta":
                    self.write(xpath,"00003071009",to)
                    self.capture_image(msgOk)
                else:
                    self.capture_image(msgOk)
                    self.fail_msg(msgFail) 
            else:
                self.capture_image(msgFail, to)
                self.fail_msg(msgFail)
                
    def ingresar_Datos_3(self,dato,text):
        to = 10
        accion = u'Ingresarr:' + u' '+ text
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datos_cheques.format(dato)
            if self.visibility_element(xpath, to):
                if dato == "banco":
                    self.write(xpath,"259",to)           
                    self.capture_image(msgOk)      
                elif dato == "sucursal":
                    self.write(xpath,"002" ,to)           
                    self.capture_image(msgOk)      
                elif dato == "codigoPostal":
                    self.write(xpath,"1227",to)           
                    self.capture_image(msgOk)                   
                elif dato == "numeroCheque":
                    self.write(xpath,"00068064",to)           
                    self.capture_image(msgOk)
#                 elif dato == "numeroCuenta":
#                     self.write(xpath,"00003071009",to)
#                     self.capture_image(msgOk)
                else:
                    self.capture_image(msgOk)
                    self.fail_msg(msgFail) 
            else:
                self.capture_image(msgFail, to)
                self.fail_msg(msgFail)


    def ingresarDatosOtrosBancos(self,dato,text):
        to = 10
        accion = u'Ingresarr:' + u' '+ text
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datos_cheques.format(dato)
            if self.visibility_element(xpath, to):
                if dato == "banco":
                    self.write(xpath,"059",to)           
                    self.capture_image(msgOk)      
                elif dato == "sucursal":
                    self.write(xpath,"047" ,to)           
                    self.capture_image(msgOk)      
                elif dato == "codigoPostal":
                    self.write(xpath,"1030",to)           
                    self.capture_image(msgOk)    
                elif dato == "numeroCheque":
                    self.write(xpath,"12345678",to)           
                    self.capture_image(msgOk)
                elif dato == "numeroCuenta":
                    self.write(xpath,"98765432101",to)
                    self.capture_image(msgOk)
                else:
                    self.capture_image(msgOk)
                    self.fail_msg(msgFail) 
            else:
                self.capture_image(msgFail, to)
                self.fail_msg(msgFail)

    def ingresar_datos_otros_bancos2(self,dato,text):
        to = 10
        accion = u'Ingresarr:' + u' '+ text
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datos_cheques.format(dato)
            if self.visibility_element(xpath, to):
                if dato == "banco":
                    self.write(xpath,"059",to)           
                    self.capture_image(msgOk)      
                elif dato == "sucursal":
                    self.write(xpath,"047" ,to)           
                    self.capture_image(msgOk)      
                elif dato == "codigoPostal":
                    self.write(xpath,"1030",to)           
                    self.capture_image(msgOk)    
                elif dato == "numeroCheque":
                    self.write(xpath,"12345678",to)           
                    self.capture_image(msgOk)            
                else:
                    self.capture_image(msgOk)
                    self.fail_msg(msgFail) 
            else:
                self.capture_image(msgFail, to)
                self.fail_msg(msgFail)

                
    def seleccionarFindeCarga(self):
        to = 60
        accion = u'Hacer clic en el Boton FIN DE CARGA'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_finDeCarga
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.doubleClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarValidarCheques(self):
        to = 60
        accion = u'Hacer clic en el Boton VALIDAR CHEQUES'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_validarCheques
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_validar_cheques_dps(self):
        to = 60
        accion = u'Hacer clic en el Boton VALIDAR CHEQUES'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_validar_cheques_dps
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

########### PAGO CHEQUES

    def seleccionarPagoCheques(self):
        to = 10
        accion = u'Seleccionar Pago Cheques'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_pago_de_cheques
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarCheckBoxFirma(self):
        to = 10
        accion = u'Seleccionar Check firma de Cliente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.chek_cliente
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

 
    def validarCantidadDeCheques(self):
        to = 10
        accion = u'Validar Cantidad De Cheques en la operacion '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cantidadCheques3
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la cantidad de cheques: {}".format(self.cantidad))
                
            else:
                self.fail_msg(msgFail)
 
    def validar_cantidad_De_cheques(self):
        to = 10
        accion = u'Validar Cantidad De Cheques en la operacion '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cantidadCheques
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la cantidad de cheques: {}".format(self.cantidad))
                
            else:
                self.fail_msg(msgFail)
       
    def ingresarDatosDeChequera(self):
        datos = ["banco","sucursal","codigoPostal","numeroCheque","numeroCuenta"]   
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque ",
                "Numero de Cuenta " ]
        
        for dato,text in zip(datos,texto):
            self.ingresarDatos(dato,text)
            
    def ingresarDatosDeChequera_2(self):
        datos = ["banco","sucursal","codigoPostal","numeroCheque","numeroCuenta"]   
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque ",
                "Numero de Cuenta " ]
        
        for dato,text in zip(datos,texto):
            self.ingresar_Datos_2(dato,text)            

    def ingresar_datos_de_chequera(self):
        datos = ["banco","sucursal","codigoPostal","numeroCheque"]   
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque "]
        
        for dato,text in zip(datos,texto):
            self.ingresarDatos(dato,text)
            
    def ingresar_datos_de_chequera_2(self):
        datos = ["banco","sucursal","codigoPostal","numeroCheque"]   
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque "]
        
        for dato,text in zip(datos,texto):
            self.ingresar_Datos_3(dato,text)
            
            
    def ingresarDatosDeChequeraOtrosBancos(self):
        datos = ["banco","sucursal","codigoPostal","numeroCheque","numeroCuenta"]
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque ",
                "Numero de Cuenta "]
        for dato,text in zip(datos,texto):
            self.ingresarDatosOtrosBancos(dato,text)
            
    def ingresar_datos_chequera_otros_bancos2(self):
        datos = ["banco","sucursal","codigoPostal","numeroCheque"]
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque "]
        for dato,text in zip(datos,texto):
            self.ingresar_datos_otros_bancos2(dato,text)
            



        
    def validarDatosOperacionDepositos(self):
        self.validarCantidadDeCheques()
        self.validar_cuenta_deposito(self.cuentaValidar1)
        self.validar_nombre(self.nombreApellido) 
        self.validar_moneda(self.tipoMoneda)
        self.validar_importe_total_a_liberar(self.importe)

     
        
    def validarDatosOperacionDepositos2(self):
        self.validarCantidadDeCheques()
        self.validar_cuenta_deposito(self.cuentaValidar2)
        self.validar_nombre(self.nombreApellido2) 
        self.validar_moneda(self.tipoMoneda)
        self.validar_importe_total_a_liberar(self.importe) 
        

        
    def validarDatosOperacionPagos(self): 
        datos = [self.cuentavalidar,self.nombreCliente +' '+self.apellidoCliente,self.tipoMoneda,'100,00']
        texto = ["Cuenta","Nombre y apellido","Moneda","Importe"] 
        for dato,text in zip(datos,texto):
            self.frecuencia = []
            self.frecuencia.append(dato)                
            self.validarDatos(dato,text)     
        print(self.frecuencia) 
    
 
    def selecionarFinalizar(self):
        to = 30
        accion = u'hacer clic en el boton "FINALIZAR"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_FinalizarTrx
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
############### PAGO CHEQUES CERTIFICADO

    def seleccionar_pago_cheques_certificado(self):
        to = 10
        accion = u'Seleccionar Pago Cheques Certificados'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_pago_de_cheques_certificado
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)





############### TRASFERENCIA 

    def seleccionarTrasferenciaAOtroCliente(self):
        to = 10
        accion = u'Seleccionar Trasferencia a otros Clientes'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_TrasferenciasAotrosClientes
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarTrasferenciaEntreCuentas(self):
        to = 10
        accion = u'Seleccionar Trasferencia Entre cuentas'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_TrasferenciasEntreCuentas
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
        
                
    def seleccionarTrasferenciaAOtrosBancos(self):
        to = 10
        accion = u'Seleccionar Trasferencia a otros Bancos'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_TrasferenciasAOtrosBancos
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)




    def ingresarCuenta2(self,cuenta,modo):               
        to = 10
        accion = u'Ingresar Cuenta: {} '.format(modo)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cuenta_firma
            if self.visibility_element(xpath, to):        
                self.write(xpath, cuenta, to)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def ingresar_Cuenta(self,cuenta,modo):               
        to = 10
        accion = u'Ingresar Cuenta: {} '.format(modo)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_cuenta_firma
            if self.visibility_element(xpath, to):        
                self.write(xpath, cuenta, to)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    
        
    def seleccionarSiguiente4(self):
        to = 60
        accion = u'Hacer clic en el Boton SIGUIENTE'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Siguiente4
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_debito_en_cuenta(self):
        to = 60
        accion = u'Hacer clic en debito en cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_debito_cuenta
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
            
    def clickRadioBtn3(self,Datos_Boton):               
        to = 10
        accion = u'Tildar la opción {}'.format(Datos_Boton)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_RadioBtn.format(Datos_Boton)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.highlight(xpath,u"Visualizarque EL tildado {} ".format(Datos_Boton))
            else:                
                self.fail_msg(msgFail)


    def mostrarTiposDeOperacion(self):
        to = 10
        accion = u'Hacer clic en el recuadro Concepto'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_moneda
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)



    def seleccionarTipoOperacion(self, Operacion):
        to = 10
        accion = u'Seleccionar Concepto {} '.format(Operacion)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):   
            if self.mostrarTiposDeOperacion:          
                xpath = plCajaInicio.opt_select.format(Operacion)
                if self.selectElement(xpath, msgOk, msgFail, to):
                    self.capture_image(msgOk)
                else:
                    self.fail_msg(msgFail)
    
    def ingresarReferencia(self,cuenta):               
        to = 10
        accion = u'Ingresar Referencia '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.inputReferencia
            if self.visibility_element(xpath, to):        
                self.write(xpath, cuenta, to)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    
    def ingresarCuitDelDestinatario(self,Cuit):               
        to = 10
        accion = u'Ingresar Referencia '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.inputCuit_Cuil
            if self.visibility_element(xpath, to):
                self.highlight(plCajaInicio.txt_dialogo, u"Visualizar la ventana Ingresar el CUIT / CUIL del Destinatario")        
                self.write(xpath, Cuit, to)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarIngresar(self):
        to = 60
        accion = u'Hacer clic en el Boton Ingresar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Ingresar
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def mostrarTiposDeOperecion(self,oparacion):
        to = 10
        accion = u'Hacer click en el recuadro Conceptos'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_moneda
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
                self.seleccionarTipoOperacion(oparacion)    
            else:
                self.fail_msg(msgFail)

    def seleccionarRecuadroCuentasCliente2(self,cuenta):               
        to = 30
        accion = u'Hacer clic en el recuadro Cuentas Cliente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_cliente
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
                self.seleccionarCuentaDeposito(cuenta)
            else:
                self.fail_msg(msgFail)

    def seleccionarRecuadroCuentasCliente3(self,cuenta):               
        to = 30
        accion = u'Hacer clic en el recuadro Cuentas Cliente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_cliente2
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
                self.seleccionarCuentaDeposito2(cuenta)
            else:
                self.fail_msg(msgFail)

    def seleccionarCuentaDeposito2(self, cuenta):
        to = 10
        accion = u'Seleccionar cuenta: {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuentaClienteDeposito2
            self.jsClick(xpath)
            xpath = plCajaInicio.opt_nroCuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def validar_cuenta_debito(self,cuenta):
        to = 10
        accion = u'Validar cuenta debito: {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la cuenta debito: {}".format(cuenta))
                
            else:
                self.fail_msg(msgFail)

    def validar_cuenta_credito(self,cuenta):
        to = 10
        accion = u'Validar cuenta credito: {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cuenta.format(cuenta)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la cuenta credito: {}".format(cuenta))
                
            else:
                self.fail_msg(msgFail)
                
    def validar_cbu_destinatario(self,cbu):
        to = 10
        accion = u'Validar CBU destinatario: {}'.format(cbu)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cbu.format(cbu)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad CBU destinatario: {}".format(cbu))
                
            else:
                self.fail_msg(msgFail)
                    
    def validar_cuit_cuil(self,cuit_cuil):
        to = 10
        accion = u'Validar cuit_cuil: {}'.format(cuit_cuil)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cuit_cuil.format(cuit_cuil)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad cuit_cuil: {}".format(cuit_cuil))
                
            else:
                self.fail_msg(msgFail)
                
    def validar_concepto(self,concepto):
        to = 10
        accion = u'Validar cuit_cuil: {}'.format(concepto)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_concepto.format(concepto)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad cuit_cuil: {}".format(concepto))
                
            else:
                self.fail_msg(msgFail)
                
    def validar_referencia(self,referencia):
        to = 10
        accion = u'Validar referencia: {}'.format(referencia)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_referencia.format(referencia)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad referencia: {}".format(referencia))
                
            else:
                self.fail_msg(msgFail)

#################COBRO DE TARJETA CREDITO

    def seleccionarCobroDeTarjetaCredito(self):
        to = 50
        accion = u'Seleccionar Cobro de Tarjeta de Credito'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_CobroDeTargetasDecredito
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def visualizarDatosTarjeta(self):
        to = 10
        accion = u'Visualizar Tarjeta "Máster"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_datosTarjetaMaster
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                datosTarjeta = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                print("Se muestran datos de tarjeta: {}".format(datosTarjeta))
            else:
                self.fail_msg(msgFail)


    def seleccionarComboBoxCobros(self,operacion):               
        to = 10
        accion = u'Hacer click en Combo Forma de pago'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_moneda
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
                self.seleccionarTipoOperacion(operacion)
                
            else:
                self.fail_msg(msgFail)



    def ingresarNroTarjeta(self,NroTarjeta,modo):               
        to = 10
        accion = u'Ingresar Cuenta: {} '.format(modo)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.txt_nroTarjeta
            if self.visibility_element(xpath, to):        
                self.write(xpath, NroTarjeta, to)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def mostrarTiposDeTarjeta(self,Moneda):
        to = 10
        accion = u'Hacer click en la Marca '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_visa
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
                self.seleccionarTipoOperacion(Moneda)    
            else:
                self.fail_msg(msgFail)


    def validar_nro_tarjeta(self,numero):
        to = 10
        accion = u'Validar numero de tarjeta {}'.format(numero)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(numero)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad numero de tarjeta: {}".format(numero))
                
            else:
                self.fail_msg(msgFail)


    def validar_marca_tarjeta(self,marca):
        to = 10
        accion = u'Validar numero de tarjeta {}'.format(marca)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(marca)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la marca de tarjeta: {}".format(marca))
                
            else:
                self.fail_msg(msgFail)
                
    def validar_forma_pago(self,forma):
        to = 10
        accion = u'Validar forma de pago: {}'.format(forma)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_trasaccion.format(forma)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la forma de pago: {}".format(forma))
                
            else:
                self.fail_msg(msgFail)

#######TAS LIBERACIONES 

    def seleccionarTasLiberaciones(self):
        to = 10
        accion = u'Seleccionar Tas liberaciones'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_tasLiberaciones
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                

    def clickEnter(self):
        to = 2
        accion = u'Precionar Enter'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plCajaInicio.input_NroTas
            if self.visibility_element(xpath, to):
                self.driver.find_element(by=By.XPATH, value=xpath).send_keys(Keys.RETURN)
                return msgOk
            else:
                self.fail_msg(msgFail)
     
     

        
        
    def ingresarNroTas(self,NroTas):               
        to = 10
        accion = u'Ingresar Numero de Tas'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_NroTas
            if self.visibility_element(xpath, to):
                self.write(xpath, NroTas, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def ingresarImporte4(self,Importe):               
        to = 10
        accion = u'Ingresar Importe'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_Importe5
            if self.visibility_element(xpath, to):
                self.write(xpath, Importe, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarDepocitar(self):               
        to = 10
        accion = u'seleccionar Depositar'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Redepositar
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
                self.jsClick(xpath)

            else:
                self.capture_image(msgFail, to)
    
    
    def mostrarTiposDeMoneda2(self,Moneda):
        to = 10
        accion = u'Hacer click en el'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_selectnumeroATM
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
                self.seleccionarTipoOperacion(Moneda)    
            else:
                self.fail_msg(msgFail)
                
 
    def ingresarImporte5(self,Importe):               
        to = 10
        accion = u'Ingresar Importe'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_Importe6
            if self.visibility_element(xpath, to):
                self.write(xpath, Importe, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
##ENVIO DE REMESA INTERNA - Externa


    def seleccionarEnvioDeRemesaInterna(self):
        to = 10
        accion = u'Seleccionar Envio de remesa Interna'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_EnvioDeRemesaInterna
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validar_lista_monedas(self):
        to = 50
        accion = u'Validar lista de monedas: Pesos, Dolares, Euros, Reales '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.list_box_monedas
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)                
                
    def mostrarMoneda(self,Moneda):
        to = 10
        accion = u'Hacer click en el desplegable moneda '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_formaDePago
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
                self.validar_lista_monedas()
                self.seleccionarTipoOperacion(Moneda)    
            else:
                self.fail_msg(msgFail)

                
    def mostrarDestino(self,destino):
        to = 10
        accion = u'Hacer click en la Marca '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_visa
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
                self.seleccionarTipoOperacion(destino)    
            else:
                self.fail_msg(msgFail)

                
##### CONSULTA DE SALDO DE CAJA


    def seleccionarConsultaDeSaldo(self):
        to = 10
        accion = u'Seleccionar Consulta de saldos'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ConsultaDeSaldos
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def obeneterSaldoCaja(self, posicion):
        to = 10
        accion = u'Obtener Saldo de Caja '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cellMoneda.format(posicion)
            if self.visibility_element(xpath, to):
                self.monedaSaldo = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                self.highlight(xpath, accion)
                
            else:
                self.fail_msg(msgFail)

    def obeneterSaldoMonedas(self, posicion):
        to = 10
        accion = u'Obtener Saldo de Caja '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cellMoneda.format(posicion)
            if self.visibility_element(xpath, to):
                self.monedaSaldo = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                self.highlight(xpath, accion)
                
            else:
                self.fail_msg(msgFail)

    def obeneterSaldoCaf(self, posicion):
        to = 10
        accion = u'Obtener Saldo del Saldo Tesoro Intermedio'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cellMonedaCaf.format(posicion)
            if self.visibility_element(xpath, to):
                self.monedaSaldo = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                self.highlight(xpath, accion)
                
            else:
                self.fail_msg(msgFail)

    def obeneterSaldoCaf2(self, posicion):
        to = 10
        accion = u'Obtener Saldo del Saldo Tesoro Intermedio'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cellMonedaCaf.format(posicion)
            if self.visibility_element(xpath, to):
                self.monedaSaldoCaf = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                self.highlight(xpath, accion)
                
            else:
                self.fail_msg(msgFail)


    def obeneterSaldoTesoroSucursal(self, posicion):
        to = 10
        accion = u'Obtener Saldo del tesoro de Sucursal '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cellMonedaTrosucursal.format(posicion)
            if self.visibility_element(xpath, to):
                self.monedaSaldoTroSucursal = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                self.highlight(xpath, accion)
                
            else:
                self.fail_msg(msgFail)


    def seleccionarSalir(self):
        to = 10
        accion = u'Seleccionar Salir'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Salir
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                

                
    def obtenerSaldosDeCaja(self,posicion):
        self.seleccionarConsultaDeSaldo()
        self.obeneterSaldoCaja(posicion)
        self.seleccionarSalir()
        
                
    def obtenerSaldosDeCaf(self,posicion):
        self.seleccionarConsultaDeSaldo()
        self.obeneterSaldoCaf(posicion)
        self.seleccionarSalir()
                                  

    def verificarSaldosDeCaja(self,posicion):
        self.obeneterSaldoCaja(posicion)
                    
                                
    def verificarSaldosDeCaf(self,posicion):
        self.obeneterSaldoCaf(posicion)
            
            
    def verificarSaldoDeRemesasDeCheques(self):  
        self.seleccionarConsultaDeTotales()
        self.mostrarTiposDeMoneda()
        self.validar_lista_monedas()
        self.seleccionarTipoDeMoneda("Pesos")
        self.seleccionarConsultar()
        self.verificarSaldoDeCheques()
        self.seleccionarCancelar()       
        
    def revision_de_saldos_caf_(self):   
        self.seleccionarConsultaDeSaldo()
        for posicion in self.posiciones:    
            self.obeneterSaldoCaf2(posicion)                 
            if self.monedaSaldoCaf == "0,00" and posicion =='1':
                self.monedas_caf.remove("Pesos")
                self.posiciones_caf.remove('1')
                print("se elimina Moneda Pesos de la lista en Tesoro intermedio")                           
            elif self.monedaSaldoCaf == "0,00" and posicion =='2':
                self.monedas_caf.remove("Dolares")
                self.posiciones_caf.remove('2')
                print("se elimina Moneda dolares de la lista en Tesoro intermedio")                               
            elif self.monedaSaldoCaf == "0,00" and posicion =='3':
                self.monedas_caf.remove("Euros")
                self.posiciones_caf.remove('3')
                print("se elimina Moneda Euros de la lista en Tesoro intermedio")        
            elif self.monedaSaldoCaf == "0,00" and posicion =='4':
                self.monedas_caf.remove("Reales")
                self.posiciones_caf.remove('4')
                print("se elimina Moneda Reales de la lista en Tesoro intermedio")                                                                        
            print(self.monedas_caf)
        self.seleccionarSalir()   
        
    def revision_de_saldos_caja(self):   
        self.seleccionarConsultaDeSaldo()
        for posicion in self.posiciones:    
            self.obeneterSaldoCaja(posicion)                 
            if self.self.monedaSaldo == "0,00" and posicion =='1':
                self.monedas_caja.remove("Pesos")
                self.posiciones_caja.remove('1')
                print("se elimina Moneda Pesos de la lista en Tesoro intermedio")                           
            elif self.self.monedaSaldo == "0,00" and posicion =='2':
                self.monedas_caf.remove("Dolares")
                self.posiciones_caja.remove('2')
                print("se elimina Moneda dolares de la lista en Tesoro intermedio")                               
            elif self.monedaSaldo == "0,00" and posicion =='3':
                self.monedas_caf.remove("Euros")
                self.posiciones_caja.remove('3')
                print("se elimina Moneda Euros de la lista en Tesoro intermedio")        
            elif self.monedaSaldo == "0,00" and posicion =='4':
                self.monedas_caja.remove("Reales")
                self.posiciones_caja.remove('4')
                print("se elimina Moneda Reales de la lista en Tesoro intermedio")                                                                        
            print(self.monedas_caf)
        self.seleccionarSalir()            
         

 
#####ENVIO DE REMESAS

    def seleccionarEnvioDeRemesa(self):
        to = 10
        accion = u'Seleccionar Envio de remesa'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_EnvioDeRemesa
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


#####CONSULTA DE TOTALES,

    def seleccionarConsultaDeTotales(self):
        to = 10
        accion = u'Seleccionar Consulta de Totales'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ConsultaDeTotales
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionarCheckNoExistenDiferencias(self,posicion):
        to = 10
        accion = u'seleccionarCheck No Existen Diferencias'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.chekCierre.format(posicion)
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCierreMonedaCaja(self,posicion):
        to = 10
        accion = u'Seleccionar Cierre Moneda'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_CierreMoneda.format(posicion)
            xpath2 = plCajaInicio.btn_CierreCaja
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)             
            elif self.visibility_element(xpath2, to):
                self.go_to_xpath(xpath2)
                self.jsClick(xpath2)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def visualizar_advertencia_de_cierre(self):
        to = 10
        accion = u'Visualizar mensaje Si inicia el proceso de cierre no podrá realizar más operaciones'
        msgOk = accion
        msgFail = u"No se pudo",msgOk
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_advertencia
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk)
                self.seleccionarSI()              

                

    def verificar_estado_monedas(self,colum):
        to = 10
        accion = u'Verificar si alguna de las monedas(Pesos, dolares, euros, reales esta cerrada)'
        msgOk = accion
        msgFail = u"No se pudo",msgOk
        with self.step(accion):
            xpath = plCajaInicio.colum_cierra.format(colum)
            if self.visibility_element(xpath, to):
                estado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                print(estado)
                if "Cerrado" in estado and colum == "2":
                    self.monedas.remove("reales")
                    self.posiciones.pop()
                    self.highlight(xpath,msgOk)
                elif "Cerrado" in estado and colum == "3":
                    self.monedas.remove("euros")
                    self.posiciones.pop()
                    self.highlight(xpath,msgOk)
                elif "Cerrado" in estado and colum == "4":
                    self.monedas.remove("dolares")
                    self.posicione.pop()
                    self.highlight(xpath,msgOk)
                elif "Cerrado" in estado and colum == "5":
                    self.monedas.remove("pesos")
                    self.posiciones.pop()
                    self.highlight(xpath,msgOk)
            else:
                self.fail_msg(msgFail)
    
            



    def seleccionarSI(self):
        to = 10
        accion = u'Seleccionar SI'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Si
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.doubleClick(xpath)
            else:
                pass
  
    def visualizar_msj_existen_cajas_sin_cerrar(self):
        to = 10
        accion = u'Visualizar mensaje Existen Cajas sin Cerrar'
        msgOk = accion
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_existen_cajas_sin_cerrar
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk)
                self.skip_msg(u"Existen Cajas sin Cerrar")
            else:
                pass
            
    def visualizar_msj_existen_monedas_con_saldos(self):
        to = 10
        accion = u'Visualizar Existen monedas con saldo en cajón'
        msgOk = accion
        with self.step(accion):
            xpath = plCajaInicio.msj_txt_existen_monedas_con_saldos
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk)
                self.skip_msg(u"Existen Cajas sin Cerrar")
            else:
                pass
  
    
    def validarMsgMonedaCerrada(self,moneda):
        to = 90
        accion = u'Validar Mensaje moneda {} cerrada'.format(moneda)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msgMonedaCerrada.format(moneda)
            xpath_2 = plCajaInicio.msgCajaCerrada
            if moneda == "pesos":
                self.visibility_element(xpath_2, to)
                self.highlight(xpath_2,msgOk)
                self.jsClick(plCajaInicio.btn_FinalizarTrx) 
            elif moneda == "dolares" or "euros" or "reales":
                self.visibility_element(xpath, to)
                self.highlight(xpath,msgOk)
                self.jsClick(plCajaInicio.btn_FinalizarTrx) 
            else:
                self.fail_msg(msgFail)

                
    
    def validarMsgMonedaCerrada_SUC(self,moneda):
        to = 90
        accion = u'Validar Mensaje moneda {} cerrada'.format(moneda)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msgMonedaCerrada.format(moneda)
            xpath_2 = plCajaInicio.msgSucursalCerrada

            if moneda == "pesos":
                self.visibility_element(xpath_2, to)
                self.highlight(xpath_2,msgOk)
                self.jsClick(plCajaInicio.btn_FinalizarTrx) 
            elif moneda == "dolares" or "euros" or "reales":
                self.visibility_element(xpath, to)
                self.highlight(xpath,msgOk)
                self.jsClick(plCajaInicio.btn_FinalizarTrx) 
            else:
                self.fail_msg(msgFail)

    def ventanaSaldoExcedidoEnCajaOCaf(self):
        to = 10
        accion = u'Verificar Mensaje de saldo Exedido en Caja o Caf'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        xpath = plCajaInicio.slp_saldoExedidoCajaCaf
        xpath2 = plCajaInicio.slp_saldoExedidoCajaCaf2
        if self.visibility_element(xpath, to):
            self.go_to_xpath(xpath)
            self.jsClick(xpath)
            self.capture_image(msgOk)
        elif self.visibility_element(xpath2, to):
            self.go_to_xpath(xpath2)
            self.jsClick(xpath2)
            self.capture_image(msgOk) 
        else:
            self.fail_msg(msgFail)


    def validarMsgCierreDeCajaRealizado(self):
        to = 10
        accion = u'Validar Cierre De Caja Realizado'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msgCajaCerrada
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk)
                self.wait(1)
                self.jsClick(plCajaInicio.btn_FinalizarTrx)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validarMsgCierreDeSucursalRealizado(self):
        to = 10
        accion = u'Validar Cierre De Sucursal Realizado'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msgSucursalCerrada
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk)
                self.wait(1)
                self.jsClick(plCajaInicio.btn_FinalizarTrx)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


############Consulta de Posición del Líquido de la Sucursal

    def seleccionarConsultaDePoicionDelLiquidoDeLaSucursal(self):
        to = 10
        accion = u'Seleccionar Consulta de Posición del Líquido de la Sucursal'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_ConsultaDelLiquidoDeLaSucursal
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def visualizarDatosDeSaldo(self,moneda,dato):
        to = 10
        accion = u'Visualizar datos de Saldo de la moneda {}'.format(moneda)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.cell_saldos.format(dato)
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                informacionSaldos = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerText')
                print(informacionSaldos)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
                
    
    def seleccionarAceptar3(self):
        to = 10
        accion = u'Seleccionar Aceptar'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_aceptar3
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
            
                
    def validarMsgTransaccionNoAutorizada(self,mensaje):
        to = 20
        accion = u'Validar Mensaje:Solo un operador con perfil Centralizador puede ingresar a esta transacción.'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msg_transaccionNoAutorizada3.format(mensaje)
            xpath2 = plCajaInicio.btn_AceptarComun
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)


############## CONSULTA DE REMESAS POR SUCURSAL

    def seleccionarConsultaDeRemesasSucursal(self):
        to = 10
        accion = u'Seleccionar Consulta de remesas por Sucursal'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_consultaRemesasPorSucursal
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def validarMensajeTransaccionAutorizada(self):
        to = 10
        accion = u'Validar Mensaje Transaccion no autorizada Usted no es centralizador'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msg_transaccionNoAutorizada
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk)
                self.wait(1)
                self.jsClick(plCajaInicio.btn_AceptarComun)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validarMensajeTransaccionAutorizada3(self,mensaje):
        to = 20
        accion = u'Validar Mensaje Transaccion no autorizada Usted no es centralizador'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msg_transaccionNoAutorizada2.format(mensaje)
            xpath2 = plCajaInicio.btn_AceptarComun
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)

            else:
                self.fail_msg(msgFail)


############## CONSULTA DE REMESAS POR OPERADOR


    def seleccionarConsultaDeRemesasOperador(self):
        to = 10
        accion = u'Seleccionar Consulta de remesas por Operador'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_consultaRemesasPorOperador
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def validarMensajeTransaccionAutorizada2(self,mensaje):
        to = 10
        accion = u'Validar el mensaje "Transacción no autorizada" "Usted es centralizador, si desea consultar remesas seleccione la opción del menú"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msg_transaccionNoAutorizada2
            if self.visibility_element(xpath, to):
                msg = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                if mensaje in msg:      
                    print("Se valida mesaje: ", msg)
                    self.highlight(xpath,msgOk)
                    self.jsClick(plCajaInicio.btn_AceptarComun)
            else:
                self.fail_msg(msgFail)

######### CONSULTA DE LIQUIDO DE CUENTA 

    def seleccionarConsultaDeLiquidoDeCuenta(self):
        to = 10
        accion = u'Hacer clic en Consulta de liquido Cuenta'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_consultaDeLiquidoDeCuenta 
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def visualizarMensaje(self, msg):
        to = 1
        accion = u'Visualizar el Mensaje ""'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.msgExito_Operacion.format()
            xpath2 = plCajaInicio.msgExito_Almacenamientos.format(msg)
            if self.visibility_element(xpath, to): 
                self.highlight(xpath,accion)
            elif self.visibility_element (xpath2,to):     
                self.highlight(xpath2,accion)  
            else:
                msgFail(msgFail)


########## CONSULTA DE SALDOS SUCURSAL 

    def seleccionarConsultaDeSaldosSucursal(self):
        to = 10
        accion = u'Seleccionar Consulta de saldos Sucursal'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_consultaDeSaldosSucursal
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
  
    def visualizarRecuadroConsultaSaldosSucursal(self):
        to = 10
        accion = u'Visualizar el recuadro de la Consulta de Saldos de Sucursal "Operadores - Tesoro Intermedio - Tesoro Sucursal"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.div_consultaSaldosSucursal
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)
    
    def visualizarTablaDeSaldos(self):
        to = 10
        accion = u'Visualizar la información del saldo de los operadores'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.td_saldosOperador
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                informacion = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                print(informacion)
            
            else:
                self.fail_msg(msgFail)
                
    def visualizarTablaDeTesoroIntermedio(self):
        to = 10
        accion = u'Visualizar la información del saldo del Tesoro Intermedio'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.td_tesoroIntermedio
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                informacion = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                print(informacion)
            else:
                self.fail_msg(msgFail)
                
                
    def visualizarTablaDeTesoroSucursal(self):
        to = 10
        accion = u'Visualizar la información de los saldos del Tesoro Sucursal"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.td_tesoroSucursal
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                informacion = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                print(informacion)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarListar(self):
        to = 60
        accion = u'Hacer clic en el Boton LISTAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_listar
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def selecionarParametro(self,parametro):               
        to = 10
        accion = u'Hacer clic en el parametro'.format(parametro)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_parametro.format(parametro)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)  
            else:                
                self.fail_msg(msgFail)

    def seleccionarBusqueda(self):
        to = 60
        accion = u'Hacer clic en el Boton Busqueda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_Busqueda
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
########## COBRO DE MULTAS

    def seleccionarCobroDeMultas(self):
        to = 10
        accion = u'Seleccionar Cobro de Multas'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cobroDeMulta
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_cuenta3(self, cuenta):
        to = 10
        accion = u'Ingresar Cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_cuenta
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, cuenta, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def ingresar_cuenta4(self, cuenta):
        to = 10
        accion = u'Ingresar Cuenta'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datosCheques_2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, cuenta, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
    
    
    def msg_NohayMultasInpagas(self):
        to = 10
        accion = u'"No hay multas impagas asociadas a esta cuenta"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.msg_not_Multas
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
                self.skip_msg(msgOk)
            else:
                pass           
             
    def seleccionarCheckMulta(self):
        to = 60
        accion = u'Marcar el check para seleccionar la Multa'
        msgOk = accion
        msgFail = u'No se udo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.chek_multa
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.fail_msg(msgFail)

    def validarCantidadDeCheques2(self,dato):
        to = 10
        accion = u'Validar Cantidad De Cheques en la operacion '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_cantidadCheques2.format(dato)
            xpath_1 = plCajaInicio.lbl_cantidadCheques4.format(dato)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la cantidad de cheques: {}".format(self.cantidad))  
            elif self.visibility_element(xpath_1, to):  
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath_1).get_property('innerHTML')
                self.highlight(xpath_1, accion)
                print(u"Se validad la cantidad de cheques: {}".format(self.cantidad))
            else:
                self.fail_msg(msgFail)

    def validarMoneda2(self,moneda):
        to = 10
        accion = u'Validar moneda'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_monedavalidar.format(moneda)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad la moneda: {}".format(self.cantidad))
                
            else:
                self.fail_msg(msgFail)

    def validarImporteTotalACobrar(self,importe):
        to = 10
        accion = u'Validar importe total a cobrar '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_importeTotal.format(importe)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad importe total a cobrar : {}".format(self.cantidad))
                
            else:
                self.fail_msg(msgFail)

############ REVERSO DE TRANSSACCION

    def seleccionarRevesoDeTrasaccion(self):
        to = 10
        accion = u'Seleccionar Reverso de Transaccion'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.lbl_reversoTrassaccion
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def ingresarNroTranssaccion(self,numero):
        to = 10
        accion = u'Ingresar Numero de transsacion'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.imput_NroSecuencia
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, numero, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)

    def mostrarTiposDeMotivos(self):
        to = 10
        accion = u'Hacer clic en el recuadro Motivo'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_motivo
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.go_to_xpath(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionarMotivo(self, motivo):
        to = 10
        accion = u'Seleccionar motivo {} '.format(motivo)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.opt_select.format(motivo)
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def validar_salida_de_msg(self):
        """Metodo para esperar que desaparezca 
        el mensaje que oculta cualquier boton"""
        intentos = 0
        while self.visibility_element2(plCajaInicio.msgExito_consulta.format("Impresion finalizada con exito")):
            intentos +=1
            if int(intentos) == 5000:
                self.fail_msg("El mensaje no a desaparecido")
        else:
            pass



    def seleccionar_buscar_cuentas(self):
        to = 60
        accion = u'Hacer clic en el Boton BUSCAR CUENTAS'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_buscarCuentas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
                
                
                
############ RECEPCION DE REMESAS

    def seleccionar_recepcion_de_Remesas(self):
        to = 10
        accion = u'Seleccionar RECEPCION DE REMESAS'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_recepcionDeRemesas
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)          
    
    
    
            
    def hacer_click_en_tilde_verde(self):
        to = 10
        accion = u'Seleccionar RECEPCION DE REMESAS'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.tilde_verde
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)        
                

    def movimiento_de_el_mouse_ala_celda(self):
        """Simular movimiento de mouse en Dicha selda"""
        celda = self.driver.find_element(By.XPATH, "//tr[@role='row'][contains(.,'Uic10022 - Tesoro Intermedio')]")
        webdriver.ActionChains(self.driver).click_and_hold(celda).perform()
        self.hacer_click_en_tilde_verde()
        
        
    def visualizar_msj_saldos_excedido(self):
        to = 60
        accion = u'Visualizar el Mensaje Saldo excedido en CAJA o CAF Continuar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.msj_saldos_excedidos
            if self.visibility_element(xpath, to): 
                self.highlight(xpath,accion)
                self.seleccionarContinuar()
            else:
                msgFail(msgFail)
      

    def visualizar_msj_cheques_sin_firmantes(self):
        to = 60
        accion = u'Visualizar el Mensaje Saldo excedido en CAJA o CAF Continuar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.msj_cheque_sin_firmantes
            if self.visibility_element(xpath, to): 
                self.highlight(xpath,accion)
                self.skip_msg(msgOk)
            else:
                pass


#CONSULTA DE REMESA GENERAL POR SUCURSAL

    def seleccionar_consulta_remesa_general_por_sucursal(self):
        to = 10
        accion = u'Seleccionar CONSULTA DE REMESA GENERAL POR SUCURSA'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):  
            xpath = plCajaInicio.lbl_consulta_de_remesa_general_por_sucursal
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_pago_de_jubilaciones_italianas(self):
        to = 10
        accion = u'Seleccionar Pago de Jubilaciones Italianas'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_pago_de_jubilaciones
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def visualizar_msj_no_hay_beneficios(self):
        to = 60
        accion = u'Visualizar el mensaje: No hay beneficios de pensiones italianas pendientes de pago para este beneficiario '
        msgSkip = accion
        with self.step(accion):            
            xpath = plCajaInicio.msj_sin_beneficios
            if self.visibility_element(xpath, to):
                self.skip_msg(msgSkip)
            else:
                pass   
                
    def seleccionar_item_nro_de_pension(self):
        to = 10
        accion = u'Seleccionar item numero de pension'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_numero_de_pension
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
                
    def seleccionar_item_tipo_doc(self):
        to = 10
        accion = u'Seleccionar item numero de documento'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_numero_de_doc
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    

                
    def ingresar_nro_pension(self, nro_pension):
        to = 10
        accion = u'Ingresar numero de pension {}'.format(nro_pension)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_nro_pension
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, nro_pension, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
    

    def visualizar_datos_pension(self):
        to = 10
        accion = u'Visualizar Datos de pension'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_pension
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def visualizar_datos_pension_2(self):
        to = 10
        accion = u'Visualizar Datos de pension'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_pension_3
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def visualizar_campo_pagos_pendientes(self):
        to = 10
        accion = u'Visualizar campos de pagos pendientes'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_pagos_pendientes
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
      
    def seleccionar_pago_pendiete(self):
        to = 10
        accion = u'Seleccionar Pago pendiente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_pago
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)      

    def seleccionar_pago_pendiete_2(self):
        to = 10
        accion = u'Seleccionar Pago pendiente'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_pago_2
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)                        
                
    def visualizar_datos_pension2(self):
        to = 10
        accion = u'Visualizar Datos de pension'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_pension_2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
  
    def visualizar_datos_pension_3(self):
        to = 10
        accion = u'Visualizar Datos de pension'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_pension_4
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                              
                
    def seleccionar_item_beneficiario(self):
        to = 10
        accion = u'Seleccionar item beneficiario'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_beneficiario
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    

    def seleccionar_item_beneficiario_2(self):
        to = 10
        accion = u'Seleccionar item beneficiario'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_beneficiario_2
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
                
    def visualizar_datos_de_la_pantalla(self):
        to = 10
        accion = u'Visualizar Datos de pantalla'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_pantalla
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def mostrar_tipos_documento(self):
        to = 10
        accion = u'Mostrar select tipos documento'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipo_doc
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
  
  
    def ingresar_nro_doc(self, nro_documento):
        to = 10
        accion = u'Ingresar numero de pension {}'.format(nro_documento)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_nro_documento
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, nro_documento, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)  
                         
    def ingresar_nro_doc_2(self, nro_documento):
        to = 10
        accion = u'Ingresar numero de pension {}'.format(nro_documento)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_nro_documento_2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, nro_documento, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)           
                
                
    def visualizar_datos_de_comfirmacion(self):
        to = 10
        accion = u'Visualizar Datos de pension'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_operacion
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def visualizar_datos_de_comfirmacion_2(self):
        to = 10
        accion = u'Visualizar Datos de pension'
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_operacion_2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)                
                
    def seleccionar_siguiente_4(self):
        to = 60
        accion = u'Hacer clic en el Boton SIGUIENTE'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_siguiente_4
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def visualizar_msj_no_hay_operadores_activos(self):
        to = 60
        accion = u'Visualizar el Mensaje no hay operadores activos'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):            
            xpath = plCajaInicio.msg_exito_no_hay_operadores_activos
            if self.visibility_element(xpath, to):
                msj_esperado = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                self.capture_image("Mensaje encontrado: {}".format(msj_esperado))
            else:
                pass
            
    def verificar_caracteres_repetidos_en_el_ticket(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.visibility_element("//html/body/p[text()]", 2)
        lista = self.driver.find_element_by_xpath("//html/body/p[text()]").get_property('innerText')
        lista = lista.replace("""Declaro bajo juramento que la presente operacion se encuentra enmarcada en el concepto A09

de las normas de Comercio Exterior y Cambios del BCRA, dentro de los limites y requisitos

fijados por la Comunicacion A 6770 dentro de los limites y requisitos fijados por la

Comunicacion A 6770, modificatorias y complementarias. La presente operacion no se ha

cursado ni se cursara por ninguna otra via, y los fondos destinados a la misma corresponden

a fondos genuinos que guardan relacion con mi situacion patrimonial. La determinacion del

impuesto PAIS se calculara sobre el importe en pesos utilizado en el momento de la adqui-

sicion de la moneda extranjera. Manifiesto que no soy beneficiario de los Creditos a Tasa

Cero acordados en el marco del articulo 9 del Decreto Nro. 332/2020 (y modificatorias).

Me comprometo a no realizar ventas de titulos valores con liquidacion en moneda extranjera

en el pais o transferencias de los mismosa entidades depositarias del exterior desde este

momento y durante los 90 dias corridos subsiguientes. Declaro bajo juramento que los fondos

adquiridos no superan los limites establecidos en los apartados 1) y 2) de la Comunicacion

A 7106 BCRA sus modificatorias y complementarias. No soy funcionario publico nacional con

rango superior de Subsecretario de Esta do (o rango equivalente),ni miembro de directorio

de banco publico nacional y del BCRA. Las informaciones consignadas son exactas y verda-

deras, y se han efectuado sin omitir,ni falsear dato alguno en los terminos previstos en

el Regimen Penal Cambiario, normas impositivas y demas normas aplicables, de las cuales

tengo pleno conocimiento, incluidas las sancio nes que disponen.

Declaro no estar alcanzado por lo indicado en la comunicacion BCRA A 7735








 -------------------------------------- 

RECIBI CONFORME 

TITULAR/APODERADO/CURADOR/TUTOR 



Aclaracion: 



La firma del presente ticket implica 

la plena conformidad del importe pagado"""," ")   
        print(lista)
        palabras = lista.split() 
        for palabra in palabras:
            if palabras.count(palabra)==2:                
                print("El la palabra (---{}---) se repite en el ticket ".format(palabra))
 
                
    def seleccionar_buscar_pension(self):
        to = 60
        accion = u'Hacer clic en el boton BUSCAR PENSION'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_buscar_pension
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_nro_pension(self):
        to = 10
        accion = u'Seleccionar numero de pension'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_numero_de_pension_2
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    


    def mostrar_tipo_doc_2(self):
        to = 10
        accion = u'mostrar tipo de documentos '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_cuenta2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.go_to_xpath(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
 
    def visualizar_comprobante(self):
        from datetime import date
        fecha_actual = date.today()         
        to = 10
        accion = u'Visualizar comprobante {}'.format(fecha_actual)
        msgOk = accion
        msgFail = "no se pudo " + msgOk 
        with self.step(accion):
            xpath = plCajaInicio.data_comprobante
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)

            else:
                self.fail_msg(msgFail)
   
    def ventana_saldo_excedido_en_caja_o_caf(self):
        to = 10
        accion = u'Verificar Mensaje de saldo Exedido en Caja o Caf'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        xpath = plCajaInicio.slp_saldoExedidoCajaCaf
        if self.visibility_element(xpath, to):
            self.highlight(xpath,msgOk)
            self.wait(1)
            self.highlight(xpath,msgOk)
            self.selectElement(plCajaInicio.btn_continuar, msgOk, msgFail, to)
        else:
            pass


    def seleccionar_deposito_de_plazo_fijo_en_cuenta(self):
        to = 10
        accion = u'Seleccionar certificacion de firma'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_deposito_plazo_fijo_en_cuenta
            self.jsClick(xpath)
            self.capture_image(msgOk)

    def seleccionar_recuadro_cuenta_debito_PL(self):
        to = 10
        accion = u'Seleccionar recuadro cuenta debito'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.div_cuentas_debito
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
                
    def seleccionar_item_cuenta(self):
        to = 10
        accion = u'Seleccionar cuenta debito '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_cuenta_cc
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    

    def seleccionar_recuadro_tp_plazo_fj(self):
        to = 10
        accion = u'Seleccionar recuadro Tipo de plazo fijo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.div_plazos_fj
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    

    def seleccionar_fecha_Vecimiento(self):
        to = 10
        accion = u'Seleccionar circulos fecha de vencimiento'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.circle
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_calendario(self):
        to = 10
        accion = u'Seleccionar calendario'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.button_calendario
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionar_item_plazo_fj(self,tipo):
        to = 10
        accion = u'Seleccionar cuenta tipo de plazo fijo {}'.format(tipo)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_tipo_plazo_fijo.format(tipo)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def ingresar_dias(self, dia):
        to = 10
        accion = u'Ingresar numero de dias'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.ipt_dia
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, dia, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionar_bto_simular(self):
        to = 60
        accion = u'Hacer clic en el boton simular'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_simular
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def visualizar_datos_de_simulacion(self):
        to = 10
        accion = u'Visualizar datos de simulacion'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.datos_simulacion
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)  

    def seleccionar_confirmar(self):
        to = 10
        accion = u'Hacer clic en el Boton CONFIRMAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_confirmar_2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)

    def seleccionar_check_marca_si_coincide(self):
        to = 60
        accion = u'Hacer clic en el check marca si coincide'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_marca_si_coincide
            if self.visibility_element(xpath, to):
                self.wait(1)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_consulta_de_plazo_fijo(self):
        to = 10
        accion = u'Seleccionar consulta de plazo fijo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_consulta_de_plazo_fijo
            self.jsClick(xpath)
            self.capture_image(msgOk)
            
    
    def seleccionar_pago_de_plazo_fijo(self):
        to = 10
        accion = u'Seleccionar Pago de plazo fijo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_pago_de_plazo_fijo
            self.jsClick(xpath)
            self.capture_image(msgOk)
     
     
    def seleccionar_imprimir(self):
        to = 10
        accion = u'Hacer clic en el Boton imprimir'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_imprimir
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)   
    
    def validar_cliente(self,cliente):
        to = 10
        accion = u'Validar cliente: {}'.format(cliente)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cbu.format(cliente)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad cliente: {}".format(cliente))
                
            else:
                self.fail_msg(msgFail)
                
                
    def validar_dni(self,dni):
        to = 10
        accion = u'Validar dni: {}'.format(dni)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.text_cbu.format(dni)
            if self.visibility_element(xpath, to):
                self.cantidad = self.driver.find_element(by=By.XPATH, value=xpath).get_property('innerHTML')
                self.highlight(xpath, accion)
                print(u"Se validad dni: {}".format(dni))
                
            else:
                self.fail_msg(msgFail)


    def ingresar_nro_certificado(self, numero):
        to = 10
        accion = u'Ingresar numero de certificado: {}'.format(numero)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_nro_certificado
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, numero, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)



    def visualizar_msj_no_hay_deposito_disponible(self):
        to = 60
        accion = u'Visualizar el mensaje Deposito no disponible para pago'
        msgSkip = accion
        with self.step(accion):            
            xpath = plCajaInicio.msj_no_hay_deposito
            if self.visibility_element(xpath, to):
                self.skip_msg(msgSkip)
            else:
                pass
            
    def visualizar_datos_plazo_fijo(self):
        to = 60
        accion = u'Visualizar en pantalla los datos del Plazo Fijo Efectivo'
        msg_fail = u"nose pudo", accion
        with self.step(accion):            
            xpath = plCajaInicio.datos_plazo_fijo
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)    
            else:
                self.fail_msg(msg_fail)

    
    def visualizar_firmante(self):
        to = 60
        accion = u'Visualizar firmantes'
        msg_fail = u"nose pudo", accion
        with self.step(accion):            
            xpath = plCajaInicio.recueadro_firmante
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)    
            else:
                self.fail_msg(msg_fail)                


    def seleccionar_chek_firmante(self):
        to = 10
        accion = u'hacer click en check firmantes'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_firmante
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)  
                
##### COMPRA MONEDA EXTRANJERA

    def seleccionar_compra_moneda_extranjera(self):
        to = 10
        accion = u'Seleccionar compra moneda extranjera'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_compra_moneda_extranjera
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
   

   
    def seleccionar_tipo_documento(self):
        to = 10
        accion = u'Seleccionar recuadro tipo de documento'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipo_doc_4
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_item_DNI(self):
        to = 10
        accion = u'Seleccionar tipo de docuento "DNI"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_DNI
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
             
    def ingresar_numero_de_DNI(self,DNI):
        to = 10
        accion = u'Ingresar numero de documento {}'.format(DNI)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_dni
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, DNI, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)

    def seleccionar_debe_precentar(self):
        to = 10
        accion = u'Seleccionar recuadro debe precentrar'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_debe_precentar
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_item_CUIL(self):
        to = 10
        accion = u'Seleccionar tipo de CUIL'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_CUIL
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)

    def ingresar_numero_CUIL(self,CUIL):
        to = 10
        accion = u'Ingresar numero de CUIL {}'.format(CUIL)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_cuil
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, CUIL, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_moneda(self):
        to = 10
        accion = u'Seleccionar recuadro moneda'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_tipo_moneda
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_item_MONEDA(self):
        to = 10
        accion = u'Seleccionar tipo de MONEDA "Dolares"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_MONEDA
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
    
    
    def ingresar_importe_a_comprar(self,importe):
        to = 10
        accion = u'Ingresar importe a comprar {}'.format(importe)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_importe_a_comprar
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, importe, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_button_cotizar(self):
        to = 10
        accion = u'Seleccionar boton cotizar'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.button_cotizar
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def visualizar_cotizacion(self):
        to = 10
        accion = u'Visualizar cotizacion'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.label_cotizacion
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_test(msgFail)
                
    def visualizar_ticket(self):
        to = 10
        accion = u'Visualizar ticket'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.html_ticket
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_test(msgFail)
    def seleccionar_Confirmar(self):
        to = 10
        accion = u'Hacer clic en el Boton CONFIRMAR'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_confirmar
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)
                
##### VENTA MONEDA EXTRANJERA

    def seleccionar_venta_moneda_extranjera(self):
        to = 10
        accion = u'Seleccionar  venta moneda extranjera'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_venta_moneda_extranjera
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
##### PAGO DE VALES


    def seleccionar_pago_de_vales(self):
        to = 10
        accion = u'Seleccionar pago de vales'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_pago_de_vales
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)


    def seleccionar_reacuadro_cuenta_debito(self):
        to = 10
        accion = u'Seleccionar reacuadro cuando debito'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_rdo_cuenta_debito
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_item_cuenta_dbt(self,cuenta):
        to = 10
        accion = u'Seleccionar Cuenta Débito "ARP - 10010218006 RESERVA DEL NORTE TEST 100.000,00'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_cuenta_dbt_2.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)

    def ingresar_numero_de_DNI_2(self,DNI):
        to = 10
        accion = u'Ingresar numero de documento: {}'.format(DNI)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_dni_2
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, DNI, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def ingresar_numero_de_legajo(self,legajo):
        to = 10
        accion = u'Ingresar numero de legajo: {}'.format(legajo)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_legajo
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, legajo, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def ingresar_numero_de_comprobante(self,comprobante):
        to = 10
        accion = u'Ingresar numero de comprobante: {}'.format(comprobante)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_comprobante
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, comprobante, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def ingresar_monto(self,monto):
        to = 10
        accion = u'Ingresar monto: {}'.format(monto)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_monto
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_reacuadro_Numero_de_Legajo(self):
        to = 10
        accion = u'Seleccionar reacuadro numero de legajo'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_rdo_numero_de_legajo
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
                
##### REINTEGRO DE VALES

    def seleccionar_reintegro_de_vales(self):
        to = 10
        accion = u'Seleccionar Reintegro de vales'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_reintegro_de_vales
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)

    def ingresar_numero_de_DNI_3(self,DNI):
        to = 10
        accion = u'Ingresar numero de documento: {}'.format(DNI)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_dni_3
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.write(xpath, DNI, to)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
###LISTADO DE CAJA CHICA
    
    def seleccionar_listado_de_caja_chica(self):
        to = 10
        accion = u'Seleccionar listado de caja chica '
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_listado_de_caja_chica
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)


###CIERRE FORZADO

    def seleccionar_cierre_forzado(self):
        to = 10
        accion = u'Seleccionar cierre forzado'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cierre_forzado
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
                
    def seleccionar_recuadro_operadores(self):
        to = 10
        accion = u'Seleccionar  reacuadro operadores'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.slc_rdo_operadores
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_verificar_operadores(self):
        to = 10
        accion = u'Verificar Operadores'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.list_operadores       
            if self.visibility_element(xpath, to):
                self.operadores = self.driver.find_element(by=By.XPATH, value=xpath).get_property('textContent')
                return self.operadores.strip()
            else:
                self.fail_test(msgFail)
                return self.operadores

    def seleccionar_item_operador(self,operador):
        to = 10
        accion = u'Seleccionar operador {}'.format(operador)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_cuenta_dbt.format(operador)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
                
    def seleccionar_sin_diferencia(self,posicion):
        to = 10
        accion = u'Seleccionar sin diferencia en celda {}'.format(posicion)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_saldos.format(posicion)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
                
    def seleccionar_cerrar_caja(self):
        to = 10
        accion = u'Seleccionar Cerrar Caja'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cerrar_caja
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_cancelar(self):
        to = 10
        accion = u'Seleccionar Cancelar'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cancelar
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
 
    def contar_los_operadores_activos(self):
        xpath_desplegable = "//div[contains(@id,'mat-select-0-panel')]"
        desplegable = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_desplegable)))
        opciones = desplegable.find_elements_by_tag_name("mat-option")
        self.cantidad_de_items = len(opciones)
        print("Número de items en el desplegable:", self.cantidad_de_items)
        return self.cantidad_de_items
                
    def verificar_operadores_activos(self):    
        self.seleccionar_cierre_forzado() 
        self.seleccionar_recuadro_operadores()
        self.vueltas = self.contar_los_operadores_activos()
        self.wait(2)
        self.seleccionar_cancelar()
        
        
###COBROS SIRES 

    def seleccionar_cobros_sires(self):
        to = 10
        accion = u'Hacer clic en la trassacicion Cobro servicios - SIRE'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cobros_sire
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_barra(self):
        to = 10
        accion = u'Tipo de Servicio a Abonar "BARRA"'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_barra
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
                
                
    def seleccionar_recuadro_servicios(self):
        to = 10
        accion = u'seleccionar recuadro servicios'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.recuadro_servicio
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)

    def seleccionar_servicio(self,servicio):
        to = 10
        accion = u'seleccionar servicios {}'.format(servicio)
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_servicio.format(servicio)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def ingresar_codigo_de_barra(self, codigo):
        to = 10
        accion = u'Ingresar  codigo de barra: {}'.format(codigo)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_codigo_barra
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, codigo, to)
                self.wait(2)
                self.driver.find_element(by=By.XPATH, value=xpath).send_keys(Keys.RETURN)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
            
            
    def visualizar_datos_servicio(self):
        to = 10
        accion = u'Visualizar pantalla con datos del Servicio'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.datos_servicio
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                self.fail_test(msgFail)
                
    def ingresar_monto_servicio(self, monto):
        to = 10
        accion = u'Ingresar monto: {}'.format(monto)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_monto
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
                
#####COBROS CML



    def seleccionar_cobros_CML(self):
        to = 10
        accion = u'Hacer clic en la trassacicion Cobro CML'
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_cobros_cml
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_test(msgFail)
                
    def seleccionar_check_box(self):
        to = 60
        accion = u'Hacer hecklist en "Mismo Documento que Cliente Identificado'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.check_box_mismo_doc
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
                
    def seleccionar_siguiente_5(self):
        to = 60
        accion = u'selecionar btn siguiente'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_siguiente_5
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_reacuadro_C_H(self):
        to = 60
        accion = u'Hacer clic en Convenios Habilitados'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.recuadro_c_h
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_opcion_(self, option):
        to = 60
        accion = u'Seleccionar : {}'.format(option)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_cobros_cml.format(option)
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_siguitente_6(self):
        to = 60
        accion = u'Seleccionar siguiente '
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.siguiente_6
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_nuevo_doc(self):
        to = 60
        accion = u'Seleccionar nuevo doc'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.b_nuevo_doc
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_recuadro_tipo(self):
        to = 60
        accion = u'Seleccionar reacuadro tipo'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.recuadro_tipo
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
        
    def seleccionar_factura(self):
        to = 60
        accion = u'Seleccionar Factura'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.factura
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                               
    def ingresar_numero(self, NRO):
        to = 10
        accion = u'Ingresar numero: {}'.format(NRO)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.imput_numero
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, NRO, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
    def ingresar_cuota(self, NRO):
        to = 10
        accion = u'Ingresar numero de cuotas: {}'.format(NRO)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.imput_cuota
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, NRO, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)


    def seleccionar_agregar(self):
        to = 60
        accion = u'Seleccionar agregar'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_agregar
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_flecha_azul(self):
        to = 60
        accion = u'Seleccionar flecha azul'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.flecha_azul_claro
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
              
              
    def validar_monto_en_verde(self,monto):
        to = 60
        accion = u'Seleccionar validar monto : {} en color verde'.format(monto)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.monto_validar.format(monto)
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk )
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
 
    def seleccionar_fin_de_carga(self):
        to = 60
        accion = u'Hacer clic en el Boton FIN DE CARGA'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_fin_de_carga
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.wait(2)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
    def seleccionar_NO(self):
        to = 60
        accion = u'¿Se utilizarán CHEQUES para realizar el pago de esta transacción? Hacer clic en "NO"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_NO
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
    def seleccionar_SI(self):
        to = 60
        accion = u'¿Se utilizarán CHEQUES para realizar el pago de esta transacción? Hacer clic en "SI"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_SI
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
 
    def visualizar_datos_resumen(self):
        to = 60
        accion = u'visualizar datos de resumen'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.datos_resumen
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk )
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
              
    def ingresar_monto_3(self, monto):
        to = 10
        accion = u'Ingresar monto: {}'.format(monto)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_monto_3
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
    
    def ingresar_monto_servicio_2(self, monto):
        to = 10
        accion = u'Ingresar monto: {}'.format(monto)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.imput_monto_2
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
                
            
    def selecionar_boton_costumers(self):
        to = 10
        accion = u'seleccionar btn Costumers'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_costumeres
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                

    def seleccionar_imprimir_2(self):
        to = 10
        accion = u'Hacer clic en el Boton imprimir'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_imprimir_2
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.highlight(xpath, accion)
                self.jsClick(xpath)
            else:
                self.fail_msg(msgFail)   
  
    def obtener_nro_del_dia(self,Dia):
        accion = u'obetener numero del dia del mes'
        with self.step(accion):
            import datetime
            if Dia == "Mañana": 
                fecha_actual = datetime.date.today()        
                dia = fecha_actual.day 
                return dia + 1
            
            elif Dia == "viernes": 
                fecha_actual = datetime.date.today()        
                dia = fecha_actual.day 
                return dia + 3
            
            elif Dia == "hoy": 
                fecha_actual = datetime.date.today()        
                dia = fecha_actual.day 
                return dia

    
    def obtener_anio(self):
        accion = u'obetener numero del dia del mes'
        with self.step(accion):
            import datetime
            fecha_actual = datetime.date.today()        
            numero_dia = fecha_actual.year
            return numero_dia 
        
    def obtener_nro_del_mes(self):
        accion = u'obetener numero del mes'
        with self.step(accion):
            import datetime
            fecha_actual = datetime.date.today()        
            mes = fecha_actual.month  
            if mes == 1:
                mes = "enero" 
                         
            elif mes == 2:
                mes = "febrero" 
                                    
            elif mes == 3:
                mes = "marzo"   
                
            elif mes == "4":
                mes = "abril"   
                        
            elif mes == "5":
                mes = "mayo"  
                      
            elif mes == "6":
                mes = "junio"  
                      
            elif mes == "7":
                mes = "julio"  
                      
            elif mes == "8":
                mes = "agosto"  
                   
            elif mes == "9":
                mes = "septiempre"
                
            elif mes == "10":
                mes = "octubre"   
                
            elif mes == "11":
                mes = "noviembre"
                
            elif mes == "11":
                mes = "diciembre"    
            return mes   
            
  
                
    def seleccionar_calendario_cheques(self):
        to = 60
        accion = u'Seleccionar Fecha "Al dia de Hoy"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_calendario
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_fecha_de_hoy(self,day,month,year):
        to = 60
        accion = u'Seleccionar Fecha "Al dia de Hoy"'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.td_fecha.format(day,month,year)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
     
    def enter(self,xpath):
        to = 2
        accion = u'Precionar Enter'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.driver.find_element(by=By.XPATH, value=xpath).send_keys(Keys.RETURN)
                return msgOk
            else:
                self.fail_msg(msgFail)           
                

                
    def ingresarDatos_cobros_cml_cheques(self,dato,text,cheque):
        to = 10
        accion = u'Ingresarr:' + u' '+ text
        msgOk = accion
        msgFail = u'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_datos_cheques.format(dato)
            if self.visibility_element(xpath, to):
                if dato == "banco":
                    self.write(xpath,"007",to)           
                    self.capture_image(msgOk)      
                elif dato == "sucursal":
                    self.write(xpath,"047" ,to)           
                    self.capture_image(msgOk)      
                elif dato == "codigoPostal":
                    self.write(xpath,"1227",to)           
                    self.capture_image(msgOk)    
                elif dato == "numeroCheque":
                    self.write(xpath,cheque,to)           
                    self.capture_image(msgOk)
                elif dato == "numeroCuenta":
                    self.write(xpath,"00014587545",to)
                    self.capture_image(msgOk)
                    self.enter(xpath)
                else:
                    self.capture_image(msgOk)
                    self.fail_msg(msgFail) 
            else:
                self.capture_image(msgFail, to)
                self.fail_msg(msgFail)
                
    def ingresar_datos_de_chequera_cml(self,cheque):
        datos = ["banco","sucursal","codigoPostal","numeroCheque","numeroCuenta"]
        texto = ["Banco ", "Sucursal ", "Codigo Postal ", "Numero de Cheque ",
                "Numero de Cuenta "]
        for dato,text in zip(datos,texto):
            self.ingresarDatos_cobros_cml_cheques(dato,text,cheque)
            


    def seleccionar_fin_de_carga_2(self):
        to = 60
        accion = u'Hacer clic en el Boton FIN DE CARGA'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_fin_de_carga_2
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def ingresar_monto_debito(self, monto):
        to = 10
        accion = u'Ingresar monto: {}'.format(monto)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.input_monto_5
            if self.selectElement(xpath, msgOk, msgFail, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else: 
                self.fail_msg(msgFail)
                
                
    def seleccionar_recuadro_cuentas_debito(self):
        to = 60
        accion = u'Hacer clic el recuadro cuentas debito'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.recuadro_cuentas_debito
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_cuentas_debito(self,cuenta):
        to = 60
        accion = u'seleccionar cuenta {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_cuentas_debito.format(cuenta)
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_btn_si_coincide(self):
        to = 60
        accion = u'Hacer clic el boton si consincide'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.btn_coincide
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_formas_de_pago(self):
        to = 60
        accion = u'Hacer clic en formas de pago'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.recuadro_pagos
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                

    def seleccionar_pago(self,cuenta):
        to = 60
        accion = u'Hacer clic en formas de pago en cuenta: {}'.format(cuenta)
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.item_pago.format(cuenta)
            if self.visibility_element(xpath, to):
                self.jsClick(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def visualizar_datos_moneda_cambio(self):
        to = 60
        accion = u'visualizar datos de moneda cambio'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()
        with self.step(accion):
            xpath = plCajaInicio.datos_moneda_cambio
            if self.visibility_element(xpath, to):
                self.highlight(xpath,msgOk )
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def visualizar_pdf(self):
        to = 10
        accion = u'visualizar datos de pdf'
        msgOk = accion
        with self.step(accion):
            xpath = plCajaInicio.datos_pdf
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
                self.skip_msg(msgOk)
            else:
                pass

    def visualizar_datos_moneda_extranjera(self):
        to = 60
        accion = u'Visualizar datos de moneda extranjera'
        msgOk = accion
        with self.step(accion):            
            xpath = plCajaInicio.dato_moneda_extranjera
            if self.visibility_element(xpath, to):
                self.highlight(xpath, msgOk)
            else:
                pass