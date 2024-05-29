# -*- coding: utf-8 -*-
class plAdminTerminales():
    tbl_terminales = "//table[contains(@class,'mat-table')]//tbody"

    txt_titulo = "//h1[contains(.,'{}')]"
    
    mnuBtnTerminales = "//span[@class='mat-button-wrapper'][contains(.,'Terminales')]/.."