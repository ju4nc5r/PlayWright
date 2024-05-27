'''
Created on 27 may. 2022

@author: GON13535
'''
# -*- coding: utf-8 -*-
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.js import js


class stMesaWebFCI(js):

    
    def seleccionar_fci(self):
        to = 10
        accion = u'Seleccionar FCI'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.FCI
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_liquidacion(self):
        to = 10
        accion = u'Seleccionar liquidacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.liquidacion
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_movimiento(self):
        to = 10
        accion = u'Seleccionar movimiento'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.movimiento
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_movimiento_a_imputar(self):
        to = 10
        accion = u'Seleccionar movimiento a imputar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.movimiento_a_imputar
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                                

    def seleccionar_procesos(self):
        to = 10
        accion = u'Seleccionar procesos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.procesos
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_autorizaciones_pendientes(self):
        to = 10
        accion = u'Seleccionar procesos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.auto_pendientes
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                

    def seleccionar_check_ok(self):
        to = 10
        accion = u'Seleccionar check ok'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.check_ok
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_aprobar(self):
        to = 10
        accion = u'Seleccionar aprobar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.check_ok
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_aceptar_autoriz(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_aceptar
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_btn_aprobar(self):
        to = 10
        accion = u'Seleccionar aprobar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_aprobar
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_acciones(self):
        to = 10
        accion = u'Seleccionar Acciones'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.acciones
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_titulos(self):
        to = 10
        accion = u'Seleccionar Titulos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.titulos
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_venta(self):
        to = 10
        accion = u'Seleccionar venta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.venta
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def seleccionar_venta_2(self):
        to = 10
        accion = u'Seleccionar venta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.venta_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def seleccionar_compra(self):
        to = 10
        accion = u'Seleccionar compra'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.compra
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)              

    def seleccionar_compra_2(self):
        to = 10
        accion = u'Seleccionar compra'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.compra_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
                
    def completarNroCliente(self,nro_cliente):
        accion = u'Completar Nro de cliente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.input_cliente
            to = 10
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath, nro_cliente, to)
                self.wait(1)
                self.capture_image(accion)
            else:    
                self.fail_msg(msgFail)
                
    
    def seleccionarBuscarCliente_por(self, xpath):
        self.abrir_tipoCliente()
        to = 10
        accion = u'seleccionar cliente '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    
    def abrir_tipoCliente(self):
        to = 10
        accion = u'abrir tipos de clientes'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.lista_cliente
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_item_nro_cliente(self):
        to = 10
        accion = u'seleccionar numero de cliente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.tipo_cliente_Nro
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_btn_buscar_cliente(self):
        to = 10
        accion = u'buscar cliente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_buscarCliente
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
                
    def seleccionar_btn_compra_del_banco(self):
        to = 10
        accion = u'seleccionar boton compra del banco'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_compra_banco
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def seleccionar_btn_venta_del_banco(self):
        to = 10
        accion = u'seleccionar boton venta del banco'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_venta_banco
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def seleccionar_check_box(self):
        to = 10
        accion = u'seleccionar check box'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.check_box
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  

    def validarCliente(self, mensaje_esperado, xpath):
        to = 10
        accion = u'Validar cliente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):            
            if self.visibility_element(xpath,to):
                self.compareText(xpath, mensaje_esperado)
                self.highlight(xpath, msgOk)
            else:
                self.fail_msg(msgFail)        
                
    def select_btn_siguiente(self, xpath):
        to = 10
        accion = u'Seleccionar siguiente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                 
                
    def select_item_fondo(self, xpath):
        to = 10
        accion = u'Seleccionar GOAL AHORRO MAX CLASE B'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
    def select_btn_suscripcion(self, xpath):
        to = 10
        accion = u'Seleccionar boton suscripcion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
    def select_btn_rescate_por_cuota_parte(self, xpath):
        to = 10
        accion = u'Seleccionar boton rescate por cuota parte'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                

    def select_btn_fondos_comunes(self, xpath):
        to = 10
        accion = u'Seleccionar boton fondos comunes'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)                
                
    def select_btn_venta_banco(self, xpath):
        to = 10
        accion = u'Seleccionar boton venta de banco'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

                
    def select_btn_aceptar(self, xpath):
        to = 10
        accion = u'Seleccionar siguiente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def select_btn_aceptar_ord_venta(self, xpath):
        to = 10
        accion = u'Seleccionar Boton Orden de venta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
    
    def select_btn_compra_banco(self, xpath):
        to = 10
        accion = u'Seleccionar boton compra banco'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                  

    def select_nom_razon_social(self, xpath):
        to = 10
        accion = u'Seleccionar nombre razon social'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_btn_seleccionar(self, xpath):
        to = 10
        accion = u'Seleccionar seleccionar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)     
                
    
    def seleccionar_recuadro_instrumentos(self, xpath):
        to = 10
        accion = u'Seleccionar recuadro instrumentos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_instrumento(self,instrumento):
        accion = u'Seleccionar instrumento'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.lista_instrumentos
            to = 10
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath, instrumento, to)
                self.wait(1)
                self.send_key(xpath,"down")
                self.send_key(xpath, "enter")
                self.capture_image(accion)
            else:    
                self.fail_msg(msgFail)            
                
    
# Metodos para buscar ultimo precio y grabar ese dato   
    
    def ingresar_monto(self,precio):
        to = 10
        accion = u'Ingresar monto'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.imput_monto
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath,precio, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
    
    def ingresar_cuotas(self,cuotas):
        to = 10
        accion = u'Ingresar cuotas {}'.format(cuotas)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.imput_cuotas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath,cuotas, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    
    def buscar_precio(self):
        accion = u'Buscar precioo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.ultimo_precio
            to = 10
            if self.visibility_element(xpath, to):
                precio = self.get_element_text(xpath)
                print (precio)
                precio = self.modificar_precio(precio)
                print (precio)
                self.wait(2)
                self.capture_image(accion)
                return precio
            else:    
                self.fail_msg(msgFail)

    def buscar_precio_2(self):
        accion = u'Buscar precioo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.ultimo_precio
            to = 10
            if self.visibility_element(xpath, to):
                precio = self.get_element_text(xpath)
                print (precio)
                precio = self.modificar_precio_2(precio)
                print (precio)
                self.wait(2)
                self.capture_image(accion)
                return precio
            else:    
                self.fail_msg(msgFail)

                
    def modificar_precio(self, precio):
        precio = precio[19:]
        precio = str(precio).replace(",",".")
        return precio
    
    def modificar_precio_2(self, precio):
        precio = precio[19:]
        precio = str(precio).replace(",000000","")
        return precio

# Metodo para ingrear CANTIDAD

    def ingresar_cantidad(self, cantidad):
        to = 10
        accion = u'Ingresar cantidad'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.cantidad_VN
            if self.visibility_element(xpath, to):
                #self.selectElement(xpath, msgOk, msgFail, to)
                #self.wait(2)
                self.write(xpath, cantidad, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                

    def ingresar_instrumento(self, instrumento):
        to = 10
        accion = u'Ingresar instrumento {}'.format(instrumento)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.readro_instrumentos
            xpath_1 = pl_MesaWebFCI.item
            if self.visibility_element(xpath, to):
                self.write(xpath, instrumento, to)
                self.wait(1)
                self.click(xpath_1)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)             
                
    def obtener_Nro_orden(self):
        to=10
        accion = u'Obtener numero de orden' 
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.nro_orden
            if self.visibility_element(xpath, to):
                orden = self.driver.find_element_by_xpath(xpath).get_property('innerHTML')
                print(orden)
                self.highlight(xpath, accion)     
                self.capture_image(msgOk)
                return orden
            else:
                self.fail_msg(msgFail)
                
    def selecionar_aceptar(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_aceptar_1
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def selecionar_confirmar(self):
        to = 10
        accion = u'Seleccionar confirmar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_confirmar
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
           

    def msj_(self):
        to = 10
        accion = u'Seleccionar confirmar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_confirmar
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)     
         
    def selecionar_aceptar_alta_de_orden(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_aceptar_orden
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
                
    def visualizar_msj_alta_exito(self):
        to = 10
        accion = u'Visualizar mensaje: La orden se dio de alta con exito '
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.msj_la_orden_exito
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 


    def obtener_nro_de_orden(self):
        to=10
        accion = u'Obtener numero de orden' 
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.nro_orden
            if self.visibility_element(xpath, to):
                orden = self.driver.find_element_by_xpath(xpath).get_property('innerHTML')
                print(u"se imprimio el numero de orden: {}".format(orden))
                self.highlight(xpath, accion)     
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def selecionar_mostrar_datos(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_mostrar_orden
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   

    def visualizar_orden(self):
        to = 10
        accion = u'Visualizar Orden de bonos y Titulos' 
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.selecionar_imprimir()
            self.capture_image(msgOk)

            
            
    def selecionar_imprimir(self):
        to = 10
        accion = u'Seleccionar imprimir '
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_imprimir
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def selecionar_ir_a_bandeja(self):
        to = 10
        accion = u'Seleccionar boton ir a bandeja '
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_ir_a_bandeja
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 

    def ingresar_precio_2(self):
        to = 10
        accion = u'Ingresar precio'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.precio
            if self.visibility_element(xpath, to):
                precio = self.buscar_precio_2()
                precio = precio.strip()
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath, precio, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    

    def selecionar_aceptar_2(self):
        to = 10
        accion = u'Seleccionar confirmar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_confirmar
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def selecionar_detalles_la_operacion(self):
        to = 10
        accion = u'Seleccionar confirmar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_confirmar
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 

    def selecionar_bandeja(self):
        to = 10
        accion = u'Seleccionar boton bandeja '
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_bandeja
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def selecionar_FCI(self):
        to = 10
        accion = u'Seleccionar boton FCI'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_FCI
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def validar_numero_de_FCI(self,numero):
        to = 10
        accion = u'Seleccionar boton FCI: {}'.format(numero)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_FCI.format(numero)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def selecionar_X(self):
        to = 10
        accion = u'Seleccionar boton X(ANULAR)'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_X
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def validar_msj_exito(self):
        to = 10
        accion = u'validar mensaje La operacion ha sido anulada satisfactoriamente'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.msj_exito
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def ingresar_numero_de_operacion(self,nro):
        to = 10
        accion = u'Ingresar numero de operacion {}'.format(nro)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.imput_nro_operacion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath,nro, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_buscar(self):
        to = 10
        accion = u'Seleccionar buscar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_buscar
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_checbox_ok(self):
        to = 10
        accion = u'Seleccionar checkbox '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.check_box_2
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_imputar(self):
        to = 10
        accion = u'Seleccionar imputar '
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebFCI.btn_imputar
            if self.visibility_element(xpath, to):
                self.click(xpath)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validar_msj_exito_2(self):
        to = 10
        accion = u'Se realizaron las imputaciones de movimientos de las operaciones seleccionadas'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.msj_exito_2
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def selecionar_bajas(self):
        to = 10
        accion = u'Seleccionar boton bajas'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.btn_bajas
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validar_numero_orden_en_bajas(self,nro):
        to = 10
        accion = u'Validar Numero de orden {} en bajas '.format(nro)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebFCI.cell_nro_orden.format(nro)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)