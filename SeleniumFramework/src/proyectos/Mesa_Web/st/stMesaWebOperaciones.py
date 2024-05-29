'''
Created on 27 may. 2022

@author: GON13535
'''
# -*- coding: utf-8 -*-
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.keys import Keys
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebOperaciones import pl_MesaWebOperaciones
from SeleniumFramework.keyboard import keyboard
from selenium.webdriver.common.by import By


class stMesaWebOperaciones(keyboard):

    
    def seleccionar_operaciones(self):
        to = 10
        accion = u'Seleccionar Operaciones'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.operaciones
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
                
    def seleccionar_acciones(self):
        to = 10
        accion = u'Seleccionar Acciones'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.acciones
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
            xpath = pl_MesaWebOperaciones.titulos
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
            xpath = pl_MesaWebOperaciones.venta
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
            xpath = pl_MesaWebOperaciones.venta_2
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
            xpath = pl_MesaWebOperaciones.compra
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
            xpath = pl_MesaWebOperaciones.compra_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
                
    def completarNroCliente(self,nro_cliente):
        accion = u'Completar Nro de cliente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.input_cliente
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
            xpath = pl_MesaWebOperaciones.lista_cliente
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
            xpath = pl_MesaWebOperaciones.tipo_cliente_Nro
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
            xpath = pl_MesaWebOperaciones.btn_buscarCliente
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
            xpath = pl_MesaWebOperaciones.btn_compra_banco
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
            xpath = pl_MesaWebOperaciones.btn_venta_banco
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
            xpath = pl_MesaWebOperaciones.check_box
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
  
    def resaltar_advertencia_sin_clasificacion(self,xpath):
        to = 10
        accion = u'Resaltar mensaje El cliente no posee clasificacion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):            
            if self.visibility_element(xpath,to):
                self.highlight(xpath, msgOk)
                self.skip_msg(msgFail)
            else:
                pass

            
    
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
                
                
    def seleccionar_recuadro_seleccionar(self, xpath):
        to = 10
        accion = u'Seleccionar seleccionar recuadro'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_item(self, xpath):
        to = 10
        accion = u'Seleccionar seleccionar item'
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
            xpath = pl_MesaWebOperaciones.lista_instrumentos
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
    
    def ingresar_precio(self):
        to = 10
        accion = u'Ingresar precio'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.precio
            if self.visibility_element(xpath, to):
                precio = self.buscar_precio()
                print(precio)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.wait(2)
                self.write(xpath, precio, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
    
    
    def buscar_precio(self):
        accion = u'Buscar precioo'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.ultimo_precio
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
            xpath = pl_MesaWebOperaciones.ultimo_precio
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
            xpath = pl_MesaWebOperaciones.cantidad_VN
            if self.visibility_element(xpath, to):
                #self.selectElement(xpath, msgOk, msgFail, to)
                #self.wait(2)
                self.write(xpath, cantidad, to)
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def ingresar_cantidad_2(self, cantidad):
        to = 10
        accion = u'Ingresar cantidad'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.cantidad_VN_2
            if self.visibility_element(xpath, to):
                self.clear(xpath)
                self.wait(1)
                celda = self.driver.find_element_by_xpath(xpath)
                celda.send_keys(cantidad)                
                self.wait(1)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresar_instrumento(self, instrumento):
        to = 10
        accion = u'Ingresar instrumento {}'.format(instrumento)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.readro_instrumentos
            xpath_1 = pl_MesaWebOperaciones.item
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
            xpath = pl_MesaWebOperaciones.nro_orden
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
        xpath = pl_MesaWebOperaciones.btn_aceptar_1
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
        xpath = pl_MesaWebOperaciones.btn_aceptar_orden
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
        xpath = pl_MesaWebOperaciones.msj_la_orden_exito
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
            xpath = pl_MesaWebOperaciones.nro_orden
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
        xpath = pl_MesaWebOperaciones.btn_mostrar_orden
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
        xpath = pl_MesaWebOperaciones.btn_imprimir
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
        xpath = pl_MesaWebOperaciones.btn_ir_a_bandeja
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
            xpath = pl_MesaWebOperaciones.precio
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
                
    def ingresar_precio_3(self,precio):
        to = 10
        accion = u'Ingresar precio'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.precio_2
            if self.visibility_element(xpath, to):
                self.clear(xpath)
                self.wait(1)
                celda = self.driver.find_element_by_xpath(xpath)
                celda.send_keys(precio)                
                self.wait(1) 
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
                
                

    def seleccionar_operaciones_genericas(self):
        to = 10
        accion = u'Seleccionar Operaciones Genericas'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.operaciones_genericas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def seleccionar_operaciones_(self):
        to = 10
        accion = u'Seleccionar Operaciones Genericas'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.operaciones_genericas
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    def seleccionar_recuadro_buscar_por(self):
        to = 10
        accion = u'Desplegar lista de datos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.lista_cliente_2
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_Nro_de_cliente(self):
        to = 10
        accion = u'Seleccionar la oppcion numero de cliente'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = pl_MesaWebOperaciones.tipo_cliente_Nro
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)


    def seleccionar_recuadro_mercado(self):
        to = 10
        accion = u'Seleccionar recuadro Mercado'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.recuadro_mercado
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def seleccionar_item_Merval(self):
        to = 10
        accion = u'Seleccionar Item Merval'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_merval
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
                
    def seleccionar_item_Mae(self):
        to = 10
        accion = u'Seleccionar Item Mae'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_mae
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
    def ingresar_instrumento_2(self,instrumento):
        to = 10
        accion = u'Ingresar instrumento: {}'.format(instrumento)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.imput_instrumento
        xpath_2 =  pl_MesaWebOperaciones.item_al30
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                celda = self.driver.find_element_by_xpath(xpath)
                celda.send_keys(instrumento)
                self.click(xpath_2)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
                
    def ingresar_cantidad_3(self,instrumento):
        to = 10
        accion = u'Ingresar instrumento: {}'.format(instrumento)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.imput_instrumento
        xpath_2 =  pl_MesaWebOperaciones.item_al30
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.write(xpath,instrumento, to)
                self.wait(1)        
                self.click(xpath_2)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
    def seleccionar_recuadro_tipo(self):
        to = 10
        accion = u'Seleccionar recuadro Tipo'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.recuadro_tipo
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)     

    def seleccionar_item_AL30(self):
        to = 10
        accion = u'Seleccionar Item  AL30'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_al30
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.driver.find_element(by=By.XPATH, value=xpath).send_keys()
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_item_Vnta(self):
        to = 10
        accion = u'Seleccionar Item Vnta'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_vnta
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  

    def seleccionar_recuadro_especie(self):
        to = 10
        accion = u'Seleccionar recuadro especie'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.recuadro_especie_pago
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)                    

    def seleccionar_item_moneda(self,moneda):
        to = 10
        accion = u'Seleccionar Item moneda: {}'.format(moneda)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_moneda_us.format(moneda)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
    def seleccionar_recuadro_carpeta_propia(self):
        to = 10
        accion = u'Seleccionar recuadro especie'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.recuadro_carpeta_propia
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_check_Nro_referencia_mae(self):
        to = 10
        accion = u'Seleccionar Check numero de referencia MAE'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.check_referencia_mae
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionar_check_Nro_orden_mae(self):
        to = 10
        accion = u'Seleccionar Check numero de orden MAE'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.check_orden_mae
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionar_item_si(self,SI):
        to = 10
        accion = u'Seleccionar Item : {}'.format(SI)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_si.format(SI)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
    def seleccionar_item_no(self,NO):
        to = 10
        accion = u'Seleccionar Item : {}'.format(NO)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_no.format(NO)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail) 
                
    def selecionar_aceptar2(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_aceptar
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
                
    def selecionar_aceptar_3(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_aceptar_2
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)  
                
                
    def selecionar_OPERACIONES(self):
        to = 10
        accion = u'Seleccionar operaciones'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_operaciones_2
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def validar_numero_de_OPERACION(self,numero):
        to = 10
        accion = u'Seleccionar boton FCI: {}'.format(numero)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_operaciones_2.format(numero)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def selecionar_boton_editar(self):
        to = 10
        accion = u'Seleccionar boton editar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_editar
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)      
                
    def selecionar_recuadro_book(self):
        to = 10
        accion = u'Seleccionar recuadro Book'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.recuadro_book
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def selecionar_Item_banking(self):
        to = 10
        accion = u'Seleccionar item banking'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_banking
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)    
                
    def selecionar_recuadro_estrategia(self):
        to = 10
        accion = u'Seleccionar recuadro estrategia'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.recuadro_estrategia
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   
                
    def selecionar_Item_Banca_Patrimonial(self):
        to = 10
        accion = u'Seleccionar item banking'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.item_banca_patrimonial
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)         
     
     
    def selecionar_aceptar_4(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_aceptar_3
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def selecionar_detalles_de_la_operacion(self):
        to = 10
        accion = u'Seleccionar aceptar'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_detalles
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def validar_cambio(self,dato,cambio):
        to = 10
        accion = u'validar cambio de: {} , {}'.format(dato,cambio)
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.label_cambio.format(cambio)
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
                
    def selecionar_cerrar_detalles(self):
        to = 10
        accion = u'Seleccionar cerrar detalles'
        msgOk, msgFail = get_msg(accion)
        xpath = pl_MesaWebOperaciones.btn_cerrar_detalles
        with self.step(accion):       
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)   