import os
import sys
import pytest
import allure
import time
from playwright.sync_api import Playwright, sync_playwright, expect

class config():

    def vaciar_carpeta_allure(self, on: bool):

        if (on != True):
            pass

        else:
            dir_project = f''
            folder = f'{dir_project}/allure-results'

            # Verificar si la carpeta existe
            if os.path.exists(folder):
                # Obtener la lista de archivos en la carpeta
                archivos = os.listdir(folder)
                # Verificar si la carpeta no está vacía
                if archivos:
                    # Vaciar la carpeta eliminando todos los archivos
                    for archivo in archivos:
                        ruta_archivo = os.path.join(folder, archivo)
                        os.remove(ruta_archivo)
                    print("La carpeta se ha vaciado exitosamente.")
                else:
                    print("La carpeta ya está vacía.")
            else:
                print("La carpeta especificada no existe.")
