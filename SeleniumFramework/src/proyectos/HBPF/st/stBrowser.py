from SeleniumFramework.sub import sub
from SeleniumFramework.src.utils.settings import url_hb


class stBrowser(sub):
    def openHB(self):
        accion = 'Abrir Home Banking'
#         msgOk=accion
#         msgFail='No se pudo ' + lower(msgOk)
        self.paso = 0
        with self.step(accion):
            self.openChrome(url_hb)
            msg = "Open Chrome"
            self.capture_image(msg)
