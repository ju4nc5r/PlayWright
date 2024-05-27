from selenium.webdriver.common.action_chains import ActionChains
from SeleniumFramework.constants.spanish_messages import MsgMouse


class mouse(object):
    def select(self, xpath, to=5):
        """
        Method to click an element
        :param xpath: String. Xpath of element
        :param to: Integer. Timeout
        :return: Boolean
        """
        if self.be_clickable(xpath, to):
            self.search_element_by_xpath(xpath).click()
            return True
        return False

    def selectElement(self, xpath, msgOk, msgFail, to=5):
        if self.visibility_element(xpath, to):
            self.select(xpath, to)
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(xpath))
            return True
        self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(xpath))
        return False

    def select_css(self, css_elem, to=5):
        if self.be_clickable_css(css_elem, to):
            self.search_element_by('css', css_elem).click()
            return True
        return False

    def selectElement_css(self, css_elem, to=5):
        if self.visibility_element_css(css_elem, to):
            self.select_scc(css_elem, to)
            self.login.info(MsgMouse.MSG_CLICK_ELEM.format(css_elem))
            return True
        self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(css_elem))
        return False

    def selectElement_highlight(self, xpath, msgOk, msgFail, sleep=5):
        if self.visibility_element(xpath, sleep):
            self.highlight(xpath, msgOk, sleep)
            self.select(xpath)
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(msgOk))
            return True
        self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(xpath))
        self.fail(msgFail)
        return False

    def doubleClick(self, xpath):
        """
        Method to do double click on an element
        :param xpath: String. Xpath of the searched element
        """
        if self.visibility_element(xpath, 10):
            elem = self.search_element_by_xpath(xpath)
            actionChains = ActionChains(self.driver)
            actionChains.double_click(elem).perform()
            self.log.info(MsgMouse.MSG_DOUBLE_CLICK.format(xpath))
            return True
        return False

    def click(self, xpath):
        """
        Method to do click on an element
        :param xpath: String. Xpath of the searched element
        """
        if self.visibility_element(xpath, 10):
            elem = self.search_element_by_xpath(xpath)
            actionChains = ActionChains(self.driver)
            actionChains.click(elem).perform()
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(xpath))
            return True
        return False


    def drag_and_drop(self, xpath, target_xpath):
        """
        Method to drag and drop an element in other element
        :param xpath: String. Xpath of the source element
        :param target_xpath: String. Xpath of the target element
        """
        to = 10
        source = self.visibility_element(xpath, to)
        target = self.visibility_element(target_xpath, to)
        if source and target:
            action_chains = ActionChains(self.driver)
            source = self.search_element_by_xpath(xpath)
            target = self.search_element_by_xpath(target_xpath)
            action_chains.drag_and_drop(source, target)
            self.log.info(MsgMouse.MSG_DRAG_DROP.format(xpath, target_xpath))
            return True
        return False

    def mouse_over_xpath(self, xpath):
        """
        Method to move the mouse over an element
        :param xpath: String. Xpath of the source element
        """
        element = self.driver.find_element_by_xpath(xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()


'''
Created on 23 oct. 2023

@author: FO433151
'''
import pyautogui


class Mouse_Dsk():

    ### MOVIMIENTOS DE MOUSE
    def zide_windows(self):
        """este metodo devuelve las proporciones de la pantalla"""
        pantalla = pyautogui.size()
        self.log.info(pantalla)
        return pantalla

    def simulate_scroll_up(self, up):
        """este metodo simula el scroll del mause para arriba"""
        pyautogui.PAUSE = 2.8
        pyautogui.scroll(up)
        self.log.info(up)

    def simulate_scroll_down(self, down):
        """este metodo simula el scroll del mause para abajo"""
        pyautogui.PAUSE = 2.8
        pyautogui.scroll(down)
        self.log.info(down)

    ##### SIMULACION DE CLICKS

    def simulate_click(self):
        """este metodo simula el click del mouse"""
        pyautogui.PAUSE = 2.8
        pyautogui.click()
        self.log.info("click a un elemto")

    def simulate_click_from_image(self, x, y):
        """este metodo simula el click del mouse ala coordenada dada"""
        pyautogui.PAUSE = 2.8
        pyautogui.click(x, y)
        self.log.info("click a un elemto X:{} Y:{}").format(x, y)
