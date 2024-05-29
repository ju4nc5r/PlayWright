from selenium.webdriver.common.by import By
from SeleniumFramework.constants.spanish_messages import MsgMouse, MsgJS
from SeleniumFramework.constants.constants import (CLICK, SCROLL, SET_ATTRIBUTE, STYLE, BORDER, NEW_TAB, BACK)


class js(object):
    def selectElement__js(self, xpath, msgOk, msgFail, sleep=5):
        """ Method to click an element by js """
        self.jsClick(xpath)
        self.log.info(MsgMouse.MSG_CLICK_ELEM.format(xpath))
        return True

    def jsClick(self, xpath):
        """ Method to click an element by js """
        localizador = self.driver.find_element(by=By.XPATH, value=xpath)
        self.driver.execute_script(CLICK, localizador)

    def go_to_xpath(self, xpath):
        """
        Method to scroll to searched element
        :param xpath: String. Xpath of searched element.
        """
        if self.visibility_element(xpath, 5):
            localizador = self.driver.find_element(by=By.XPATH, value=xpath) 
            self.driver.execute_script(SCROLL, localizador)
            self.log.info(MsgJS.MSG_SCROLL.format(xpath))
            return True
        return False

    def highlight(self, xpath, description):
        """
        Method to highlight an element
        :param xpath: String. Xpath of searched element
        :param description: String. Description of screenshot
        """
        def apply_style(s):
            """ Method to apply a style for highlight """
            self.driver.execute_script(SET_ATTRIBUTE, objeto, s)
        self.visibility_element(xpath)
        objeto = self.driver.find_element(by=By.XPATH, value=xpath)
        estilo_original = objeto.get_attribute(STYLE)
        apply_style(BORDER)
        self.log.info(MsgJS.MSG_HIGHLIGHT.format(xpath))
        self.wait(0.1)
        self.capture_image(description, sleep=0.2)
        apply_style(estilo_original)

    def create_tab_js(self, url):
        """
        Method to execute a js script to create a new tab in the browser
        :param url: String. URL for the new tab
        """
        self.driver.execute_script(NEW_TAB.format(url))
        self.log.info(MsgJS.MSG_CREATE_TAB.format(url))

    def back_js(self):
        """
        Method to return to a previous page
        """
        self.driver.execute_script(BACK)
        self.log.info(MsgJS.MSG_BACK)
