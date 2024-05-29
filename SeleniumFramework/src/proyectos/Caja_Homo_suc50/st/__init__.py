from SeleniumFramework.src.utils.settings import caja_user, caja_pass

def inicioICaja(self):
    self.finalizo = False
    self.logueado = False
    self.skip = False
#     self.HacerCierreSesion = False
    self.openICaja()
    # self.user = caja_user
    # self.clave = caja_pass

def inicioAdminCaja(self):
    self.finalizo = False
    self.skip = False
    self.logueado = False
#     self.HacerCierreSesion = False
    self.openAdminCaja()
    self.user = caja_user
    self.clave = caja_pass

def inicioAutorizCaja(self):
    self.finalizo = False
    self.logueado = False
    self.skip = False
    self.openAutorizCaja()
    # self.user = caja_user
    # self.clave = caja_pass
    
def fin(self):
#     if self.HacerCierreSesion:       
#         self.deslogueo()
    
    if self.finalizo:        
        self.ok_test()
        
    elif self.skip:
        pass
        
    else:           
        self.fail_test(self.error)
        
#     if self.cerrarSesion:
    self.close_browser()