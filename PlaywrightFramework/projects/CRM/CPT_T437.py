from playwright.sync_api import Playwright, sync_playwright, expect
import re

def test_CPT_T437(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://sapfiorihw11.sis.ad.bia.itau:8021/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html#Shell-home")
    page.get_by_role("button", name="Reporte de solicitudes").click()
    page.locator("[id=\"__xmlview0--processTypeSelect-vhi\"]").click()
    page.locator("[id=\"__item58-__xmlview0--tree-0-selectMulti\"]").click()
 #   page.get_by_role("treeitem", name=" Aumento de Línea").click()
 #   page.get_by_text("Aumento de Línea", exact=True).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("combobox", name="Fecha de Creación").click()
    page.get_by_role("combobox", name="Fecha de Creación").fill("01012022")
    page.get_by_role("combobox", name="Fecha de Vencimiento").click()
    page.get_by_role("combobox", name="Fecha de Vencimiento").fill("04012022")
    page.get_by_text("BuscarIr").click()
    expect(page.locator("div").filter(has_text=re.compile(r"^0000023344$"))).to_be_visible(timeout=10000)
    page.locator("div").filter(has_text=re.compile(r"^0000023344$")).click()
    page.get_by_role("grid", name="Solicitudes").get_by_text("Id de solicitud").click()
    page.get_by_role("menuitem", name="Clasificar en orden ascendente").click()
    page.get_by_role("columnheader", name="Id BPM").get_by_text("Id BPM").click()
    page.get_by_role("grid", name="Solicitudes").get_by_text("Tipo de solicitud").click()
    page.get_by_role("grid", name="Solicitudes").get_by_text("Estado de solicitud").click()
    page.get_by_role("grid", name="Solicitudes").get_by_text("Fecha de Creación").click()
    page.get_by_text("Envio a Evaluación").click()
    page.get_by_role("grid", name="Solicitudes").get_by_text("Fecha de Vencimiento").click()
    page.get_by_role("columnheader", name="Columna 7 de 56 Fecha de Vencimiento").click()
    page.locator("[id=\"__xmlview0--dynamicPageId-contentFitContainer\"]").click()
    page.get_by_role("button", name="Exportar a Excel").click()
    page.get_by_text("Exportando archivo").click()
    page.locator("[id=\"__dialog0-title\"]").click()
    page.locator("[id=\"__indicator0-remainingBar\"]").click()
    page.get_by_role("button", name="Cancelar").click()
    page.on("download", lambda download: print(download.path()))
    #expect(page.get_by_role("button", name="Cancelar")).not_be_visible(timeout=10000)
    page1 = context.new_page()
    page1.goto("file:///C:/Users/jv432568/Downloads/")

#   logger.isEnabled(name, severity)
#    absolute_url = f"file:///C:/Users/jv432568/Downloads/"

#    # Download the file using requests
#    file = requests.get(absolute_url)
#    with open('install.txt', 'wb') as f:
#        f.write(file.content)


    # ---------------------
    context.close()
    browser.close()

