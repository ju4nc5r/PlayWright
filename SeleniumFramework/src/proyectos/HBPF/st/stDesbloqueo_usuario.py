from SeleniumFramework.src.proyectos.HBPF.st.stBOeliminar_cliente import stBOeliminar_cliente


class stDesbloqueo_usuario(stBOeliminar_cliente):
    def desbloqueo_usuario(self):
        self.solicitud_desbloqueo()

    def solicitud_desbloqueo(self):
        self.login(self.user_BO, self.clave_BO)
        self.seleccionarMenuAdministrarClientes()

    def login(self, usuario, clave):
        self.completarUsuario(usuario)
        self.seleccionarContinuar()
        self.completarClave(clave)
        self.seleccionarIngresar()

    def seleccionar_DesbloqueoOperadores(self):
        self.seleccionarClientes()
        