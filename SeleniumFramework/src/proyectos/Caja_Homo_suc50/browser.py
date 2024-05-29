import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from SeleniumFramework.constants.spanish_messages import MsgBrowser
from SeleniumFramework.constants.constants import (SAFEBROWSING, AUTOLOGIN, N_TRUSTED_URIS, AUTOMATIC_NTLM,
                                         N_DELEGATION, DOMAIN, PROXY, BINARY, IGNORE_CERTIFICATE, CHROME, FIREFOX,
                                         CHROME_P, FIREFOX_P, CHROME_EO)


class browser(object):
    def openChrome(self, url):
        """
        Open a Chrome browser and create a log
        :param url: String. Url to open
        """
        self.createLog()
        try:
            self.log.info(MsgBrowser.MSG_OPEN_CHROME)                 
            options = webdriver.ChromeOptions()
            options.add_argument('--kiosk-printing')
            options.add_argument('--ignore-certificate-errors')
            self.driver = webdriver.Chrome((ChromeDriverManager().install()))
            self.maximize_screen()
            self.set_url(url)
        except Exception as e:
            self.fail_test(e)
            
            
    def openChromeIncognito(self, url):
        """
        Open a Chrome browser Incognito and create a log
        :param url: String. Url to open
        """
        #self.createLog()
        try:              
            options = webdriver.ChromeOptions()
            options.add_argument('--kiosk-printing')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            self.driver = webdriver.Chrome(options=options)
            self.maximize_screen()
            self.set_url(url)
        except Exception as e:
            #self.fail_test(e)
            raise e
    

    def openFirefox(self, url):
        """
        Open a Firefox browser and create a log
        :param url: String. Url to open
        """
        self.createLog()
        self.log.info(MsgBrowser.MSG_OPEN_FIREFOX)
        self.driver = webdriver.Firefox()
        self.maximize_screen()
        self.set_url(url)

    def openIE(self, url):
        """
        Open a IE browser and create a log
        :param url: String. Url to open
        """
        self.createLog()
        self.log.info(MsgBrowser.MSG_OPEN_IE)
        self.driver = webdriver.Ie()
        self.maximize_screen()
        self.set_url(url)

    def openFirefox_w_prop(self, url):
        """
        Open a Firefox browser with properties, and create a log
        :param url: String. Url to open
        """
        self.createLog()
        self.log.info(MsgBrowser.MSG_OPEN_FIREFOX)
        opts = FirefoxOptions()
        opts.set_preference(SAFEBROWSING, True)
        opts.set_preference(AUTOLOGIN, True)
        opts.set_preference(N_TRUSTED_URIS, DOMAIN)
        opts.set_preference(AUTOMATIC_NTLM, DOMAIN)
        opts.set_preference(N_DELEGATION, DOMAIN)
        myProxy = PROXY
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myProxy,
            'ftpProxy': myProxy,
            'sslProxy': myProxy,
            'noProxy': ''}
        )
        self.driver = webdriver.Firefox(
            firefox_binary=BINARY,
            # firefox_profile = self.keys["TestSIS"],
            firefox_options=opts, proxy=proxy
        )
        self.maximize_screen()
        self.set_url(url)
        return self.driver

    def openChrome_w_prop(self, url):
        """
        Open a Chrome browser with properties, and create a log
        :param url: String. Url to open
        """
        self.createLog()
        try:
            self.log.info(MsgBrowser.MSG_OPEN_CHROME)
            options = webdriver.ChromeOptions()
            options.add_argument(IGNORE_CERTIFICATE)
            self.driver = webdriver.Chrome(options=options)
            self.maximize_screen()
            self.set_url(url)
            return self.driver
        except Exception as e:
            self.fail_test(e)
        
    def openChrome_with_experimental_options(self, url):
        """
        Open a Chrome browser and create a log
        Avoid download pop up
        :param url: String. Url to open
        """
        #self.createLog()
        working_directory = os.getcwd()
        try:              
            self.log.info(MsgBrowser.MSG_OPEN_CHROME)
            options = webdriver.ChromeOptions()
            options.add_argument('--kiosk-printing')
            options.add_argument('--ignore-certificate-errors')
            options.add_experimental_option("prefs", {
                "download.default_directory": working_directory +"\\files",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False})
            self.driver = webdriver.Chrome(options=options)
            self.maximize_screen()
            self.set_url(url)
        except Exception as e:
            self.fail_test(e)
            raise e

    def mobileEmulation(self, url, device='iPhone X'):
        """
        Emulate a mobile device in chrome
        :param url: String. URL to test
        :param device: String. Name of device to use. The names of devices
                       are in Chrome Toggle device toolbar. Default value is
                       iPhone X.
        """
        self.createLog()
        mobile_emulation = dict(deviceName=device)
        self.log.info(MsgBrowser.MSG_MOBILE.format(device))
        self.mobile(url, mobile_emulation)

    def mobileEmulationBySize(self, url, width=375, height=812, pixel_ratio=3):
        """
        Emulate a mobile device by size in Chrome
        :param url: String. URL to test
        :param width: Integer. Set the css width value.
        :param height: Integer. Set the css height value.
        :param pixel_ratio: float. Set the pixel_ratio.
            Default value is iPhone X size.
            For more size, visit https://www.mydevice.io/
        """
        self.createLog()
        metric = dict(width=width, height=height, pixel_ratio=pixel_ratio)
        mobile_emulation = dict(deviceMetrics=metric)
        self.log.info(MsgBrowser.MSG_MOBILE_SIZE.format(width, height,
                                                        pixel_ratio))
        self.mobile(url, mobile_emulation)

    def mobile(self, url, mobile_emulation):
        """ Method to emulate a device interface """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation",
                                               mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options = chrome_options)
        self.set_windows_size('375','812')
        self.driver.get(url)

    def openBrowser(self, naveg, url):
        """
        Open the browser
        :param naveg: String. Name of browser
        :param url: String. Url to open
        """
        if naveg.lower() == CHROME:
            self.openChrome(url)
        elif naveg.lower() == FIREFOX:
            self.openFirefox(url)
        elif naveg.lower() == FIREFOX_P:
            self.openFirefox_w_prop(url)
        elif naveg.lower() == CHROME_EO:
            self.openChrome_with_experimental_options(url)
        if naveg.lower() == CHROME_P:
            self.openChrome_w_prop(url)
        

    def close_browser(self):
        """ Close the browser """
        self.driver.quit()
        self.log.info(MsgBrowser.MSG_CLOSE_BROWSER)      

    def get_tabs(self):
        """ Method to obtain all of current tabs in the browser """
        return self.driver.window_handles

    def new_tab(self, url='about:blank'):
        """ Method to create a new tab in the browser """
        self.log.info(MsgBrowser.MSG_NEW_TAB.format(url))
        self.create_tab_js(url)
        self.change_tab(len(self.get_tabs())-1)

    def change_tab(self, position):
        """ Method to change the active tab """
        tabs = self.get_tabs()
        try:
            tab = tabs[position]
        except IndexError:
            self.log.error(MsgBrowser.MSG_CHANGE_TAB_ERROR.format(position))
            return False
        self.driver.switch_to.window(tab)
        self.log.info(MsgBrowser.MSG_CHANGE_TAB.format(position))

    def close_tab(self):
        """ Method to close he active tab """
        self.driver.close()
        self.log.info(MsgBrowser.MSG_CLOSE_TAB)
        try:
            self.change_tab(0)
        except WebDriverException:
            self.log.info(MsgBrowser.MSG_CLOSE_BROWSER)

    def back(self):
        """ Return to a previous page """
        self.driver.back()
        self.log.info(MsgBrowser.MSG_BACK_PAGE)

    def forward(self):
        """ Forward to a next page """
        self.driver.forward()
        self.log.info(MsgBrowser.MSG_FORWARD_PAGE)

    def maximize_screen(self):
        """ Method to maximize the screen of browser """
        self.driver.maximize_window()
        #self.log.info(MsgBrowser.MSG_MAXIMIZE) 

    def get_windows_size(self):
        """ Method to obtain window size """
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        self.log.info(MsgBrowser.MSG_WINDOW_SIZE.format(width, height)) 
        return width, height

    def set_windows_size(self, width, height):
        """ Method to set window size """
        self.driver.set_window_size(width, height)
        self.log.info(MsgBrowser.MSG_SET_WINDOW_SIZE.format(width, height))

    def set_url(self, url):
        """ Method to set url """
        self.driver.get(url)
        #self.log.info(MsgBrowser.MSG_URL.format(url))

    def get_url(self):
        """ Method to obtain current url """
        url = self.driver.current_url
        self.log.info(MsgBrowser.MSG_CURRENT_URL.format(url))
        return url

    def refresh_page(self):
        """ Method to refresh current page """
        self.driver.refresh()
        self.log.info(MsgBrowser.MSG_REFRESH)

    def get_html(self):
        """ Method to obtain html from the page """
        xpath = '//*'
        source = self.get_attribute(xpath, 'outerHTML')
        return source

    def print_page(self):
        pass
