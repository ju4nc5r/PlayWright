# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.pageLoc.plAdminParametria import plAdminParametria
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.st.pasos import abrirNavegador
from selenium.webdriver.common.by import By

# from proyectos.Caja_Homo_suc50.constants.constants import (
#     USUARIO_INVALIDO, USUARIO_BLOQUEADO, USUARIO_YA_LOGUEADO, CLAVE_VENCIDA,
#     INTENTAR, REVISAR, LOGUEADO
# )
from SeleniumFramework.common_functions import get_msg

class stAdminParametria(abrirNavegador):
    def validarLimitesMaxMin(self):
        to = 10
        accion = "Validar tabla limites maximos y minimos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.tbl_parametria
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)

    def validarTituloParametria(self,leyendaTitulo):
        to = 10
        accion = "Validar titulo de parametria :".format(leyendaTitulo)
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.txt_titulo.format(leyendaTitulo)
            if self.visibility_element(xpath, to):
                self.highlight(xpath, accion)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarEditarSucursal(self, param):
        to = 10
        accion = 'Seleccionar boton Editar Sucursal de "' + param + '"'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.col_esperada.format('1')
            xpathFormat = plAdminParametria.col_esperada
            if self.visibility_element(xpath, to):
                self.ident = False
                i = 1
                while self.ident == False:
                    if self.get_element_text(xpathFormat.format(i)) == param:
                        xpathFinish = xpathFormat.format(i)
                        with self.step(accion):
                            self.highlight(xpathFinish, xpathFinish)
                        self.ident = True
                        break
                    i = i + 1
                xpathEdit = xpathFinish + plAdminParametria.col_editar
                self.selectElement(xpathEdit, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
                
    def seleccionarEditarSucursales(self):
        to = 10
        accion = 'Seleccionar boton Editar Sucursales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.btn_editarSucursales
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def visualizarTiposDeLimite(self):
        to = 10
        accion = 'Visualizar tipos de limites a editar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.slc_tipoLimite
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarTipoDeLimite(self, param):
        to = 10
#         accion = 'Seleccionar tipo de limite'
        accion = 'Seleccionar tipo de limite "' + param + '"'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.btn_tipoLimite.format('1')
            xpathFormat = plAdminParametria.btn_tipoLimite
            if self.visibility_element(xpath, to):
                self.ident = False
                i = 1
                while self.ident == False:
                    if self.get_element_text(xpathFormat.format(i)) == param:
                        xpathFinish = xpathFormat.format(i)
                        self.ident = True
                        break
                    i = i + 1
                self.selectElement(xpathFinish, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarLimitePesos(self, monto):
        to = 10
        accion = 'Ingresar limite en pesos'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.ipt_limPesos
            if self.visibility_element(xpath, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def ingresarLimiteDolares(self, monto):
        to = 10
        accion = 'Ingresar limite en dolares'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.ipt_limDolar
            if self.visibility_element(xpath, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def ingresarLimiteEuros(self, monto):
        to = 10
        accion = 'Ingresar limite en euros'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.ipt_limEuro
            if self.visibility_element(xpath, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def ingresarLimiteReales(self, monto):
        to = 10
        accion = 'Ingresar limite en reales'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.ipt_limReal
            if self.visibility_element(xpath, to):
                self.write(xpath, monto, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarGuardarLimites(self):
        to = 10
        accion = 'Seleccionar guardar limites'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.btn_guardarLim
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
        
    def seleccionarAceptarCambios(self):
        to = 10
        accion = 'Seleccionar aceptar cambios'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.btn_aceptarCambios
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def validarMensajeDeActualizacion(self, msjEsperado):
        to = 10
        accion = 'Validar mensaje: Se ha actualizado para todas las sucursales el límite'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.txt_msjEsperado
            if self.visibility_element(xpath, to):
                print("texto mensaje exito mostrado: " + self.get_element_text(xpath))
#                 if self.get_element_text(xpath) == msjEsperado:
                if msjEsperado in self.get_element_text(xpath):
                    self.highlight(xpath, accion)
                    xpath = plAdminParametria.btn_cerrarMjeExito
                    self.jsClick(xpath)
                else:
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def validarCambiosDeLimites(self, param, pesos, dolar, euro, real):
        to = 10
        accion = 'validar cambios en los limites "' + param + '"'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            # le digo por que xpath empezar de la tabla
            xpath = plAdminParametria.col_esperada.format('1')
            # guardo un xpath sin pasar posicion para luego setearsela 
            xpathFormat = plAdminParametria.col_esperada
            # pregunto si el xpath es visible para empezar de la tabla es visible
            if self.visibility_element(xpath, to):
                # creo una variable para usarla como true/false para saber si entro o no al if
                self.ident = False
                # genero un contador
                i = 1
                # creo un while para recorrer cada posicion de la tabla hasta que la variable ident de true
                while self.ident == False:
                    # aca es donde uso el xpath sin posicion y se la seteo acorde al contador,
                    # donde pregunta si el texto del xpath es igual al valor que le paso por parametro
                    if self.get_element_text(xpathFormat.format(i)) == param:
                        # si es igual, lo guardo en otra variable,la que se va a usar en los metodos de abajo para validar los cambios
                        xpathFinish = xpathFormat.format(i)
                        with self.step(accion):
                            self.go_to_xpath(xpathFinish)
                            self.highlight(xpathFinish, xpathFinish)
                        self.ident = True
                        break
                    # si no es igual, le agrego +1 al contador para que verifique una posicion distinta, osea un xpath mas abajo de la tabla
                    i = i + 1
                # se validan los campos con el xpath correcto, osea el que entro al if y es igual al parametro mandado en la funcion
                print("-----------")
                print(xpathFinish)
                print(pesos)
                print("-----------")
                self.validarCambiosLimitePesos(xpathFinish, pesos)
                self.validarCambiosLimiteDolar(xpathFinish, dolar)
                self.validarCambiosLimiteEuro(xpathFinish, euro)
                self.validarCambiosLimiteReal(xpathFinish, real)
                self.capture_image(msgOk)
                
            else:
                self.fail_msg(msgFail)
    
    def validarCambiosLimitePesos(self, param, pesos):
        to = 10
        accion = "Validar cambios limite en pesos"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = param + plAdminParametria.col_pesos
            if self.visibility_element(xpath, to):                
                if self.get_element_text(xpath) == pesos:
                    self.highlight(xpath, accion)
                else:
                    self.highlight(xpath, accion)
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
    def validarCambiosLimiteDolar(self, param, dolar):
        to = 10
        accion = "Validar cambios limite en dolar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = param + plAdminParametria.col_dolar
            if self.visibility_element(xpath, to):                
                if self.get_element_text(xpath) == dolar:
                    self.highlight(xpath, accion)
                else:
                    self.highlight(xpath, accion)
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    def validarCambiosLimiteEuro(self, param, euro):
        to = 10
        accion = "Validar cambios limite en euro"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = param + plAdminParametria.col_euro
            if self.visibility_element(xpath, to):                
                if self.get_element_text(xpath) == euro:
                    self.highlight(xpath, accion)                    
                    self.capture_image(msgOk)
                else:
                    self.highlight(xpath, accion)
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)
    
    def validarCambiosLimiteReal(self, param, real):
        to = 10
        accion = "Validar cambios limite en real"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = param + plAdminParametria.col_real
            if self.visibility_element(xpath, to):                
                if self.get_element_text(xpath) == real:
                    self.highlight(xpath, accion)                    
                    self.capture_image(msgOk)
                else:
                    self.highlight(xpath, accion)
                    self.fail_msg(msgFail)
            else:
                self.fail_msg(msgFail)

    # items por pagina

    def mostrarItemsPorPagina(self):
        to = 10
        accion = 'mostrar cantidad de items por pagina'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.slc_items
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
    
    def seleccionarDiezItems(self):
        to = 10
        accion = 'seleccionar 10 items por pagina'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = plAdminParametria.btn_items_10
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)