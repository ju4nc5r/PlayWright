# -*- coding: utf-8 -*-
import pytest
from sub import sub
from SeleniumFramework.src.proyectos.HBPF.pageLoc.DatosPersonales import DatosPersonales
from SeleniumFramework.src.proyectos.HBPF.pageLoc.Perfil import Perfil
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plLogin import plLogin


class stDatosPersonales(sub):
    def datosPersonales(self):
        self.seleccionarMenuPerfil()
        self.verificarDatosPersonales()

    def seleccionarMenuPerfil(self):
        accion = 'Seleccionar menu desplegable del perfil'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = Perfil.btn_Perfil_xp
            self.go_to_xpath(xpath)
            self.selectElement(xpath, msgOk, msgFail)
            self.seleccionarDatosPersonales()

    def seleccionarDatosPersonales(self):
        accion = 'Seleccionar datos personales'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        xpath = Perfil.opt_DatosPersonales_xp
        if(self.visibility_element(xpath)):
            self.capture_image(msgOk)
            if not self.selectElement(xpath, msgOk, msgFail):
                # Se hace esto si justo se mostro el elemento y no se
                # alcanzo a hacer click
                self.jsClick(xpath)
        else:
            self.jsClick(xpath)

    def verificarDatosPersonales(self):
        accion = 'Verificar datos personales'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        to = 10
        with self.step(accion):
            xpath = DatosPersonales.lbl_Titulo_Datos_Personales_xp
            if(self.visibility_element(xpath), to):
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)

    def seleccionarModificarCelMail(self):
        accion = 'Seleccionar modificar celular/email'
        msgOk = accion
        msgFail = 'No se pudo ' + accion.lower()
        to = 10
        with self.step(accion):
            xpath = DatosPersonales.btn_Modificar_CelMail_xp
            if(self.visibility_element(xpath), to):
                self.selectElement(xpath, msgOk, msgFail)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)

    def seleccionarModificarDomParticular(self):
        accion = 'Seleccionar modificar domicilio particular'
        msgOk = accion
        msgFail = 'No se pudo ' + accion.lower()
        to = 10
        with self.step(accion):
            xpath = DatosPersonales.btn_Modificar_DomParticular_xp
            if(self.visibility_element(xpath), to):
                self.selectElement(xpath, msgOk, msgFail)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)

    def seleccionarModificarDomLaboral(self):
        accion = 'Seleccionar modificar domicilio laboral'
        msgOk = accion
        msgFail = 'No se pudo ' + accion.lower()
        with self.step(accion):
            xpath = DatosPersonales.btn_Modificar_DomLaboral_xp
            if(self.visibility_element(xpath)):
                self.selectElement(xpath, msgOk, msgFail)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)

    def seleccionarVolver(self):
        accion = 'Seleccionar boton volver'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.btn_Cambio_Volver_xp
            if(self.visibility_element(xpath)):
                self.selectElement(xpath, msgOk, msgFail)
                self.capture_image(msgOk)
                self.verificarDatosPersonales()
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)

    def seleccionarCancelar(self):
        accion = 'Seleccionar boton cancelar'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.btn_Cambio_Cancelar_xp
            if(self.visibility_element(xpath)):
                self.selectElement(xpath, msgOk, msgFail)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)

    def seleccionarContinuar(self, ignorarFalla=False):
        """
        Metodo para seleccionar el boton continuar en la modificacion de datos
        personales. Tener en cuenta que este botón se utiliza en varios lugares
        de la modificacion de datos, por ende, son varios los elementos
        esperados
        :param ignorarFalla: Boolean. Por default se encuentra en True. Se
                             lo utiliza por si el error es un evento esperado
        """
        accion = 'Seleccionar boton continuar'
        msgOk = accion
        msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.btn_Cambio_Continuar_xp
            if(self.visibility_element(xpath)):
                self.selectElement(xpath, msgOk, msgFail)
                self.capture_image(msgOk)
            else:
                self.capture_image(msgFail)
                pytest.fail(msgFail)
            # Se esperan los diferentes elementos
            self.verificarLuegoDeContinuar(ignorarFalla)

    def verificarLuegoDeContinuar(self, falla):
        xpath1 = DatosPersonales.inp_clave_itau
        xpath2 = DatosPersonales.pnl_Error_xp
        xpath3 = plLogin.titulo_inicio
        elem_list = [xpath1, xpath2, xpath3]
        timeout = 10
        numero = self.array_visibility(elem_list, timeout)
        if numero == 0:
            self.go_to_xpath(DatosPersonales.inp_clave_itau)
            self.capture_image('Se esta mostrando el input para la clave')
        elif numero == 2:
            self.capture_image('Se volvio al inicio del homebanking')
        else:
            msg = 'Se esta mostrando el mensaje de error'
            if falla:
                texto = self.get_element_text(xpath2)
                if self.msjEsperado in texto:
                    self.capture_image(msg)
                else:
                    self.fail_msg('No esta pressente el mensaje esperado')
            else:
                self.fail_msg(msg)

    def seleccionarConfirmar(self):
        accion = 'Seleccionar el boton Confirmar'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            xpath = DatosPersonales.btn_Confirmar_xp
            self.selectElement(xpath, msgOk, '', to)
            # Compruebo que se este mostrando la imagen del comprobante
            xpath = DatosPersonales.img_comprobante
            if self.verificarComprobante():
                self.capture_image(
                    'Se muestra el comprobante de la modificacion de datos'
                )
            else:
                self.fail_msg(msgFail)

    def verificarComprobante(self):
        """Metodo para verificar que se esta mostrando el comprobante"""
        xpath1 = DatosPersonales.img_comprobante
        xpath2 = DatosPersonales.pnl_Error_xp
        timeout = 10
        return self.double_visibility_element(xpath1, xpath2, timeout)

    def verificarIngreseClave(self):
        # accion = 'Verificar que se muestre el campo para la clave itau'
        xpath = DatosPersonales.inp_clave_itau
        to = 10
        return self.visibility_element(xpath, to)

    def verificarClaveItau(self):
        """
        Metodo para verificar que se esta mostrando, o no, un mensaje de error
        """
        xpath1 = DatosPersonales.inp_clave_itau
        xpath2 = DatosPersonales.pnl_Error_xp
        timeout = 10
        if self.double_visibility_element(xpath1, xpath2, timeout):
            self.capture_image('Se muestra el input para la clave itau')
            return True
        return False

    def verificarError(self):
        """Metodo para verificar que se muestre el mensaje de error"""
        accion = 'Verificar el mensaje de error'
        msgOk = 'Se pudo {}'.format(accion.lower())
        msgFail = 'No se pudo {}'.format(accion.lower())
        xpath = DatosPersonales.pnl_Error_xp
        to = 10
        with self.step(accion):
            if self.visibility_element(xpath, to):
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)

    def actualizarTelefonoParticular(self):
        accion = 'Modificar telefono particular'
        msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.txt_CambioDpl_Tel_CodInterurbano_xp
            self.write(xpath, self.codInterU, 3)
            xpath2 = DatosPersonales.txt_CambioDpl_Tel_Telefono_xp
            self.write(xpath2, self.TelNum, 3)
            self.capture_image(msgOk)

    def actualizarTelefonoParticularAlternativo(self):
        accion = 'Modificar telefono particular'
        msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.txt_CambioDpl_TelAlt_CodInterurbano_xp
            self.write(xpath, self.codInterU, 3)
            xpath2 = DatosPersonales.txt_CambioDpl_TelAlt_Telefono_xp
            self.write(xpath2, self.AltTelNum, 3)
            self.capture_image(msgOk)

    def actualizarCodigoPostal(self):
        accion = 'Modificar codigo postal'
        msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.txt_CambioDpl_Dom_CodPostal_xp
            self.write(xpath, self.codPostal, 3)
            self.capture_image(msgOk)

    def actualizarEmail(self,email):
        to = 10
        accion = 'Modificar eMail'
        msgOk = accion
        # msgFail = 'No se pudo ' + msgOk.lower()
        with self.step(accion):
            xpath = DatosPersonales.txt_CambioCm_Mail
            self.write(xpath, email, to)
            self.capture_image(msgOk)

    def actualizarNumCalle(self):
        accion = 'Modficiar numero de domicilio'
        msgOk = 'Se pudo {}'.format(accion.lower())
        # msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            self.write(DatosPersonales.inp_CambioDpl_Dom_NumCalle_xp,
                       self.numCalle, to)
            self.capture_image(msgOk)

    def get_paso_actual(self):
        """Metodo para obtener el paso actual de la modificacion de datos"""
        return self.get_element_text(DatosPersonales.div_paso_actual)

    def ingresarClaveItau(self):
        """Metodo para ingresar la clave itau en el input correspondiente"""
        accion = "Ingresar clave itau"
        msgOk = 'Se pudo {}'.format(accion.lower())
        # msgFail = 'No {}'.format(msgOk.lower())
        to = 10
        with self.step(accion):
            xpath = DatosPersonales.inp_clave_itau
            self.write(xpath, self.clave, to)
            self.capture_image(msgOk)

    def verificarDatosModificados(self):
        """
        Metodo para verificar que se haya modificado correctamente la altura
        de la direccion particular
        """
        accion = u'Verificar que se modificó el dato'
        msgOk = u'Se pudo {}'.format(accion.lower())
        msgFail = u'No {}'.format(msgOk.lower())
        with self.step(accion):
            xpath = DatosPersonales.txt_DirParticular
            texto = self.get_element_text(xpath)
            if str(self.numCalle) in texto:
                self.capture_image(msgOk)
            else:
                self.fail_msg(msgFail)
