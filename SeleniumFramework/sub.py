# -*- coding: utf-8 -*-
import pytest
import time
from SeleniumFramework.constants.spanish_messages import MsgSearch
from SeleniumFramework.constants.spanish_messages import (
    MSG_RETRY, MSG_WAITING, MSG_UPLOAD, MSG_UPLOAD_DONE, MSG_UPLOAD_FAIL)
from selenium.common.exceptions import WebDriverException
from SeleniumFramework.browser import browser
from SeleniumFramework.mouse import mouse
from SeleniumFramework.keyboard import keyboard
from SeleniumFramework.search import search
from SeleniumFramework.select_element import select
from SeleniumFramework.error_management import errors
from SeleniumFramework.js import js
from SeleniumFramework.image import image
from SeleniumFramework.webelement import webelement
from SeleniumFramework.log import log
from SeleniumFramework.allure_driver import allure_driver


class sub(browser, keyboard, mouse, search, select, js,
          image, webelement, log, allure_driver, errors):

    def verifySelection_highlight(self, verificar_xpath, accion, sleep=7):
        if self.visibility_element(verificar_xpath, sleep):
            self.resaltar(verificar_xpath, accion, sleep)
            self.capture_image(MsgSearch.MSG_VERIFY.format(accion))
            return True
        self.wait(2)
        self.capture_image(accion)
        self.log.error(MsgSearch.MSG_VERIFY_ERROR.format(accion))
        pytest.fail(accion)
        return False

    def resaltar(self, xpath, descripcion, sleep=0.1):
        self.visibility_element(xpath)
        objeto = self.driver.self.driver.find_element(by=By.XPATH, value=xpath)

        def aplicar_estilo(s):
            self.driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1])", objeto, s)
        estilo_original = objeto.get_attribute('style')
        aplicar_estilo("border: 4px solid red")
        self.wait(sleep)
        self.capture_image(descripcion)
        aplicar_estilo(estilo_original)

    def verify_values(self, initxpath, endxpath, msgOk, msgFail, find_text):
        self.log.info(MsgSearch.MSG_VERIFY_VALUES.format(len(find_text)))
        elementos_no_encontrados = []
        i = 0
        cont = 0
        while i < len(find_text):
            xpath = '{}{}{}'.format(initxpath, i, endxpath)
            if self.verifiy_value(xpath, msgOk, msgFail, find_text[i]):
                cont += 1
            else:
                self.capturar_imagen(msgFail)
                if self.visibility_element(xpath):
                    elementos_no_encontrados.append(
                                                self.get_element_text(xpath))
            i += 1
        if cont == len(find_text):
            self.log.info(msgOk)
        else:
            self.log.error(msgFail)
        self.log.info(MsgSearch.MSG_VERIFY_VALUES_RESULT.format(len(find_text),
                                              len(elementos_no_encontrados),
                                              find_text))

    def goToSection(self, xpath, msgOk, msgFail):
        if self.go_to_xpath(xpath):
            self.capture_image(msgOk)
        else:
            self.capture_image(msgFail)

    def countItems(self, xpathini, xpathend, indice=0):
        contador = 0
        list_textos_encontrados = []
        xpath = xpathini + str(indice) + xpathend
        while self.visibility_element(xpath):

            contador = contador + 1
            self.log.info("elemento = %s" %self.get_element_text(xpath))
            list_textos_encontrados.append(self.get_element_text(xpath))
            indice += 1
            xpath = xpathini + str(indice) + xpathend
        else:
            self.log.info("No existen mas elementos para contar")
        self.log.info("Contar Elementos-Contador = %d" % contador)
        self.captureImage()
        return contador, list_textos_encontrados

    def SearchTableElements(
        self, xpathini, xpathend, indice, findText, msgOk, msgFail):
        contador, lista = self.countItems(xpathini, xpathend, indice)
        if findText in lista:
            self.log.info(msgOk)
        else:
            pytest.fail(msgFail)
        return contador, lista

    def SearchTableElements_paged(
        self, xpathini, xpathend, indice, findText, paginado_xpath):
        listanueva = []
        contador, lista = self.countItems(xpathini, xpathend, indice)
        while self.visibility_element(paginado_xpath):
            self.driver.find_element_by_xpath(paginado_xpath).click()
            contador, listanueva = self.countItems(xpathini, xpathend, indice)
#             listanueva= itertools.chain(lista,listanueva)
        # else:
        #     return False
        return listanueva

    def retrySelection(
        self, xpath_select, xpath_verif, accion, msgOk, msgFail, to):
        flag_verif = False
        for i in range(1, 3):
            self.log.info(MSG_RETRY.format(i))
            if not flag_verif:
                if not self.select(xpath_select, to):
                    flag_verif = False
                if self.visibility_element(xpath_verif, to):
                    self.verifySelection(xpath_verif, accion, to)
                    flag_verif = True
                    break
                else:
                    flag_verif = False
        if flag_verif:
            return True
        return False

    def wait(self, seconds):
        """
        Method to wait the few second in the application
        :param seconds: Integer. Second to wait
        """
        self.log.info(MSG_WAITING.format(seconds))
        time.sleep(seconds)

    def compareText(self, xpath, expected_text):
        """
        Method to compare two string, one is from a webelement and the other
        is an expected text
        :param xpath: String. Xpath of the element
        :param expected_text: String.
        :return: Boolean
        """
        text = self.get_element_text(xpath)
        if expected_text in text:
            self.capture_image(MsgSearch.MSG_COMPARE_TEXT.format(
                expected_text, xpath))
            return True
        self.log.error(
            MsgSearch.DSC_COMPARE_TEXT.format(expected_text, text)
        )
        self.capture_image(MsgSearch.MSG_COMPARE_TEXT_FAIL)
        return False

    def uploadFile(self, xpath, filePath, to=10):
        """
        Method to upload a file in a button, without use the windows's explore
        :param xpath: String. You need the element with input tag and file type
                      in the button. For example, //input[@type='file'].
        :param filePath: String. Path of the file to upload.
        :param to: Integer. Time to wait for the element
        :return: Boolean. Return True if the method could upload the file.
                          Return False if the method couldn't find the file.
        """
        self.log.info(MSG_UPLOAD)
        try:
            self.write(xpath, filePath, to)
            self.log.info(MSG_UPLOAD_DONE.format(filePath))
            return True
        except WebDriverException:
            self.log.warning(MSG_UPLOAD_FAIL.format(filePath))
            return False
