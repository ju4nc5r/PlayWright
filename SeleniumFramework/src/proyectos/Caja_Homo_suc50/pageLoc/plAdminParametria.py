# -*- coding: utf-8 -*-
class plAdminParametria():
    tbl_parametria = "//table[contains(@class,'mat-table')]//tbody"
    
    txt_titulo = "//h1[contains(.,'{}')]"
    
    btn_editarSucursales = "//span[@class='mat-button-wrapper'][contains(.,'Editar sucursales')]"

    slc_tipoLimite = "//mat-select[@formcontrolname='idTipoLimite']"

    btn_tipoLimite = "//mat-option[contains(.,'')][{}]"

    ipt_limPesos = "//input[contains(@formcontrolname,'pesos')]"
    ipt_limDolar = "//input[contains(@formcontrolname,'dolares')]"
    ipt_limEuro = "//input[contains(@formcontrolname,'euros')]"
    ipt_limReal  = "//input[contains(@formcontrolname,'reales')]"

    btn_guardarLim = "//button[contains(@class,'btnYes mat-button')]"

    btn_aceptarCambios = "//button[contains(@class,'btnYes')]"

#     txt_msjEsperado = "//div[contains(@class,'alertMessage')]"
    txt_msjEsperado = "//div[contains(@class,'container-fluid')]"
    btn_cerrarMjeExito = "//button[contains(.,'X')]" 


    col_esperada = "//tr[{}]//td[contains(.,'')][2]"

    col_editar = "//preceding-sibling::td[1]"
    col_pesos = "//following-sibling::td[2]"
    col_dolar = "//following-sibling::td[3]" 
    col_euro = "//following-sibling::td[4]"
    col_real = "//following-sibling::td[5]"

    # items por pagina

    slc_items = "//mat-select[contains(@class,'mat-select ng-tns')]"

    btn_items_10 = "//mat-option[contains(@class,'mat-option') and contains(.,'10')]"