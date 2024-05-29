from PlaywrightFramework.config.utils import config

def limpiar_result(project, on):
    confg = config()
    confg.vaciar_carpeta_allure(project=project, on=on)
