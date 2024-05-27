from PlaywrightFramework.projects.HBPF.st.stBrowser import stBrowser
from PlaywrightFramework.allure_driver import allure_driver


class stLoginNew(stBrowser):
    allure = allure_driver()

    def completarUsuario(self):
        accion = 'Completar Usuario'
        with self.allure.simple_step(accion):

            self.page.get_by_placeholder("usuario").click()
            self.page.get_by_placeholder("usuario").fill("Usuarioautouno1")