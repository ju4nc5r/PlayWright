# -*- coding: utf-8 -*-
import time, os, glob
from os.path import join
from SeleniumFramework.src.proyectos.Caja_Homo.settings import pathTickets, dirExtArch
from selenium.webdriver.common.keys import Keys
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







    def verificarSaldoDeCheques(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            self.saldoCheques = self.ticket[3819:3829].strip()
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
            self.NumeroTrans = self.ticket[189:202].strip()
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
            self.NumeroTrans = self.ticket[108:115].strip()
            print ("Numero de Trassaccion: ",self.NumeroTrans)
            self.cerrarArchTicket()


    def verificar_nro_transaccion_cheques(self):
        to = 30
        accion = 'Validar ticket'
        msgOk = accion
        msgFail = 'No se pudo '+ msgOk.lower()
        with self.step(accion):
            self.abrirArchTicket2()
            time.sleep(2)
            self.NumeroTrans = self.ticket[100:202].strip()
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

