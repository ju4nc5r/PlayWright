# -*- coding: utf-8 -*-
class plAdminConsulta():
    tbl_operadores = "//table[contains(@class,'mat-table')]//tbody"
    tbl_MovDeCajas = "//table[contains(@class,'mat-table')]//tbody"
    tbl_terminales_regis = "//table[contains(@class,'mat-table')]//tbody"
    btn_buscarMovi = "//div[contains(@class,'col-md-2')]//button[contains(@class,'mat-button')]"
    
    btn_imprimir = "//button[contains(.,'Imprimir')]"
    btn_descargar = "//button[contains(.,'Descargar')]"

    txt_titulo = "//h1[contains(.,'{}')]"
    
    txt_titulo2 = "//h2[contains(.,'{}')]"

    tbl_saldos2 = "(//table[@class='mat-table'])[2]"
    tbl_saldos2_ultLinea = "(//table[@class='mat-table'])[2]"
    
    btn_Imprimir_1 = "(//button[@class='mat-button'][contains(.,'Imprimir')])[1]"
    
    lst_TotSaldosTerminal = "//div[contains(@class,'datagrid')]"
    
    btn_Imprimir_2 = "(//button[@class='mat-button'])[2]"
    
    lst_TotSaldosSucursal = "//div[contains(@class,'datagrid')]"

    slc_TipoMoneda = "//mat-select[contains(@formcontrolname,'moneda')]"

    opt_moneda = "//mat-option[contains(.,'{}')]"

    btn_buscarTotales = "//button[contains(@class,'mat-button') and contains(.,'Buscar')]"

    tbl_ingresos = "//h2[contains(.,'Ingresos de caja')]/following-sibling::div[1]//table[contains(@class,'mat-table')]"

    tbl_egresos = "//h2[contains(.,'Egresos de caja')]/following-sibling::div[1]//table[contains(@class,'mat-table')]"
    
    tbl_liquido = "//h2[contains(.,'Liquido de caja')]/following-sibling::div[1]//table[contains(@class,'mat-table')]"

    tbl_listado = "//table[contains(@class,'mat-table')]"

    lst_TotIngresosCaja = "//h4[contains(.,'Ingreso de Caja')]/following::table[1]"
    lst_TotEgresosCaja = "//h4[contains(.,'Egreso de Caja')]/following::table[1]"
    lst_TotLiquidoCaja = "//h4[contains(.,'Liquido de Caja')]/following::table[1]"

    slc_sucursal = "//mat-select[contains(@formcontrolname,'sucursal')]"

    opt_sucursal = "//mat-option[contains(.,'{}')]"

    slc_condicion = "//mat-select[contains(@formcontrolname,'condicion')]"

    opt_condicion = "//mat-option[contains(.,'{}')]"

    ipt_operador = "//input[contains(@formcontrolname,'operador')]"

    div_extracciones = "//span[contains(.,'Extracciones')]/following-sibling::div"

    div_depositos = "//span[contains(.,'Dep')]/following-sibling::div"

    div_compraventa = "//span[contains(.,'Moneda')]/following-sibling::div"
    
    check_divs = "/mat-checkbox[{}]/label"

    check_todo = "//mat-checkbox[contains(@formcontrolname,'selecTodo')]/label"

    ipt_importe = "//input[contains(@formcontrolname,'valor')]"

    ipt_fecha = "//input[contains(@formcontrolname,'pickerDesde')]"