from playwright.sync_api import Playwright, sync_playwright, expect


def test_CPT_T2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://sapfiorihw11.sis.ad.bia.itau:8021/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html#Shell-home")
    page.locator("xpath=(//div[@class='sapMGTHdrContent OneByOne'][contains(.,'Visi')and contains(.,' 360')])[1]").click()
#    page.get_by_role("button", name="Visión 360°", exact=True).click()
    page.get_by_role("textbox", name="Tipo de Documento").click()
    page.get_by_role("textbox", name="Número de Documento").click()
    page.get_by_role("textbox", name="Número de Raíz").click()
    page.get_by_role("textbox", name="Nombre").click()
    page.get_by_role("textbox", name="Apellido").click()
    page.get_by_role("textbox", name="Número de cliente").click()
    page.get_by_role("textbox", name="Teléfono").click()
    page.get_by_role("textbox", name="E-mail").click()
    page.get_by_role("textbox", name="Red Social", exact=True).click()
    page.get_by_role("textbox", name="ID de Red Social").click()

    # ---------------------
    context.close()
    browser.close()


