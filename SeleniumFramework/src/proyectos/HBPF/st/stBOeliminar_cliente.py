# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.st.pasos import abrirNavegador
from SeleniumFramework.src.proyectos.HBPF.loc.locBO_eliminarCliente import locBO_eliminarCliente
from SeleniumFramework.common_functions import get_msg


class stBOeliminar_cliente(abrirNavegador):

    # con pendientes
    def stBOeliminar_cliente(self):
        """ Metodo para soliciar la baja de un cliente"""
        self.completarUsuario(self.user_BO)
        self.seleccionarContinuar()
        self.completarClave(self.clave_BO)
        self.seleccionarIngresar()
        self.seleccionarMenuAdministrarClientes()
        self.seleccionarClientes()
        self.seleccionarTipoDocumento()
        self.completarNroDocumento()
        self.seleccionarBuscar()
        self.seleccionarClienteListado()
        self.seleccionarCmdEliminar()
        self.seleccionarCmdAceptar()
        self.verificarOperacionSatisfactoria()
        self.seleccionarCmdOk()
        self.verificarEstadoPendienteEliminacion()
        self.seleccionarCmdSalir()
        self.confirmarCmdCerrarSesion()

    def confirmarEliminar_Cliente(self):
        """
        Metodo para confirmar la baja de un cliente. Primero se tiene
        que ejecutar el metodo stBOeliminar_cliente
        """
        self.completarUsuario(self.user2_BO)
        self.seleccionarContinuar()
        self.completarClave(self.clave2_BO)
        self.seleccionarIngresar()
        self.seleccionarMenuAdministrarClientes()
        self.seleccionarClientes()
        self.seleccionarTipoDocumento()
        self.completarNroDocumento()
        self.seleccionarBuscar()
        self.seleccionarClienteListado()
        self.seleccionarCmdAutorizar()
        self.seleccionarCmdAutorizarAceptar()
#         self.verificarOperacionSatisfactoria() (Se comenta porque el msj de BO ,no es verdadero)

    def desadherir_usuario(self):
        """
        Metodo para realizar la baja de un cliente. Se realiza la solicitud
        y la confirmacion de la baja del cliente.
        """
        accion = 'Desadherir usuario'
        with self.simple_step(accion):
            self.stBOeliminar_cliente()
            self.confirmarEliminar_Cliente()

    def completarUsuario(self, user):
        to = 10
        accion = 'Completar Usuario'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            self.write(str(locBO_eliminarCliente.inputUsuario), user, to)
            self.capture_image(msgOk)

    def seleccionarContinuar(self):
        to = 10
        accion = 'Seleccionar Continuar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.cmdContinuar
            self.visibility_element(xpath, to)
            self.selectElement(xpath, msgOk, msgFail, to)

    def completarClave(self, clave):
        accion = 'Seleccionar Continuar'
        to = 10
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.inputClave
            self.visibility_element(xpath, to)
            self.write(xpath, clave, to)
            self.capture_image(msgOk)

    def seleccionarIngresar(self):
        to = 10
        accion = 'Seleccionar Ingresar'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath_select = locBO_eliminarCliente.cmdIngresar
            xpath_verif = locBO_eliminarCliente.titulo_controlCenter
            self.selectElement(xpath_select, msgOk, msgFail, to)
            self.verifySelection(xpath_verif, accion, to)

    def seleccionarMenuAdministrarClientes(self):
        to = 10
        accion = 'Seleccionar Menu Administrar Clientes'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.menuAdministracionClientes
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(msgOk)

    def seleccionarClientes(self):
        to = 15
        accion = 'Seleccionar Clientes'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.subMenu_cliente
            xpath_verif = locBO_eliminarCliente.TipoDocumento
            self.selectElement__js(xpath, msgOk, msgFail, to)
            self.verifySelection(xpath_verif, accion, to)
    
    def seleccionarDesbloqueoOp(self):
        to = 15
        accion = 'Seleccionar Desbloqueo de operadores'
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.desbloqueo_Operador
            xpath_verif = locBO_eliminarCliente.TipoDocumento
            self.selectElement__js(xpath, msgOk, msgFail, to)
            self.verifySelection(xpath_verif, accion, to)

    def seleccionarTipoDocumento(self):
        accion = 'Seleccionar Clientes'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.TipoDocumento
            self.select_by_value(xpath, self.tipoDoc)
            self.capture_image(msgOk)

    def completarNroDocumento(self):
        to = 15
        accion = 'completar Nro. Documento'
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.NroDocumento
            self.write(xpath, self.nroDoc, to)
            self.capture_image(msgOk)

    def seleccionarBuscar(self):
        to = 15
        accion = "Seleccionar Buscar"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = locBO_eliminarCliente.cmdBuscar
            self.selectElement(xpath, msgOk, msgFail, to)

    def seleccionarClienteListado(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            self.capture_image(accion)
            xpath = ".//*[@id='tag_row1']/td[1]"
            if self.visibility_element(xpath, to):
                self.selectElement(xpath, msgOk, msgFail, to)
            else:
                self.skip_msg('El usuario no esta dado de alta')

    def seleccionarCmdEliminar(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = "//input[contains(@value,'Eliminar')]"
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = "//div[contains(@class,'titulo')]"
            self.verifySelection(xpath, accion, to)

    def seleccionarCmdAceptar(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = "//input[contains(@value,'Aceptar')]"
            self.selectElement(xpath, msgOk, msgFail, to)

    def verificarOperacionSatisfactoria(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = (
                "//fieldset[contains(.,"
                "'ha sido realizada satisfactoriamente')]"
            )
            self.verifySelection(xpath, msgOk, to)

    def seleccionarCmdOk(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = "//input[contains(@value,'Ok')]"
            self.selectElement(xpath, msgOk, msgFail, to)

    def verificarEstadoPendienteEliminacion(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, _ = get_msg(accion)
        with self.step(accion):
            xpath = "//td[contains(.,'Activo Pend. Eliminaci')]"
            self.verifySelection(xpath, msgOk, to)

    def seleccionarCmdSalir(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = "//a[contains(.,'Salir  ')]"
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = (
                "//button[contains(@class,'btn primario') and "
                "contains(.,'Cerrar')]"
            )
            self.verifySelection(xpath, msgOk, to)

    def confirmarCmdCerrarSesion(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = (
                "//button[contains(@class,'btn primario') and "
                "contains(.,'Cerrar')]"
            )
            self.selectElement(xpath, msgOk, msgFail, to)
            self.capture_image(msgOk)

    def seleccionarCmdAutorizar(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = "//input[contains(@value,'Autorizar')]"
            self.selectElement(xpath, msgOk, msgFail, to)
            xpath = "//input[contains(@value,'Aceptar')]"
            self.verifySelection(xpath, msgOk, to)

    def seleccionarCmdAutorizarAceptar(self):
        to = 15
        accion = "Seleccionar Cliente Listado"
        msgOk, msgFail = get_msg(accion)
        with self.step(accion):
            xpath = "//input[contains(@value,'Aceptar')]"
            self.selectElement(xpath, msgOk, msgFail, to)
