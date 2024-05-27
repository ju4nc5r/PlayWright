from ..st.stBrowser import stBrowser
from PlaywrightFramework.config.utils import config

def inicio_test(self, clean=False) -> None:
    utils = config()
    utils.vaciar_carpeta_allure(on=clean)
    self.finalizo = False

def finalizar_test(self):
    if self.finalizo:
        self.HB.deslogueo()
        self.HB.closeHB()
        #self.ok_test()