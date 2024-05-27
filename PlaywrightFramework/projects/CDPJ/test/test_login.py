import pytest
import allure
from PlaywrightFramework.config.utils import config
from PlaywrightFramework.projects.HBPF import limpiar_result
import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


@allure.epic('Login')
@allure.feature('Login Selecta')
@allure.story('Camino exitoso de login con validación de textos y objetos')
@allure.issue('https://linkaticketabierto.com')
@allure.testcase('https://linkatestdezephyr.com')

def test_login(playwright: Playwright) -> None:
    """
    Passed Scenario
    """

    limpiar_result(project='HBPF', on=True)
    with allure.step("Ingreso a la home"):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="../HBPF/files/videos/login/") #record_video_dir="videos/"
        page = context.new_page()
        page.goto("https://internethomo.sis.ad.bia.itau/internet/sso")

    with allure.step("Ingreso de usuario"):
        page.get_by_placeholder("usuario").click()
        page.get_by_placeholder("usuario").fill("Usuarioautouno1")

    with allure.step("Ingreso de contraseña"):
        page.get_by_placeholder("usuario").press("Tab")
        page.get_by_placeholder("contraseña").fill("Bb112233")

    with allure.step("Click en ingresar"):
        page.get_by_role("button", name="Ingresar").click()
        page.screenshot(path="../HBPF/files/captures/ingreso1.png")
        screen.attach_element('captures/ingreso1.png', 'clickIngresar')
        time.sleep(20)

    with allure.step("Se verifican elementos"):
        page.get_by_text("UNO UNO AUTOMATIZACIONÚltimo").click()
        page.get_by_role("link", name="Cerrar Sesión").click()

    # ---------------------
    context.close()
    browser.close()
