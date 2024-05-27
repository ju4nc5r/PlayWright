# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Inte.pageLoc.plAdminConsulta import plAdminConsulta
from SeleniumFramework.src.proyectos.Caja_Inte.st.pasos import abrirNavegador
from SeleniumFramework.common_functions import get_msg
from selenium.webdriver.common.by import By
import time

class stAdminConsulta(abrirNavegador):
    def validarTablaOperadores(self):
        to = 10
        accion = "Ver que exista la tabla de operadores"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_operadores
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def validarTablaTerminalesregistradas(self):
        to = 10
        accion = "Ver que exista la tabla de Terminales registradas"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_terminales_regis
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)              
                               
    def validarTituloConsulta(self,leyendaTitulo):
        to = 10
        accion = "Validar titulo de la consulta :".format(leyendaTitulo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.txt_titulo.format(leyendaTitulo)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)                
#                 self.highlight(xpath, accion) se comenta para cambiar que el xpath no quede en la descripción y se ponga una leyenda con la accion                
#                 self.capture_image(msgOk)  se comenta para que no quede duplicada la captura que ya hace el highlight
            else:
                self.fail_msg(msgFail)
                
    def validarTitulo2Consulta(self,leyendaTitulo):
        to = 10
        accion = "Validar titulo de la consulta :".format(leyendaTitulo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
#             Ir al boton imprimir que esta más arriba para que se pueda ver la tabla 
            xpath = plAdminConsulta.btn_Imprimir_1
            self.goToSection(xpath, msgOk, msgFail)
#             validar titulo y segunda tabla totales
            xpath = plAdminConsulta.txt_titulo2.format(leyendaTitulo)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)


    def validarTablaSaldosCajas(self):
        to = 10
        accion = "Ver que exista la tabla con los saldos de caja"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_operadores
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)               
            else:
                self.fail_msg(msgFail)


    def validarTablaSaldosCajasSuc(self):
        to = 10
        accion = "Ver que exista la tabla con los saldos de caja por sucursal"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_saldos2
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)   

    
    def validarTablaMovimientosdecaja(self):
        to = 10
        accion = "Ver que exista la tabla Movimientos de caja"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_MovDeCajas
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarBuscarMovimientos(self):
        to = 10
        accion = "Seleccionar Buscar Movimientos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.btn_buscarMovi
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarImprimirMovimientos(self):
        to = 10
        accion = 'Seleccionar Imprimir Movimientos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.driver.execute_script("window.scrollTo(0,600);") #Se hace scrool porque el goto_xpath no funciona en este caso
            time.sleep(1)
            xpath = plAdminConsulta.btn_imprimir
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)                
#                 Se hace foco en el botón Imprimir (totales por sucursal) y se da enter y escape para imprimir y cerrar dialogo impresión 
                element = self.driver.find_element(by=By.XPATH, value=xpath)
                element.send_keys("") 
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.driver.switch_to.window(self.driver.window_handles[1])
                xpath = plAdminConsulta.lst_TotSaldosSucursal
                self.highlight(xpath, "Movimientos por sucursal")                
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                self.fail_msg(msgFail)


    def seleccionarDescargarMovimientos(self):
        to = 10
        accion = "Seleccionar Descargar Movimientos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.btn_descargar
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def ImprimirSaldosPorTerminal(self):
        # seleccionarImprimirMovimientos        
        to = 10
        accion = 'Seleccionar Imprimir saldos por terminal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.btn_Imprimir_1
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)
#               Se hace foco en el botón Imprimir (totales por sucursal) y se resalta
                element = self.driver.find_element(by=By.XPATH, value=xpath)
                element.send_keys("") 
                self.highlight(xpath, accion)   
                self.selectElement(xpath, msgOk, msgFail, to)
                self.driver.switch_to.window(self.driver.window_handles[1])
                xpath = plAdminConsulta.lst_TotSaldosTerminal
                self.highlight(xpath, "Saldos por terminal")
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                self.fail_msg(msgFail)
                
    def ImprimirSaldosPorSucursal(self):        
        to = 10
        accion = 'Seleccionar Imprimir totales saldos por sucursal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.driver.execute_script("window.scrollTo(0,700);") #Se hace scrool porque el goto_xpath no funciona en este caso
            time.sleep(1)
            xpath = plAdminConsulta.btn_Imprimir_2
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)                
#                 Se hace foco en el botón Imprimir (totales por sucursal) y se da enter y escape para imprimir y cerrar dialogo impresión 
                element = self.driver.find_element(by=By.XPATH, value=xpath)
                element.send_keys("") 
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.driver.switch_to.window(self.driver.window_handles[1])
                xpath = plAdminConsulta.lst_TotSaldosSucursal
                self.highlight(xpath, "Saldos por sucursal")                
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                self.fail_msg(msgFail)
 
 
    def seleccionarBuscarTotales(self):
        to = 10
        accion = "Seleccionar Buscar Totales"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.btn_buscarTotales
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarMoneda(self):
        to = 10
        accion = 'Seleccionar moneda'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.slc_TipoMoneda
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTipoMoneda(self, moneda):
        to = 10
        accion = 'Seleccionar tipo de moneda'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.opt_moneda.format(moneda)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def visualizarIngresos(self):
        to = 10
        accion = "Visualizar tabla de ingresos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_ingresos
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    def visualizarEgresos(self):
        to = 10
        accion = "Visualizar tabla de egresos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_egresos
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    def visualizarLiquido(self):
        to = 10
        accion = "Visualizar tabla de Liquido"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_liquido
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def seleccionarImprimirTotales(self):
        to = 10
        accion = 'Seleccionar Imprimir totales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.driver.execute_script("window.scrollTo(0,700);") #Se hace scrool porque el goto_xpath no funciona en este caso
            time.sleep(1)
            xpath = plAdminConsulta.btn_imprimir
            if self.visibility_element(xpath, to):
                self.go_to_xpath(xpath)                
#                 Se hace foco en el botón Imprimir (totales por sucursal) y se da enter y escape para imprimir y cerrar dialogo impresión 
                element = self.driver.find_element(by=By.XPATH, value=xpath)
                element.send_keys("") 
                self.highlight(xpath, accion)
                self.selectElement(xpath, msgOk, msgFail, to)
                self.driver.switch_to.window(self.driver.window_handles[1])
                xpath = plAdminConsulta.lst_TotIngresosCaja
                self.highlight(xpath, "totales ingresos")  
                xpath = plAdminConsulta.lst_TotEgresosCaja
                self.go_to_xpath(xpath)
                self.highlight(xpath, "totales egresos")    
                xpath = plAdminConsulta.lst_TotLiquidoCaja
                self.go_to_xpath(xpath)
                self.highlight(xpath, "totales liquido") 
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                self.fail_msg(msgFail)           
    
    def seleccionarSucursal(self):
        to = 10
        accion = 'Seleccionar sucursal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.slc_sucursal
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarNumSucursal(self, sucursal):
        to = 10
        accion = 'Seleccionar numero de sucursal'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.opt_sucursal.format(sucursal)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarCondicion(self):
        to = 10
        accion = 'Seleccionar condicion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.slc_condicion
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
        
    def seleccionarTipoCondicion(self, condicion):
        to = 10
        accion = 'Seleccionar tipo de condicion'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.opt_condicion.format(condicion)
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarOperador(self, operador):
        to = 10
        accion = 'Ingresar operador'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAdminConsulta.ipt_operador, operador, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTodasLasOpcEtracciones(self):
        to = 10
        accion = 'Seleccionar todas las opciones de extracciones'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.div_extracciones
            if self.visibility_element(xpath, to):
                # creo una variable para usarla como true/false para saber si entro o no al if
                self.ident = False
                # genero un contador
                i = 1
                # creo un while para recorrer cada posicion de la tabla hasta que la variable ident de true
                while self.ident == False:
                    checkbox = plAdminConsulta.check_divs.format(i)
                    xpathCheck = xpath + checkbox
                    self.wait(5)
                    self.selectElement(xpathCheck, msgOk, msgFail, to)
                    # self.jsClick(xpathCheck)
                    if (i == 5):
                        self.ident = True
                        break
                    # si no es igual, le agrego +1 al contador para que verifique una posicion distinta, osea un xpath mas abajo de la tabla
                    i = i + 1
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTodasLasOpcDepositos(self):
        to = 10
        accion = 'Seleccionar todas las opciones de depositos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.div_depositos
            if self.visibility_element(xpath, to):
                # creo una variable para usarla como true/false para saber si entro o no al if
                self.ident = False
                # genero un contador
                i = 1
                # creo un while para recorrer cada posicion de la tabla hasta que la variable ident de true
                while self.ident == False:
                    checkbox = plAdminConsulta.check_divs.format(i)
                    xpathCheck = xpath + checkbox
                    self.wait(5)
                    self.selectElement(xpathCheck, msgOk, msgFail, to)
                    # self.jsClick(xpathCheck)
                    if (i == 5):
                        self.ident = True
                        break
                    # si no es igual, le agrego +1 al contador para que verifique una posicion distinta, osea un xpath mas abajo de la tabla
                    i = i + 1
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTodasLasOpcCompraVenta(self):
        to = 10
        accion = 'Seleccionar todas las opciones de compra/venta'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.div_compraventa
            if self.visibility_element(xpath, to):
                # creo una variable para usarla como true/false para saber si entro o no al if
                self.ident = False
                # genero un contador
                i = 1
                # creo un while para recorrer cada posicion de la tabla hasta que la variable ident de true
                while self.ident == False:
                    checkbox = plAdminConsulta.check_divs.format(i)
                    xpathCheck = xpath + checkbox
                    self.wait(5)
                    self.selectElement(xpathCheck, msgOk, msgFail, to)
                    # self.jsClick(xpathCheck)
                    if (i == 5):
                        self.ident = True
                        break
                    # si no es igual, le agrego +1 al contador para que verifique una posicion distinta, osea un xpath mas abajo de la tabla
                    i = i + 1
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTodasLasOpc(self):
        to = 10
        accion = 'Seleccionar todas las opciones'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.check_todo
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarImporte(self, importe):
        to = 10
        accion = 'Ingresar importe'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            if self.write(plAdminConsulta.ipt_importe, importe, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def validarFechaDia(self, fecha):
        to = 10
        accion = 'Validar fecha del dia'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.ipt_fecha
            if self.visibility_element(xpath, to):
                input_value = self.driver.find_element(by=By.XPATH, value=xpath).get_property('value')
                if input_value == fecha:
                    self.highlight(xpath, accion)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def visualizarInformacion(self):
        to = 10
        accion = "Visualizar en pantalla la informacion  los Movimientos y/o TX realizadas"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminConsulta.tbl_listado
            self.go_to_xpath(xpath)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)