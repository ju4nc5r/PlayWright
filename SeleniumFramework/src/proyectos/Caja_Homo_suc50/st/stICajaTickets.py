# -*- coding: utf-8 -*-
import time, os, glob
from os.path import join
from SeleniumFramework.src.proyectos.Caja_Homo_suc50.settings import pathTickets, dirExtArch
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pytest

    
class stICajaTickets():

    def visualizarTicket2(self,pagTkt=1):
        to = 30
        accion = u'Validar que se imprime el ticket'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()

        with self.step(accion):
            self.abrirArchTicket2(pagTkt)
            self.cerrarArchTicket()



    def visualizarTicket(self,pagTkt=1):
        to = 30
        accion = u'Validar que se imprime el ticket'
        msgOk = accion
        msgFail = u'No se pudo '+ msgOk.lower()

        with self.step(accion):
            self.abrirArchTicket(pagTkt)
            self.cerrarArchTicket()

    def verificar_Nro_servicios(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.NumeroTrans = self.ticket[224:227].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()

    def verificar_Nro_servicios_2(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.NumeroTrans = self.ticket[218:221].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()


    def verificar_numero_de_transaccion_cheques(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            self.NumeroTrans = self.ticket[0:2].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()
            

    def verificar_autorizante(self,autorizante):
        to = 30
        accion = 'Valida que en el ticket muestre al Autorizante " TX. AUTORIZADA POR UIC10023'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            if autorizante in self.ticket:
                print ("Autorizante:",autorizante)
            else:
                pytest.fail(msgFail)
            self.cerrarArchTicket()
                        
    def obtener_nro_transaccion_pf(self):
        to = 30
        accion = 'Valida que en el ticket muestre al Autorizante " TX. AUTORIZADA POR UIC10023'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            self.nro = self.ticket[199:204].strip()
            print ("numero: ",self.nro)
            self.cerrarArchTicket()
    
            
                        
            
    def verificar_numero_de_transaccion_cheques_2(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            self.NumeroTrans = self.ticket[0:5].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()

    def verificar_numero_de_transaccion(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.NumeroTrans = self.ticket[114:118].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()


    def verificarSaldoDeCheques(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.saldoCheques = self.ticket[3824:3834].strip()
            print ("Saldo de Deposito de Cheque: ",self.saldoCheques)
            self.cerrarArchTicket()
            
    def verificarNumeroDeTransaccion(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.NumeroTrans = self.ticket[210:215].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()
            
    def verificarNumeroDeTransaccion_2(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.NumeroTrans = self.ticket[213:219].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()

    def verificar_Numero_de_transaccion_terceros(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            for indice in range (len(self.ticket)):
                caracter = self.ticket[indice]
                print("En el indice {} tenemos a '{}'".format(indice, caracter))
            self.NumeroTrans = self.ticket[212:216].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()


    def verificarNumeroDeTransaccionCobrosDeMulta(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            self.NumeroTrans = self.ticket[204:218].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()

#     def validarTicketIngresoNumerarioPesos(self):
#         to = 30
#         accion = 'Validar ticket'
#         msgOk = accion
#         msgFail = 'No se pudo '+ msgOk.lower()
#  
#         with self.step(accion):
#             self.abrirArchTicket()
#             time.sleep(6)
#             tktUsuario = self.ticket[67:75]
#             print ("usuario ticket " + tktUsuario)
#             print ("Usuario " + self.user)
#             self.log.info("Usuario Ticket "+  tktUsuario)
#             self.log.info("Usuario "+ self.user)
#             
#             if tktUsuario == self.user:
#                 print ("Usuario OK")
#             else:
#                 pytest.fail("No se pudo validar campo usuario del ticket")
#             self.cerrarArchTicket()
#             
#         
#     def validarTicketIngresoNumerarioDolares(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[68:76]
#         print ("usuario ticket " + tktUsuario)
#         print ("Usuario " + self.user)
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()
# 
# 
#     def validarTicketIngresoNumerarioEuros(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[68:76]
#         print ("usuario ticket " + tktUsuario)
#         print ("Usuario " + self.user)
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()
#         
#     def validarTicketIngresoNumerarioReales(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[67:75]
#         print ("usuario ticket " + tktUsuario)
#         print ("Usuario " + self.user)
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()
#         
# 
#     def validarTicketEgresoNumerarioPesos(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[66:74]
#         print ("usuario ticket " + tktUsuario)
#         print ("Usuario " + self.user)
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
# 
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()
#         
#         
#     def validarTicketEgresoNumerarioDolares(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[68:76]
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
# 
#         print ("usuario ticket " + tktUsuario)
#         print ("Usuario " + self.user)
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()
# 
# 
#     def validarTicketEgresoNumerarioEuros(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[68:76]
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
#         print ("usuario ticket " + tktUsuario)
#         print ("Usuario " + self.user)
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()
#         
#     def validarTicketEgresoNumerarioReales(self):
#         self.abrirArchTicket()
#         tktUsuario = self.ticket[67:75]
#         print ("usuario ticket " + tktUsuario)
#         self.log.info("Usuario Ticket "+  tktUsuario)
#         self.log.info("Usuario "+ self.user)
#         print ("Usuario " + self.user)
#         if tktUsuario == self.user:
#             print ("Usuario OK")
#         else:
#             pytest.fail("No se pudo validar campo usuario del ticket")
#         self.cerrarArchTicket()


        
    def abrirArchTicket(self, pagTkt=1):
        
        self.wait(10) #  se espera por apertura dialogo de impresión que aggregaron
        fechaHoy = (time.strftime("%Y%m%d"))
        list_of_files = glob.glob(pathTickets+fechaHoy+dirExtArch) 
        latest_file = max(list_of_files, key=os.path.getctime)
        nameFileTicket = latest_file[-20:]
        dirFileTicket = latest_file[:-20]        
        print (nameFileTicket)
        print (dirFileTicket)
        self.log.info("PATH DEL ARCHIVO DEL TICKET")
        self.log.info(dirFileTicket)
        self.log.info("NOMBRE ARCHIVO DEL TICKET")
        self.log.info(nameFileTicket)
        self.archTicket = open(join(dirFileTicket, nameFileTicket), 'r')
        self.ticket = self.archTicket.read()
        self.log.info("CONTENIDO DEL ARCHIVO DEL TICKET")
        self.log.info(self.ticket)
        print (self.ticket)

#       Se abre con el archivo del ticket en el browser en una nueva solapa y se captura image 
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(dirFileTicket+nameFileTicket)
        self.capture_image(dirFileTicket+nameFileTicket)
        #     Se hace avance de pagina y captura segun tenga dos o tres paginas de largo
        if pagTkt >= 2:      
            self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            self.capture_image(dirFileTicket+nameFileTicket)
        if pagTkt ==3:        
            self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            self.capture_image(dirFileTicket+nameFileTicket)
#     Se vuelve a la solapa principal
        self.driver.switch_to.window(self.driver.window_handles[0])


    def abrirArchTicket2(self, pagTkt=1):      
        self.wait(2) #  se espera por apertura dialogo de impresión que aggregaron
        fechaHoy = (time.strftime("%Y%m%d"))
        list_of_files = glob.glob(pathTickets+fechaHoy+dirExtArch) 
        latest_file = max(list_of_files, key=os.path.getctime)
        nameFileTicket = latest_file[-20:]
        dirFileTicket = latest_file[:-20]        
        print (nameFileTicket)
        print (dirFileTicket)
        self.log.info("PATH DEL ARCHIVO DEL TICKET")
        self.log.info(dirFileTicket)
        self.log.info("NOMBRE ARCHIVO DEL TICKET")
        self.log.info(nameFileTicket)
        self.archTicket = open(join(dirFileTicket, nameFileTicket), 'r')
        self.ticket = self.archTicket.read()
        self.log.info("CONTENIDO DEL ARCHIVO DEL TICKET")
        self.log.info(self.ticket)
        print (self.ticket)

#       Se abre con el archivo del ticket en el browser en una nueva solapa y se captura image 
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(dirFileTicket+nameFileTicket)
        self.capture_image(dirFileTicket+nameFileTicket)
        #     Se hace avance de pagina y captura segun tenga dos o tres paginas de largo
        if pagTkt >= 2:      
            self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            self.capture_image(dirFileTicket+nameFileTicket)
        if pagTkt ==3:        
            self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            self.capture_image(dirFileTicket+nameFileTicket)
        self.driver.close()
#     Se vuelve a la solapa principal
        self.driver.switch_to.window(self.driver.window_handles[0])


           
    def cerrarArchTicket(self):
        self.archTicket.close()

