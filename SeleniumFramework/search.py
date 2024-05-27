from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from SeleniumFramework.constants.spanish_messages import MsgSearch
from SeleniumFramework.common_functions import get_msg


class search(object):
    def search_element_by_xpath(self, xpath):
        """
        Method to search an element by xpath
        :param xpath: String. Xpath of searched element
        :return: WebElement.
        """
        return self.search_element_by(By.XPATH, xpath)

    def search_element_by_id(self, elem_id):
        """
        Method to search an element by id
        :param elem_id: String. Id of searched element
        :return: WebElement.
        """
        return self.search_element_by(By.ID, elem_id)

    def search_element_by(self, by, value):
        self.log.info(MsgSearch.MSG_SEARCH_ELEM_BY.format(by, value))
        return self.driver.find_element(by, value)

    def search_elements(self, xpath, to):
        """
        Method to get all elements present by xpath
        :param xpath: String. Elements to search
        :param to: Integer. Timeout
        :return: list of WebElement
        """
        if self.visibility_element(xpath, to):
            elems = self.driver.find_elements_by_xpath(xpath)
            self.log.info(MsgSearch.MSG_SEARCH_ELEMS.format(
                                                        len(elems), xpath))
            return elems
        return None
    
    def search_elements_no_visibility(self, xpath, to):
        """
        Method to get all elements present by xpath
        :param xpath: String. Elements to search
        :param to: Integer. Timeout
        :return: list of WebElement
        """
        elems = self.driver.find_elements_by_xpath(xpath)
        self.log.info(MsgSearch.MSG_SEARCH_ELEMS.format(
                                                    len(elems), xpath))
        return elems

    def visibility_element(self, xpath, to=2):
        """
        Method to wait for an element to be visible
        :param xpath: String. Xpath of searched element
        :param to: Integer. Timeout
        """
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            self.log.warning(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(xpath))
            return False
        self.log.info(MsgSearch.MSG_SEARCH_ELEM.format(xpath))
        return True
    
    
    def visibility_element2(self, xpath, to=2):
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            return False
        return True
        

    def visibility_element_css(self, css_elem, to=2):
        """
        Method to wait for an element to be visible
        :param xpath: String. Xpath of searched element
        :param to: Integer. Timeout
        """
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                         css_elem)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            self.log.warning(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(css_elem))
            return False
        self.log.info(MsgSearch.MSG_SEARCH_ELEM.format(css_elem))
        return True

    def be_clickable(self, xpath, to=2):
        """
        Method to wait for an element to be clickable
        :param xpath: String. Xpath of searched element
        :param to: Integer. Timeout
        """
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            self.log.error(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(xpath))
            return False
        return True

    def be_clickable_css(self, css_elem, to=2):
        """
        Method to wait for an element to be clickable
        :param css: String. Css of searched element
        :param to: Integer. Timeout
        """
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_elem)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            self.log.error(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(css_elem))
            return False
        return True

    def double_visibility_element(self, xpath1, xpath2, timeout):
        """
        Method to wait two element.
        :param xpath1: String. First element to wait
        :param xpath2: Strign. Second element to wait
        :param timeout: Integer. Timeout
        :return: True if find first element.
                 False if find second element.
                 None if none of elements is found
        """
        self.log.info(MsgSearch.MSG_DOUBLE_SEARCH)
        while timeout > 0:
            if self.visibility_element(xpath1, 1):
                return True
            elif self.visibility_element(xpath2, 1):
                return False
            timeout -= 1
        self.fail(MsgSearch.MSG_DOUBLE_SEARCH_ERROR)

    def array_visibility(self, elem_list, timeout):
        """
        Method to wait many element in a list. Return the finded element index
        :param elem_list: List. List of xpath of elements
        :param timeout: Integer. Timeout in seconds
        :return: Integer. Index of finded element
        """
        self.log.info(MsgSearch.MSG_ARRAY_SEARCH)
        finded = None
        while timeout > 0:
            for elem in elem_list:
                if self.visibility_element(elem, 0):
                    finded = elem
                    break
            timeout -= 1
            #self.wait(1)
            if finded is not None:
                break
        if finded is None:
            self.fail(MsgSearch.MSG_DOUBLE_SEARCH_ERROR)
        else:
            return elem_list.index(finded)

    def verifySelection(self, xpath, accion, to=7):
        """
        Method to check if an element if visible
        :param xpath: String. Xpath of the element
        :param accion: String. Description to attach in allure
        :param to: Integer. TimeOut
        """
        if self.visibility_element(xpath, to):
            self.capture_image(MsgSearch.MSG_VERIFY.format(accion))
            return True
        self.wait(2)
        self.log.error(MsgSearch.MSG_VERIFY_ERROR.format(accion))
        accion = 'No {}'.format(accion.lower())
        self.capture_image(accion)
        self.fail(accion)
        return False

    def verify_value(
            self, xpath, msgOk, msgFail, find_text, sleep=5, capturar=True):
        """
        Method to compare an element's text with a text
        :param xpath. String. Xpath of the searched element
        :param find_text: String. Expected text.
        :return: True. If text of element is same as the expected text
                 False. If text of element isn't same
        """
        self.wait(sleep)
        if self.visibility_element(xpath):
            value = self.get_element_text(xpath)
        else:
            self.fail(msgFail)
            return False
        if capturar:
            self.capture_image(
                MsgSearch.DSC_COMPARE_TEXT.format(find_text, value)
            )
        if value == find_text:
            self.log.info(MsgSearch.MSG_COMPARE_TEXT.format(find_text, xpath))
            return True
        self.fail(
            MsgSearch.MSG_COMPARE_TEXT_ERROR.format(find_text, xpath)
        )
        return False

    def checkFields(self, listaCampos, msgOk, msgFail):
        """
        Method to search many items in the browser
        :param listaCampos: list. List of xpath of searched element
        """
        listaOK = []
        listaNoOk = []
        for elem in listaCampos:
            if self.visibility_element(elem):
                listaOK.append(elem)
            else:
                listaNoOk.append(elem)

        if len(listaNoOk) > 1:
            self.log.error(MsgSearch.MSG_CHECK_FIELD_ERROR)
            self.fail(msgFail)
            self.capturar_imagen(msgFail)
        else:
            self.capturar_imagen(msgOk)
        self.log.info(MsgSearch.MSG_RESULT_CHECK_FIELD.format(
            len(listaCampos), len(listaOK), len(listaNoOk))
        )

    def verify(self, verificar_xpath, to=7):
        if self.visibility_element(verificar_xpath, to):
            return True
        return False

    def checkElement(self, xpath, accion, to=10):
        """
        Method to check if an element is visible in the webpage. If it's
        visible, then highlight the element and capture an image,
        else if it isn't visible, then show
        an error
        :param xpath: String. String of the element
        :param msgOk: String. String to print in the screenshoot
        :param msgFail: String. String of error to print in the log
        """
        msgOk, msgFail = get_msg(accion)
        if self.visibility_element(xpath, to):
            self.highlight(xpath, msgOk)
        else:
            self.fail(msgFail)
