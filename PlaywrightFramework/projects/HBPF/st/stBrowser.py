import time
import os
from playwright.sync_api import Playwright, sync_playwright, expect, Page
from PlaywrightFramework.allure_driver import allure_driver
import allure

class stBrowser():

    URL = "https://internethomo.sis.ad.bia.itau/internet/sso"
    allureDriver = allure_driver()

    def __init__(self, nav_off=True, rec='') -> None:
        # Inicializar Playwright
        playwright = sync_playwright().start()
        self.playwright = playwright

        # Inicializar Browser
        browser = self.playwright.chromium.launch(headless=nav_off)
        self.browser = browser

        # Inicializar context
        if rec == '':
            context = self.browser.new_context(ignore_https_errors=True)

        else:
            self.path_image = f'../{rec}/captures'
            self.path_video = f'../{rec}/videos'
            context = self.browser.new_context(record_video_dir=self.path_video, ignore_https_errors=True)
        '''
        elif 'test' in os.getcwd():
            print('Ruta actual:', os.getcwd())
            rec_new = f'{os.path.dirname(os.getcwd())}/{rec}'
            print(f'Ruta de guardado:', rec_new)
            self.path_image = f'{rec_new}/captures/'
            self.path_video = f'{rec_new}/videos/'
            context = self.browser.new_context(record_video_dir=self.path_video)
        '''
        self.context = context

        # Inicializar Page
        page = self.context.new_page()
        self.page = page

        #Inicializar Allure
        #self.alluredriver = allure.allure_driver

    def openHB(self) -> None:
        accion = "Abrir browser"
        with allure.step(accion):
            self.page.goto(url=self.URL)
            self.screen2allure(accion)

    def closeHB(self) -> None:
        accion = "Cerrar browser"
        with allure.step(accion):
            self.context.close()
            self.browser.close()
            self.playwright.stop()
            self.video2allure()

    def screen2allure(self, accion):
        name = accion.replace(" ", "")
        folder = self.path_image
        dir_save = f'{folder}/{name}.png'
        self.page.screenshot(path=dir_save)
        self.allureDriver.attach_element(dir_save, accion)

    def video2allure(self):
        folder = self.path_video
        if os.path.isdir(folder):
            files = os.listdir(folder)
            if files:
                file = files[0]
                ruta_file = os.path.join(folder, file)
                self.allureDriver.attach_video(ruta_file, "Video")
        else:
            print(f'No existen videos en la carpeta {folder}')

    def login(self):
        self.completarUsuario()
        self.completarPassword()
        self.seleccionarIngresar()

    def completarUsuario(self):
        accion = "Completar Usuario"
        with allure.step(accion):
            self.page.get_by_placeholder("usuario").click()
            self.page.get_by_placeholder("usuario").fill("Usuarioautouno1")
            self.screen2allure(accion)

    def completarPassword(self):
        accion = "Completar contraseña"
        with allure.step(accion):
            self.page.get_by_placeholder("usuario").press("Tab")
            self.page.get_by_placeholder("contraseña").fill("Bb112233")
            self.screen2allure(accion)

    def seleccionarIngresar(self):
        accion = "Seleccionar Ingresar"
        with allure.step(accion):
            self.page.get_by_role("button", name="Ingresar").click()
            time.sleep(10)
            self.screen2allure(accion)

    def deslogueo(self):
        accion = "Cerrar sesión"
        with allure.step(accion):
            self.page.get_by_role("link", name="UNO").click()
            self.page.locator("xpath=//a[@id='Salir']").click(timeout=60000)
            self.screen2allure(accion)

    def selecccionarPerfil(self):
        accion = "Seleccionar perfil"
        with allure.step(accion):
            self.page.get_by_role("link", name="UNO").click()
            self.screen2allure(accion)

    def seleccionarDatosPersonales(self):
        accion = "Seleccionar datos personales"
        with allure.step(accion):
            self.page.get_by_role("link", name="Datos personales").click()
            self.screen2allure(accion)

    def validarCamposDatosPersonales(self):
        accion = "Validar campos de datos personales"
        with allure.step(accion):
            expect(self.page.get_by_text("Celular / e-mail")).to_be_visible()
            expect(self.page.get_by_text("Domicilio particular")).to_be_visible()
            self.page.locator("#tableAlign3430").click()
            expect(self.page.get_by_text("Domicilio laboral")).to_be_visible()
            self.screen2allure(accion)

    def seleccionarMenuProductos(self):
        accion = "Seleccionar productos"
        with allure.step(accion):
            self.page.get_by_role("link", name="Productos").click()
            self.screen2allure(accion)

    def consultarCBUyAlias(self):
        accion = "Consultar de CBU y alias"
        with allure.step(accion):
            self.page.get_by_role("link", name="Consulta de CBU y alias").click()
            time.sleep(15)
            self.screen2allure(accion)

    def seleccionarConsultaMovimientos(self):
        accion = "Seleccionar Consulta de Movimientos"
        with allure.step(accion):
            self.page.get_by_role("link", name="Consulta de Movimientos").click()
            time.sleep(15)
            self.screen2allure(accion)

    def validarCamposMovimientos(self):
        accion = "Validar campos  Consulta Movimientos"
        with allure.step(accion):
            expect(self.page.get_by_role("button", name="Consulta de Movimientos")).to_be_visible()
            expect(self.page.get_by_role("button", name="Movimientos futuros")).to_be_visible()
            expect(self.page.get_by_text("consulta de CBU y alias", exact=True)).to_be_visible()
            expect(self.page.get_by_text("resumen digital", exact=True)).to_be_visible()
            expect(self.page.get_by_role("cell", name="Caja de ahorro pesos", exact=True)).to_be_visible()
            self.screen2allure(accion)

    def seleccionarDetalleTarjDeb(self):
        accion = "Seleccionar Detalle Tarjeta de Debito"
        with allure.step(accion):
            self.page.get_by_role("link", name="Detalle tarjeta de débito").click()
            expect(self.page.locator("#constantLabel0")).to_contain_text("Detalle de tarjeta de débito")
            self.screen2allure(accion)

    def validarCamposDetalleDeb(self):
        accion = "Validar campos del detalle de debito"
        with allure.step(accion):
            expect(self.page.locator("#label_selectField03")).to_contain_text("Tarjeta")
            expect(self.page.locator("#label_textField055")).to_contain_text("Nombre y apellido")
            expect(self.page.locator("#label_floatField0")).to_contain_text(
                "Límite diario de extracción en cajeros Macro BMA")
            expect(self.page.locator("#label_optionField0")).to_contain_text("Seguro contra robo en cajero")
            expect(self.page.locator("#richText1")).to_contain_text("Bloqueo/Reposición")
            expect(self.page.locator("#richText2")).to_contain_text("Cuenta para operar en el exterior")
            expect(self.page.locator("#richText069")).to_contain_text("Blanqueo de PIN")
            self.screen2allure(accion)

    def validacionTextosDetalle(self):
        accion = "Validación de textos del detalle de debito"
        with allure.step(accion):
            expect(self.page.locator("#richText2")).to_contain_text(
                "Si estás en el exterior y tenés consumos en moneda extranjera, podés elegir desde qué cuenta querés "
                "que se debiten")
            expect(self.page.locator("#richText1")).to_contain_text(
                "Si necesitás una nueva tarjeta de débito, podés pedirla desde acá")
            expect(self.page.locator("#richText069")).to_contain_text(
                "Si necesitas blanquaear la clave de cajero automático, podes pedirla desde acá")











