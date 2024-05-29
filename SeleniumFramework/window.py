# -*- coding: utf-8 -*-s
'''
Created on 23 oct. 2023

@author: FO433151
'''
import pygetwindow
import pyautogui


class Window():
    
    def check_if_application_running(self, application_name):
        '''
        Verifica si una aplicacicion escritorio dada esta en ejecucion.
        '''
        all_windows = pygetwindow.getWindowsWithTitle(application_name)
        if len(all_windows) > 0:
            return True
        return False  
    
    
    def close_application(self,application_name):
        '''
        Cierra una aplicacion de escritorio dada.
        '''
        try:
            app_window = pygetwindow.getWindowsWithTitle(application_name)[0]
            app_window.close()
            return True
        except IndexError:
            return False
    
    
    def salir_de_app(self,application_name):
        if self.close_application(application_name):
            self.log.info("Se ha cerrado la aplicacion: {}".format(application_name))
        else:
            self.log.info("No se pudo encontrar la aplicacion: {}".format(application_name))

    
    def focus_application(self,application_name):
        '''
        Hace foco en una aplicacion de escritorio dada
        '''
        try:
            app_window = pygetwindow.getWindowsWithTitle(application_name)[0]
            app_window.activate()
            return True
        except IndexError:
            return False
 
 
    def hacer_focus_app(self,application_name):
        if self.focus_application(application_name):
            self.log.info("se ha hecho foco en la aplicacion:{} ".format(application_name))
        else:
            self.log.info("no se pudo encontrar la aplicacion:{} ".format(application_name))
                        
     
    def wait(self,time):
        self.log.info("se produce una pausa de {}".format(str(time)))
        pyautogui.PAUSE = time


    def sleep(self,time):
        time.sleep(time)
        self.log.info("se produce una pausa de {}".format(str(time)))
    
    

    
    
    
        
    
    
    
    