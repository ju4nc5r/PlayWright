import requests
from time import strftime
from io import BytesIO
from os.path import join
from PIL import Image
from base64 import b64decode
import pyautogui
from SeleniumFramework.constants.spanish_messages import MsgImage
from SeleniumFramework.constants.constants import PNG_FILE


class image(object):
    def captureImage(self):
        """
        Save a screenshot of browser in the test folder
        :return: String. Path of the screenshot
        """
        hora = strftime("%H%M%S")  # format 24 hours
        nombre_img = PNG_FILE.format(hora)
        img = join(self.path, nombre_img)
        self.driver.get_screenshot_as_file(img)
        return img

    def capture_image(self, description, sleep=1):
        """
        Method to attach a image in allure
        :param description: String. Description of screenshot
        """
        self.wait(sleep)
        IMAGEN = self.captureImage()
        CAPTURA = Image.open(IMAGEN, mode="r")
        ImageProcess = BytesIO()
        CAPTURA.save(ImageProcess, format="PNG")
        ImageProcess = ImageProcess.getvalue()
        self.attach_element(ImageProcess, description)
        self.log.info(MsgImage.MSG_SCREENSHOT.format(description))

    def get_image(self, xpath, filename):
        """
        Method to obtain an image from web, searched by xpath
        :param xpath: String. Xpath of the element
        :param filename: String. Filename of the image
        """
        if self.visibility_element(xpath, 10):
            tag_name = self.get_tag_name(xpath)
            if tag_name == 'img' or tag_name == 'canvas':
                source = self.get_attribute(xpath, 'src')
            else:
                self.log.error(MsgImage.MSG_GET_IMAGE_ERROR.format(xpath))
        else:
            return False

        # If the image is in base 64
        if 'base64' in source:
            base = source.split(',')[1]
            source = b64decode(base)
        else: # if de source is an url
            image = requests.get(source)
            source = image.content
        with open(filename, 'wb') as file:
            file.write(source)
        image = Image.open(filename)
        self.log.info(MsgImage.MSG_GET_IMAGE.format(xpath, filename))
        return image

    def element_screenshoot(self, xpath):
        """
        Method to obtain a screenshot of the searched element
        :param xpath: String. Xpath of the searched element
        :return: Image. Image object of the searched element
        """
#         Esto probar con python3
#         elem = self.search_element_by_xpath(xpath)
#         source = elem.screenshot_as_base64()
#         image = Image.open(BytesIO(b64decode(source)))
#         return image

        # Este metodo no funciona si:
        #        - El elemento se encuentra fuera de los pixeles que puede
        #          mostrar el monitor (si se usa el scroll)
        #        - El elemento es mas grande que los pixeles que puede mostrar
        #          el monitor
        pantalla = self.buffer_screenshoot()
        x, y = self.get_location(xpath)
        height, width = self.get_size(xpath)
        left = x
        top = y
        right = x + width
        bottom = y + height
        box = (left, top, right, bottom)
        im = pantalla.crop(box)
        return im

    def buffer_screenshoot(self):
        """
        Method to create an image element of screenshot. This image is in
        buffer.
        :return: Image. Screenshot
        """
        source = self.driver.get_screenshot_as_base64()
        image = Image.open(BytesIO(b64decode(source)))
        self.log.info(MsgImage.MSG_SCREENSHOT_BUFFER)
        return image

'''
Created on 23 oct. 2023

@author: FO433151
'''
class Img_dsk():
    def captureImage(self):

        """
        Save a screenshot of browser in the test folder
        :return: String. Path of the screenshot
        """
        hora = strftime("%H%M%S")  # format 24 hours
        nombre_img = PNG_FILE.format(hora)
        self.img = join(self.path, nombre_img)
        try:
            pyautogui.screenshot(self.img)
            self.log.info("Se saca captura de pantalla")
            return self.img
        except Exception as E:
            self.log.info(E)

    def capture_image(self, description, sleep=1):
        """
        Method to attach a image in allure
        :param description: String. Description of screenshot
        """
        pyautogui.PAUSE = 2.5
        IMAGEN = self.captureImage()
        CAPTURA = Image.open(IMAGEN, mode="r")
        ImageProcess = BytesIO()
        CAPTURA.save(ImageProcess, format="PNG")
        ImageProcess = ImageProcess.getvalue()
        self.attach_element(ImageProcess, description)
        self.log.info(MsgImage.MSG_SCREENSHOT.format(description))