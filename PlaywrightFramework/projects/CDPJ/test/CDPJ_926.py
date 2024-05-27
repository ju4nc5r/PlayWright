from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_NHBE(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mcyfronthomo.sis.ad.bia.itau/login")
    page.get_by_label("Usuario").click()
    page.locator("#login-page__form div").filter(has_text="Contraseña").nth(4).click()
    page.get_by_label("Contraseña").fill("Zz112233")
    page.locator("#login-page__form div").filter(has_text="Contraseña").nth(4).click()
    page.locator(".mat-form-field-infix").first.click()
    page.get_by_label("Usuario").fill("automationfirmatotal")
    page.get_by_label("Usuario").click()
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").fill("Zz112233")
    page.get_by_role("button", name="Ingresar").click()
    page.wait_for_timeout(3000)
    page.get_by_role("link", name="activa menu icon Echeq").click()
    page.wait_for_timeout(3000)
    page.get_by_role("link", name="activa menu icon Mis Cuentas").click()
    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()
