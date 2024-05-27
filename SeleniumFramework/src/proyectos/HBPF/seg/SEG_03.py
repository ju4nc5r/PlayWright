# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, string
import time
import sys
import allure
from SeleniumFramework.image import image


@allure.feature(u'Login')
@allure.story(u'Realizar login')
@allure.testcase(u"SEG-01")
@allure.title(u'Login')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
    """
)
# Inicializar el navegador
class Login():
    cont = 0
    image = image()

    while (cont < 3):

        url = "https://internethomo.sis.ad.bia.itau/internet/sso"

        # Abrir la pagina web
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        image.capture_image("Se abrio el navegador")

        # Encontrar el campo de nombre de usuario y completarlo
        username_field = driver.find_element_by_id("login_textField0")
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        username_field.send_keys(username)

        # Encontrar el campo de contrasena y completarlo
        password_field = driver.find_element_by_id('login_textField1')
        claveRandom = random.randint(1111111111, 9999999999)
        password_field.send_keys(claveRandom)

        # Encontrar el boton de inicio de sesi�n y hacer clic en el
        login_button = driver.find_element_by_xpath("//p[contains(text(),'Ingresar')]")
        login_button.click()
        time.sleep(3)

        # Esperar a que la pagina se cargue completamente
        driver.implicitly_wait(10)  # Esperar un maximo de 10 segundos para que la pagina se cargue completamente

        # Cerrar el navegador
        driver.quit()

        cont = cont + 1