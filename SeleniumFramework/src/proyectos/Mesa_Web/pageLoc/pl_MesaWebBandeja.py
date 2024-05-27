'''
Created on 1 jun. 2022

@author: GON13535
'''
# -*- coding: utf-8 -*-
class pl_MesaWebBandeja():
    
    menu_bandeja = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/ul[1]/li[1]/a[1]"
    menu_ordenes = "//span[@class='ui-button-text'][contains(.,'Ordenes')]"
    menu_operaciones = "//span[@class='ui-button-text'][contains(.,'Operaciones')]"
    menu_FCI = "//span[@class='ui-button-text'][contains(.,'FCI')]"
    menu_bajas = "//span[@class='ui-button-text'][contains(.,'Bajas')]"
    #following = "//h2[contains(.,'Ingresos de caja')]/following-sibling::div[1]//table[contains(@class,'mat-table')]"
    
    registro_de_orden = "//tbody[@role='alert'][contains(.,'{}')]"
    
    acciones_detalle_orden = "/html[1]/body[1]/div[1]/div[2]/form[1]/span[3]/div[1]/table[1]/tbody[1]/tr[1]/td[16]/span[1]/a[1]/i[1]"