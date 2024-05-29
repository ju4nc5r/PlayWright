# -*- coding: utf-8 -*-
from SeleniumFramework.sub import sub
from SeleniumFramework.src.proyectos.HBPF.pageLoc.Perfil import Perfil
from SeleniumFramework.src.proyectos.HBPF.pageLoc.CambioClave import CambioClave
from SeleniumFramework.src.proyectos.HBPF.loc.locLogin import locLogin
from SeleniumFramework.common_functions import get_msg


class stCambioClave(sub):
    def cambiarClave(self, ignorarFalla=False,
                     equivocarClaveActual=False, equivocarRepe=False):
        """
        Metodo para entra al menu de perfiles y cambiar la clave de un
        cliente.
        :param ignorarFalla: Boolean. Boleando para ignorar si se muestra el
                             mensaje de error, si este es un elemento esperado
        :param equicocarClaveActual: Boolean. Booleano para ingresar una clave
                no valida, y esperar a que se muestre el mensaje esperado.
        :param equivocarRepe: Boolean. Booleano para ingresar un clave
                incorrecta en el campo de la confirmacion de la clave.
        :return: Boolean. Si se logro o no realizar el cambio de clave
        """
        self.seleccionarMenuPerfil()
        self.seleccionarCambiarClave()
        self.escribirClaveActual(equivocarClaveActual)
        self.escribirClaveNueva()
        self.reescribirClaveNueva(equivocarRepe)
        self.seleccionarConfirmar()
        if self.verificar_cambio(ignorarFalla):
            return True
        return False

    def verificar_cambio(self, falla):
        """
        Metodo para verificar si se pudo realizar el cambio de clave o se
        muestra el mensaje de error
        :param falla: Boolean. True, si se debe ignorar la falla
                               False, si no se debe ignorar la falla
        """
        
        
        
        # SE AGREGA PASO DE ALLURE PARA QUE LA CAPTURA QUEDE LUEGO DE CONFIRMAR
        #  Y SE MODIFICA ACCION PARA QUE INDIQUE LA VALIDACIÓN DEL TICKET de 
        # CAMBIO CLAVE O DEL MENSAJE DE ERROR
       
        
        accion = u'Se pudo realizar el cambio de clave y validar ticket'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            xpath1 = CambioClave.img_Ticket
            xpath2 = CambioClave.lbl_Error_xp
            xpath3 = CambioClave.lbl_Error_2_xp
            elem_list = [xpath1, xpath2, xpath3]
            index = self.array_visibility(elem_list, to)
            if index == 0:
                self.capture_image(msgOk)
                return True
            elif index in (1, 2):
                if falla:
                    self.verificarError()
                else:
                    self.fail_msg(msgFail)
            return False

#         to = 10
#         xpath1 = CambioClave.img_Ticket
#         xpath2 = CambioClave.lbl_Error_xp
#         xpath3 = CambioClave.lbl_Error_2_xp
#         elem_list = [xpath1, xpath2, xpath3]
#         index = self.array_visibility(elem_list, to)
#         if index == 0:
#             self.capture_image('Se realizo la modificacion')
#             return True
#         elif index in (1, 2):
#             if falla:
#                 self.verificarError()
#             else:
#                 self.fail_msg('No se pudo realizar el cambio de clave')
#         return False
#         
        
                

    def seleccionarCambiarClave(self):
        accion = 'Seleccionar cambiar de clave'
        msgOk, msgFail = get_msg(accion)
        to = 10
        with self.step(accion):
            self.selectElement(Perfil.opt_CambioClave_xp, msgOk, msgFail, 10)
            if self.visibility_element(CambioClave.titulo, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def seleccionarMenuPerfil(self):
        accion = 'Seleccionar menu desplegable del perfil'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = Perfil.btn_Perfil_xp
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail)
            self.capture_image(msgOk)

    def escribirClaveActual(self, equivocarClaveActual):
        accion = 'Escribir clave actual'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = CambioClave.text_ClaveActual_xp
            self.selectElement(xpath, msgOk, msgFail)
            if (equivocarClaveActual):
                self.write(xpath, self.clave + 'j', 5)
            else:
                self.write(xpath, self.clave, 5)

    def escribirClaveNueva(self):
        accion = 'Escribir clave nueva'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = CambioClave.text_ClaveNueva_xp
            self.selectElement(xpath, msgOk, msgFail)
            self.write(xpath, self.claveNueva, 5)

    def reescribirClaveNueva(self, equivocarRepe):
        accion = 'Escribir nuevamente la clave nueva'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = CambioClave.text_Repetir_ClaveNueva_xp
            self.selectElement(xpath, msgOk, msgFail)
            if (equivocarRepe):
                self.write(xpath, self.claveNueva + 'j', 5)
            else:
                self.write(xpath, self.claveNueva, 5)

    def seleccionarConfirmar(self):
        accion = 'Seleccionar confirmar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = CambioClave.btn_Confirmar_xp
            self.selectElement(xpath, msgOk, msgFail)
            self.capture_image(msgOk)

    def verificarError(self):
        accion = 'Verificar aparicion de error'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath1 = CambioClave.lbl_Error_xp
            xpath2 = CambioClave.lbl_Error_2_xp
            if (self.double_visibility_element(xpath1, xpath2, 15)):
                self.capture_image(msgOk)
            else:
                self.capture_image(msgOk)

    def seleccionarCancelar(self):
        accion = 'Seleccionar cancelar'
        msgOk, msgFail = get_msg(accion)
        to = 15
        with self.step(accion):
            xpath = CambioClave.btn_Cancelar_xp
            self.selectElement(xpath, msgOk, msgFail, to)
            self.verificarCancelar()
            self.capture_image(msgOk)

    def verificarCancelar(self):
        accion = 'Verificar cancelar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locLogin.titulo_esperado
            if self.visibility_element(xpath):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
