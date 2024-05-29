from SeleniumFramework.src.utils.settings import caja_user, caja_pass

def inicioICaja(self):
    self.finalizo = False
    self.logueado = False
    self.openICaja()
    # self.user = caja_user
    # self.clave = caja_pass

def inicioAdminCaja(self):
    self.finalizo = False
    self.logueado = False
    self.openAdminCaja()
    self.user = caja_user
    self.clave = caja_pass

def inicioAutorizCaja(self):
    self.finalizo = False
    self.logueado = False
    self.openAutorizCaja()
    # self.user = caja_user
    # self.clave = caja_pass
    
def fin(self):
    if self.logueado:
        self.deslogueo()
    
    if self.finalizo:        
        self.ok_test()
    else:           
        self.fail_test(self.error)
    self.close_browser()