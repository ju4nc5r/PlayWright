# -*- coding: utf-8 -*-
from PlaywrightFramework.allure_driver import allure_driver
from PlaywrightFramework.image import image
from PlaywrightFramework.projects.HBPF.st.stBrowser import stBrowser


class stLogin(stBrowser):
    allure = allure_driver()
    def __init__(self) -> None:
        page = stBrowser(nav_off=False, rec=f'../files/videos/{self._testMethodName}')
        self.HB = page
        #self.result_links = page.locator('a[data-testid="result-title-a"]')
        #self.search_input = page.locator('#search_form_input')


    def deslogueo(self):
        ''' Metodo para realizar el logout de la aplicacion de homebanking '''
        accion = u'Desloguear de la aplicacion'
        xpath1 = locLogin.btnConfig
        xpath = locLogin.btnSalir
        msgOk, msgFail = get_msg(accion)
        to = 3
        with self.step(accion):
            self.selectElement(xpath1, msgOk, msgFail, to)
            self.select_by_text(xpath, "Cerrar Sesión")
            #self.select_option(xpath, msgOk, msgFail, to, "Cerrar Sesión")
            #self.selectListByPartialText(xpath, "Cerrar Sesión")