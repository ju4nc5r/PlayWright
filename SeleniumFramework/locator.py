# -*- coding: utf-8 -*-s
'''
Created on 23 oct. 2023

@author: FO433151
'''
import time
import pyautogui
from PIL import Image


class Locator():

    def locate_buton_from_image(self,img):
        """lo busca el boton que se encuentra en la imagen 
        que se le pasa como parametro y le da click"""
        x, y = pyautogui.locateCenterOnScreen(img)
        time.sleep(2) 
        pyautogui.click(x,y)

    def buscar_ventana_en_imagen(self,ventana_imagen, pantalla_imagen):
        """ Busca la imagen de la ventana que se le da como parametro """
        ventana = pyautogui.locate(ventana_imagen, pantalla_imagen, grayscale=True)
        if ventana is not None:
            return True
        else:
            return False

    def detect_windows(self,ruta_ventana):
        """Compara si la ventana dada como parametro se encuentra
         en la captura de pantalla de el metedod self.captureImage """
        self.captureImage()
        captura_pantalla = self.img 
        time.sleep(2)
        ventana_imagen = Image.open(ruta_ventana)
        pantalla_imagen = captura_pantalla
        time.sleep(2)
        if self.buscar_ventana_en_imagen(ventana_imagen, pantalla_imagen):
            self.log.info("La ventana esta precente en la captura de pantalla.")
        else:
            self.log.info("La ventana no esta presente en la captura de pantalla.")


# # Captura de pantalla
# captura_pantalla = pyautogui.screenshot()
#  
# # Ruta de la imagen de la ventana que buscas
# ruta_ventana = 'ruta/a/la/imagen/ventana.png'
#  
# # Carga de im�genes
# ventana_imagen = Image.open(ruta_ventana)
# pantalla_imagen = captura_pantalla
#  
# # Comprobaci�n
# if buscar_ventana_en_imagen(ventana_imagen, pantalla_imagen):
#     print("La ventana esta precente en la captura de pantalla.")
# else:
#     print("La ventana no esta presente en la captura de pantalla.")
    
    