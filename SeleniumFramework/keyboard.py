from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException
from SeleniumFramework.constants.spanish_messages import MsgKeyboard


class keyboard(object):
    def send_key(self, xpath, key):
        """
        Method to enter a specific key by string
        :param key: String. Name of key to use
        """
        key_object = self.obtain_key(key)
        if key_object is not None:
            self.search_element_by_xpath(xpath).send_keys(key_object)
            self.log.info(MsgKeyboard.MSG_INPUT_KEY.format(key, xpath))
        else:
            self.log.warning(MsgKeyboard.MSG_INPUT_KEY_ERROR)

    def combine_keys(self, xpath, key_list):
        """
        Method to enter a combination of keys in a element
        :param xpath: String. Xpath of element
        :param key_list: list. list of name of keys
        """
        keys = ''
        for i in key_list:
            key = self.obtain_key(i)
            keys += key
        self.search_element_by_xpath(xpath).send_keys(keys)
        self.log.info(MsgKeyboard.MSG_INPUT.format(keys, xpath))

    def obtain_key(self, key):
        """
        Method to search a key object by string
        :param key: String. Name of key to use
        """
        key = key.lower()
        mapa = {
            'enter': Keys.ENTER,
            'alt': Keys.ALT,
            'backspace': Keys.BACKSPACE,
            'control': Keys.CONTROL,
            'delete': Keys.DELETE,
            'escape': Keys.ESCAPE,
            'shift': Keys.SHIFT,
            'space': Keys.SPACE,
            'tab': Keys.TAB,
            'end': Keys.END,
            'home': Keys.HOME,
            'page_down': Keys.PAGE_DOWN,
            'page_up': Keys.PAGE_UP,
            'up': Keys.UP,
            'down': Keys.DOWN,
            'left': Keys.LEFT,
            'right': Keys.RIGHT,
            'f1': Keys.F1,
            'f2': Keys.F2,
            'f3': Keys.F3,
            'f4': Keys.F4,
            'f5': Keys.F5,
            'f6': Keys.F6,
            'f7': Keys.F7,
            'f8': Keys.F8,
            'f9': Keys.F9,
            'f10': Keys.F10,
            'f11': Keys.F11,
            'f12': Keys.F12
        }
        try:
            return mapa[key]
        except KeyError:
            return key

    def write(self, xpath, text, to):
        """
        Method to write a text in a input.
        :param xpath: String. Xpath of the searched element.
        :param text: String/Integer. Text to input
        :param to: Integer. Timeout
        """
        if self.visibility_element(xpath, to):
            self.clear(xpath)
            if text is None:
                text = ''
            self.search_element_by_xpath(xpath).send_keys(text)
            self.log.info(MsgKeyboard.MSG_INPUT.format(xpath, text))
            return True
        else:
            return False
        
    def write_2(self, xpath, text, to):
        """
        Method to write a text in a input.
        :param xpath: String. Xpath of the searched element.
        :param text: String/Integer. Text to input
        :param to: Integer. Timeout
        """
        if self.visibility_element(xpath, to):
            self.clear(xpath)
            if text is None:
                text = ''
            self.search_element_by_xpath(xpath).send_keys(text)
            return True
        else:
            return False

    def write_css(self, css_elem, text, timeout):
        """
        Method to write a text in a input.
        :param xpath: String. Xpath of the searched element.
        :param text: String/Integer. Text to input
        :param to: Integer. Timeout
        """
        if self.visibility_element_css(css_elem, timeout):
            self.clear_css(css_elem)
            self.search_element_by_xpath(css_elem).send_keys(text)
            self.log.info(MsgKeyboard.MSG_INPUT.format(css_elem, text))
            return True
        else:
            return False

    def clear(self, xpath):
        """
        Method to clear an input or a textarea
        :param xpath: String. Xpath of the element
        """
        try:
            self.search_element_by_xpath(xpath).clear()
            self.log.info(MsgKeyboard.MSG_CLEAR)
        except InvalidElementStateException as e:
            self.log.error(MsgKeyboard.MSG_CLEAR_ERROR.format(e, xpath))

    def clear_css(self, css_elem):
        """
        Method to clear an input or a textarea
        :param xpath: String. Xpath of the element
        """
        try:
            self.search_element_by('css', css_elem).clear()
            self.log.info(MsgKeyboard.MSG_CLEAR)
        except InvalidElementStateException as e:
            self.log.error(MsgKeyboard.MSG_CLEAR_ERROR.format(e, css_elem))
